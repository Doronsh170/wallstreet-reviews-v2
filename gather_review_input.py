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
  daily_prep | daily_summary | weekly_summary | intraday_update    (Wall Street)
  israel_prep | israel_summary | israel_weekly_summary             (Tel Aviv, tweet-only)

Usage:
  python gather_review_input.py daily_summary
"""

import json
import os
import re
import sys
import time
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from zoneinfo import ZoneInfo

import requests

# ══════════════════════════════════════════════════════════════
# CONFIG
# ══════════════════════════════════════════════════════════════

ISR_TZ = ZoneInfo("Asia/Jerusalem")
NY_TZ = ZoneInfo("America/New_York")

VALID_MODES = ("daily_prep", "daily_summary", "weekly_summary", "intraday_update",
               "israel_prep", "israel_summary", "israel_weekly_summary")
# Israeli-market modes are tweet-only (no Finnhub layer), summarizing the curated
# Hebrew X sources into the signature prep/summary format for the Tel Aviv exchange.
# israel_weekly_summary is the combined weekly review: it sums up the week that ended
# AND prepares the reader for the coming Tel Aviv trading week (macro, reports, events).
ISRAEL_MODES = ("israel_prep", "israel_summary", "israel_weekly_summary")
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
# Rolling record of settled daily closes, keyed by symbol → date → close. Built up
# by the post-session runs (daily_summary / weekly_summary) and committed to the
# repo, so the weekly review can compute TRUE weekly changes without the premium
# Finnhub candle endpoint. See compute_weekly_lines().
MARKET_HISTORY_FILE = Path("market_history.json")
MARKET_HISTORY_MAX_POINTS = 370  # ~1 trading year per symbol
WEEKLY_PRIOR_MAX_AGE_DAYS = 10   # a prior-week close older than this is too stale to trust
SOURCES_FILE = Path("sources/wallstreet.txt")
DEFAULT_ACCOUNTS = ["StockMKTNewz", "AIStockSavvy", "wallstengine", "KobeissiLetter", "gurgavin"]
TASE_SOURCES_FILE = Path("sources/tase.txt")
TASE_DEFAULT_ACCOUNTS = ["fundercoil", "SponserNews", "globesnews", "calcalist", "TheMarker",
                         "ynetmoney", "ModiShafrir", "matanshitrit", "CalcalistTech"]

MAX_TWEETS_PER_ACCOUNT = int(os.environ.get("MAX_TWEETS_PER_ACCOUNT", "10"))
MAX_TWEETS_FOR_REVIEW = int(os.environ.get("MAX_TWEETS_FOR_REVIEW", "40"))

PY_TO_HEB = {0: "שני", 1: "שלישי", 2: "רביעי", 3: "חמישי", 4: "שישי", 5: "שבת", 6: "ראשון"}

EXPECTED_FIRST_HEADING = {
    "daily_prep": "נקודות מרכזיות",
    "daily_summary": "סיכום המסחר",
    "weekly_summary": "סיכום השבוע",
    "intraday_update": "עדכון ביניים",
    "israel_prep": "לקראת יום המסחר",
    "israel_summary": "סיכום המסחר",
    "israel_weekly_summary": "סיכום השבוע",
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


def http_get(url: str, *, params: Optional[Dict[str, Any]] = None,
             headers: Optional[Dict[str, str]] = None, timeout: int = 15,
             attempts: int = 3, label: str = "") -> requests.Response:
    """GET with retries + exponential backoff. Retries network errors, 5xx and 429 —
    transient API hiccups should not cost a whole gather run."""
    last_exc: Optional[Exception] = None
    for i in range(attempts):
        try:
            r = requests.get(url, params=params, headers=headers, timeout=timeout)
            if r.status_code >= 500 or r.status_code == 429:
                raise requests.RequestException(f"HTTP {r.status_code}")
            return r
        except requests.RequestException as e:
            last_exc = e
            if i < attempts - 1:
                wait = 2 ** (i + 1)
                print(f"  {label or url}: {e} — retry {i + 1}/{attempts - 1} in {wait}s")
                time.sleep(wait)
    raise last_exc  # type: ignore[misc]


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
    if mode == "israel_prep":
        return f"נקודות חשובות לקראת יום המסחר בבורסה בתל אביב 🇮🇱 – יום {day_name}, {heb_date(date_str)}"
    if mode == "israel_summary":
        return f"סיכום יום המסחר בבורסה בתל אביב 🇮🇱 – יום {day_name}, {heb_date(date_str)}"
    if mode == "israel_weekly_summary":
        return f"סיכום שבועי והכנה לשבוע המסחר הבא בבורסה בתל אביב 🇮🇱 – {week_range}"
    return f"סיכום שבועי והכנה לשבוע הבא בוול סטריט 🇺🇸 – {week_range}"


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


# Israeli trading week for these reviews: Monday–Friday (closed Saturday/Sunday).
# We do not maintain an Israeli holiday calendar here — the reviews are on-demand,
# so a run on a holiday is simply not triggered.
def is_israel_trading_day(dt: datetime) -> bool:
    return dt.weekday() < 5


def get_next_israel_trading_day(now: datetime) -> datetime:
    d = now + timedelta(days=1)
    for _ in range(10):
        if is_israel_trading_day(d):
            return d
        d += timedelta(days=1)
    return now + timedelta(days=1)


def get_last_israel_trading_day(now: datetime) -> datetime:
    # After ~17:30 Israel time a trading day has closed, so today itself is the
    # last completed session; otherwise walk back to the previous trading day.
    if is_israel_trading_day(now) and now.hour >= 18:
        return now
    d = now - timedelta(days=1)
    for _ in range(10):
        if is_israel_trading_day(d):
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
    # Bottom-line label for the summary reviews: "למחר" only when the next trading
    # session is literally the next calendar day. A Friday summary (next session is
    # only next week) must say "לשבוע הבא" instead.
    bl_label = "שורה תחתונה למחר"

    if mode == "daily_prep":
        target = now if is_trading_day(now, holidays) else get_next_trading_day(now, holidays)
        title_date_str, title_day_name = target.strftime("%Y-%m-%d"), PY_TO_HEB[target.weekday()]
        target_is_trading = is_trading_day(target, holidays)
        review_date = title_date_str
    elif mode == "daily_summary":
        target = get_last_trading_day(now, holidays)
        title_date_str, title_day_name = target.strftime("%Y-%m-%d"), PY_TO_HEB[target.weekday()]
        review_date = title_date_str
        nxt = get_next_trading_day(target, holidays)
        bl_label = "שורה תחתונה למחר" if (nxt.date() - target.date()).days == 1 else "שורה תחתונה לשבוע הבא"
    elif mode == "intraday_update":
        review_date = date_str
    elif mode == "israel_prep":
        target = now if is_israel_trading_day(now) else get_next_israel_trading_day(now)
        title_date_str, title_day_name = target.strftime("%Y-%m-%d"), PY_TO_HEB[target.weekday()]
        target_is_trading = is_israel_trading_day(target)
        review_date = title_date_str
    elif mode == "israel_summary":
        target = get_last_israel_trading_day(now)
        title_date_str, title_day_name = target.strftime("%Y-%m-%d"), PY_TO_HEB[target.weekday()]
        target_is_trading = is_israel_trading_day(target)
        review_date = title_date_str
        nxt = get_next_israel_trading_day(target)
        bl_label = "שורה תחתונה למחר" if (nxt.date() - target.date()).days == 1 else "שורה תחתונה לשבוע הבא"
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
        "bl_label": bl_label,
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

def read_accounts(mode: str = "") -> List[str]:
    src_file, defaults = (
        (TASE_SOURCES_FILE, TASE_DEFAULT_ACCOUNTS) if mode in ISRAEL_MODES
        else (SOURCES_FILE, DEFAULT_ACCOUNTS)
    )
    if src_file.exists():
        accounts = [
            line.strip().lstrip("@")
            for line in src_file.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.strip().startswith("#")
        ]
        if accounts:
            return accounts
    return defaults


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
    # Israeli sources post in Hebrew, so the English keyword list above barely fires
    # for them — these Hebrew market terms let genuine TASE headlines rank.
    heb_keywords = [
        "בורסה", "מדד", "ת\"א", "תל אביב", "מניה", "מניית", "דוח", "דוחות", "רווח", "הכנסות",
        "תחזית", "ריבית", "בנק ישראל", "אינפלציה", "מדד המחירים", "אג\"ח", "הנפקה", "שקל",
        "דולר", "עלייה", "ירידה", "זינק", "צנח", "רכישה", "מיזוג", "ביטקוין", "נפט", "זהב",
    ]
    score += 7 * sum(1 for k in heb_keywords if k in t["text"])
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


def fetch_and_select_tweets(since: Optional[datetime] = None, mode: str = "") -> Tuple[str, List[str]]:
    """Returns (formatted tweet blocks, top cashtags mentioned).
    since — keep only tweets created at/after this moment (intraday window).
    mode — selects the source account list (Israeli modes read sources/tase.txt)."""
    if not TWITTER_API_KEY:
        print("  No TWITTER_API_KEY — skipping tweets (the review will rely on the chat model's web search)")
        return "", []
    # With a time window most tweets get dropped, so take more per account.
    per_account = MAX_TWEETS_PER_ACCOUNT * 2 if since is not None else MAX_TWEETS_PER_ACCOUNT
    all_tweets: List[Dict[str, Any]] = []
    for acc in read_accounts(mode):
        try:
            r = http_get(
                f"{TWITTER_BASE}/twitter/user/last_tweets",
                headers={"X-API-Key": TWITTER_API_KEY},
                params={"userName": acc, "includeReplies": "false"},
                timeout=25, label=f"@{acc}",
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
        r = http_get(f"{FINNHUB_BASE}/quote", params={"symbol": symbol, "token": FINNHUB_API_KEY},
                     timeout=10, label=f"Finnhub {symbol}")
        if not r.ok:
            return None
        d = r.json()
        price, pct, prev = float(d.get("c") or 0), float(d.get("dp") or 0), float(d.get("pc") or 0)
        if price <= 0 or prev <= 0:
            return None
        # 't' is the UNIX time of the last trade — used to check the quote actually
        # settled on the target Friday before it can anchor a weekly change.
        return {"price": price, "pct": pct, "prev_close": prev, "ts": int(d.get("t") or 0)}
    except Exception as e:
        print(f"  Finnhub error for {symbol}: {e}")
        return None


def direction_word(pct: float, threshold: float = 0.15) -> str:
    if pct >= threshold:
        return "עולה"
    if pct <= -threshold:
        return "יורד"
    return "יציב/כמעט ללא שינוי"


def load_market_history() -> Dict[str, Dict[str, float]]:
    if MARKET_HISTORY_FILE.exists():
        try:
            return json.loads(MARKET_HISTORY_FILE.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"  market_history.json unreadable ({e}) — starting a fresh history")
    return {}


def record_market_history(history: Dict[str, Dict[str, float]], snapshot_date: str,
                          closes: Dict[str, float]) -> None:
    """Store each symbol's SETTLED close under snapshot_date (YYYY-MM-DD) and persist.
    Called only from post-session modes, where the current price is a real close."""
    for sym, price in closes.items():
        if price and price > 0:
            history.setdefault(sym, {})[snapshot_date] = round(float(price), 4)
    for sym, points in history.items():  # keep the file bounded
        if len(points) > MARKET_HISTORY_MAX_POINTS:
            for old in sorted(points)[:-MARKET_HISTORY_MAX_POINTS]:
                points.pop(old, None)
    MARKET_HISTORY_FILE.write_text(
        json.dumps(history, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    print(f"  market_history.json updated ({snapshot_date}, {len(closes)} symbols)")


def quote_close_date(ts: int) -> Optional[str]:
    """NY-market calendar date (YYYY-MM-DD) of a Finnhub quote's last trade, or None."""
    if not ts or ts <= 0:
        return None
    return datetime.fromtimestamp(ts, NY_TZ).date().isoformat()


