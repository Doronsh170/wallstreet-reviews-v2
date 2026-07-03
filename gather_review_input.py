"""
gather_review_input.py — collects RAW MATERIAL ONLY for a Wall Street Hebrew review.

NO language-model API is used anywhere in this script. It only gathers:
  tweets (TwitterAPI.io), verified market data + economic calendar (Finnhub),
  trading-day/date context, and the prior published review from data.json.

Output:
  raw_review_input.md    — one paste-ready block: full instructions + all raw data.
                           Copy the WHOLE file into Claude / ChatGPT.
  raw_review_input.json  — machine-readable snapshot (mode, expected title, dates,
                           verified percentages). Used later by paste_review.py to
                           validate and publish the review into data.json.

Modes (REVIEW_MODE env var or first CLI argument):
  daily_prep | daily_summary | weekly_summary

Usage:
  python gather_review_input.py daily_summary
"""

import json
import os
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from zoneinfo import ZoneInfo

import requests

# ══════════════════════════════════════════════════════════════
# CONFIG
# ══════════════════════════════════════════════════════════════

ISR_TZ = ZoneInfo("Asia/Jerusalem")
NY_TZ = ZoneInfo("America/New_York")

VALID_MODES = ("daily_prep", "daily_summary", "weekly_summary")
REVIEW_MODE = (
    (sys.argv[1] if len(sys.argv) > 1 else "")
    or os.environ.get("REVIEW_MODE", "")
).strip().lower()
if REVIEW_MODE not in VALID_MODES:
    raise SystemExit(f"Usage: python gather_review_input.py <mode>\nmode must be one of {VALID_MODES}")

# Both keys are OPTIONAL. Data-API keys only — no LLM API anywhere.
TWITTER_API_KEY = os.environ.get("TWITTER_API_KEY", "").strip()
FINNHUB_API_KEY = os.environ.get("FINNHUB_API_KEY", "").strip()

TWITTER_BASE = "https://api.twitterapi.io"
FINNHUB_BASE = "https://finnhub.io/api/v1"

DATA_JSON = Path("data.json")
OUT_MD = Path("raw_review_input.md")
OUT_JSON = Path("raw_review_input.json")
SOURCES_FILE = Path("sources/wallstreet.txt")
DEFAULT_ACCOUNTS = ["AIStockSavvy", "wallstengine", "DeIaone", "StockMKTNewz", "zerohedge", "financialjuice"]

MAX_TWEETS_PER_ACCOUNT = int(os.environ.get("MAX_TWEETS_PER_ACCOUNT", "10"))
MAX_TWEETS_FOR_REVIEW = int(os.environ.get("MAX_TWEETS_FOR_REVIEW", "40"))

PY_TO_HEB = {0: "שני", 1: "שלישי", 2: "רביעי", 3: "חמישי", 4: "שישי", 5: "שבת", 6: "ראשון"}


def israel_date_label(date_str: str) -> str:
    """Return visible Israeli date format D.M.YYYY from YYYY-MM-DD.
    Kept separate from machine dates, because data.json still needs ISO dates."""
    try:
        y, m, d = [int(x) for x in date_str.split("-")]
        return f"{d}.{m}.{y}"
    except Exception:
        return date_str


def israel_week_range_label(week_range: Optional[str]) -> str:
    if not week_range:
        return ""
    return week_range.replace("/", ".")

EXPECTED_FIRST_HEADING = {
    "daily_prep": "נקודות מרכזיות",
    "daily_summary": "סיכום המסחר",
    "weekly_summary": "סיכום השבוע",
}

FALLBACK_US_HOLIDAYS = [
    "2026-01-01", "2026-01-19", "2026-02-16", "2026-04-03", "2026-05-25",
    "2026-06-19", "2026-07-03", "2026-09-07", "2026-11-26", "2026-12-25",
]

CASHTAG_RE = re.compile(r"(?<![A-Za-z0-9_])\$([A-Z]{1,6})(?![A-Za-z0-9_])")
NON_TICKER = {
    "USD", "EUR", "GBP", "JPY", "USA", "EU", "UK", "AM", "PM", "ET", "ETF", "IPO", "API",
    "AI", "ML", "EPS", "CEO", "CFO", "FED", "GDP", "CPI", "PPI", "PMI", "ISM", "NFP",
    "FOMC", "VIX", "DXY", "SPX", "NDX", "DJI", "RUT",
}


