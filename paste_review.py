"""
paste_review.py — publishes a chat-written review into data.json.

NO language-model API is used. Everything here is deterministic:
  - parses the JSON you pasted back from Claude/ChatGPT (tolerates ```json fences
    and surrounding text),
  - forces the exact title, date, one section, exact heading, "* " bullets,
  - runs the anti-hallucination guards against the Finnhub snapshot taken at
    gather time: an asset direction check and a per-ticker sign-flip check —
    a material contradiction FAILS the publish and data.json is not touched
    (no silent auto-rewrites: a wrong direction means the whole bullet needs
    a rewrite, not a patched verb),
  - enforces the signature length: daily reviews are EXACTLY 6 bullets with a
    per-bullet word cap, the weekly is 8-10,
  - fixes known recurring errors (tense before market open, political titles,
    IPO/ETF confusion), strips URLs, removes duplicate bullets,
  - writes the result into data.json under the right key for the website.

Usage:
  python paste_review.py                    # reads review_output.json
  python paste_review.py my_reply.json      # or any file containing the chat reply

Requires raw_review_input.json (created by gather_review_input.py) in the same folder.
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Set
from zoneinfo import ZoneInfo

ISR_TZ = ZoneInfo("Asia/Jerusalem")
NY_TZ = ZoneInfo("America/New_York")

DATA_JSON = Path("data.json")
SNAPSHOT_FILE = Path("raw_review_input.json")
DEFAULT_INPUT = Path("review_output.json")
# Every published review is also appended to a monthly archive file
# (archive/YYYY-MM.json) so the site can show past reviews, not just the latest.
ARCHIVE_DIR = Path("archive")

DATA_JSON_KEY = {
    "daily_prep": "dailyPrep",
    "daily_summary": "dailySummary",
    "weekly_summary": "weeklySummary",
    "intraday_update": "intradayUpdate",
    "israel_prep": "israelPrep",
    "israel_summary": "israelSummary",
    "israel_weekly_summary": "israelWeeklySummary",
}

# The intraday update summarizes the sources: bullet count is driven by the
# material topics in the window, and a quiet window is a single bullet
# ("אין מספיק עדכונים משמעותיים..."). Below 5 in a signature review means the
# chat skipped material and needs another round.
# The Israeli reviews are tweet-only, so a thin source day may legitimately yield
# a short review (or the single "not enough material" bullet) — floor of 1.
MIN_BULLETS = {"intraday_update": 1, "israel_prep": 1, "israel_summary": 1,
               "israel_weekly_summary": 1}

# Signature length (CLAUDE.md): the US daily reviews are EXACTLY 6 bullets
# including the bottom line, each 4-5 lines; the weekly is 8-10 bullets.
# Enforced here so an overgrown review never reaches the site.
EXACT_BULLETS = {"daily_prep": 6, "daily_summary": 6}
BULLET_RANGE = {"weekly_summary": (8, 10)}
MAX_BULLET_WORDS = 100     # hard cap per daily bullet, headline included
TARGET_BULLET_WORDS = 85   # above this → warning (the 4-5 line target is ~60-80)
MAX_SUMMARY_ITEM_WORDS = 28  # a תקציר item should be ~20 words — warning only

BULLET_CHARS = r'[•■●▪▫◦‣⁃–—]'

TEXT_FIXES = [
    (r'הנשיא\s+לשעבר\s+טראמפ', 'הנשיא טראמפ', 'Trump is the current president'),
    (r'נשיא\s+ארה"ב\s+לשעבר\s+טראמפ', 'נשיא ארה"ב טראמפ', 'Trump is the current president'),
    (r'הנשיא\s+לשעבר\s+דונלד\s+טראמפ', 'הנשיא דונלד טראמפ', 'Trump is the current president'),
    (r'טראמפ\s*,?\s*הנשיא\s+לשעבר', 'טראמפ, הנשיא', 'Trump is the current president'),
    (r'הנשיא\s+ביידן', 'הנשיא לשעבר ביידן', 'Biden is the FORMER president'),
    (r'אמזון\s+השיקה?\s+את\s+Claude', 'Anthropic השיקה את Claude', 'Claude is by Anthropic'),
    (r'AWS\s+השיקה?\s+את\s+Claude', 'Anthropic השיקה את Claude', 'Claude is by Anthropic'),
    (r'מיקרוסופט\s+השיקה?\s+את\s+ChatGPT', 'OpenAI השיקה את ChatGPT', 'ChatGPT is by OpenAI'),
    (r'הנפקה\s+ראשונית\s+לציבור\s*\(ETF\)', 'תעודת סל (ETF)', 'IPO ≠ ETF'),
    (r'תעודת\s+סל\s*\(IPO\)', 'הנפקה ראשונית (IPO)', 'ETF ≠ IPO'),
    (r'תנודתיותת', 'תנודתיות', 'typo: תנודתיותת'),
]

# The intraday update must never say "מסחר במזומן" / "שוק המזומן" (awkward calque
# of "cash market") — deterministic rewrite, applied to intraday_update only.
INTRADAY_TEXT_FIXES = [
    (r'המסחר\s+במזומן', 'המסחר הרגיל', 'forbidden phrase "המסחר במזומן"'),
    (r'במסחר\s+במזומן', 'במסחר הרגיל', 'forbidden phrase "במסחר במזומן"'),
    (r'מסחר\s+במזומן', 'מסחר רגיל', 'forbidden phrase "מסחר במזומן"'),
    (r'שוק\s+המזומן', 'המסחר הרגיל', 'forbidden phrase "שוק המזומן"'),
]

# Hebrew company names for rewriting "* $TSLA:" bullet openers → "* מניית טסלה (TSLA):"
HEB_COMPANY_NAMES = {
    "TSLA": "טסלה", "AMZN": "אמזון", "META": "מטא", "AAPL": "אפל", "MSFT": "מיקרוסופט",
    "GOOGL": "אלפאבית", "GOOG": "אלפאבית", "NVDA": "אנבידיה", "NFLX": "נטפליקס",
    "INTC": "אינטל", "AMD": "AMD", "AVGO": "ברודקום", "MU": "מיקרון", "TSM": "TSMC",
    "HOOD": "רובינהוד", "COIN": "קוינבייס", "PLTR": "פלנטיר", "UBER": "אובר", "ORCL": "אורקל",
    "BA": "בואינג", "DIS": "דיסני", "JPM": "ג'יי.פי מורגן", "GS": "גולדמן זאקס",
    "DAL": "דלתא איירליינס", "XOM": "אקסון מוביל", "CVX": "שברון", "BABA": "עליבאבא",
}

ISO_DATE_IN_TEXT_RE = re.compile(r'\b(20\d{2})-(\d{2})-(\d{2})\b')
FUTURE_DATA_PHRASE_RE = re.compile(r'[,;]?\s*נתון בפועל עדיין לא קיים[,;]?\s*')

PRE_MARKET_TENSE_FIXES = [
    (r'השוק\s+נפתח\s+הבוקר', 'השוק צפוי להיפתח', 'market has not opened yet'),
    (r'השווקים\s+נפתחו\s+הבוקר', 'השווקים צפויים להיפתח', 'markets have not opened yet'),
    (r'המסחר\s+נפתח\s+הבוקר', 'המסחר צפוי להיפתח', 'trading has not opened yet'),
    (r'המדדים?\s+(?:פתחו?|פותח|נפתחו?)\s+(?:את\s+)?(?:היום|הבוקר|המסחר)', 'המדדים צפויים להיפתח', 'indices have not opened yet'),
    (r'וול\s+סטריט\s+נפתחה\s+הבוקר', 'וול סטריט צפויה להיפתח', 'Wall Street has not opened yet'),
    (r'פתיחת\s+המסחר\s+היתה', 'פתיחת המסחר צפויה להיות', 'opening has not happened yet'),
    (r'המסחר\s+היום\s+התנהל', 'המסחר היום צפוי להתנהל', 'trading has not happened yet'),
    (r'המשקיעים\s+הגיבו\s+הבוקר', 'המשקיעים צפויים להגיב', 'no reaction yet — market closed'),
    (r'הגיבו\s+בפתיחה', 'יגיבו בפתיחה', 'no reaction yet — market closed'),
]

FORBIDDEN_META_PHRASES = ["לפי הציוץ", "ציוץ נוסף", "הציוץ", "ציוץ", "לפי פוסט", "הפוסט", "###", "##", "**"]

UP_WORDS = [
    "עולה", "עולים", "עלו", "עלה", "עלייה", "בעלייה", "מטפס", "מטפסים", "טיפס", "טיפסו",
    "מזנק", "מזנקים", "זינק", "זינקו", "קופץ", "קופצים", "קפץ", "קפצו", "התחזק", "התחזקו",
    "מתחזק", "מתחזקים", "מוסיף", "מוסיפים", "הוסיף", "הוסיפו",
]
DOWN_WORDS = [
    "יורד", "יורדים", "ירד", "ירדו", "ירידה", "בירידה", "נופל", "נופלים", "נפל", "נפלו",
    "צונח", "צונחים", "צנח", "צנחו", "נחלש", "נחלשו", "נחלשת", "נחלשים", "מאבד", "מאבדים",
    "איבד", "איבדו", "נסוג", "נסוגו", "נסיגה",
]
# Word boundaries (?<!\w)...(?!\w) are MANDATORY when matching direction words:
# without them "נפל" matches inside "אינפלציה", "זינק" inside "זינקה",
# "יורד" inside "יורדות", "עולה" inside "פעולה" — and an innocent sentence
# gets flagged as a contradiction.
#
# DIRECTION_ASSETS notes:
# - "dollar" matches only "הדולר"/DXY/UUP — a bare "דולר" appears in every
#   price ("79 דולר לחבית", "מיליארד דולר") and must not trigger the check.
# - "yields" moves INVERSELY to its measurement symbol (TLT): bond prices up
#   means yields down. A sentence about "תשואות" is checked against the
#   inverted TLT direction, and suppresses the bond-price check ("long_bonds")
#   for that sentence, because "תשואות האג"ח" is a yields story.
DIRECTION_ASSETS = {
    "oil": {"symbols": ["USO", "BNO"], "label": "נפט", "terms": ["נפט", "WTI", "Brent", "ברנט", "crude", "oil"]},
    "gold": {"symbols": ["GLD"], "label": "זהב", "terms": ["זהב", "gold"]},
    "bitcoin": {"symbols": ["IBIT"], "label": "ביטקוין", "terms": ["ביטקוין", "bitcoin", "BTC", "IBIT"]},
    "dollar": {"symbols": ["UUP"], "label": "דולר", "terms": ["הדולר", "DXY", "UUP"]},
    "vix": {"symbols": ["VIXY"], "label": "תנודתיות / VIX", "terms": ["VIX", "תנודתיות", "VIXY"]},
    "long_bonds": {"symbols": ["TLT"], "label": "אג\"ח ארוכות", "terms": ["TLT", "אג\"ח", "אגח"]},
    "yields": {"symbols": ["TLT"], "label": "תשואות", "terms": ["תשואות", "התשואה", "Treasury"], "invert": True},
}

TICKER_UP_TOKENS = UP_WORDS + ["עלתה", "מטפסת", "מזנקת", "זינקה", "קופצת", "קפץ", "קפצה", "קפצו",
                               "מתחזקת", "התחזקה", "ירוק", "בירוק", "מוסיפה", "מוסיף", "הוסיפה", "הוסיף",
                               "הובילה את העליות", "הוביל את העליות", "הובילו את העליות",
                               "בלטה לחיוב", "בלט לחיוב", "בלטו לחיוב"]
TICKER_DOWN_TOKENS = DOWN_WORDS + ["יורדת", "ירדה", "נופלת", "נפלה", "צונחת", "צנחה", "צניחה", "נחלשה",
                                   "אדום", "באדום", "מאבדת", "איבדה",
                                   "הובילה את הירידות", "הוביל את הירידות", "הובילו את הירידות",
                                   "בלטה לשלילה", "בלט לשלילה", "בלטו לשלילה"]


# ══════════════════════════════════════════════════════════════
# Helpers
# ══════════════════════════════════════════════════════════════

def extract_first_json_object(text: str) -> Dict[str, Any]:
    """Tolerates ```json fences, leading/trailing chatter, and citation brackets."""
    text = text.strip()
    text = re.sub(r'```(?:json)?', '', text)
    start = text.find("{")
    if start < 0:
        raise ValueError("לא נמצא אובייקט JSON בקובץ. ודא שהעתקת את תשובת הצ'אט המלאה.")
    depth, in_str, esc = 0, False, False
    for i in range(start, len(text)):
        ch = text[i]
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
            continue
        if ch == '"':
            in_str = True
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return json.loads(text[start:i + 1])
    raise ValueError("אובייקט ה-JSON לא נסגר — כנראה שהתשובה נקטעה. בקש מהצ'אט להחזיר את ה-JSON שוב במלואו.")