def weekly_pct_from_history(history: Dict[str, Dict[str, float]], symbol: str,
                            monday_str: str, week_close: float) -> Optional[Tuple[float, float, str]]:
    """weekly % = (week_close − last settled close BEFORE the week's Monday) / that close.
    Returns None when there is no such prior close, or it is too stale to be the
    genuine prior-week close (guards against multi-week gaps in the history)."""
    priors = [(dt, px) for dt, px in history.get(symbol, {}).items()
              if dt < monday_str and px and px > 0]
    if not priors:
        return None
    prior_date, prior_close = max(priors)
    if (date.fromisoformat(monday_str) - date.fromisoformat(prior_date)).days > WEEKLY_PRIOR_MAX_AGE_DAYS:
        return None
    return (week_close - prior_close) / prior_close * 100, prior_close, prior_date


def compute_weekly_lines(history: Dict[str, Dict[str, float]], labeled_symbols: List[Tuple[str, str]],
                         monday_str: str, current_prices: Dict[str, float],
                         close_dates: Dict[str, Optional[str]], week_close_date: str) -> Tuple[List[str], List[str]]:
    """Build the WEEKLY PERFORMANCE lines from the stored close history.
    A weekly % is emitted for a symbol ONLY when BOTH anchors are trustworthy:
      1. current price whose last trade SETTLED on the week's Friday (week_close_date),
         so an intraday / stale quote never masquerades as an end-of-week close, and
      2. a prior close in market_history.json dated before the week and still fresh.
    Returns (lines, missing_labels) — missing = symbols with no reliable weekly figure."""
    lines: List[str] = []
    missing: List[str] = []
    for symbol, label in labeled_symbols:
        cur = current_prices.get(symbol)
        if not cur or cur <= 0:
            missing.append(label)
            continue
        if close_dates.get(symbol) != week_close_date:  # anchor 1: settled end-of-week close
            missing.append(label)
            print(f"  {symbol} WEEKLY: quote is not a settled close for {week_close_date} "
                  f"(last trade {close_dates.get(symbol)}) — skipping")
            continue
        res = weekly_pct_from_history(history, symbol, monday_str, cur)  # anchor 2: prior close
        if res is None:
            missing.append(label)
            print(f"  {symbol} WEEKLY: no reliable prior-week close in history yet — skipping")
            continue
        pct, prior_close, prior_date = res
        lines.append(f"  {label}: weekly {pct:+.2f}% (from ${prior_close:.2f} to ${cur:.2f})")
        print(f"  {symbol} WEEKLY: {pct:+.2f}% (prior close {prior_date} → current {week_close_date})")
    return lines, missing


