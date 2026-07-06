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

VALID_MODES = ("daily_prep", "daily_summary", "weekly_summary", "intraday_update")
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
DEFAULT_ACCOUNTS = ["StockMKTNewz", "AIStockSavvy", "wallstengine", "KobeissiLetter", "gurgavin"]

MAX_TWEETS_PER_ACCOUNT = int(os.environ.get("MAX_TWEETS_PER_ACCOUNT", "10"))
MAX_TWEETS_FOR_REVIEW = int(os.environ.get("MAX_TWEETS_FOR_REVIEW", "40"))

PY_TO_HEB = {0: "שני", 1: "שלישי", 2: "רביעי", 3: "חמישי", 4: "שישי", 5: "שבת", 6: "ראשון"}

EXPECTED_FIRST_HEADING = {
    "daily_prep": "נקודות מרכזיות",
    "daily_summary": "סיכום המסחר",
    "weekly_summary": "סיכום השבוע",
    "intraday_update": "עדכון ביניים",
}

INTRADAY_WINDOW_HOURS = 2

FALLBACK_US_HOLIDAYS = [
    "2026-01-01", "2026-01-19", "2026-02-16", "2026-04-03", "2026-05-25",
    "2026-06-19", "2026-07-03", "2026-09-07", "2026-11-26", "2026-12-25",
]

# Promotional/engagement-bait tweets (webinars, giveaways) carry no market news —
# in the tight intraday window they crowd out real headlines, so drop them there.
PROMO_TWEET_RE = re.compile(
    r"giveaway|webinar|sweepstakes?|promo code|discount code|affiliate link|"
    r"secure your seats?|winners will be|like & (?:rt|retweet)|rt this post|"
    r"comment a ticker|tap the bell",
    re.IGNORECASE,
)

CASHTAG_RE = re.compile(r"(?<![A-Za-z0-9_])\$([A-Z]{1,6})(?![A-Za-z0-9_])")
NON_TICKER = {
    "USD", "EUR", "GBP", "JPY", "USA", "EU", "UK", "AM", "PM", "ET", "ETF", "IPO", "API",
    "AI", "ML", "EPS", "CEO", "CFO", "FED", "GDP", "CPI", "PPI", "PMI", "ISM", "NFP",
    "FOMC", "VIX", "DXY", "SPX", "NDX", "DJI", "RUT",
}


def heb_date(date_str: str) -> str:
    """'2026-07-06' → '6.7.2026' — Israeli display format for visible text."""
    try:
        y, m, d = date_str.split("-")
        return f"{int(d)}.{int(m)}.{y}"
    except Exception:
        return date_str


def build_expected_title(mode: str, day_name: str, date_str: str, week_range: Optional[str],
                         time_str: Optional[str] = None) -> str:
    if mode == "daily_prep":
        return f"נקודות חשובות לקראת פתיחת המסחר בוול סטריט 🇺🇸 – יום {day_name}, {heb_date(date_str)}"
    if mode == "daily_summary":
        return f"סיכום יום המסחר בוול סטריט 🇺🇸 – יום {day_name}, {heb_date(date_str)}"
    if mode == "intraday_update":
        return f"עדכון ביניים מוול סטריט 🇺🇸 – יום {day_name}, {heb_date(date_str)}, {time_str}"
    return f"סיכום שבוע המסחר בוול סטריט 🇺🇸 – {week_range}"


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


def get_market_state(now_il: datetime, holidays: List[str]) -> str:
    """US market session right now: open / premarket / afterhours / closed."""
    ny = now_il.astimezone(NY_TZ)
    if not is_trading_day(ny, holidays):
        return "closed"
    t = (ny.hour, ny.minute)
    if t < (4, 0):
        return "closed"
    if t < (9, 30):
        return "premarket"
    if t < (16, 0):
        return "open"
    if t < (20, 0):
        return "afterhours"
    return "closed"


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
    elif mode == "intraday_update":
        review_date = date_str
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
        "time_str": now.strftime("%H:%M"),
        "window_from": (now - timedelta(hours=INTRADAY_WINDOW_HOURS)).strftime("%H:%M"),
        "market_state": get_market_state(now, holidays),
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