def apply_to_result_texts(result: Dict[str, Any], fn) -> Dict[str, Any]:
    if isinstance(result.get("title"), str):
        result["title"] = fn(result["title"])
    # The authored summary (one short point per story) goes through every text
    # fix and guard exactly like the bullets do.
    if isinstance(result.get("summary"), list):
        result["summary"] = [fn(x) if isinstance(x, str) else x for x in result["summary"]]
    for section in result.get("sections", []) or []:
        if isinstance(section.get("heading"), str):
            section["heading"] = fn(section["heading"])
        content = section.get("content")
        if isinstance(content, str):
            section["content"] = fn(content)
        elif isinstance(content, list):
            section["content"] = [fn(x) if isinstance(x, str) else x for x in content]
    return result


def review_text_blob(result: Dict[str, Any]) -> str:
    texts = [str(result.get("title") or "")]
    if isinstance(result.get("summary"), list):
        texts.extend(str(x) for x in result["summary"])
    for section in result.get("sections", []):
        c = section.get("content", "")
        texts.append("\n".join(str(x) for x in c) if isinstance(c, list) else str(c))
    return "\n".join(texts)


# ══════════════════════════════════════════════════════════════
# Structure enforcement
# ══════════════════════════════════════════════════════════════

def normalize_bullets(text: str) -> str:
    if not isinstance(text, str) or not text.strip():
        return text
    lines = text.split("\n")
    result = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            result.append("")
            continue
        converted = re.sub(rf'^{BULLET_CHARS}\s+', '* ', stripped)
        converted = re.sub(r'^-\s+', '* ', converted)
        if converted.startswith('* '):
            result.append(converted)
        elif re.match(r'^\$[A-Z]{1,5}\s*:', stripped):
            result.append('* ' + stripped)
        elif re.match(r'^[^\n]{2,40}:\s+\S', stripped) and len(lines) >= 3:
            result.append('* ' + stripped)
        else:
            result.append(stripped)
    return "\n".join(l for l in result if l.strip() or not l)