def fetch_market_data(weekly: bool, top_cashtags: List[str], d: Dict[str, Any],
                      record_close: bool) -> Tuple[str, Dict[str, float], Dict[str, Dict[str, float]], bool]:
    """Returns (prompt_block, etf_pcts, ticker_quotes_snapshot, weekly_available).
    The snapshot lets paste_review.py verify ticker directions later without a live API.
    weekly_available is False when the weekly summary could not get a single real
    weekly figure, so the prompt can switch to its qualitative-only guardrail."""
    if not FINNHUB_API_KEY:
        print("  No FINNHUB_API_KEY — skipping market data")
        return "", {}, {}, False
    lines: List[str] = []
    pcts: Dict[str, float] = {}
    current_prices: Dict[str, float] = {}
    close_dates: Dict[str, Optional[str]] = {}
    for symbol, label in FINNHUB_SYMBOLS.items():
        q = finnhub_quote(symbol)
        if q:
            pcts[symbol] = q["pct"]
            current_prices[symbol] = q["price"]
            close_dates[symbol] = quote_close_date(q.get("ts", 0))
            lines.append(f"  {label}: ${q['price']:.2f} (daily: {q['pct']:+.2f}%), prev close: ${q['prev_close']:.2f}")
            print(f"  Finnhub {symbol}: ${q['price']:.2f} ({q['pct']:+.2f}%)")
    if not lines:
        return "", {}, {}, False

    # Snapshot quotes for the tickers the tweets talk about — the review will
    # most likely mention these, and the publish step verifies directions.
    ticker_quotes: Dict[str, Dict[str, float]] = {}
    for t in top_cashtags:
        q = finnhub_quote(t)
        if q:
            ticker_quotes[t] = q
            current_prices[t] = q["price"]
            close_dates[t] = quote_close_date(q.get("ts", 0))
            print(f"  Ticker snapshot {t}: ${q['price']:.2f} ({q['pct']:+.2f}%)")

    # Persist today's closes so future weekly runs have the prior-week anchor. Only
    # store symbols whose quote actually SETTLED on the review date — never an
    # intraday price — so the history holds genuine end-of-day closes.
    history = load_market_history()
    if record_close and d.get("review_date"):
        settled = {s: p for s, p in current_prices.items() if close_dates.get(s) == d["review_date"]}
        if settled:
            record_market_history(history, d["review_date"], settled)
        else:
            print(f"  no symbols settled on {d['review_date']} — nothing recorded to history")

    block = [
        "══ VERIFIED MARKET DATA (from Finnhub API — these are FACTS, do NOT override with guesses) ══",
        "DAILY PERFORMANCE:",
        *lines,
    ]
    if ticker_quotes:
        block += ["", "INDIVIDUAL STOCKS mentioned in the source tweets (verified quotes):"]
        for t, q in ticker_quotes.items():
            block.append(f"  ${t}: ${q['price']:.2f} (daily: {q['pct']:+.2f}%), prev close: ${q['prev_close']:.2f}")
    weekly_available = False
    if weekly:
        monday_str = (date.fromisoformat(d["review_date"]) - timedelta(days=4)).isoformat()
        labeled = [(s, FINNHUB_SYMBOLS[s]) for s in WEEKLY_SYMBOLS if s in current_prices]
        labeled += [(t, f"${t}") for t in ticker_quotes]  # individual stocks get a weekly figure too
        weekly_lines, weekly_missing = compute_weekly_lines(
            history, labeled, monday_str, current_prices, close_dates, d["review_date"])
        if weekly_lines:
            weekly_available = True
            block += ["", "WEEKLY PERFORMANCE (use THESE for weekly changes in the weekly summary, NOT the daily numbers):",
                      *weekly_lines]
            if weekly_missing:
                block += ["", ("NOTE — no weekly figure is available for: " + ", ".join(weekly_missing) +
                               ". For these do NOT state a weekly percentage. Describe the direction qualitatively, "
                               "or use the daily move only and label it clearly as the last trading day's change.")]
        else:
            block += ["", ("⚠️ WEEKLY PERFORMANCE DATA UNAVAILABLE this run (the close history is still being built up). "
                           "Do NOT state ANY weekly percentage and do NOT present a daily change as a weekly change. "
                           "Tell the week's arc qualitatively (direction and drivers). If you cite a specific percentage, "
                           "make explicit that it is the last trading day's move, not the weekly change.")]
            print("  WEEKLY PERFORMANCE unavailable — prompt switched to qualitative-only guardrail")

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
    return "\n".join(block), pcts, ticker_quotes, weekly_available


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
        r = http_get(
            f"{FINNHUB_BASE}/calendar/economic",
            params={
                "from": (now - timedelta(days=days_back)).strftime("%Y-%m-%d"),
                "to": (now + timedelta(days=days_forward)).strftime("%Y-%m-%d"),
                "token": FINNHUB_API_KEY,
            },
            timeout=15, label="Finnhub economic calendar",
        )
        if not r.ok:
            print(f"  Finnhub economic calendar: status {r.status_code}")
            return ""
        us_events = []
        scheduled_events = []
        dropped_outside_window = 0
        for e in r.json().get("economicCalendar", []):
            if e.get("country") != "US":
                continue
            unit = e.get("unit", "")
            if e.get("actual") is None:
                # Not released yet — a SCHEDULED event, relevant for the preparation part.
                if days_forward > 0 and since is None:
                    line = f"  {e.get('time', '')[:16]} UTC | {e.get('event', '')}"
                    if e.get("estimate") is not None:
                        line += f": forecast={e['estimate']}{unit}"
                    if e.get("prev") is not None:
                        line += f", previous={e['prev']}{unit}"
                    if e.get("impact"):
                        line += f" [{e['impact']} impact]"
                    scheduled_events.append(line)
                continue
            if since is not None:
                event_dt = parse_econ_time(e.get("time", ""))
                if event_dt is None or event_dt < since:
                    dropped_outside_window += 1
                    continue
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
        if scheduled_events:
            print(f"  Econ: {len(scheduled_events)} scheduled upcoming events")
        if not us_events and not scheduled_events:
            return ""
        header = (
            "══ VERIFIED US ECONOMIC DATA RELEASED INSIDE THE TWO-HOUR WINDOW (from Finnhub — FACTS, you MUST include them) ══"
            if since is not None else
            "══ VERIFIED US ECONOMIC DATA (from Finnhub — FACTS, you MUST include them) ══"
        )
        if not us_events:
            return "\n".join([
                "══ SCHEDULED US ECONOMIC EVENTS AHEAD (from Finnhub — times are UTC, convert with the offset block) ══",
                *scheduled_events,
                "- Use these for the preparation/look-ahead points. Give times in Israel time with the consensus and previous reading.",
                "══════════════════════════════════════════════════════════════════════════════",
            ])
        tail = []
        if scheduled_events:
            tail = [
                "",
                "SCHEDULED US ECONOMIC EVENTS AHEAD (not yet released — times are UTC, convert with the offset block):",
                *scheduled_events,
                "- Use these for the preparation/look-ahead points. Give times in Israel time with the consensus and previous reading.",
            ]
        return "\n".join([
            header,
            *us_events,
            "- Every data point above MUST appear in the review, woven into analytical bullets (not raw numbers).",
            "- Always explain WHY the number matters for Fed policy / markets.",
            "- Do NOT say data 'is expected' if it already has an actual value above — it was ALREADY released.",
            *tail,
            "══════════════════════════════════════════════════════════════════════════════",
        ])
    except Exception as e:
        print(f"  Finnhub economic calendar error: {e}")
        return ""