def parse_tweet_time(s: str) -> Optional[datetime]:
    """Parses the createdAt formats TwitterAPI.io returns. None if unparseable."""
    s = str(s or "").strip()
    if not s:
        return None
    try:  # classic Twitter format: "Thu Jul 03 17:40:12 +0000 2026"
        return datetime.strptime(s, "%a %b %d %H:%M:%S %z %Y")
    except ValueError:
        pass
    try:  # ISO 8601, with or without Z
        dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except ValueError:
        return None


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


def fetch_and_select_tweets(since: Optional[datetime] = None) -> Tuple[str, List[str]]:
    """Returns (formatted tweet blocks, top cashtags mentioned).
    since — keep only tweets created at/after this moment (intraday window)."""
    if not TWITTER_API_KEY:
        print("  No TWITTER_API_KEY — skipping tweets (the review will rely on the chat model's web search)")
        return "", []
    # With a time window most tweets get dropped, so take more per account.
    per_account = MAX_TWEETS_PER_ACCOUNT * 2 if since is not None else MAX_TWEETS_PER_ACCOUNT
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
            all_tweets.extend(tweets[:per_account])
        except Exception as e:
            print(f"  Error fetching @{acc}: {e}")
    dedup = {t["text"]: t for t in all_tweets}
    pool = list(dedup.values())
    if since is not None:
        in_window, too_old, unparsed, promo = [], 0, 0, 0
        for t in pool:
            ts = parse_tweet_time(t["createdAt"])
            if ts is None:
                unparsed += 1
            elif ts < since:
                too_old += 1
            elif PROMO_TWEET_RE.search(t["text"]):
                promo += 1
            else:
                in_window.append(t)
        print(f"  Time-window filter (since {since.astimezone(ISR_TZ):%H:%M} Israel): "
              f"kept {len(in_window)}, dropped {too_old} older, {promo} promotional, "
              f"{unparsed} unparseable timestamps")
        pool = in_window
    selected = sorted(pool, key=tweet_score, reverse=True)[:MAX_TWEETS_FOR_REVIEW]
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
    (["USO", "BNO"], "נפט (WTI/ברנט)"),
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
        "The ETF tickers above (SPY/QQQ/DIA/USO/GLD/...) are measurement instruments for YOUR verification only — NEVER name them, Finnhub, or the word 'proxy' in the visible Hebrew text.",
        "For exact index LEVELS (points), gold/oil absolute prices, VIX level, Bitcoin price, 10Y yield: verify via web search. Do NOT estimate them from ETF prices.",
        "For sector performance (XLE/XLK/...): USE ONLY the Finnhub numbers above — never invent sector percentages.",
        "If ANY percentage you write contradicts the data above, you are WRONG. Fix it.",
        "══════════════════════════════════════════════════════════════════════════════",
    ]
    return "\n".join(block), pcts, ticker_quotes