def enforce_structure(result: Dict[str, Any], first_heading: str, expected_title: str) -> Dict[str, Any]:
    original_title = result.get("title", "")
    result["title"] = expected_title
    if original_title != expected_title:
        print(f"  ✅ Title overridden: '{original_title}' → '{expected_title}'")

    sections = result.get("sections", [])
    if not isinstance(sections, list) or not sections:
        raise ValueError("ה-JSON לא מכיל sections. בקש מהצ'אט להחזיר את המבנה המדויק שהוגדר בהנחיות.")

    merged_parts, converted = [], 0
    for s in sections:
        heading = str(s.get("heading", ""))
        c = s.get("content", "")
        if isinstance(c, list):
            c = "\n".join(str(x) for x in c)
        text = str(c).strip()
        if not text:
            continue
        if "שורה תחתונה" in heading or heading.lower().strip() in {"bottom line", "the bottom line"}:
            # The bottom line belongs in the review — fold it in as the closing bullet.
            if not text.lstrip().startswith("*"):
                text = "* בשורה התחתונה: " + re.sub(r'^\s*[*•\-–—]+\s*', '', text)
            converted += 1
        merged_parts.append(text)
    if len(sections) != 1 or converted:
        print(f"  ✅ Sections normalized: {len(sections)} → 1; bottom-line sections folded into a closing bullet: {converted}")
    result["sections"] = [{"heading": first_heading, "content": normalize_bullets("\n".join(merged_parts))}]
    return result