def get_macro_checklist(mode: str, date_str: str, week_range: Optional[str],
                        window: Optional[str] = None) -> str:
    if mode == "intraday_update":
        return f"""══ WEB SEARCH POLICY ══
Web search is for VERIFICATION ONLY — confirming a name, time or figure that already appears in the source
tweets, for the window {window} Israel time on {date_str}. Do NOT use it to find additional news, headlines,
prices or macro data. Content that is not present in the tweets does not enter the update.
══════════════════════════════════"""
    if mode == "israel_weekly_summary":
        return f"""══ WEB SEARCH POLICY (WEEKLY — TWO PARTS) ══
SUMMARY of the week that ended ({week_range or date_str}): the stories come EXCLUSIVELY from the source posts
below. Web search is for VERIFICATION ONLY there — confirming a name or figure that already appears in a source
post. Do NOT use it to add news, index levels, prices or macro data to the summary part.
PREPARATION for the COMING Tel Aviv trading week: here you MAY use web search to confirm the SCHEDULED calendar
only — Bank of Israel (בנק ישראל) rate decisions, Israeli macro releases (מדד המחירים לצרכן, אבטלה, צמיחה) and
the notable Tel Aviv earnings reports due, with their dates and Israel times. Scheduled-calendar items only,
never speculative news or invented figures.
══════════════════════════════════"""
    if mode in ISRAEL_MODES:
        return """══ WEB SEARCH POLICY ══
Web search is for VERIFICATION ONLY — confirming a name or figure that already appears in the source posts.
Do NOT use it to find additional news, index levels, prices or macro data. Content that is not present in the
sources does not enter the review.
══════════════════════════════════"""
    if mode == "daily_summary":
        return f"""══ MANDATORY MACRO TIMING CHECK (verification only) ══
Use web search to verify the macro calendar for {date_str}: which of the majors (CPI headline AND core,
PPI, NFP, Jobless Claims, Consumer Sentiment, ISM PMI, GDP, Retail Sales, FOMC decision/minutes) were
actually released today and which are still ahead. This check protects TIMING ONLY — a release enters the
review as a story only if it appears in the source tweets or the verified economic block, with the figures
they provide (actual, forecast, previous AND the market implication). Never present an already-released
event as upcoming, and never import from the search a macro story the sources did not cover.
IN ADDITION — verify the NEXT session's scheduled macro calendar (Israel times, consensus) for the
bottom-line point.
══════════════════════════════════"""
    if mode == "weekly_summary":
        return f"""══ MANDATORY MACRO TIMING CHECK (verification only) ══
The week's macro stories come ONLY from the source tweets and the verified economic block, with the figures
they provide. Use web search to VERIFY, never to add: (1) that every release you describe as belonging to
the week of {week_range or date_str} was indeed released in that week (headline AND core where relevant),
and that nothing already released is written as 'expected', and (2) the COMING week's schedule for the
preparation points: economic releases and Fed events (with dates, Israel times and consensus where
available) and the key earnings reports scheduled, and what the market will look for in each.
Do NOT import from the search a macro story the sources did not cover, and do NOT fill in missing
actual/forecast/previous figures from memory or from search results.
══════════════════════════════════"""
    return f"""══ SCHEDULED DATA CHECK (verification only) ══
Use web search to verify what US economic data is scheduled for release on {date_str} — release time in
Israel time, market consensus and the previous reading — and to cross-check that nothing you present as
upcoming was already released. This is schedule verification only: do NOT use the search to import news
stories the source tweets did not cover.
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
    elif mode == "israel_prep":
        prior = data.get("israelSummary")
        header = ("══ CONTEXT: THE PREVIOUS TEL AVIV DAILY SUMMARY — DO NOT REPEAT THIS CONTENT ══\n"
                  "Already published. Your briefing is FORWARD-LOOKING. Mention an item below ONLY if there is a "
                  "genuinely NEW development about it.")
    elif mode == "israel_summary":
        prior = data.get("israelPrep")
        header = ("══ CONTEXT: THIS SESSION'S TEL AVIV PRE-MARKET BRIEFING ══\n"
                  "Published before the session. Use it to resolve what was expected into what happened, do NOT "
                  "quote it verbatim.")
    else:
        return ""
    if not (prior and prior.get("sections")):
        return ""
    content = "\n\n".join(f"[{s.get('heading', '')}]\n{s.get('content', '')}" for s in prior["sections"])
    return f"{header}\n\n{content}\n══════════════════════════════════════════════════════════════"


# ══════════════════════════════════════════════════════════════
# PROMPT — the full paste-ready instruction block
# ══════════════════════════════════════════════════════════════

# Source-exclusivity + pre-output self-verification (the error-prevention
# mechanism): every mode's prompt (1) declares the curated X sources as the ONLY
# story source — with Finnhub as the only price/direction source in the US
# modes — restricting web search to narrow VERIFICATION purposes, and (2) ends
# with a mandatory self-check the model must run before returning the JSON.

def get_source_hierarchy(mode: str) -> str:
    """The source-exclusivity block for the Finnhub-backed US modes. The
    tweet-only modes (intraday + Israel) already carry equivalent exclusivity
    wording inside their mode instructions, so they get no extra block."""
    if mode == "daily_prep":
        purposes = """Web search is permitted for FOUR narrow purposes ONLY:
  a. Verifying the futures direction and percentage for the opening point.
  b. Verifying TODAY'S scheduled macro calendar (Israel times, consensus, previous reading), and cross-checking
     that an event you present as upcoming was not already released.
  c. Verifying a claim of an all-time high / 52-week high before writing it.
  d. Confirming absolute levels (S&P 500 in points, oil in $/barrel, VIX level, 10Y yield) IF you choose to
     cite them. If verification fails or is ambiguous — omit the absolute level and use the % change instead."""
    elif mode == "daily_summary":
        purposes = """Web search is permitted for THREE narrow purposes ONLY:
  a. Verifying a claim of an all-time high / 52-week high before writing it.
  b. Confirming absolute levels (S&P 500 in points, oil in $/barrel, VIX level, 10Y yield) IF you choose to
     cite them. If verification fails or is ambiguous — omit the absolute level and use the % change instead.
  c. Verifying the NEXT session's scheduled macro calendar (Israel times, consensus) for the bottom-line point,
     and cross-checking that an event you present as upcoming was not already released."""
    elif mode == "weekly_summary":
        purposes = """Web search is permitted for THREE narrow purposes ONLY:
  a. Verifying a claim of an all-time high / 52-week high before writing it.
  b. Confirming absolute levels (S&P 500 in points, oil in $/barrel, VIX level, 10Y yield) IF you choose to
     cite them. If verification fails or is ambiguous — omit the absolute level and use the % change instead.
  c. Verifying the COMING week's schedule (macro releases, Fed events, key earnings) for the preparation points."""
    else:
        return ""
    return f"""══ SOURCE HIERARCHY — THE FOUNDATION OF THIS REVIEW ══
The review is built EXCLUSIVELY from two sources:
1. The VERIFIED MARKET DATA and ECONOMIC blocks (Finnhub) — the ONLY source for prices, percentages and directions.
2. The source tweets below — the ONLY source for stories, news and narrative.
{purposes}
FORBIDDEN: adding any story, event, or data point that originates from web search alone and does not appear
in the tweets or the Finnhub blocks. Search is a verification tool, never a story source. If the tweets did not
cover a story — the review does not cover it either.
══════════════════════════════════════════════════════"""


BULLET_COUNT_NOTE = {
    "daily_prep": "EXACTLY 6 bullets including the bottom line",
    "daily_summary": "EXACTLY 6 bullets including the bottom line",
    "weekly_summary": "8-10 bullets",
    "israel_prep": "6-9 bullets",
    "israel_summary": "6-9 bullets",
    "israel_weekly_summary": "6-9 bullets",
    "intraday_update": "one bullet per material topic, no minimum and no cap",
}


def get_self_verification(mode: str) -> str:
    """The mandatory pre-output checklist appended to EVERY mode's prompt."""
    count_note = BULLET_COUNT_NOTE[mode]
    if mode in ("intraday_update",) + ISRAEL_MODES:
        carve_out = (" (the scheduled-calendar items verified for the preparation points excepted)"
                     if mode == "israel_weekly_summary" else "")
        checks = f"""1. NUMBERS: every percentage, price and figure traces to a specific source post{carve_out}.
   Any number you cannot point to a source line for — DELETE it or the whole claim.
2. SCOPE: no story, price, index level or data point appears that is absent from the source posts{carve_out}.
3. DIRECTIONS: every directional claim (עלה/ירד/זינק/צנח) is stated by a source post — you did not determine
   any direction or magnitude yourself.
4. ATTRIBUTION: a story a source reports citing a news outlet keeps "לפי <outlet>". A story appearing in only
   ONE source post with no outlet attribution carries "לפי דיווחים" — never stated as an established fact.
5. FORMAT: no ";", no em dash, no ISO dates, no raw-ticker bullet openings, and the bullet count fits the
   instructions above ({count_note}).
6. SUMMARY ARRAY: one item per bullet, same order, same headlines, distilled (not copied) sentences, and every
   number/direction in the summary passes checks 1-4 as well."""
    else:
        if mode == "weekly_summary":
            timing_check = """2. WEEKLY vs DAILY: every weekly change uses the WEEKLY PERFORMANCE block. Every symbol listed in the
   "no weekly figure" note is described qualitatively or as a daily move labeled as such."""
        else:
            timing_check = """2. TIMING: no event already released is described as upcoming ("צפוי היום"), and the market-session state
   matches the instructions (never describe a closed market as open or trading)."""
        checks = f"""1. NUMBERS: every percentage, price and figure traces to a specific line in the Finnhub blocks, a specific
   tweet, or one of the permitted verification searches. Any number you cannot point to a source for —
   DELETE it or the whole claim.
{timing_check}
3. DIRECTIONS: every directional word matches the DIRECTIONAL FACTS block and the sign of the Finnhub change.
4. SIGN-FLIP: no stock that fell is described positively.
5. ATTRIBUTION: every single-source story carries "לפי <outlet>" or "לפי דיווחים".
6. SCOPE: no story or data point appears that is absent from both the tweets and the Finnhub blocks
   (the permitted verification purposes excepted).
7. FORMAT: no ";", no em dash, no ISO dates, no raw-ticker bullet openings, ticker in parentheses on every
   first mention, headline under 40 chars with no ":" inside it, and the bullet count is right ({count_note}).
8. SUMMARY ARRAY: one item per bullet, same order, same headlines, distilled (not copied) sentences, and every
   number/direction in the summary passes checks 1-5 as well."""
    return f"""══ PRE-OUTPUT SELF-VERIFICATION (MANDATORY — do this BEFORE returning the JSON) ══
Go over every bullet you wrote and check, one by one:
{checks}
If ANY check fails — fix the bullet and re-run the checks. Only then return the JSON.
══════════════════════════════════════════════════════════════════════════════"""