def build_expected_title(mode: str, day_name: str, date_str: str, week_range: Optional[str]) -> str:
    visible_date = israel_date_label(date_str)
    if mode == "daily_prep":
        return f"נקודות חשובות לקראת פתיחת המסחר בוול סטריט 🇺🇸 – יום {day_name}, {visible_date}"
    if mode == "daily_summary":
        return f"סיכום יום המסחר בוול סטריט 🇺🇸 – יום {day_name}, {visible_date}"
    return f"סיכום שבוע המסחר בוול סטריט 🇺🇸 – {israel_week_range_label(week_range)}"


# ══════════════════════════════════════════════════════════════
# TRADING DAY / DATES
# ══════════════════════════════════════════════════════════════

def load_data_json() -> Dict[str, Any]:
    try:
        return json.loads(DATA_JSON.read_text(encoding="utf-8"))
    except Exception:
        return {}


def load_holidays() -> List[str]:
    holidays = load_data_json().get("marketStatus", {}).get("usHolidays2026", [])
    return holidays or FALLBACK_US_HOLIDAYS


def is_trading_day(dt: datetime, holidays: List[str]) -> bool:
    return dt.weekday() < 5 and dt.strftime("%Y-%m-%d") not in holidays


def get_next_trading_day(now: datetime, holidays: List[str]) -> datetime:
    d = now + timedelta(days=1)
    for _ in range(10):
        if is_trading_day(d, holidays):
            return d
        d += timedelta(days=1)
    return now + timedelta(days=1)


def get_last_trading_day(now: datetime, holidays: List[str]) -> datetime:
    if is_trading_day(now, holidays) and now.hour >= 23:
        return now
    d = now - timedelta(days=1)
    for _ in range(10):
        if is_trading_day(d, holidays):
            return d
        d -= timedelta(days=1)
    return now - timedelta(days=1)


def get_prev_week_range_str(now: datetime) -> str:
    weekday = now.weekday()
    monday = now - timedelta(days=weekday) if weekday >= 5 else now - timedelta(days=weekday + 7)
    friday = monday + timedelta(days=4)
    return f"{monday.strftime('%d/%m')}–{friday.strftime('%d/%m/%Y')}"


def compute_dates(mode: str, now: datetime, holidays: List[str]) -> Dict[str, Any]:
    date_str = now.strftime("%Y-%m-%d")
    day_name = PY_TO_HEB[now.weekday()]
    title_date_str, title_day_name = date_str, day_name
    week_range: Optional[str] = None
    target_is_trading = is_trading_day(now, holidays)

    if mode == "daily_prep":
        target = now if is_trading_day(now, holidays) else get_next_trading_day(now, holidays)
        title_date_str, title_day_name = target.strftime("%Y-%m-%d"), PY_TO_HEB[target.weekday()]
        target_is_trading = is_trading_day(target, holidays)
        review_date = title_date_str
    elif mode == "daily_summary":
        target = get_last_trading_day(now, holidays)
        title_date_str, title_day_name = target.strftime("%Y-%m-%d"), PY_TO_HEB[target.weekday()]
        review_date = title_date_str
    else:
        week_range = get_prev_week_range_str(now)
        weekday = now.weekday()
        monday = now - timedelta(days=weekday) if weekday >= 5 else now - timedelta(days=weekday + 7)
        review_date = (monday + timedelta(days=4)).strftime("%Y-%m-%d")

    return {
        "date_str": date_str, "day_name": day_name,
        "title_date_str": title_date_str, "title_day_name": title_day_name,
        "week_range": week_range, "target_is_trading": target_is_trading,
        "review_date": review_date,
    }