def normalize_summary(result: Dict[str, Any]) -> Dict[str, Any]:
    """The optional authored summary is a list of short one-line points (one per
    story) shown on the site above the full review. Keep it only if it is a clean
    list of non-empty strings, stripping any leading bullet marks — otherwise drop
    it so the site falls back to deriving a gist from the full bullets."""
    summ = result.get("summary")
    if not isinstance(summ, list):
        if summ is not None:
            result.pop("summary", None)
        return result
    cleaned = []
    for item in summ:
        if not isinstance(item, str):
            continue
        line = re.sub(rf'^\s*(?:\*|{BULLET_CHARS}|-)\s+', '', item.strip())
        if line:
            cleaned.append(line)
    if cleaned:
        result["summary"] = cleaned
        print(f"  ✅ Authored summary kept ({len(cleaned)} points)")
    else:
        result.pop("summary", None)
    return result


def fix_numeric_spacing(text: str) -> str:
    text = re.sub(r"(\d)\.\s+(\d)", r"\1.\2", text)
    text = re.sub(r"(\d)\s+%", r"\1%", text)
    return text


def apply_text_fixes(result: Dict[str, Any]) -> Dict[str, Any]:
    def fix(text: str) -> str:
        for pattern, replacement, desc in TEXT_FIXES:
            new_text = re.sub(pattern, replacement, text)
            if new_text != text:
                print(f"  ✅ Auto-fixed: {desc}")
                text = new_text
        return fix_numeric_spacing(text)
    return apply_to_result_texts(result, fix)


def _rewrite_ticker_opener(line: str) -> str:
    m = re.match(r'^(\*\s*)(\$)?([A-Z]{1,6})\s*:\s*(.*)$', line)
    if not m:
        return line
    has_dollar, ticker = m.group(2), m.group(3)
    # Without a $ prefix, rewrite only known tickers (avoid mangling "* AI:" etc.)
    if not has_dollar and ticker not in HEB_COMPANY_NAMES:
        return line
    name = HEB_COMPANY_NAMES.get(ticker)
    lead = f"מניית {name} ({ticker})" if name else f"מניית {ticker}"
    return f"{m.group(1)}{lead}: {m.group(4)}"


def apply_style_fixes(result: Dict[str, Any]) -> Dict[str, Any]:
    """Deterministic Hebrew-style safety net:
    ISO dates in visible text → Israeli format, no semicolons, no
    'נתון בפועל עדיין לא קיים', bullet openers with Hebrew company names."""
    def fix(text: str) -> str:
        new = ISO_DATE_IN_TEXT_RE.sub(lambda m: f"{int(m.group(3))}.{int(m.group(2))}.{m.group(1)}", text)
        if new != text:
            print("  ✅ Style: ISO dates in text converted to Israeli format")
            text = new
        if ";" in text:
            text = re.sub(r'\s*;\s*', ', ', text)
            print("  ✅ Style: semicolons replaced with commas")
        new = FUTURE_DATA_PHRASE_RE.sub(', ', text)
        if new != text:
            new = re.sub(r',\s*,+', ',', new)
            new = re.sub(r'\s+([,.])', r'\1', new)
            print("  ✅ Style: removed 'נתון בפועל עדיין לא קיים'")
            text = new
        lines = [_rewrite_ticker_opener(l) for l in text.split("\n")]
        if lines != text.split("\n"):
            print("  ✅ Style: raw $TICKER bullet openers rewritten with Hebrew company names")
        return "\n".join(lines)
    return apply_to_result_texts(result, fix)


def apply_intraday_fixes(result: Dict[str, Any]) -> Dict[str, Any]:
    def fix(text: str) -> str:
        for pattern, replacement, desc in INTRADAY_TEXT_FIXES:
            new_text = re.sub(pattern, replacement, text)
            if new_text != text:
                print(f"  ✅ Intraday fix: {desc}")
                text = new_text
        return text
    return apply_to_result_texts(result, fix)


def strip_meta_and_markdown(result: Dict[str, Any]) -> Dict[str, Any]:
    def clean(text: str) -> str:
        text = text.replace("**", "").replace("###", "").replace("##", "")
        return text
    return apply_to_result_texts(result, clean)


# ══════════════════════════════════════════════════════════════
# Direction guards — against the snapshot from gather time
# ══════════════════════════════════════════════════════════════

def direction_from_pct(pct: Any, threshold: float = 0.15) -> Optional[str]:
    try:
        pct = float(pct)
    except Exception:
        return None
    if pct >= threshold:
        return "up"
    if pct <= -threshold:
        return "down"
    return "flat"


def _has_direction_word(text: str, words: List[str]) -> bool:
    return any(re.search(rf'(?<!\w){re.escape(w)}(?!\w)', text) for w in words)