SHARED_RULES = """Rules:
- Write ONLY in Hebrew. English only for tickers ($AAPL), index names (S&P 500), and well-known financial terms in parentheses on first use.
- Be specific: every claim must include a number, percentage, or ticker. No vague statements.
- Do NOT repeat information across bullets. One company = one bullet (merge multiple news items).
- No buy/sell recommendations, no price targets of your own, no "כדאי לקנות/למכור".
- EVERY number must come from: (1) the verified Finnhub data above, (2) a specific tweet, or (3) one of the PERMITTED verification searches listed in the SOURCE HIERARCHY block. NEVER invent, estimate, or recall numbers from memory or from general knowledge. When in doubt, omit the number and keep the story, or omit the point entirely.
- If a tweet contradicts the Finnhub data, the Finnhub data is correct.
- SINGLE-SOURCE ATTRIBUTION: a story reported in the tweets citing a news outlet (WSJ, NYT, FT, Axios, Reuters) keeps that attribution in Hebrew: "לפי WSJ", "לפי דיווח ב-NYT". A story appearing in only ONE tweet with no outlet attribution is written with a hedge: "לפי דיווחים" — never as an established fact.
- Directional words (צונח/יורד/מזנק/עולה) are factual claims — they MUST match the DIRECTIONAL FACTS block.
- Sector percentages (XLE/XLK/...) — ONLY from the Finnhub data. Missing sector → omit.
- Never claim an all-time high (שיא כל הזמנים) or 52-week high without web-search verification or an explicit tweet stating it. A tweet-sourced high keeps its scope exactly: 52-week high ≠ all-time high.
- CPI mentioned → ALWAYS both headline AND Core CPI. Economic data → always actual vs forecast vs previous.
- IPO (הנפקה ראשונית) ≠ ETF (תעודת סל). Nasdaq 100 (QQQ, ~NDX) ≠ Nasdaq Composite (IXIC) — never mix their levels.
- Attribution: Claude→Anthropic, ChatGPT→OpenAI, Gemini→Google. Donald Trump is the CURRENT US President — never "לשעבר".
- No URLs, no Markdown links, no source domains in brackets. Attribution style: לפי Reuters / לפי Bloomberg only.
- Dates in visible text: Israeli format ONLY, e.g. "יום שני, 6.7.2026". NEVER write an ISO date (2026-07-06) inside the title or the bullets.
- NEVER use the ";" character anywhere. Use a comma or start a new sentence instead.
- NEVER use an em dash / double hyphen ("—" or "--") as a clause separator. Use a comma, a colon, or start a new sentence instead.
- Never write "נתון בפועל עדיין לא קיים". If a figure has not been released yet, give only the forecast (צפי) and the previous reading (נתון קודם).
- Never OPEN a bullet with a raw ticker like "$TSLA:" or "$AMZN:". Open with the Hebrew company name: "מניית טסלה (TSLA):", "מניית אמזון (AMZN):", "מניית מטא (META):".
- EVERY Hebrew company/stock name gets its ticker in parentheses on FIRST mention — "קורוויב (CRWV)", "ג'יי.פי מורגן (JPM)" — both in the bullet body AND in the summary item. Indices (S&P 500) and private companies with no listed ticker are exempt.
- Correct Hebrew causative syntax: a driver "הקפיץ את מחיר הנפט" (never "קפץ את הנפט"), and price moves belong to "מחיר הנפט/הזהב", not to the asset as a direct object.
- Finnhub and the measurement ETFs (SPY/QQQ/DIA/USO/BNO/GLD/UUP/VIXY/TLT...) are a hidden verification layer ONLY. NEVER mention Finnhub, "proxy", "דרך USO", "האינדיקציה מ-", or any technical data-source wording in the visible text — describe the asset itself (נפט, זהב, דולר, תשואות) directly.
- SIGN-FLIP: if the verified data shows a stock DOWN, do NOT describe it positively (עלתה/התחזקה/הובילה/בלטה לחיוב). If the news is positive but the stock fell, write: "למרות החדשות, המניה ירדה"."""

# The signature point format shared by daily_prep / daily_summary / weekly_summary —
# modeled on the author's own published briefings (specific mini-headline + deep prose).
POINT_STYLE = """SIGNATURE POINT FORMAT (the author's own style — follow it exactly):
- Each point is ONE bullet: "* <כותרת קצרה>: <גוף הנקודה>".
- The opening mini-headline: 2-6 Hebrew words, SPECIFIC to the story — e.g. "מניות השבבים ממשיכות לרכז עניין",
  "הנפט ממשיך לטפס", "אבן דרך במגזר הבריאות", "סנטימנט מעורב בפתיחה" — never a generic label like
  "חדשות" / "מאקרו" / "מניות". Up to 40 characters, and NO ":" inside the headline itself.
  A single-stock story opens with "מניית <שם בעברית> (TICKER)".
- After the headline: flowing, professional Hebrew prose — 2-3 concise sentences (a 4th only when the story
  truly demands it). EVERY point must deliver real depth: (1) what happened, with the few figures that carry
  the story, (2) the background and context (על רקע..., בעקבות...), and (3) why it matters — the mechanism or
  the implication for investors. Never leave a point as a bare headline-fact.
- STRONG points only: fewer, deeper points beat many thin ones. This is a briefing, not an article — no
  filler points, no padding.
- Voice: a senior investment advisor who lives and breathes Wall Street, explaining the market to clients —
  analytical, confident, readable. Weave the numbers into the story, don't stack them."""

# The signature point format for the Israeli (Tel Aviv) prep/summary reviews.
# Same depth and structure as the Wall Street style, but the voice, examples and
# market references belong to the Tel Aviv exchange.
ISRAEL_POINT_STYLE = """SIGNATURE POINT FORMAT (follow it exactly):
- Each point is ONE bullet: "* <כותרת קצרה>: <גוף הנקודה>".
- The opening mini-headline: 2-6 Hebrew words, SPECIFIC to the story — e.g. "הבנקים ממשיכים להוביל",
  "אבן דרך בסקטור הנדל\"ן", "סנטימנט זהיר לקראת הפתיחה" — never a generic label like "חדשות" / "מאקרו".
  Up to 40 characters, and NO ":" inside the headline itself. A single-stock story opens with
  "מניית <שם החברה> (טיקר אם הופיע בציוץ)".
- After the headline: flowing, professional Hebrew prose — 2-3 concise sentences. EVERY point delivers real
  depth: (1) what happened, with the few figures that carry the story (ONLY figures that appear in a source),
  (2) the background and context (על רקע..., בעקבות...), and (3) why it matters for the investor.
- STRONG points only: fewer, deeper points beat many thin ones. This is a briefing, not an article.
- Voice: a senior investment advisor explaining the Tel Aviv market to clients — analytical, confident,
  readable. Weave the numbers into the story, don't stack them."""

# intraday_update summarizes the sources only — no Finnhub blocks exist in its prompt,
# so it gets a reduced rule set with no references to verified market data.
INTRADAY_RULES = """Rules:
- Write ONLY in Hebrew. English only for tickers ($AAPL), index names (S&P 500), and well-known financial terms in parentheses on first use.
- EVERY number in the update must appear in a source tweet. NEVER invent, estimate, or recall numbers from memory. A topic whose tweet has no figures is summarized WITHOUT figures.
- No buy/sell recommendations, no price targets, no "כדאי לקנות/למכור".
- Attribution: Claude→Anthropic, ChatGPT→OpenAI, Gemini→Google. Donald Trump is the CURRENT US President — never "לשעבר".
- No URLs, no Markdown links, no source domains in brackets. Attribution style: לפי Reuters / לפי Bloomberg only, and only when the tweet itself cites them.
- SINGLE-SOURCE ATTRIBUTION: a story appearing in only ONE source post with no outlet attribution is written with a hedge: "לפי דיווחים" — never as an established fact.
- Dates in visible text: Israeli format ONLY, e.g. "יום שני, 6.7.2026". NEVER write an ISO date (2026-07-06) inside the title or the bullets.
- NEVER use the ";" character anywhere. Use a comma or start a new sentence instead.
- NEVER use an em dash / double hyphen ("—" or "--") as a clause separator. Use a comma, a colon, or start a new sentence instead.
- Never OPEN a bullet with a raw ticker like "$TSLA:" or "$AMZN:". Open with the Hebrew company name: "מניית טסלה (TSLA):", "מניית אמזון (AMZN):", "מניית מטא (META):".
- Never mention in the review that the items came from tweets/posts/X accounts."""