def parse_econ_time(s: str) -> Optional[datetime]:
    """Finnhub economic-calendar 'time' is UTC, e.g. '2026-07-03 12:30:00'."""
    s = str(s or "").strip()
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M"):
        try:
            return datetime.strptime(s, fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    return None


def fetch_economic_data(days_back: int, days_forward: int, since: Optional[datetime] = None) -> str:
    """since — intraday window start: keep only releases at/after it. Data released
    yesterday or earlier today must NOT reach the intraday update with a MUST-include order."""
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
        dropped_outside_window = 0
        for e in r.json().get("economicCalendar", []):
            if e.get("country") != "US" or e.get("actual") is None:
                continue
            if since is not None:
                event_dt = parse_econ_time(e.get("time", ""))
                if event_dt is None or event_dt < since:
                    dropped_outside_window += 1
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
        if since is not None:
            print(f"  Econ window filter: kept {len(us_events)}, dropped {dropped_outside_window} outside the window")
        if not us_events:
            return ""
        header = (
            "══ VERIFIED US ECONOMIC DATA RELEASED INSIDE THE TWO-HOUR WINDOW (from Finnhub — FACTS, you MUST include them) ══"
            if since is not None else
            "══ VERIFIED US ECONOMIC DATA (from Finnhub — FACTS, you MUST include them) ══"
        )
        return "\n".join([
            header,
            *us_events,
            "- Every data point above MUST appear in the review, woven into analytical bullets (not raw numbers).",
            "- Always explain WHY the number matters for Fed policy / markets.",
            "- Do NOT say data 'is expected' if it already has an actual value above — it was ALREADY released.",
            "══════════════════════════════════════════════════════════════════════════════",
        ])
    except Exception as e:
        print(f"  Finnhub economic calendar error: {e}")
        return ""


def get_macro_checklist(mode: str, date_str: str, week_range: Optional[str],
                        window: Optional[str] = None) -> str:
    if mode == "intraday_update":
        return f"""══ WEB SEARCH POLICY ══
Web search is for VERIFICATION ONLY — confirming numbers, times and names that already appear in the source
tweets or in the verified data blocks, for the window {window} Israel time on {date_str}. Do NOT use it to
find additional news, headlines or macro data. Content that is not present in the tweets does not enter the update.
══════════════════════════════════"""
    if mode == "daily_summary":
        return f"""══ MANDATORY MACRO DATA CHECK ══
Use web search to check if ANY of these were released on {date_str}: CPI (headline AND core),
PPI (headline AND core), NFP, Jobless Claims, Consumer Sentiment (Michigan), ISM PMI, GDP,
Retail Sales, FOMC decision/minutes. If released — include with actual, forecast, previous,
AND the market implication. If none — skip, but you MUST check first.
══════════════════════════════════"""
    if mode == "weekly_summary":
        return f"""══ MANDATORY MACRO DATA CHECK ══
Use web search to find ALL major US economic data released during the week of {week_range or date_str}:
CPI (headline+core, monthly+annual), PPI, NFP/employment, Jobless Claims, Consumer Sentiment,
ISM PMI, FOMC, GDP, Retail Sales. For EVERY data point: actual, forecast, previous, market implication.
Do NOT skip Core CPI if headline CPI was released. Do NOT write 'expected' about data already released.
══════════════════════════════════"""
    return f"""══ SCHEDULED DATA CHECK ══
Use web search to find what US economic data is scheduled for release on {date_str}.
Include the release time in Israel time and the market consensus/forecast.
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
    elif mode == "intraday_update":
        candidates = [data.get(k) for k in ("intradayUpdate", "dailySummary", "dailyPrep")]
        prior = max(
            (p for p in candidates if isinstance(p, dict) and p.get("date") and p.get("sections")),
            key=lambda p: str(p.get("date", "")), default=None,
        )
        header = ("══ CONTEXT: THE MOST RECENT PUBLISHED REVIEW — DO NOT REPEAT THIS CONTENT ══\n"
                  "Already published on the site. Your update covers ONLY the last two hours. Mention an item "
                  "below ONLY if there is a genuinely NEW development about it inside the two-hour window.")
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
- Dates in visible text: Israeli format ONLY, e.g. "יום שני, 6.7.2026". NEVER write an ISO date (2026-07-06) inside the title or the bullets.
- NEVER use the ";" character anywhere. Use a comma or start a new sentence instead.
- Never write "נתון בפועל עדיין לא קיים". If a figure has not been released yet, give only the forecast (צפי) and the previous reading (נתון קודם).
- Never OPEN a bullet with a raw ticker like "$TSLA:" or "$AMZN:". Open with the Hebrew company name: "מניית טסלה (TSLA):", "מניית אמזון (AMZN):", "מניית מטא (META):".
- Finnhub and the measurement ETFs (SPY/QQQ/DIA/USO/BNO/GLD/UUP/VIXY/TLT...) are a hidden verification layer ONLY. NEVER mention Finnhub, "proxy", "דרך USO", "האינדיקציה מ-", or any technical data-source wording in the visible text — describe the asset itself (נפט, זהב, דולר, תשואות) directly.
- SIGN-FLIP: if the verified data shows a stock DOWN, do NOT describe it positively (עלתה/התחזקה/הובילה/בלטה לחיוב). If the news is positive but the stock fell, write: "למרות החדשות, המניה ירדה"."""


def mode_instructions(mode: str, d: Dict[str, Any], has_tweets: bool = True) -> str:
    if mode == "intraday_update":
        state_heb = {
            "open": "השוק פתוח — שעות המסחר הרגילות בניו יורק",
            "premarket": "טרום מסחר (pre-market) — השוק טרם נפתח היום",
            "afterhours": "אחרי סגירה (after-hours) — המסחר הרגיל הסתיים היום",
            "closed": "השוק סגור (לילה / סוף שבוע / חג)",
        }[d["market_state"]]
        base = f"""You are a senior Wall Street market analyst writing an on-demand INTRADAY UPDATE in Hebrew,
covering ONLY the last two hours: {d['window_from']}–{d['time_str']} שעון ישראל, on {d['date_str']} (יום {d['day_name']}).
Market state right now: {state_heb}. Frame ALL market descriptions accordingly — if the regular session is
not open, NEVER describe the market as trading or reacting. Futures / pre-market / after-hours moves may be
described, but always labeled as such (בחוזים העתידיים, בטרום מסחר, במסחר המאוחר).

SINGLE SOURCE OF CONTENT — the source tweets below:
- The update is based EXCLUSIVELY on the source tweets at the bottom of this prompt — every one of them was
  posted inside the two-hour window. The verified in-window economic data block (if present) may support them.
- Do NOT add stories, headlines, price moves or macro data that do not appear in those tweets: no external
  headlines, no recap of earlier sessions, no stale daily-session data, no unrelated macro themes, and
  nothing from the prior-review context block.
- Web search is for VERIFICATION ONLY — confirming numbers, times and names that already appear in the
  tweets. NEVER use it to discover or add new stories.
- Ignore tweets with no market substance. If NO market-material tweet remains, the update must say so
  honestly — "אין עדכון מהותי בשעתיים האחרונות" — and stay short. Never pad.
- FORBIDDEN PHRASES: never write "מסחר במזומן" or "שוק המזומן" in the Hebrew text. Refer to the regular
  session as "המסחר הרגיל".
- When a tweet's time is known, anchor it in the text: "בשעה 22:40 שעון ישראל".

TIMEFRAME OF NUMBERS — critical:
- The verified Finnhub percentages above are DAILY changes (vs. the previous close), NOT two-hour changes.
  They may be used ONLY as a short half-sentence of context for something a tweet talks about, labeled
  explicitly "מתחילת היום" — never as standalone content, never presented as a two-hour move.
- A two-hour figure ("בשעתיים האחרונות עלתה ב-...") may appear ONLY if a source tweet states it explicitly.
- Direction words must still match the DIRECTIONAL FACTS block (daily direction), framed as "מתחילת היום"."""
        if d["market_state"] == "closed":
            structure = """THE US MARKET IS CLOSED RIGHT NOW — frame everything as a closed market, but the bullet count is
driven by the source tweets, NOT by a fixed number:
* עדכון: open with וול סטריט סגורה כעת (לילה / סוף שבוע / חג — לפי המצב) ואין תנועה תוך-יומית אמיתית, plus a
  short characterization of the window.
* Then ONE bullet per market-material story from the source tweets — cover EVERY material tweet from the
  window, each anchored to its Israel time when known. Merge tweets about the same story/company into one
  bullet. Overnight/futures moves only as labeled (בחוזים העתידיים, במסחר המאוחר), and daily Finnhub figures
  only as "מתחילת היום" context, per the rules above.
* מה הלאה: close with when the regular session resumes (Israel time) and, ONLY if known from the tweets or
  the verified data, the next key scheduled event.
Write as many story bullets as the material tweets genuinely support — no cap. If NO market-material tweet
remains, return ONLY the two framing bullets (עדכון + מה הלאה) with "אין עדכון מהותי בשעתיים האחרונות".
Never pad with content from outside the tweets."""
        elif not has_tweets:
            structure = """NO source tweets were gathered inside the window — return a SHORT update of EXACTLY 2 bullets:
* עדכון: open with "אין עדכון מהותי בשעתיים האחרונות", plus one sentence on the current market state
  (futures / pre-market / after-hours direction ONLY if it appears in the verified data, labeled "מתחילת היום").
* מה הלאה: the next scheduled item to watch (Israel time), ONLY if known from the verified data — otherwise
  simply when the next session opens. Do NOT use web search to fill either bullet with news."""
        else:
            structure = """EXACTLY 4 bullets, in this order — ALL content derived from the source tweets:
* מה קרה בשעתיים האחרונות: the single most important development FROM THE TWEETS and the immediate market
  reaction (or the futures / pre-market / after-hours reaction if the regular session is not open).
* הסיפור המרכזי: WHY it matters — cause-and-effect for the main tweet-sourced driver, with the transmission
  mechanism explained simply only when genuinely relevant.
* מניות ונכסים בתנועה: the 1-3 most notable movers THAT THE TWEETS MENTION, each with its trigger.
  Stock items open with "מניית <שם בעברית> (TICKER)".
* מה הלאה: what to watch in the COMING hours, based on the tweets and the verified data — Israel time, with
  the consensus where known.
If the tweets genuinely support fewer than 4 bullets, write fewer (minimum 2) rather than padding with
content from outside the tweets."""
        return f"""{base}

{structure}
Each bullet: 2-3 short sentences of flowing Hebrew prose — not a list of figures. After the Hebrew label,
continue in Hebrew words — never open with a ticker, a price or an English term. No ETF proxies, no Finnhub,
no ISO dates."""
    if mode == "daily_prep":
        if d["target_is_trading"]:
            if d["date_str"] == d["title_date_str"]:
                status = ("The briefing is for TODAY. The US cash market has NOT opened yet — never describe it as open, "
                          "trading, or having reacted. Use 'השוק צפוי להיפתח', 'המשקיעים יעקבו אחר'. Futures may be described "
                          "in present tense; the cash market may not.")
            else:
                status = (f"This runs on {d['date_str']} but the briefing is for the NEXT trading day: {d['title_date_str']} "
                          f"(יום {d['title_day_name']}). Do NOT use 'היום'/'הבוקר' — use 'ביום {d['title_day_name']}'. "
                          f"Do NOT describe futures/pre-market as live — they are not available yet.")
        else:
            status = f"The target date {d['title_date_str']} is NOT a trading day (weekend/US holiday). State this in the first bullet."
        return f"""You are a senior Wall Street market analyst writing a PRE-MARKET briefing in Hebrew.
Script run date: {d['date_str']} (יום {d['day_name']}). Briefing target date: {d['title_date_str']} (יום {d['title_day_name']}).
{status}

This is a professional, readable BRIEFING — NOT a data dump. FORWARD-LOOKING ONLY: no yesterday's index
performance, no closing levels, and nothing that already appears in the prior-context block.
EXACTLY 5 bullets, in this order:
* תמונת פתיחה: the mood and backdrop heading into the session — the single most important theme, and futures
  direction ONLY (no percentage unless a specific futures figure appears in the sources; never copy an ETF
  percentage as a futures percentage).
* הסיפור המרכזי: the main driver investors will watch and why it matters, with the transmission mechanism
  explained simply (event → oil → inflation → rates → equities) only when it is genuinely relevant.
* מאקרו ואירועים: the economic releases and Fed events scheduled for the day — Israel time, consensus and the
  previous reading, plus one sentence on why the number matters. If nothing is scheduled, say so in one short
  sentence and point to the next key date.
* דוחות ומניות במוקד: expected earnings and the 1-3 most important NEW overnight stock stories (company news,
  analyst moves). Stock items open with "מניית <שם בעברית> (TICKER)". Positive news about a falling stock →
  "למרות החדשות, המניה ירדה".
* שורה תחתונה: what will decide the direction of the session, in 1-2 sentences.
Each bullet: 2-4 short sentences of flowing Hebrew prose — not a list of figures. After the Hebrew label,
continue in Hebrew words — never open with a ticker, a price or an English term. Do NOT stack prices, price
targets and percentages: pick only the few figures that carry the story. No ETF proxies, no Finnhub, no ISO dates."""
    if mode == "daily_summary":
        return f"""You are a senior Wall Street market analyst writing an end-of-day market review in Hebrew for
{d['title_date_str']} (יום {d['title_day_name']}). PAST TENSE. This is a professional, readable MARKET REVIEW —
NOT a data dump. EXACTLY 5 bullets, in this order:
* המדדים: what the major indices did (direction + rounded %), one flowing analytical sentence or two.
* הסיפור של היום: WHY the market moved — the main driver(s), with clear cause-and-effect.
* סקטורים ומניות בולטות: the 1-3 most notable sector/stock stories with the reason. Stock items open with "מניית <שם בעברית> (TICKER)".
* סחורות, דולר ותשואות: oil, gold, dollar and yields in brief — direction and meaning, not a list of prices.
* שורה תחתונה למחר: what investors should watch in the next session.
Each bullet: 2-4 short sentences. Do NOT list ETF prices, do NOT dump long series of percentages or price levels,
do NOT mention Finnhub or any ETF proxy in the text. Explain the day — don't copy the data.
Every direction word MUST match the DIRECTIONAL FACTS block."""
    return f"""You are a senior Wall Street strategist writing a weekly review in Hebrew for the trading week
{d['week_range']}. PAST TENSE. ONLY events and moves from THIS specific week.
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
        mode_instructions(mode, d, bool(tweets)),
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
- No **, no ##, no HTML, no URLs inside content.""",
        "",
        get_time_conversion_block(now_il),
    ]
    for block in (market_block, econ_block, checklist, prior_context):
        if block:
            parts += ["", block]
    if tweets:
        parts += ["", f"Source tweets/posts from X (Twitter) — gathered {d['date_str']}. Never mention in the review that these came from tweets/posts:", "", tweets]
    elif mode == "intraday_update":
        parts += ["", (f"NOTE: no source tweets from the window {d['window_from']}–{d['time_str']} Israel time were "
                       f"gathered for this run. Per the rules above, return the SHORT 2-bullet form — do NOT use web "
                       f"search to fill the update with news, and do NOT recycle older headlines, stale daily data or "
                       f"unrelated macro.")]
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
    expected_title = build_expected_title(
        REVIEW_MODE, d["title_day_name"], d["title_date_str"], d["week_range"], d["time_str"],
    )

    print(f"Gathering raw input: {REVIEW_MODE} for {d['date_str']} ({d['day_name']})")
    print(f"  Target: {d['title_date_str']} ({d['title_day_name']}), week_range: {d['week_range']}")
    if REVIEW_MODE == "intraday_update":
        print(f"  Window: {d['window_from']}–{d['time_str']} Israel time, market state: {d['market_state']}")
    print(f"  Expected title: {expected_title}")

    print("\n── Tweets ──")
    since = now - timedelta(hours=INTRADAY_WINDOW_HOURS) if REVIEW_MODE == "intraday_update" else None
    tweets, top_cashtags = fetch_and_select_tweets(since)

    print("\n── Finnhub market data ──")
    market_block, pcts, ticker_quotes = fetch_market_data(REVIEW_MODE == "weekly_summary", top_cashtags)

    print("\n── Economic calendar ──")
    econ_days = {
        "daily_prep": (1, 1), "daily_summary": (1, 0),
        "weekly_summary": (7, 0), "intraday_update": (1, 0),
    }[REVIEW_MODE]
    econ_block = fetch_economic_data(*econ_days, since=since)
    checklist = get_macro_checklist(
        REVIEW_MODE, d["date_str"], d["week_range"], f"{d['window_from']}–{d['time_str']}",
    )

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