def market_direction_check(result: Dict[str, Any], pcts: Dict[str, float]) -> None:
    """Asset-level direction check (oil/gold/bitcoin/dollar/VIX/bonds/yields)
    against the gather-time Finnhub snapshot, on the bullets AND the summary.

    A verified contradiction FAILS the publish. This guard used to auto-replace
    the direction verb in place — that patched one word but left the bullet's
    headline, logic and summary contradicting it (a published bullet ended up
    with "הזהב נסוג" in the headline, "הזהב עלה" in the body and "הזהב ירד" in
    the summary), so the whole bullet must be rewritten instead.
    A direction claim against a ~flat/mixed reading is a warning only."""
    directions: Dict[str, Dict[str, Any]] = {}
    for key, meta in DIRECTION_ASSETS.items():
        dirs = [d for d in (direction_from_pct(pcts.get(s)) for s in meta["symbols"] if s in pcts) if d]
        if not dirs:
            continue
        nonflat = [d for d in dirs if d != "flat"]
        if not nonflat:
            direction = "flat"
        elif all(d == nonflat[0] for d in nonflat):
            direction = nonflat[0]
        else:
            direction = "mixed"
        if meta.get("invert") and direction in ("up", "down"):
            direction = "up" if direction == "down" else "down"
        directions[key] = {"direction": direction, "meta": meta}
    if not directions:
        return

    heb = {"up": "עלייה", "down": "ירידה"}
    hard: List[str] = []
    soft: List[str] = []

    def term_in(text: str, terms: List[str]) -> bool:
        return any(t.lower() in text.lower() for t in terms)

    def check_fragment(frag: str, info: Dict[str, Any]) -> None:
        has_up = _has_direction_word(frag, UP_WORDS)
        has_down = _has_direction_word(frag, DOWN_WORDS)
        if has_up == has_down:  # neither, or both even inside one clause — ambiguous, skip
            return
        claimed = "up" if has_up else "down"
        direction = info["direction"]
        label = info["meta"]["label"]
        if direction in ("flat", "mixed"):
            soft.append(f"{label}: הטקסט טוען {heb[claimed]} אבל הנתון המאומת היה כמעט ללא שינוי/מעורב."
                        f"\n     הטקסט: {frag.strip()[:200]}")
        elif claimed != direction:
            hard.append(f"{label}: הטקסט טוען {heb[claimed]} אבל הנתון המאומת בזמן האיסוף הראה {heb[direction]}."
                        f"\n     הטקסט: {frag.strip()[:200]}")

    def scan_text(text: str) -> None:
        for line in str(text).split("\n"):
            for sent in re.split(r'(?<=[\.\!\?])\s+', line):
                if not sent.strip():
                    continue
                for key, info in directions.items():
                    terms = info["meta"]["terms"]
                    if not term_in(sent, terms):
                        continue
                    # "תשואות האג"ח עלו" is a yields story — don't judge it as a bond-price story.
                    if key == "long_bonds" and "yields" in directions and term_in(sent, directions["yields"]["meta"]["terms"]):
                        continue
                    # A sentence mixing up- and down-words ("הזהב ירד, בעוד ה-VIX עלה",
                    # or a headline contradicting its own body across the ":") is split
                    # into clauses so each claim is judged on its own. The colon split
                    # skips times like "22:40".
                    frags = [sent]
                    if _has_direction_word(sent, UP_WORDS) and _has_direction_word(sent, DOWN_WORDS):
                        frags = [f for f in re.split(r'[,;]|(?<!\d):(?!\d)|\sבעוד\s', sent) if term_in(f, terms)]
                    for frag in frags:
                        check_fragment(frag, info)

    for section in result.get("sections", []):
        if isinstance(section.get("content"), str):
            scan_text(section["content"])
    for item in result.get("summary", []) or []:
        if isinstance(item, str):
            scan_text(item)

    for w in soft:
        print(f"  ⚠️  אזהרה (נכס כמעט ללא שינוי בנתון המאומת): {w}")
    if hard:
        details = "\n  ".join(hard)
        raise ValueError(
            f"הפרסום נכשל: {len(hard)} סתירות כיוון בנכסים (נפט/זהב/דולר/תשואות/VIX):\n  {details}\n"
            f"מה לעשות: שכתב את הבולט כולו (כותרת, גוף ותקציר) כך שהכיוון, ההסבר והלוגיקה "
            f"יתאימו לנתון המאומת — אל תחליף רק את מילת הכיוון."
        )
    print("  ✅ אין סתירות כיוון בנכסים שנבדקו")