# The Israeli WEEKLY review is tweet-only like the other Israel modes, but its
# preparation block looks ahead to the coming week, so it may cite SCHEDULED-calendar
# figures (release dates/times) verified via web search — the one carve-out from the
# strict "every number from a source" rule that governs the summary block.
ISRAEL_WEEKLY_RULES = """Rules:
- Write ONLY in Hebrew. English only for tickers, index names, and well-known financial terms in parentheses on first use.
- SUMMARY of the week that ended: EVERY number must appear in a source post. NEVER invent, estimate, or recall numbers from memory. A story whose source carries no figures is summarized WITHOUT figures.
- PREPARATION for the coming week: you MAY state SCHEDULED-calendar dates and Israel times (Bank of Israel decisions, Israeli macro releases, Tel Aviv earnings) verified via web search. Nothing else may be added from web search.
- No buy/sell recommendations, no price targets, no "כדאי לקנות/למכור".
- Attribution: Claude→Anthropic, ChatGPT→OpenAI, Gemini→Google. Donald Trump is the CURRENT US President — never "לשעבר".
- No URLs, no Markdown links, no source domains in brackets. Attribution style: לפי Reuters / לפי Bloomberg only, and only when a source itself cites them.
- SINGLE-SOURCE ATTRIBUTION: a story appearing in only ONE source post with no outlet attribution is written with a hedge: "לפי דיווחים" — never as an established fact.
- Dates in visible text: Israeli format ONLY, e.g. "יום שני, 6.7.2026". NEVER write an ISO date (2026-07-06) inside the title or the bullets.
- NEVER use the ";" character anywhere. Use a comma or start a new sentence instead.
- NEVER use an em dash / double hyphen ("—" or "--") as a clause separator. Use a comma, a colon, or start a new sentence instead.
- Never OPEN a bullet with a raw ticker. Open with the Hebrew company name.
- Never mention in the review that the items came from tweets/posts/X accounts."""


