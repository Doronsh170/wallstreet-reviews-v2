"""
paste_review.py — publishes a chat-written review into data.json.

NO language-model API is used. Everything here is deterministic:
  - parses the JSON you pasted back from Claude/ChatGPT (tolerates ```json fences
    and surrounding text),
  - forces the exact title, date, one section, exact heading, "* " bullets,
  - runs the anti-hallucination guards against the Finnhub snapshot taken at
    gather time: asset direction guard (auto-fix), and a per-ticker sign-flip
    guard — a material sign-flip FAILS the publish and data.json is not touched,
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

DATA_JSON_KEY = {
    "daily_prep": "dailyPrep",
    "daily_summary": "dailySummary",
    "weekly_summary": "weeklySummary",
    "intraday_update": "intradayUpdate",
}

# The intraday update is intentionally short (4 bullets); the rest need 5+.
MIN_BULLETS = {"intraday_update": 4}

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
    "מזנק", "מזנקים", "זינק", "זינקו", "קופץ", "קופצים", "התחזק", "התחזקו", "מתחזק", "מתחזקים",
]
DOWN_WORDS = [
    "יורד", "יורדים", "ירד", "ירדו", "ירידה", "בירידה", "נופל", "נופלים", "נפל", "נפלו",
    "צונח", "צונחים", "צנח", "צנחו", "נחלש", "נחלשו", "נחלשת", "נחלשים", "מאבד", "מאבדים", "איבד", "איבדו",
]
DIRECTION_REPLACEMENTS_UP = {
    "צונחים": "עולים", "צונח": "עולה", "צנחו": "עלו", "צנח": "עלה",
    "יורדים": "עולים", "יורד": "עולה", "ירדו": "עלו", "ירד": "עלה", "ירידה": "עלייה", "בירידה": "בעלייה",
    "נופלים": "עולים", "נופל": "עולה", "נפלו": "עלו", "נפל": "עלה",
    "נחלשים": "מתחזקים", "נחלש": "התחזק", "נחלשו": "התחזקו", "נחלשת": "מתחזקת",
    "מאבדים": "מוסיפים", "מאבד": "מוסיף", "איבדו": "הוסיפו", "איבד": "הוסיף",
}
DIRECTION_REPLACEMENTS_DOWN = {
    "מזנקים": "יורדים", "מזנק": "יורד", "זינקו": "ירדו", "זינק": "ירד",
    "עולים": "יורדים", "עולה": "יורד", "עלו": "ירדו", "עלה": "ירד", "עלייה": "ירידה", "בעלייה": "בירידה",
    "מטפסים": "יורדים", "מטפס": "יורד", "טיפסו": "ירדו", "טיפס": "ירד",
    "קופצים": "יורדים", "קופץ": "יורד", "התחזקו": "נחלשו", "התחזק": "נחלש", "מתחזקים": "נחלשים", "מתחזק": "נחלש",
}
ANY_DIRECTION_RE = re.compile(
    r'(מזנקים|מזנק|זינקו|זינק|מטפסים|מטפס|טיפסו|טיפס|עולים|עולה|עלו|עלה|בעלייה|'
    r'יורדים|יורד|ירדו|ירד|בירידה|צונחים|צונח|צנחו|צנח|נופלים|נופל|נפלו|נפל|'
    r'נחלשים|נחלש|נחלשו|נחלשת)'
)
DIRECTION_ASSETS = {
    "oil": {"symbols": ["USO", "BNO"], "label": "נפט", "terms": ["נפט", "WTI", "Brent", "ברנט", "crude", "oil"]},
    "gold": {"symbols": ["GLD"], "label": "זהב", "terms": ["זהב", "gold"]},
    "bitcoin": {"symbols": ["IBIT"], "label": "ביטקוין", "terms": ["ביטקוין", "bitcoin", "BTC", "IBIT"]},
    "dollar": {"symbols": ["UUP"], "label": "דולר", "terms": ["דולר", "DXY", "UUP"]},
    "vix": {"symbols": ["VIXY"], "label": "תנודתיות / VIX", "terms": ["VIX", "תנודתיות", "VIXY"]},
    "long_bonds": {"symbols": ["TLT"], "label": "אג\"ח ארוכות", "terms": ["TLT", "אג\"ח", "אגח", "Treasury", "תשואות"]},
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
        elif re.match(r'^[^\n]{2,35}:\s+\S', stripped) and len(lines) >= 3:
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

    merged_parts, dropped = [], 0
    for s in sections:
        heading = str(s.get("heading", ""))
        c = s.get("content", "")
        if isinstance(c, list):
            c = "\n".join(str(x) for x in c)
        if "שורה תחתונה" in heading or heading.lower().strip() in {"bottom line", "the bottom line"}:
            dropped += 1
            continue
        if str(c).strip():
            merged_parts.append(str(c).strip())
    if not merged_parts:
        for s in sections:
            c = s.get("content", "")
            if isinstance(c, list):
                c = "\n".join(str(x) for x in c)
            if str(c).strip():
                merged_parts.append(str(c).strip())
    if len(sections) != 1 or dropped:
        print(f"  ✅ Sections normalized: {len(sections)} → 1; dropped bottom-line sections: {dropped}")
    result["sections"] = [{"heading": first_heading, "content": normalize_bullets("\n".join(merged_parts))}]
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


def apply_market_direction_guard(result: Dict[str, Any], pcts: Dict[str, float]) -> Dict[str, Any]:
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
        directions[key] = {"direction": direction, "meta": meta}
    if not directions:
        return result

    def fix_sentence(sent: str) -> str:
        for info in directions.values():
            direction = info["direction"]
            if not any(t.lower() in sent.lower() for t in info["meta"]["terms"]):
                continue
            has_up = any(w in sent for w in UP_WORDS)
            has_down = any(w in sent for w in DOWN_WORDS)
            if direction == "up" and has_down and not has_up:
                for src, dst in sorted(DIRECTION_REPLACEMENTS_UP.items(), key=lambda x: -len(x[0])):
                    sent = re.sub(rf'(?<!\w){re.escape(src)}(?!\w)', dst, sent)
                print(f"  ✅ Direction guard fixed contradiction: {info['meta']['label']} should be UP")
            elif direction == "down" and has_up and not has_down:
                for src, dst in sorted(DIRECTION_REPLACEMENTS_DOWN.items(), key=lambda x: -len(x[0])):
                    sent = re.sub(rf'(?<!\w){re.escape(src)}(?!\w)', dst, sent)
                print(f"  ✅ Direction guard fixed contradiction: {info['meta']['label']} should be DOWN")
            elif direction in ("flat", "mixed") and (has_up or has_down):
                sent = ANY_DIRECTION_RE.sub("נעים בתנודתיות", sent)
                print(f"  ✅ Direction guard neutralized mixed/flat direction: {info['meta']['label']}")
        return sent

    def fix_text(text: str) -> str:
        out_lines = []
        for line in text.split("\n"):
            parts = re.split(r'(?<=[\.\!\?])\s+', line)
            out_lines.append(" ".join(fix_sentence(p) for p in parts))
        return "\n".join(out_lines)

    for section in result.get("sections", []):
        if isinstance(section.get("content"), str):
            section["content"] = fix_text(section["content"])
    return result


def ticker_direction_check(result: Dict[str, Any], ticker_quotes: Dict[str, Dict[str, float]],
                           threshold: float = 0.3) -> None:
    """Per-bullet sign-flip check against the gather-time snapshot.
    A HIGH-severity contradiction (bullet says up, verified quote says down, or
    vice versa) FAILS the publish — data.json is not touched. A claim against a
    ~flat quote is only a warning (usually a real pre/after-market move)."""
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
    if hard:
        details = "\n  ".join(hard)
        raise ValueError(
            f"הפרסום נכשל: {len(hard)} סתירות כיוון מהותיות (sign-flip) במניות:\n  {details}\n"
            f"מה לעשות: חזור לצ'אט, הצג לו את הבולטים האלה ואת האחוז המאומת, "
            f"ובקש לתקן את הכיוון והאחוז או להסיר את הבולט. אז הדבק שוב ל-review_output.json."
        )
    print("  ✅ אין סתירות כיוון מהותיות במניות שנבדקו")


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

    print("── Text fixes ──")
    result = strip_meta_and_markdown(result)
    result = apply_text_fixes(result)
    result = apply_style_fixes(result)

    print("── Market direction guard (vs gather-time Finnhub snapshot) ──")
    result = apply_market_direction_guard(result, snapshot.get("etf_pcts", {}))

    print("── Per-ticker direction check (vs snapshot) ──")
    # Raises on a material sign-flip → publish fails, data.json untouched.
    ticker_direction_check(result, snapshot.get("ticker_quotes", {}))

    print("── Tense guard / links / dedupe ──")
    result = apply_pre_market_tense_guard(result, mode)
    result = strip_links_from_result(result)
    result = dedupe_exact_review_lines(result)

    print("── Final validation ──")
    hard_content_validation(result, MIN_BULLETS.get(mode, 5))
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

    bullets = result["sections"][0]["content"].count("\n* ") + 1
    print(f"\n✅ data.json עודכן → {DATA_JSON_KEY[mode]} ({bullets} בולטים)")
    print("   כעת: git add data.json && git commit && git push (או שה-workflow עושה זאת אוטומטית)")


if __name__ == "__main__":
    main()
