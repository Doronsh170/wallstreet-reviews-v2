"""examples/weekly_history_demo.py — how the weekly summary anchors every weekly %.

Runnable proof (uses the REAL functions from gather_review_input.py) that:
  1. every emitted weekly % is (prior close from market_history.json) → (current
     price from the live quote); and
  2. if the quote is NOT a reliable end-of-week close (intraday / stale last trade,
     not the week's Friday), NO weekly % is shown for that symbol.

Run:  python examples/weekly_history_demo.py
"""
import os
import sys
from datetime import datetime

os.environ.setdefault("REVIEW_MODE", "weekly_summary")
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import gather_review_input as g  # noqa: E402


def ts_at(date_str: str, hour: int = 16, minute: int = 0) -> int:
    """UNIX timestamp for a NY-market wall-clock time (16:00 ET = the closing print)."""
    y, m, d = map(int, date_str.split("-"))
    return int(datetime(y, m, d, hour, minute, tzinfo=g.NY_TZ).timestamp())


# 1) The prior-week Friday closes that market_history.json holds after the 10.7 seed.
history = {
    "SPY":  {"2026-07-10": 754.95},
    "QQQ":  {"2026-07-10": 725.51},
    "META": {"2026-07-10": 669.21},
    "MU":   {"2026-07-10": 979.30},
}

# 2) The weekly run fires for the 13–17.7.2026 week.
monday = "2026-07-13"
friday = "2026-07-17"   # week_close_date — the current anchor MUST settle on this day.

# 3) Live quotes captured when the run fires (Sat 18.7). 'ts' = time of the last trade.
quotes = {
    # settled on Friday 17.7 AND have a prior close in history → weekly % emitted
    "SPY":  {"price": 761.80, "ts": ts_at(friday)},
    "META": {"price": 690.40, "ts": ts_at(friday)},
    "MU":   {"price": 968.10, "ts": ts_at(friday)},
    # settled on Friday but NO prior close in history → excluded (missing anchor 2)
    "TSLA": {"price": 402.10, "ts": ts_at(friday)},
    # has a prior close, but the quote is a Thursday intraday price, NOT a settled
    # end-of-week close → excluded (fails anchor 1)
    "QQQ":  {"price": 731.00, "ts": ts_at("2026-07-16", 11, 30)},
}

current_prices = {s: q["price"] for s, q in quotes.items()}
close_dates = {s: g.quote_close_date(q["ts"]) for s, q in quotes.items()}

labeled = [("SPY", "S&P 500 (SPY ETF)"), ("QQQ", "Nasdaq 100 (QQQ ETF)"),
           ("META", "$META"), ("MU", "$MU"), ("TSLA", "$TSLA")]

lines, missing = g.compute_weekly_lines(
    history, labeled, monday, current_prices, close_dates, friday)

print("\n== WEEKLY PERFORMANCE block the model receives ==")
print("WEEKLY PERFORMANCE (use THESE for weekly changes in the weekly summary, NOT the daily numbers):")
for line in lines:
    print(line)

print("\n== provenance — every % = prior anchor (history) + current price (quote) ==")
for sym, label in labeled:
    res = g.weekly_pct_from_history(history, sym, monday, current_prices[sym]) \
        if close_dates[sym] == friday else None
    if res:
        pct, prior_close, prior_date = res
        print(f"  {label}: prior ${prior_close:.2f} on {prior_date} (market_history.json)"
              f" + current ${current_prices[sym]:.2f} settled {close_dates[sym]} (quote) = {pct:+.2f}%")

print("\n== excluded — no weekly % shown ==")
for sym, label in labeled:
    if label in missing:
        reason = (f"quote is a {close_dates[sym]} price, not a settled {friday} close"
                  if close_dates[sym] != friday else
                  "no prior-week close in market_history.json")
        print(f"  {label}: {reason}")