def mode_instructions(mode: str, d: Dict[str, Any], has_tweets: bool = True) -> str:
    if mode == "intraday_update":
        state_heb = {
            "open": "השוק פתוח — שעות המסחר הרגילות בניו יורק",
            "premarket": "טרום מסחר (pre-market) — השוק טרם נפתח היום",
            "afterhours": "אחרי סגירה (after-hours) — המסחר הרגיל הסתיים היום",
            "closed": "השוק סגור (לילה / סוף שבוע / חג)",
        }[d["market_state"]]
        return f"""You are writing a SHORT INTRADAY UPDATE in Hebrew for a financial website. The update is a
plain-language SUMMARY of what the curated X (Twitter) sources posted in the last two hours —
{d['window_from']}–{d['time_str']} שעון ישראל, on {d['date_str']} (יום {d['day_name']}) — and nothing else.
Market state right now: {state_heb}. Never describe the market as trading or reacting when the regular
session is not open.

THE UPDATE SUMMARIZES THE SOURCES — it is NOT market analysis:
- Content comes EXCLUSIVELY from the source tweets at the bottom of this prompt. Nothing else enters the
  update: no price data, no daily-change percentages, no movers lists, no macro backdrop, no external
  headlines, no recap of earlier sessions, and no independent market interpretation of your own.
- The update does NOT determine who rose or fell in trading. Do NOT attach a price, percentage or direction
  to any story — unless the tweet itself states that figure/move explicitly, in which case report it as the
  source reported it.
- FILTER: keep only market-material posts. Ignore promotional posts, engagement bait, and posts with no
  market substance. A bare list of tickers with no story is NOT material.
- ONE bullet per topic. Several tweets about the same topic/company → merge into ONE bullet.
- Include EVERY material topic from the window — there is NO fixed bullet count, no minimum and no cap.
- Each bullet: 1-2 short, clear Hebrew sentences. Open with a short Hebrew topic label, then the summary.
  Anchor a bullet to its time when known using "בשעה 22:40" only. All times in this update are Israel time
  (already stated once in the window line above), so do NOT append "שעון ישראל" to individual bullets — it is
  redundant. At most one bullet may carry it if truly needed for clarity.
- If the window does not contain enough material posts, return a single bullet saying simply:
  "* אין מספיק עדכונים משמעותיים מהמקורות בחלון הזמן הזה." — nothing else. Never pad.
- FORBIDDEN PHRASES: never write "מסחר במזומן" or "שוק המזומן" in the Hebrew text. Refer to the regular
  session as "המסחר הרגיל".
- Web search may be used ONLY to verify a name, time or figure that already appears in a tweet — NEVER to
  discover or add stories, prices or data."""
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
        return f"""You are a senior Wall Street investment advisor writing your signature PRE-MARKET briefing in Hebrew.
Script run date: {d['date_str']} (יום {d['day_name']}). Briefing target date: {d['title_date_str']} (יום {d['title_day_name']}).
{status}

{POINT_STYLE}

This is a professional BRIEFING — NOT a data dump. FORWARD-LOOKING ONLY: no yesterday's index performance,
no closing levels, and nothing that already appears in the prior-context block.
EXACTLY 6 points TOTAL (including the bottom-line point) — short and focused, not an article. Each point
is 4-5 lines. Fewer, deeper points beat many thin ones, so pick only the strongest stories of the morning:
* FIRST point — the opening picture: futures direction WITH a verified percentage (from the sources or your
  web search — never an ETF percentage presented as a futures percentage). No verified futures figure →
  open with the strongest concrete fact of the morning instead. NEVER open with mood-only sentences
  ("אווירה זהירה", "סנטימנט מעורב") — every sentence must carry a fact, a number or a mechanism.
* MIDDLE points (4) — ONE point per real story. Pick the STRONGEST stories of the morning FROM THE SOURCE
  TWEETS (and the verified Finnhub blocks), using the menu below as categories — do NOT force every category,
  and do NOT import a story that web search found on its own:
  - The day's macro releases and Fed events: Israel time, consensus and the previous reading, and why the
    number matters for rates and equities. Nothing scheduled → one short point saying so and naming the next key date.
  - The central story investors will watch today, with the transmission mechanism explained simply
    (אירוע → נפט → אינפלציה → ריבית → מניות) when genuinely relevant.
  - 1-3 overnight stock/sector stories: expected earnings, major company news, analyst moves. Each significant
    story gets its OWN point. Positive news about a falling stock → "למרות החדשות, המניה ירדה".
  - Commodities when moving: oil with its geopolitical/supply backdrop, gold.
  - שוק החוב והתנודתיות: the 10Y yield and the VIX level (verified via web search) and what they signal about positioning.
  - Geopolitics / Washington politics with market impact.
  - Overnight sessions in Europe and Asia, a notable investor move, IPO or M&A — when truly material.
* LAST point — "שורה תחתונה: ..." — what will decide the direction of the session, in 1-2 sentences.
No ETF proxies, no Finnhub, no ISO dates."""
    if mode == "daily_summary":
        return f"""You are a senior Wall Street investment advisor writing your signature END-OF-DAY review in Hebrew for
{d['title_date_str']} (יום {d['title_day_name']}). PAST TENSE.

{POINT_STYLE}

This is a professional MARKET REVIEW — NOT a data dump. Explain the day — don't copy the data.
EXACTLY 6 points TOTAL (including the bottom-line point) — short and focused, not an article. Each point
is 4-5 lines. Fewer, deeper points beat many thin ones, so pick only the strongest stories of the day.
NEVER write mood-only sentences ("אווירה זהירה אך תומכת", "סנטימנט מעורב") — every sentence must carry a
fact, a number or a mechanism. A sentence whose deletion loses no information must be deleted.
* FIRST point — the day's story in one narrative (headline that captures the day, e.g. "יום תנודתי שהסתיים בירוק"):
  what the major indices did (direction + rounded %, from the verified data) woven into ONE story of the
  session — how it opened, what moved it, how it closed — not a list of numbers.
* MIDDLE points (4) — ONE point per real story. Pick the STRONGEST stories of the day FROM THE SOURCE TWEETS
  (and the verified Finnhub blocks), using the menu below as categories — do NOT force every category, and do
  NOT import a story that web search found on its own:
  - הסיפור של היום: WHY the market moved — the main driver, with clear cause-and-effect and the transmission
    mechanism explained simply.
  - Macro data released today: actual vs forecast vs previous AND the market implication (repricing of rate
    expectations, yields, sector rotation).
  - Leading and lagging sectors (sector percentages ONLY from the verified data) and what drove them.
  - 1-3 notable stock stories with the REASON for each move. Each significant story gets its own point.
  - Commodities, dollar and yields — direction and meaning, not a list of prices.
  - After-hours earnings, or geopolitics that moved markets today — when truly material.
* LAST point — "{d['bl_label']}: ..." — what investors should watch in the next session and why.
Every direction word MUST match the DIRECTIONAL FACTS block."""
    if mode == "israel_prep":
        if d["target_is_trading"]:
            if d["date_str"] == d["title_date_str"]:
                status = ("The briefing is for TODAY's Tel Aviv session. The exchange has NOT opened yet — never "
                          "describe it as open or trading. Use 'הבורסה צפויה להיפתח', 'המשקיעים יעקבו אחר'.")
            else:
                status = (f"This runs on {d['date_str']} but the briefing is for the NEXT Tel Aviv trading day: "
                          f"{d['title_date_str']} (יום {d['title_day_name']}). Do NOT use 'היום'/'הבוקר' — use "
                          f"'ביום {d['title_day_name']}'.")
        else:
            status = f"The target date {d['title_date_str']} is NOT a Tel Aviv trading day. State this in the first bullet."
        return f"""You are a senior investment advisor writing a signature PRE-MARKET briefing in Hebrew for the
TEL AVIV STOCK EXCHANGE (הבורסה לניירות ערך בתל אביב). Script run date: {d['date_str']} (יום {d['day_name']}).
Briefing target date: {d['title_date_str']} (יום {d['title_day_name']}). {status}

{ISRAEL_POINT_STYLE}

THIS BRIEFING SUMMARIZES THE CURATED HEBREW SOURCES — it is FORWARD-LOOKING:
- Content comes EXCLUSIVELY from the source posts at the bottom of this prompt. Do NOT add prices, index
  levels, percentages, movers or macro data that do not appear in a source. A figure enters ONLY if a source
  states it explicitly. Web search is for VERIFICATION of a name/figure already in a source, never to add news.
- Cover what the Tel Aviv investor should watch heading into the session: the leading themes and stories from
  the sources (companies, sectors, reports, macro from Bank of Israel, global backdrop as the sources frame it).
- 6-9 STRONG points TOTAL. FIRST point sets the picture heading into the session (headline like
  "סנטימנט זהיר לקראת הפתיחה"). MIDDLE points — ONE point per real story from the sources. LAST point —
  "שורה תחתונה: ..." — what will decide the direction of the Tel Aviv session, in 1-2 sentences.
- If the sources do not contain enough material, write fewer points rather than padding. Never invent stories.
No US market data, no Wall Street framing unless a source raises it, no ISO dates."""
    if mode == "israel_summary":
        return f"""You are a senior investment advisor writing a signature END-OF-DAY review in Hebrew for the
TEL AVIV STOCK EXCHANGE (הבורסה לניירות ערך בתל אביב) for {d['title_date_str']} (יום {d['title_day_name']}). PAST TENSE.

{ISRAEL_POINT_STYLE}

THIS REVIEW SUMMARIZES THE CURATED HEBREW SOURCES — it explains the day that ended:
- Content comes EXCLUSIVELY from the source posts at the bottom of this prompt. Do NOT add prices, index
  levels, percentages, movers or macro data that do not appear in a source. A figure (index move, a stock's
  change, a report number) enters ONLY if a source states it explicitly. Web search verifies a name/figure
  already in a source, never adds news of its own.
- Do NOT independently determine who rose or fell. Direction and magnitude for any story come from the source.
- 6-9 STRONG points TOTAL. FIRST point tells the day's story in one narrative (headline like
  "יום ירוק בהובלת הבנקים") from what the sources reported about the session. MIDDLE points — ONE point per
  real story (companies, sectors, reports, Bank of Israel, notable moves) as the sources framed them.
  LAST point — "{d['bl_label']}: ..." — what the Tel Aviv investor should watch next session and why.
- If the sources do not contain enough material, write fewer points rather than padding. Never invent stories.
No US market data, no Wall Street framing unless a source raises it, no ISO dates."""
    if mode == "israel_weekly_summary":
        return f"""You are a senior investment advisor writing your signature WEEKLY review in Hebrew for the
TEL AVIV STOCK EXCHANGE (הבורסה לניירות ערך בתל אביב) for the trading week {d['week_range']}. The review does
BOTH: it sums up the Tel Aviv week that ended AND prepares the reader for the coming Tel Aviv trading week.
PAST TENSE for the summary points. ONLY events and moves from THIS specific week in the summary points.

{ISRAEL_POINT_STYLE}

THIS REVIEW SUMMARIZES THE CURATED HEBREW SOURCES for the week that ended, then looks ahead:
- The SUMMARY stories come EXCLUSIVELY from the source posts below. Do NOT add prices, index levels, percentages,
  movers or macro data that do not appear in a source. A figure enters the summary ONLY if a source states it.
- Do NOT independently determine who rose or fell over the week. Direction and magnitude come from the sources.
- For the PREPARATION points you MAY use web search to confirm the COMING week's SCHEDULED calendar only
  (Bank of Israel decisions, Israeli macro releases, notable Tel Aviv earnings) with dates and Israel times.
6-9 STRONG points TOTAL in three blocks, in this order:
* OPENING point — "השבוע שהיה: ..." — 3-5 sentences telling the ARC of the Tel Aviv week as one story, as the
  sources framed it: how it opened, what set the tone, how it closed. Describe direction and drivers
  qualitatively, with only figures that appear in a source.
* SUMMARY points (3-5) — ONE thematic point per major Tel Aviv story of the week (banks, real estate, tech,
  defense, notable companies, Bank of Israel, the global backdrop as the sources frame it), each with its own
  specific headline. Pick the STRONGEST stories from the sources — do NOT force categories or pad.
* PREPARATION points (1-2) — the COMING Tel Aviv week:
  - "השבוע הקרוב במאקרו: ..." — the scheduled Bank of Israel decisions and Israeli macro releases with dates and
    Israel times (from the sources, or verified via web search of the scheduled calendar).
  - "דוחות בשבוע הקרוב: ..." — the notable Tel Aviv earnings reports due and what the market will watch in them
    (merge into the macro point when the slate is thin).
* CLOSING point — "בשורה התחתונה: ..." — 2-4 sentences of synthesis: what the week taught the Tel Aviv investor
  and the frame for the coming week.
If the sources do not contain enough material, write fewer points rather than padding. Never invent stories.
No US market data, no Wall Street framing unless a source raises it, no ISO dates."""
    if d.get("has_weekly"):
        weekly_num_rule = (
            "Use the WEEKLY PERFORMANCE numbers for weekly index changes — NOT the daily numbers, and never "
            "confuse Friday's daily change with the weekly change. Where only a daily number is given for a "
            "symbol, do NOT present it as a weekly change.")
        weekly_arc_rule = "with the weekly index numbers woven into the narrative"
    else:
        weekly_num_rule = (
            "No WEEKLY PERFORMANCE numbers are available this run. Do NOT state ANY weekly percentage and never "
            "present a daily change as the weekly change. If you cite a specific percentage, make explicit that it "
            "is the last trading day's move only.")
        weekly_arc_rule = ("describing the week's direction and drivers qualitatively (no invented weekly "
                           "percentages)")
    return f"""You are a senior Wall Street investment advisor writing your signature WEEKLY review in Hebrew for the
trading week {d['week_range']}. The review does BOTH: sums up the week that ended AND prepares the reader for
the coming week. PAST TENSE for the summary points. ONLY events and moves from THIS specific week in the
summary points. {weekly_num_rule}

{POINT_STYLE}

8-10 points TOTAL in three blocks, in this order (the weekly review is the extended one, but every sentence
must still carry a fact, a number or a mechanism — no mood-only filler):
* OPENING point — "השבוע שהיה: ..." — 3-5 sentences telling the ARC of the week as one story: how it opened,
  what flipped the sentiment, how it closed, {weekly_arc_rule}.
* SUMMARY points (4-6) — ONE thematic point per major story of the week, each with its own specific headline.
  Pick the STRONGEST stories FROM THE TWEETS — do NOT force every category, and do NOT import stories from
  outside the tweets:
  - Fed policy signals and rate expectations, ONLY if they appear in the tweets, with the probabilities as quoted.
  - Macro data ONLY as it appears in the tweets or the verified economic block, with the full numbers they
    provide (actual vs forecast vs previous) and the market implication — merge related releases into one point.
    Do NOT web-search for macro data the sources did not cover, and do NOT fill in missing
    actual/forecast/previous figures from memory.
  - The week's defining sector/technology story, with the transmission mechanism.
  - Notable company news: earnings, M&A, milestones — merged where related.
  - Commodities and the dollar with weekly context, or geopolitics with market impact.
* PREPARATION points (1-2) — the COMING week (verify the schedule via web search — permitted use c):
  - "השבוע הקרוב במאקרו: ..." — the scheduled releases and Fed events with dates, Israel times and consensus.
  - "דוחות בשבוע הקרוב: ..." — the key earnings reports scheduled and what the market will look for in them
    (merge into the macro point when the earnings slate is thin).
* CLOSING point — "בשורה התחתונה: ..." — 2-4 sentences of synthesis: what the week taught us, the fragilities
  and the opportunities, and the frame for the coming week. Seasonal/historical context is welcome when verified."""