def get_time_conversion_block(now_il: datetime) -> str:
    ny = now_il.astimezone(NY_TZ)
    offset = int((now_il.utcoffset() - ny.utcoffset()).total_seconds() // 3600)

    def conv(h: int, m: int) -> str:
        return f"{h + offset}:{m:02d}"

    return f"""US-ISRAEL TIME OFFSET TODAY: +{offset} hours (add {offset} hours to US Eastern Time)
Key times in Israel time today:
- US economic data releases (CPI, NFP, PPI, GDP, Jobless Claims): {conv(8, 30)} שעון ישראל
- ISM PMI, JOLTS, Consumer Confidence: {conv(10, 0)} שעון ישראל
- FOMC rate decision / minutes: {conv(14, 0)} שעון ישראל | Fed Chair press conference: {conv(14, 30)} שעון ישראל
- US market open: {conv(9, 30)} שעון ישראל | US market close: {conv(16, 0)} שעון ישראל
USE ONLY THESE TIMES. Do NOT calculate your own offset."""


# ══════════════════════════════════════════════════════════════
# TWEETS (optional — skipped gracefully if no TWITTER_API_KEY)
# ══════════════════════════════════════════════════════════════

def read_accounts() -> List[str]:
    if SOURCES_FILE.exists():
        accounts = [
            line.strip().lstrip("@")
            for line in SOURCES_FILE.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.strip().startswith("#")
        ]
        if accounts:
            return accounts
    return DEFAULT_ACCOUNTS


def looks_like_tweet(x: Any) -> bool:
    return isinstance(x, dict) and isinstance(x.get("text") or x.get("fullText") or x.get("content"), str)


def find_tweets(obj: Any) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    if looks_like_tweet(obj):
        out.append(obj)
    elif isinstance(obj, list):
        for item in obj:
            out.extend(find_tweets(item))
    elif isinstance(obj, dict):
        for key in ("tweets", "data", "items", "results"):
            if key in obj:
                out.extend(find_tweets(obj[key]))
        if not out:
            for v in obj.values():
                out.extend(find_tweets(v))
    dedup: Dict[str, Dict[str, Any]] = {}
    for t in out:
        key = str(t.get("id") or t.get("url") or t.get("text") or "")
        if key:
            dedup[key] = t
    return list(dedup.values())


def normalize_tweet(tweet: Dict[str, Any], account: str) -> Dict[str, Any]:
    text = re.sub(r"\s+", " ", str(tweet.get("text") or tweet.get("fullText") or tweet.get("content") or "")).strip()
    return {
        "account": account,
        "createdAt": tweet.get("createdAt") or tweet.get("created_at") or tweet.get("date") or "",
        "text": text,
        "cashtags": sorted({m.group(1).upper() for m in CASHTAG_RE.finditer(text)}),
        "likeCount": int(tweet.get("likeCount") or 0),
        "viewCount": int(tweet.get("viewCount") or 0),
        "is_retweet": text.startswith("RT @"),
    }


def tweet_score(t: Dict[str, Any]) -> float:
    text = t["text"].lower()
    score = 30.0 if t["cashtags"] else 0.0
    keywords = [
        "breaking", "just in", "fed", "fomc", "cpi", "ppi", "pce", "jobs", "payrolls", "claims",
        "earnings", "guidance", "upgrade", "downgrade", "price target", "contract", "ipo",
        "ai", "nvidia", "apple", "google", "tesla", "semiconductor", "chips", "m&a", "acquisition",
        "oil", "gold", "yield", "treasury", "dollar", "tariff", "futures", "nasdaq", "s&p",
    ]
    score += 7 * sum(1 for k in keywords if k in text)
    if t["viewCount"] >= 100000:
        score += 15
    elif t["viewCount"] >= 25000:
        score += 8
    if t["likeCount"] >= 500:
        score += 10
    elif t["likeCount"] >= 100:
        score += 5
    if t["is_retweet"]:
        score -= 25
    return score


def fetch_and_select_tweets() -> Tuple[str, List[str]]:
    """Returns (formatted tweet blocks, top cashtags mentioned)."""
    if not TWITTER_API_KEY:
        print("  No TWITTER_API_KEY — skipping tweets (the review will rely on the chat model's web search)")
        return "", []
    all_tweets: List[Dict[str, Any]] = []
    for acc in read_accounts():
        try:
            r = requests.get(
                f"{TWITTER_BASE}/twitter/user/last_tweets",
                headers={"X-API-Key": TWITTER_API_KEY},
                params={"userName": acc, "includeReplies": "false"},
                timeout=25,
            )
            print(f"  @{acc}: status={r.status_code}")
            if not r.ok:
                print(f"    -> Error: {r.text[:200]}")
                continue
            tweets = [normalize_tweet(t, acc) for t in find_tweets(r.json())]
            tweets = [t for t in tweets if t["text"]]
            print(f"    -> {len(tweets)} tweets")
            all_tweets.extend(tweets[:MAX_TWEETS_PER_ACCOUNT])
        except Exception as e:
            print(f"  Error fetching @{acc}: {e}")
    dedup = {t["text"]: t for t in all_tweets}
    selected = sorted(dedup.values(), key=tweet_score, reverse=True)[:MAX_TWEETS_FOR_REVIEW]
    if not selected:
        print("  ⚠️  Zero usable tweets — continuing with market data only")
        return "", []
    counts: Dict[str, int] = {}
    blocks = []
    for t in selected:
        ts = f" [{t['createdAt']}]" if t["createdAt"] else ""
        blocks.append(f"@{t['account']}{ts}: {t['text']}")
        for c in t["cashtags"]:
            if c not in NON_TICKER:
                counts[c] = counts.get(c, 0) + 1
    top_cashtags = [s for s, _ in sorted(counts.items(), key=lambda x: -x[1])[:12]]
    print(f"  Selected {len(selected)} of {len(dedup)} unique tweets; cashtags: {top_cashtags}")
    return "\n\n".join(blocks), top_cashtags


# ══════════════════════════════════════════════════════════════
# FINNHUB — verified market data, weekly, econ calendar, ticker snapshot
# ══════════════════════════════════════════════════════════════

FINNHUB_SYMBOLS = {
    "SPY": "S&P 500 (SPY ETF)", "QQQ": "Nasdaq 100 (QQQ ETF)", "DIA": "Dow Jones (DIA ETF)",
    "IWM": "Russell 2000 (IWM ETF)",
    "XLE": "Energy Sector (XLE ETF)", "XLK": "Technology Sector (XLK ETF)",
    "XLF": "Financials Sector (XLF ETF)", "XLY": "Consumer Discretionary Sector (XLY ETF)",
    "XLV": "Healthcare Sector (XLV ETF)", "XLI": "Industrials Sector (XLI ETF)",
    "XLP": "Consumer Staples Sector (XLP ETF)", "XLU": "Utilities Sector (XLU ETF)",
    "USO": "WTI Crude Oil (USO ETF)", "BNO": "Brent Crude Oil (BNO ETF)",
    "GLD": "Gold (GLD ETF)", "SLV": "Silver (SLV ETF)", "IBIT": "Bitcoin (IBIT ETF)",
    "TLT": "US 20Y+ Bonds (TLT ETF)", "UUP": "US Dollar (UUP ETF)", "VIXY": "VIX Volatility (VIXY ETF)",
}
WEEKLY_SYMBOLS = ["SPY", "QQQ", "DIA", "IWM", "XLE", "XLK", "XLF", "XLY", "XLV", "USO", "BNO", "GLD", "IBIT", "TLT"]

DIRECTION_ASSETS_LABELS = [
    (["USO", "BNO"], "נפט (WTI/Brent proxies)"),
    (["GLD"], "זהב"),
    (["IBIT"], "ביטקוין"),
    (["UUP"], "דולר"),
    (["VIXY"], "תנודתיות / VIX"),
    (["TLT"], "אג\"ח ארוכות / TLT"),
]


def finnhub_quote(symbol: str) -> Optional[Dict[str, float]]:
    try:
        r = requests.get(f"{FINNHUB_BASE}/quote", params={"symbol": symbol, "token": FINNHUB_API_KEY}, timeout=8)
        if not r.ok:
            return None
        d = r.json()
        price, pct, prev = float(d.get("c") or 0), float(d.get("dp") or 0), float(d.get("pc") or 0)
        if price <= 0 or prev <= 0:
            return None
        return {"price": price, "pct": pct, "prev_close": prev}
    except Exception as e:
        print(f"  Finnhub error for {symbol}: {e}")
        return None


def direction_word(pct: float, threshold: float = 0.15) -> str:
    if pct >= threshold:
        return "עולה"
    if pct <= -threshold:
        return "יורד"
    return "יציב/כמעט ללא שינוי"


def fetch_weekly_lines() -> List[str]:
    lines: List[str] = []
    now_ts = int(time.time())
    from_ts = now_ts - 14 * 86400
    for symbol in WEEKLY_SYMBOLS:
        label = FINNHUB_SYMBOLS.get(symbol, symbol)
        try:
            r = requests.get(
                f"{FINNHUB_BASE}/stock/candle",
                params={"symbol": symbol, "resolution": "D", "from": from_ts, "to": now_ts, "token": FINNHUB_API_KEY},
                timeout=8,
            )
            if not r.ok:
                continue
            d = r.json()
            closes, stamps = d.get("c") or [], d.get("t") or []
            if len(closes) < 5:
                continue
            dated = [(datetime.fromtimestamp(ts, tz=timezone.utc), c) for ts, c in zip(stamps, closes)]
            today = datetime.now(timezone.utc)
            this_week = [(dt, c) for dt, c in dated if dt.isocalendar()[:2] == today.isocalendar()[:2]]
            if not this_week:
                last_wk = dated[-1][0].isocalendar()[:2]
                this_week = [(dt, c) for dt, c in dated if dt.isocalendar()[:2] == last_wk]
            before = [c for dt, c in dated if dt < this_week[0][0]]
            if not before:
                continue
            prev_close, week_close = before[-1], this_week[-1][1]
            pct = (week_close - prev_close) / prev_close * 100
            lines.append(f"  {label}: weekly {pct:+.2f}% (from ${prev_close:.2f} to ${week_close:.2f})")
            print(f"  Finnhub {symbol} WEEKLY: {pct:+.2f}%")
        except Exception as e:
            print(f"  Finnhub weekly error for {symbol}: {e}")
    return lines


def fetch_market_data(weekly: bool, top_cashtags: List[str]) -> Tuple[str, Dict[str, float], Dict[str, Dict[str, float]]]:
    """Returns (prompt_block, etf_pcts, ticker_quotes_snapshot).
    The snapshot lets paste_review.py verify ticker directions later without a live API."""
    if not FINNHUB_API_KEY:
        print("  No FINNHUB_API_KEY — skipping market data")
        return "", {}, {}
    lines: List[str] = []
    pcts: Dict[str, float] = {}
    for symbol, label in FINNHUB_SYMBOLS.items():
        q = finnhub_quote(symbol)
        if q:
            pcts[symbol] = q["pct"]
            lines.append(f"  {label}: ${q['price']:.2f} (daily: {q['pct']:+.2f}%), prev close: ${q['prev_close']:.2f}")
            print(f"  Finnhub {symbol}: ${q['price']:.2f} ({q['pct']:+.2f}%)")
    if not lines:
        return "", {}, {}

    # Snapshot quotes for the tickers the tweets talk about — the review will
    # most likely mention these, and the publish step verifies directions.
    ticker_quotes: Dict[str, Dict[str, float]] = {}
    for t in top_cashtags:
        q = finnhub_quote(t)
        if q:
            ticker_quotes[t] = q
            print(f"  Ticker snapshot {t}: ${q['price']:.2f} ({q['pct']:+.2f}%)")

    block = [
        "══ VERIFIED MARKET DATA (from Finnhub API — these are FACTS, do NOT override with guesses) ══",
        "DAILY PERFORMANCE:",
        *lines,
    ]
    if ticker_quotes:
        block += ["", "INDIVIDUAL STOCKS mentioned in the source tweets (verified quotes):"]
        for t, q in ticker_quotes.items():
            block.append(f"  ${t}: ${q['price']:.2f} (daily: {q['pct']:+.2f}%), prev close: ${q['prev_close']:.2f}")
    if weekly:
        weekly_lines = fetch_weekly_lines()
        if weekly_lines:
            block += ["", "WEEKLY PERFORMANCE (use these for the weekly summary, NOT the daily numbers):", *weekly_lines]

    block += ["", "DIRECTIONAL FACTS — Hebrew direction words (עולה/יורד/צונח/מזנק) MUST match these:"]
    for symbols, label in DIRECTION_ASSETS_LABELS:
        vals = [(s, pcts[s]) for s in symbols if s in pcts]
        if not vals:
            continue
        dirs = {direction_word(p) for _, p in vals}
        word = dirs.pop() if len(dirs) == 1 else "מעורב — להשתמש בניסוח ניטרלי בלבד"
        block.append(f"  {label}: {word} ({', '.join(f'{s}: {p:+.2f}%' for s, p in vals)})")

    block += [
        "",
        "The % changes above are ACCURATE — use them for direction and magnitude.",
        "For exact index LEVELS (points), gold/oil absolute prices, VIX level, Bitcoin price, 10Y yield: verify via web search. Do NOT estimate them from ETF prices.",
        "For sector performance (XLE/XLK/...): USE ONLY the Finnhub numbers above — never invent sector percentages.",
        "If ANY percentage you write contradicts the data above, you are WRONG. Fix it.",
        "══════════════════════════════════════════════════════════════════════════════",
    ]
    return "\n".join(block), pcts, ticker_quotes


def fetch_economic_data(days_back: int, days_forward: int) -> str:
    if not FINNHUB_API_KEY:
        return ""
    now = datetime.now(ISR_TZ)
    try:
        r = requests.get(
            f"{FINNHUB_BASE}/calendar/economic",
            params={
                "from": (now - timedelta(days=days_back)).strftime("%Y-%m-%d"),
                "to": (now + timedelta(days=days_forward)).strftime("%Y-%m-%d"),
                "token": FINNHUB_API_KEY,
            },
            timeout=12,
        )
        if not r.ok:
            print(f"  Finnhub economic calendar: status {r.status_code}")
            return ""
        us_events = []
        for e in r.json().get("economicCalendar", []):
            if e.get("country") != "US" or e.get("actual") is None:
                continue
            unit = e.get("unit", "")
            line = f"  {e.get('time', '')[:10]} | {e.get('event', '')}: actual={e['actual']}{unit}"
            if e.get("estimate") is not None:
                line += f", forecast={e['estimate']}{unit}"
            if e.get("prev") is not None:
                line += f", previous={e['prev']}{unit}"
            if e.get("impact"):
                line += f" [{e['impact']} impact]"
            us_events.append(line)
            print(f"  Econ: {e.get('event', '')} = {e['actual']}{unit}")
        if not us_events:
            return ""
        return "\n".join([
            "══ VERIFIED US ECONOMIC DATA (from Finnhub — FACTS, you MUST include them) ══",
            *us_events,
            "- Every data point above MUST appear in the review, woven into analytical bullets (not raw numbers).",
            "- Always explain WHY the number matters for Fed policy / markets.",
            "- Do NOT say data 'is expected' if it already has an actual value above — it was ALREADY released.",
            "══════════════════════════════════════════════════════════════════════════════",
        ])
    except Exception as e:
        print(f"  Finnhub economic calendar error: {e}")
        return ""


def get_macro_checklist(mode: str, date_str: str, week_range: Optional[str]) -> str:
    visible_date = israel_date_label(date_str)
    visible_week = israel_week_range_label(week_range)
    if mode == "daily_summary":
        return f"""══ MANDATORY MACRO DATA CHECK ══
Use web search to check if ANY of these were released on {visible_date}: CPI (headline AND core),
PPI (headline AND core), NFP, Jobless Claims, Consumer Sentiment (Michigan), ISM PMI, GDP,
Retail Sales, FOMC decision/minutes. If released — include with actual, forecast, previous,
AND the market implication. If none — skip, but you MUST check first.
Use Israeli date format in visible Hebrew text. Do not write ISO dates such as YYYY-MM-DD.
══════════════════════════════════"""
    if mode == "weekly_summary":
        return f"""══ MANDATORY MACRO DATA CHECK ══
Use web search to find ALL major US economic data released during the week of {visible_week or visible_date}:
CPI (headline+core, monthly+annual), PPI, NFP/employment, Jobless Claims, Consumer Sentiment,
ISM PMI, FOMC, GDP, Retail Sales. For EVERY data point: actual, forecast, previous, market implication.
Do NOT skip Core CPI if headline CPI was released. Do NOT write 'expected' about data already released.
Use Israeli date format in visible Hebrew text. Do not write ISO dates such as YYYY-MM-DD.
══════════════════════════════════"""
    return f"""══ SCHEDULED DATA CHECK ══
Use web search to find what US economic data is scheduled for release on {visible_date}.
Include the release time in Israel time and the market consensus/forecast.
If a data point is scheduled for the future, do NOT write that the actual value does not exist.
Simply write the scheduled time, consensus/forecast, and previous reading.
Use Israeli date format in visible Hebrew text. Do not write ISO dates such as YYYY-MM-DD.
══════════════════════════════════"""


def get_prior_review_context(mode: str, data: Dict[str, Any]) -> str:
    if mode == "daily_prep":
        prior = data.get("dailySummary")
        header = ("══ CONTEXT: YESTERDAY'S DAILY SUMMARY — DO NOT REPEAT THIS CONTENT ══\n"
                  "Already published. Your briefing is FORWARD-LOOKING. Mention an item below ONLY if there is a genuinely NEW overnight development about it.")
    elif mode == "daily_summary":
        prior = data.get("dailyPrep")
        header = ("══ CONTEXT: THIS MORNING'S PRE-MARKET BRIEFING ══\n"
                  "Published before the session. Use it to resolve scheduled items (expected → actual), do NOT quote it verbatim.")
    else:
        return ""
    if not (prior and prior.get("sections")):
        return ""
    content = "\n\n".join(f"[{s.get('heading', '')}]\n{s.get('content', '')}" for s in prior["sections"])
    return f"{header}\n\n{content}\n══════════════════════════════════════════════════════════════"


# ══════════════════════════════════════════════════════════════
# PROMPT — the full paste-ready instruction block
# ══════════════════════════════════════════════════════════════

SHARED_RULES = """Rules:
- Write ONLY in Hebrew. English only for tickers ($AAPL), index names (S&P 500), and well-known financial terms in parentheses on first use.
- Be specific: every claim must include a number, percentage, or ticker. No vague statements.
- Do NOT repeat information across bullets. One company = one bullet (merge multiple news items).
- No buy/sell recommendations, no price targets of your own, no "כדאי לקנות/למכור".
- EVERY number must come from: (1) the verified Finnhub data above, (2) a specific tweet, or (3) your web search. NEVER invent, estimate, or recall numbers from memory. When in doubt, omit.
- If a tweet contradicts the Finnhub data, the Finnhub data is correct.
- Directional words (צונח/יורד/מזנק/עולה) are factual claims — they MUST match the DIRECTIONAL FACTS block.
- Sector percentages (XLE/XLK/...) — ONLY from the Finnhub data. Missing sector → omit.
- Never claim an all-time high (שיא כל הזמנים) without web-search verification.
- CPI mentioned → ALWAYS both headline AND Core CPI. Economic data → always actual vs forecast vs previous.
- IPO (הנפקה ראשונית) ≠ ETF (תעודת סל). Nasdaq 100 (QQQ, ~NDX) ≠ Nasdaq Composite (IXIC) — never mix their levels.
- Attribution: Claude→Anthropic, ChatGPT→OpenAI, Gemini→Google. Donald Trump is the CURRENT US President — never "לשעבר".
- No URLs, no Markdown links, no source domains in brackets. Attribution style: לפי Reuters / לפי Bloomberg only.
- Visible dates must use Israeli format only, for example: יום שני, 6.7.2026. Do NOT write YYYY-MM-DD inside the Hebrew review text.
- Do NOT use the semicolon character ; anywhere in the visible review. Use a comma or a full stop.
- For future scheduled data, do NOT write "נתון בפועל עדיין לא קיים" or any equivalent. Write only the scheduled time, consensus/forecast, and previous reading.
- Do NOT start bullets with raw tickers such as $TSLA or $AMZN. Use natural wording: מניית טסלה (TSLA): or מניית אמזון (AMZN):.
- Finnhub is a background validation layer only. Never mention "Finnhub", "האינדיקציה מ-Finnhub", or ETF-proxy phrasing such as "דרך USO" in the visible review.
- Commodities/currencies must be written as a short human market paragraph, not as a mechanical list of ETF proxies.
- Avoid broken RTL/ticker formatting. Prefer Hebrew company name + ticker in parentheses."""


def mode_instructions(mode: str, d: Dict[str, Any]) -> str:
    run_visible_date = israel_date_label(d["date_str"])
    target_visible_date = israel_date_label(d["title_date_str"])
    if mode == "daily_prep":
        if d["target_is_trading"]:
            if d["date_str"] == d["title_date_str"]:
                status = ("The briefing is for TODAY. The US cash market has NOT opened yet — never describe it as open, "
                          "trading, or having reacted. Use 'השוק צפוי להיפתח', 'המשקיעים יעקבו אחר'. Futures may be described "
                          "in present tense; the cash market may not.")
            else:
                status = (f"This runs on {run_visible_date} but the briefing is for the NEXT trading day: {target_visible_date} "
                          f"(יום {d['title_day_name']}). Do NOT use 'היום'/'הבוקר' — use 'ביום {d['title_day_name']}'. "
                          f"Do NOT describe futures/pre-market as live — they are not available yet.")
        else:
            status = f"The target date {target_visible_date} is NOT a trading day (weekend/US holiday). State this in the first bullet."
        return f"""You are a senior Wall Street market analyst writing a PRE-MARKET briefing in Hebrew.
Script run date: {run_visible_date} (יום {d['day_name']}). Briefing target date: {target_visible_date} (יום {d['title_day_name']}).
{status}

FORWARD-LOOKING ONLY: no yesterday's index performance, no closing levels, zero backward-looking data,
and nothing that already appears in the prior-context block. 7-12 bullets covering: scheduled economic data
(Israel times + consensus), expected earnings, NEW overnight geopolitical developments (always with the market
transmission mechanism: event → oil → inflation → rates → equities), NEW overnight company news and analyst moves,
commodity/currency signals. Futures: direction only unless a specific futures percentage appears in the sources —
never copy an ETF percentage as a futures percentage."""
    if mode == "daily_summary":
        return f"""You are a senior Wall Street market analyst writing an end-of-day market wrap in Hebrew for
{target_visible_date} (יום {d['title_day_name']}). PAST TENSE. Explain WHY things happened, not just what.
7-12 bullets ordered by market impact: index performance (%, point levels, context), macro data with FULL numbers
and market reaction, key market-moving events with cause-and-effect, commodities/currencies/VIX with %,
notable stock moves with the reason ($TICKER +/- %), sector rotation (ONLY from the Finnhub sector data).
If two bullets describe causally linked events, merge them into one bullet that explains the link."""
    return f"""You are a senior Wall Street strategist writing a weekly review in Hebrew for the trading week
{israel_week_range_label(d['week_range'])}. PAST TENSE. ONLY events and moves from THIS specific week.
Use the WEEKLY PERFORMANCE numbers for weekly index changes — NOT the daily numbers, and never confuse
Friday's daily change with the weekly change. 8-14 bullets: weekly index performance with leading/lagging sectors,
all macro data of the week with FULL numbers, key market-moving events with the transmission mechanism,
commodities with weekly context, notable company news/earnings/M&A merged where related, earnings-season outlook."""


def build_paste_block(mode: str, d: Dict[str, Any], expected_title: str, market_block: str,
                      econ_block: str, checklist: str, prior_context: str, tweets: str,
                      now_il: datetime) -> str:
    first_heading = EXPECTED_FIRST_HEADING[mode]
    parts = [
        "אתה כותב סקירה פיננסית בעברית לאתר. קרא את כל ההנחיות והנתונים למטה, השתמש בחיפוש אינטרנט לאימות, והחזר JSON בלבד.",
        "",
        mode_instructions(mode, d),
        "",
        SHARED_RULES,
        "",
        f"""CRITICAL — OUTPUT FORMAT (MANDATORY):
- Return ONLY a JSON object, no backticks, no explanations, in EXACTLY this structure:
{{
  "title": "{expected_title}",
  "date": "{d['review_date']}",
  "sections": [
    {{
      "heading": "{first_heading}",
      "content": "* נושא ראשון: משפט אנליטי תמציתי עם מספרים.\\n* נושא שני: ...\\n* נושא שלישי: ..."
    }}
  ]
}}
- EXACTLY 1 section. Heading EXACTLY "{first_heading}". Title EXACTLY as given above.
- content = one string, bullets separated by \\n, each bullet starts with "* ".
- No "שורה תחתונה"/summary section — merge any concluding insight as a regular bullet.
- No **, no ##, no HTML, no URLs inside content.
- The visible title may contain Israeli date format. The JSON date field may remain ISO for the site logic, but do not copy ISO dates into content.
- If you write any bullet about a stock, start it naturally, for example: "* מניית אמזון (AMZN): ..." not "* $AMZN: ...".""",
        "",
        get_time_conversion_block(now_il),
    ]
    for block in (market_block, econ_block, checklist, prior_context):
        if block:
            parts += ["", block]
    if tweets:
        parts += ["", f"Source tweets/posts from X (Twitter) — gathered {d['date_str']}. Never mention in the review that these came from tweets/posts:", "", tweets]
    else:
        parts += ["", "NOTE: no tweets were gathered for this run. Base the review on the verified data above plus your own web search of today's major market news from reliable sources (Reuters, Bloomberg, CNBC)."]
    parts += ["", "החזר עכשיו אך ורק את ה-JSON בפורמט שהוגדר למעלה."]
    return "\n".join(parts)


# ══════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════

def main() -> None:
    now = datetime.now(ISR_TZ)
    holidays = load_holidays()
    d = compute_dates(REVIEW_MODE, now, holidays)
    expected_title = build_expected_title(REVIEW_MODE, d["title_day_name"], d["title_date_str"], d["week_range"])

    print(f"Gathering raw input: {REVIEW_MODE} for {d['date_str']} ({d['day_name']})")
    print(f"  Target: {d['title_date_str']} ({d['title_day_name']}), week_range: {d['week_range']}")
    print(f"  Expected title: {expected_title}")

    print("\n── Tweets ──")
    tweets, top_cashtags = fetch_and_select_tweets()

    print("\n── Finnhub market data ──")
    market_block, pcts, ticker_quotes = fetch_market_data(REVIEW_MODE == "weekly_summary", top_cashtags)

    print("\n── Economic calendar ──")
    econ_days = {"daily_prep": (1, 1), "daily_summary": (1, 0), "weekly_summary": (7, 0)}[REVIEW_MODE]
    econ_block = fetch_economic_data(*econ_days)
    checklist = get_macro_checklist(REVIEW_MODE, d["date_str"], d["week_range"])

    prior_context = get_prior_review_context(REVIEW_MODE, load_data_json())
    if prior_context:
        print(f"  Injected prior-review context ({len(prior_context)} chars)")

    paste_block = build_paste_block(
        REVIEW_MODE, d, expected_title, market_block, econ_block, checklist,
        prior_context, tweets, now,
    )
    OUT_MD.write_text(paste_block, encoding="utf-8")

    snapshot = {
        "mode": REVIEW_MODE,
        "generated_at": now.isoformat(),
        "expected_title": expected_title,
        "first_heading": EXPECTED_FIRST_HEADING[REVIEW_MODE],
        "review_date": d["review_date"],
        "title_date_str": d["title_date_str"],
        "title_day_name": d["title_day_name"],
        "week_range": d["week_range"],
        "etf_pcts": pcts,
        "ticker_quotes": ticker_quotes,
    }
    OUT_JSON.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\n✅ Wrote {OUT_MD} ({len(paste_block):,} chars) — copy its ENTIRE content into Claude/ChatGPT.")
    print(f"✅ Wrote {OUT_JSON} (snapshot for the publish step).")
    print("\nNext steps:")
    print("  1. Copy all of raw_review_input.md into Claude or ChatGPT (with web search enabled).")
    print("  2. Save the JSON reply into review_output.json.")
    print("  3. Run: python paste_review.py   (validates + publishes into data.json)")


if __name__ == "__main__":
    main()