def ticker_direction_check(result: Dict[str, Any], ticker_quotes: Dict[str, Dict[str, float]],
                           threshold: float = 0.3, hard_fail: bool = True) -> None:
    """Per-bullet sign-flip check against the gather-time snapshot.
    A HIGH-severity contradiction (bullet says up, verified quote says down, or
    vice versa) FAILS the publish — data.json is not touched. A claim against a
    ~flat quote is only a warning (usually a real pre/after-market move).
    hard_fail=False (weekly review) downgrades everything to warnings: the weekly
    text describes WEEKLY moves, and the snapshot only holds DAILY percentages —
    a contradiction there is usually not a hallucination."""
    if not ticker_quotes:
        return
    hard: List[str] = []
    soft: List[str] = []
    heb = {"up": "עלייה", "down": "ירידה"}
    content = result["sections"][0].get("content", "")
    for bullet in (l for l in str(content).split("\n") if l.strip()):
        for ticker, q in ticker_quotes.items():
            # Match "$TSLA", "(TSLA)" and bare "TSLA" — bullet openers are
            # rewritten to "מניית טסלה (TSLA):", so $-only matching would miss them.
            if not re.search(rf'(?<![A-Za-z0-9]){re.escape(ticker)}(?![A-Za-z0-9])', bullet):
                continue
            has_up = any(re.search(rf'(?<!\w){re.escape(t)}(?!\w)', bullet) for t in TICKER_UP_TOKENS)
            has_down = any(re.search(rf'(?<!\w){re.escape(t)}(?!\w)', bullet) for t in TICKER_DOWN_TOKENS)
            claimed = "up" if (has_up and not has_down) else "down" if (has_down and not has_up) else None
            if claimed is None:
                continue
            pct = float(q["pct"])
            actual = "flat" if abs(pct) < threshold else ("up" if pct > 0 else "down")
            if claimed == actual:
                continue
            msg = (f"${ticker}: הבולט טוען {heb[claimed]} אבל הנתון המאומת בזמן האיסוף היה {pct:+.2f}%."
                   f"\n     הבולט: {bullet.strip()[:200]}")
            if actual == "flat":
                soft.append(msg)
            else:
                hard.append(msg)
    for w in soft:
        print(f"  ⚠️  אזהרה (ציטוט כמעט ללא שינוי — ייתכן מהלך פרה/אפטר-מרקט): {w}")
    if hard and not hard_fail:
        for w in hard:
            print(f"  ⚠️  אזהרה (סקירה שבועית — הכיוון נבדק מול נתון יומי בלבד): {w}")
        return
    if hard:
        details = "\n  ".join(hard)
        raise ValueError(
            f"הפרסום נכשל: {len(hard)} סתירות כיוון מהותיות (sign-flip) במניות:\n  {details}\n"
            f"מה לעשות: חזור לצ'אט, הצג לו את הבולטים האלה ואת האחוז המאומת, "
            f"ובקש לתקן את הכיוון והאחוז או להסיר את הבולט. אז הדבק שוב ל-review_output.json."
        )
    print("  ✅ אין סתירות כיוון מהותיות במניות שנבדקו")


# ══════════════════════════════════════════════════════════════
# Macro schedule check — "scheduled today" claims must be verified
# ══════════════════════════════════════════════════════════════

# A review once presented the CPI as "due today" two days after it was
# released. The script cannot know the real calendar, so it never auto-fixes —
# it flags EVERY bullet that presents a macro event as scheduled today, so the
# writer must consciously confirm each one against a web-searched calendar
# (see CLAUDE.md, "אימות אירועי מאקרו") before pushing.
MACRO_EVENT_TERMS = [
    "CPI", "PPI", "NFP", "FOMC", "ISM", "GDP",
    "מדד המחירים לצרכן", "מדד המחירים ליצרן", "דוח התעסוקה",
    "החלטת ריבית", "החלטת הריבית", "פרוטוקול", "תביעות אבטלה", "תביעות האבטלה",
    "מכירות קמעונאיות", "המכירות הקמעונאיות", "אמון הצרכנים", "הספר הבז'",
]
SCHEDULED_TODAY_RE = re.compile(
    r'(?:ש?[יית]תפרסמו?|ש?יפורסמו?|צפויי?ה?ם?|במוקד)\s+היום|היום\s+ב-\d{1,2}:\d{2}'
)


def macro_schedule_check(result: Dict[str, Any]) -> None:
    flagged: List[str] = []
    content = result["sections"][0].get("content", "")
    for bullet in (l for l in str(content).split("\n") if l.strip()):
        if not SCHEDULED_TODAY_RE.search(bullet):
            continue
        events = [t for t in MACRO_EVENT_TERMS if t in bullet]
        if events:
            flagged.append(f"[{', '.join(events)}] {bullet.strip()[:150]}")
    if not flagged:
        print("  ✅ אין טענות 'מתפרסם היום' על אירועי מאקרו")
        return
    print(f"  ⚠️  MACRO-CHECK: {len(flagged)} בולטים מציגים אירוע מאקרו כמתוכנן להיום — "
          f"חובה לוודא כל אחד מול לוח אירועים שאומת בחיפוש אינטרנט (ראה CLAUDE.md):")
    for f in flagged:
        print(f"     - {f}")


# ══════════════════════════════════════════════════════════════
# Tense guard, links, dedupe, validation
# ══════════════════════════════════════════════════════════════

def is_before_us_market_open(now_il: datetime) -> bool:
    ny = now_il.astimezone(NY_TZ)
    if ny.weekday() >= 5:
        return False
    return (ny.hour, ny.minute) < (9, 30)


def apply_pre_market_tense_guard(result: Dict[str, Any], mode: str) -> Dict[str, Any]:
    if mode != "daily_prep" or not is_before_us_market_open(datetime.now(ISR_TZ)):
        return result

    def fix(text: str) -> str:
        for pattern, replacement, desc in PRE_MARKET_TENSE_FIXES:
            new_text = re.sub(pattern, replacement, text)
            if new_text != text:
                print(f"  ✅ Pre-market tense fixed: {desc}")
                text = new_text
        return text

    return apply_to_result_texts(result, fix)