def build_paste_block(mode: str, d: Dict[str, Any], expected_title: str, market_block: str,
                      econ_block: str, checklist: str, prior_context: str, tweets: str,
                      now_il: datetime) -> str:
    first_heading = EXPECTED_FIRST_HEADING[mode]
    example_content = (
        "* נושא ראשון: משפט אנליטי תמציתי עם מספרים.\\n* נושא שני: ...\\n* נושא שלישי: ..."
        if mode == "intraday_update" else
        "* כותרת קצרה וספציפית: שניים עד ארבעה משפטים של פרוזה אנליטית עם המספרים המרכזיים, ההקשר והמשמעות.\\n* כותרת נוספת: ..."
    )
    source_hierarchy = get_source_hierarchy(mode)
    parts = [
        "אתה כותב סקירה פיננסית בעברית לאתר. קרא את כל ההנחיות והנתונים למטה, השתמש בחיפוש אינטרנט לאימות בלבד, והחזר JSON בלבד.",
        "",
        mode_instructions(mode, d, bool(tweets)),
    ]
    # The Finnhub-backed US modes carry the explicit source-hierarchy block; the
    # tweet-only modes state their exclusivity inside the mode instructions.
    if source_hierarchy:
        parts += ["", source_hierarchy]
    parts += [
        "",
        # Tweet-only modes (intraday + Israeli reviews) get the reduced rule set with
        # no references to a verified Finnhub layer, which they do not have. The Israeli
        # weekly gets a variant that permits scheduled-calendar figures for its prep block.
        ISRAEL_WEEKLY_RULES if mode == "israel_weekly_summary"
        else INTRADAY_RULES if mode in ("intraday_update",) + ISRAEL_MODES
        else SHARED_RULES,
        "",
        # The error-prevention mechanism: every mode ends its instruction section
        # with a mandatory pre-output self-check before the JSON may be returned.
        get_self_verification(mode),
        "",
        f"""CRITICAL — OUTPUT FORMAT (MANDATORY):
- Return ONLY a JSON object, no backticks, no explanations, in EXACTLY this structure:
{{
  "title": "{expected_title}",
  "date": "{d['review_date']}",
  "summary": ["כותרת הנקודה: תמצית אמיתית של הנקודה במשפט קצר אחד", "כותרת שנייה: ...", "..."],
  "sections": [
    {{
      "heading": "{first_heading}",
      "content": "{example_content}"
    }}
  ]
}}
- EXACTLY 1 section. Heading EXACTLY "{first_heading}". Title EXACTLY as given above.
- content = one string, bullets separated by \\n, each bullet starts with "* ".
- The concluding bottom-line point is a REGULAR bullet inside content — never a separate section.
- No **, no ##, no HTML, no URLs inside content.
- "summary" = an array with ONE item per bullet in content, in the SAME order (include the bottom-line point too).
  Each item is "<אותה כותרת קצרה של הנקודה>: <משפט תמציתי אחד>". The sentence must DISTILL the essence of the point —
  what happened and why it matters — in your own words, up to ~20 words. Do NOT copy the first sentence of the
  bullet verbatim. All the same verification and direction rules apply to the summary as to the bullets.""",
    ]
    # The US time-conversion block is irrelevant to Tel Aviv reviews.
    if mode not in ISRAEL_MODES:
        parts += ["", get_time_conversion_block(now_il)]
    for block in (market_block, econ_block, checklist, prior_context):
        if block:
            parts += ["", block]
    if tweets:
        source_note = (
            "מקורות מרשת X (בעברית) — Never mention in the review that these came from posts/X:"
            if mode in ISRAEL_MODES else
            f"Source tweets/posts from X (Twitter) — gathered {d['date_str']}. Never mention in the review that these came from tweets/posts:"
        )
        parts += ["", source_note, "", tweets]
    elif mode == "intraday_update":
        parts += ["", (f"NOTE: no source tweets from the window {d['window_from']}–{d['time_str']} Israel time were "
                       f"gathered for this run. Per the rules above, return the single bullet "
                       f"\"* אין מספיק עדכונים משמעותיים מהמקורות בחלון הזמן הזה.\" — do NOT use web search to fill "
                       f"the update with news, and do NOT recycle older headlines or unrelated macro.")]
    elif mode in ISRAEL_MODES:
        parts += ["", ("NOTE: no source posts were gathered for this run. These reviews are sourced ONLY from the "
                       "curated Hebrew X accounts, so do NOT fabricate a review from web search or memory. Return a "
                       "single bullet stating there is not enough source material right now: "
                       "\"* אין מספיק חומר מהמקורות להפקת סקירה כרגע.\"")]
    else:
        parts += ["", ("NOTE: no source tweets were gathered for this run, so the stories layer is missing. Build the "
                       "review ONLY from the verified Finnhub blocks above (indices, sectors, commodities, economic "
                       "data) plus the permitted verification searches (scheduled calendar, futures). Do NOT import "
                       "news stories from web search or memory — describe the verified moves and the scheduled "
                       "calendar instead.")]
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
    tweets, top_cashtags = fetch_and_select_tweets(since, REVIEW_MODE)

    # Tweet-only modes (intraday + Israeli reviews) carry no Finnhub layer.
    tweet_only = REVIEW_MODE in ("intraday_update",) + ISRAEL_MODES

    print("\n── Finnhub market data ──")
    if tweet_only:
        # These modes only summarize the sources — no price data, no movers, no
        # percentages. Nothing from Finnhub enters their prompt.
        print(f"  {REVIEW_MODE} summarizes the sources only — skipping market data")
        market_block, pcts, ticker_quotes, weekly_available = "", {}, {}, False
    else:
        # Post-session modes carry a settled close; record it so weekly runs can
        # compute true weekly changes from the accumulated history.
        record_close = REVIEW_MODE in ("weekly_summary", "daily_summary")
        market_block, pcts, ticker_quotes, weekly_available = fetch_market_data(
            REVIEW_MODE == "weekly_summary", top_cashtags, d, record_close)
    d["has_weekly"] = weekly_available

    print("\n── Economic calendar ──")
    if tweet_only:
        print(f"  {REVIEW_MODE} summarizes the sources only — skipping economic calendar")
        econ_block = ""
    else:
        econ_days = {
            "daily_prep": (1, 1), "daily_summary": (1, 0), "weekly_summary": (7, 7),
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