def strip_links_from_result(result: Dict[str, Any]) -> Dict[str, Any]:
    def clean(text: str) -> str:
        text = re.sub(r'\s*\(?\s*\[[^\]\n]{1,120}\]\s*\(\s*https?://.*?\)\s*\)?', '', text, flags=re.DOTALL)
        text = re.sub(r'\s*\(?\s*\[[^\]\n]{1,120}\]\s*[\r\n]+\s*https?://\S+\s*\)?', '', text)
        text = re.sub(r'\s*\(?https?://\S+', '', text)
        text = re.sub(r'\s*\(?utm_source=openai\)?', '', text)
        text = re.sub(r'\s*\(?\[[A-Za-z0-9 ._-]+\.(?:com|org|net|io|co|gov|edu|finance)[^\]\n]*\]\)?', '', text)
        text = re.sub(r'\s*[()]{2,}\s*', ' ', text)
        text = re.sub(r'\s*\(\s*\)', '', text)
        text = re.sub(r'[ \t]{2,}', ' ', text)
        return text.strip()
    return apply_to_result_texts(result, clean)


def dedupe_exact_review_lines(result: Dict[str, Any]) -> Dict[str, Any]:
    def line_key(line: str) -> str:
        key = re.sub(r'^\s*[*•\-]+\s*', '', str(line or "").strip())
        return re.sub(r'\s+', ' ', key).strip()

    for section in result.get("sections", []) or []:
        content = section.get("content")
        if not isinstance(content, str):
            continue
        seen: Set[str] = set()
        out = []
        for line in content.splitlines():
            key = line_key(line)
            if key and key in seen:
                continue
            if key:
                seen.add(key)
            out.append(line)
        section["content"] = "\n".join(out).strip()
    return result


def hard_content_validation(result: Dict[str, Any], min_bullets: int = 5) -> None:
    """Failures here mean the chat reply needs another round — the error message
    tells you exactly what to ask the chat to fix."""
    blob = review_text_blob(result)
    hits = [p for p in FORBIDDEN_META_PHRASES if p in blob]
    if hits:
        raise ValueError(f"הסקירה מכילה ביטויים אסורים: {hits}. בקש מהצ'אט לשכתב בלי להזכיר ציוצים/פוסטים ובלי Markdown.")
    tech_hits = [p for p in ("finnhub", "proxy") if p in blob.lower()]
    if re.search(r'דרך\s+[A-Z]{2,6}(?![A-Za-z])', blob):
        tech_hits.append("דרך <TICKER>")
    if "האינדיקציה מ" in blob:
        tech_hits.append("האינדיקציה מ-")
    if tech_hits:
        raise ValueError(
            f"הסקירה חושפת את שכבת האימות הטכנית: {tech_hits}. "
            f"בקש מהצ'אט לתאר את הנכס עצמו (נפט/זהב/דולר/תשואות) בלי להזכיר Finnhub, proxy או תעודות סל של מדידה."
        )
    if not re.search(r"[א-ת]", blob):
        raise ValueError("הסקירה לא בעברית. בקש מהצ'אט לכתוב את הסקירה בעברית בלבד.")
    content = result["sections"][0].get("content", "")
    bullets = [l for l in str(content).split("\n") if l.strip().startswith("* ")]
    if len(bullets) < min_bullets:
        raise ValueError(f"רק {len(bullets)} בולטים בסקירה — נדרשים לפחות {min_bullets}. בקש מהצ'אט סקירה מלאה יותר.")


def bullet_length_check(result: Dict[str, Any], mode: str) -> None:
    """Enforces the signature length so a bloated review never publishes:
    daily reviews are EXACTLY 6 bullets with a hard per-bullet word cap,
    the weekly is 8-10 bullets. Other modes are length-free by design."""
    content = result["sections"][0].get("content", "")
    bullets = [l for l in str(content).split("\n") if l.strip().startswith("* ")]
    exact = EXACT_BULLETS.get(mode)
    if exact is not None and len(bullets) != exact:
        raise ValueError(
            f"בסקירה {len(bullets)} בולטים — הסקירה היומית היא בדיוק {exact} נקודות כולל השורה התחתונה. "
            f"מזג או מחק את הנקודות החלשות (או פצל אם חסרות), ועדכן גם את התקציר באותו סדר."
        )
    rng = BULLET_RANGE.get(mode)
    if rng and not (rng[0] <= len(bullets) <= rng[1]):
        raise ValueError(
            f"בסקירה {len(bullets)} בולטים — הסקירה השבועית היא {rng[0]}-{rng[1]} נקודות. התאם את מספר הנקודות."
        )
    if exact is not None:
        for b in bullets:
            n = len(b.split())
            if n > MAX_BULLET_WORDS:
                raise ValueError(
                    f"בולט ארוך מדי ({n} מילים, המקסימום {MAX_BULLET_WORDS}): \"{b.strip()[:60]}...\" "
                    f"קצר אותו ל-4-5 שורות: השאר רק את העובדות שנושאות את הסיפור ואת הפואנטה למשקיע."
                )
            if n > TARGET_BULLET_WORDS:
                print(f"  ⚠️  בולט ארוך ({n} מילים, היעד עד ~{TARGET_BULLET_WORDS}): {b.strip()[:60]}...")
    for item in result.get("summary", []) or []:
        n = len(str(item).split())
        if n > MAX_SUMMARY_ITEM_WORDS:
            print(f"  ⚠️  פריט תקציר ארוך ({n} מילים, היעד ~20): {str(item)[:60]}...")


# ══════════════════════════════════════════════════════════════
# Archive
# ══════════════════════════════════════════════════════════════

def archive_review(mode: str, result: Dict[str, Any], published_at: str) -> Path:
    """Adds the published review to archive/<YYYY-MM>.json and refreshes
    archive/index.json (the month list the site's archive tab reads).
    A re-publish of the same review (same mode + same title, e.g. a fix round
    after a failed guard) replaces the earlier entry instead of duplicating it.
    Intraday updates carry the run time in the title, so each run of the day
    is archived as its own entry. Runs only after all guards passed — a failed
    publish never reaches the archive."""
    month = str(result.get("date", ""))[:7]
    if not re.fullmatch(r"20\d{2}-\d{2}", month):
        month = str(published_at)[:7]
    path = ARCHIVE_DIR / f"{month}.json"
    try:
        archive = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        archive = {}
    entries = [e for e in archive.get("entries", [])
               if not (e.get("mode") == mode
                       and (e.get("review") or {}).get("title") == result.get("title"))]
    entries.append({"mode": mode, "publishedAt": published_at, "review": result})
    entries.sort(key=lambda e: str(e.get("publishedAt", "")), reverse=True)
    ARCHIVE_DIR.mkdir(exist_ok=True)
    path.write_text(json.dumps({"month": month, "entries": entries}, ensure_ascii=False, indent=2),
                    encoding="utf-8")
    months = sorted((p.stem for p in ARCHIVE_DIR.glob("20??-??.json")), reverse=True)
    (ARCHIVE_DIR / "index.json").write_text(
        json.dumps({"months": months}, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


# ══════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════

def main() -> None:
    if not SNAPSHOT_FILE.exists():
        raise SystemExit("חסר raw_review_input.json — הרץ קודם: python gather_review_input.py <mode>")
    snapshot = json.loads(SNAPSHOT_FILE.read_text(encoding="utf-8"))
    mode = snapshot["mode"]
    expected_title = snapshot["expected_title"]
    first_heading = snapshot["first_heading"]
    review_date = snapshot["review_date"]

    input_file = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    if not input_file.exists():
        raise SystemExit(
            f"חסר {input_file} — הדבק לתוכו את תשובת ה-JSON מהצ'אט (אפשר כולל ```json והסברים מסביב)."
        )

    print(f"Publishing {mode} (gathered {snapshot.get('generated_at', '')[:16]})")
    result = extract_first_json_object(input_file.read_text(encoding="utf-8"))

    print("\n── Structure enforcement ──")
    result = enforce_structure(result, first_heading, expected_title)
    result = normalize_summary(result)

    print("── Text fixes ──")
    result = strip_meta_and_markdown(result)
    result = apply_text_fixes(result)
    result = apply_style_fixes(result)
    if mode == "intraday_update":
        result = apply_intraday_fixes(result)

    print("── Market direction check (vs gather-time Finnhub snapshot) ──")
    if mode in ("weekly_summary", "israel_weekly_summary"):
        # The weekly text describes WEEKLY moves and the snapshot holds DAILY
        # percentages — checking against them would flag correct sentences.
        # (The Israeli weekly is tweet-only, so its snapshot is empty anyway.)
        print("  weekly review — skipping the daily-based direction check")
    else:
        market_direction_check(result, snapshot.get("etf_pcts", {}))

    print("── Per-ticker direction check (vs snapshot) ──")
    # Raises on a material sign-flip → publish fails, data.json untouched.
    # Weekly reviews describe weekly moves, so the daily snapshot is warnings-only there.
    ticker_direction_check(result, snapshot.get("ticker_quotes", {}),
                           hard_fail=(mode != "weekly_summary"))

    print("── Macro schedule check ──")
    macro_schedule_check(result)

    print("── Tense guard / links / dedupe ──")
    result = apply_pre_market_tense_guard(result, mode)
    result = strip_links_from_result(result)
    result = dedupe_exact_review_lines(result)

    print("── Final validation ──")
    hard_content_validation(result, MIN_BULLETS.get(mode, 5))
    bullet_length_check(result, mode)
    print("  ✅ Validation passed")

    original_date = result.get("date", "")
    if original_date != review_date:
        print(f"  ✅ Date overridden: '{original_date}' → '{review_date}'")
    result["date"] = review_date
    result = {k: v for k, v in result.items() if not str(k).startswith("_")}

    try:
        data = json.loads(DATA_JSON.read_text(encoding="utf-8"))
    except Exception:
        data = {}
    data["lastUpdated"] = datetime.now(ISR_TZ).isoformat()
    data[DATA_JSON_KEY[mode]] = result
    DATA_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    archive_path = archive_review(mode, result, data["lastUpdated"])

    bullets = result["sections"][0]["content"].count("\n* ") + 1
    print(f"\n✅ data.json עודכן → {DATA_JSON_KEY[mode]} ({bullets} בולטים)")
    print(f"   הארכיון עודכן → {archive_path}")
    print("   כעת: git add data.json archive && git commit && git push (או שה-workflow עושה זאת אוטומטית)")


if __name__ == "__main__":
    main()
