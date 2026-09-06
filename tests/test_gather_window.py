"""Tests for the source-material window in gather_review_input.py.

Until this layer existed, only intraday_update filtered posts by time — every other
mode fed the model "the account's latest tweets" regardless of age. A real run of
israel_summary for 31.8.2026 carried six posts from July (up to seven weeks old) and
three from the day AFTER the session it was summarising. These tests lock the window
shut so that cannot come back.
"""
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

import pytest

# gather_review_input resolves its mode at import time from argv/env and exits on a
# bad one, so give it a valid mode and a clean argv before importing.
os.environ.setdefault("REVIEW_MODE", "daily_prep")
_saved_argv = sys.argv
sys.argv = [str(Path(__file__).resolve().parent.parent / "gather_review_input.py")]
import gather_review_input as g  # noqa: E402
sys.argv = _saved_argv

ISR = ZoneInfo("Asia/Jerusalem")
ALL_MODES = g.VALID_MODES


def il(y, m, d, hh=0, mm=0):
    return datetime(y, m, d, hh, mm, tzinfo=ISR)


def dates_for(mode, now):
    return g.compute_dates(mode, now, g.FALLBACK_US_HOLIDAYS)


def window_for(mode, now):
    return g.compute_tweet_window(mode, now, dates_for(mode, now))


# ── the window itself ────────────────────────────────────────────

@pytest.mark.parametrize("mode", ALL_MODES)
def test_every_mode_is_bounded_on_the_since_side(mode):
    """The regression that mattered: no mode may accept posts of unlimited age."""
    now = il(2026, 9, 1, 7, 0)
    since, _ = window_for(mode, now)
    assert since is not None, f"{mode} accepts posts of any age"
    assert since <= now


@pytest.mark.parametrize("mode", ALL_MODES)
def test_window_is_never_inverted(mode):
    now = il(2026, 9, 1, 7, 0)
    since, until = window_for(mode, now)
    if until is not None:
        assert since < until


def test_intraday_window_is_unchanged():
    now = il(2026, 8, 14, 17, 40)
    since, until = window_for("intraday_update", now)
    assert since == now - timedelta(hours=g.INTRADAY_WINDOW_HOURS)
    assert until is None


@pytest.mark.parametrize("mode", ["daily_prep", "israel_prep"])
def test_prep_modes_look_back_one_night(mode):
    now = il(2026, 8, 20, 8, 30)
    since, until = window_for(mode, now)
    assert since == now - timedelta(hours=g.PREP_WINDOW_HOURS)
    assert until is None, "a prep review wants the freshest posts, with no upper bound"


def test_daily_summary_covers_the_session_and_its_after_hours():
    # Run the morning after the 31.8 session, as the real runs do.
    now = il(2026, 9, 1, 6, 55)
    d = dates_for("daily_summary", now)
    assert d["review_date"] == "2026-08-31"
    since, until = window_for("daily_summary", now)
    assert since == il(2026, 8, 31, 9, 0)
    assert until == il(2026, 9, 1, 9, 0)
    # US close is 23:00 Israel; the after-hours reaction must still be inside.
    assert since < il(2026, 9, 1, 1, 30) < until


def test_israel_summary_covers_the_tase_session():
    now = il(2026, 9, 1, 6, 55)
    since, until = window_for("israel_summary", now)
    assert since == il(2026, 8, 31, 6, 0)
    assert until == il(2026, 9, 1, 6, 0)
    assert since < il(2026, 8, 31, 9, 30) < il(2026, 8, 31, 17, 30) < until


@pytest.mark.parametrize("mode", ["weekly_summary", "israel_weekly_summary"])
def test_weekly_opens_at_the_monday_of_the_reviewed_week(mode):
    now = il(2026, 8, 16, 8, 0)          # Sunday, reviewing 10/08–14/08
    d = dates_for(mode, now)
    assert d["review_date"] == "2026-08-14"
    since, until = window_for(mode, now)
    assert since == il(2026, 8, 10, 0, 0)
    assert until is None, "weekend commentary feeds the coming-week half"


def test_unparseable_review_date_still_yields_a_window():
    since, until = g.compute_tweet_window("daily_summary", il(2026, 9, 1, 7, 0),
                                          {"review_date": "not-a-date"})
    assert since is not None and until is None


# ── the filter that applies it ───────────────────────────────────

def fake_api(tweets, per_account=False):
    """Stubs http_get so fetch_and_select_tweets sees exactly `tweets` per account.
    per_account=True makes each account's texts distinct, so the exact-text dedupe
    does not collapse them into one."""
    def get(*a, **k):
        acct = (k.get("params") or {}).get("userName", "")
        body = [dict(t, text=f"{t['text']} ({acct})", id=f"{acct}-{t['id']}")
                for t in tweets] if per_account else tweets

        class R:
            ok = True
            status_code = 200

            @staticmethod
            def json():
                return {"tweets": body}

        return R()

    return get


def distinct_story(i):
    """Six words shared with no other post, so the near-duplicate collapse leaves it
    alone and the test measures only the per-mode cap."""
    letters = "abcdefghijklmnopqrstuvwxyz"
    return " ".join("z" + letters[(i * 6 + j) // 26 % 26] + letters[(i * 6 + j) % 26] + "q"
                    for j in range(6))


_ids = iter(range(1, 100000))


def tweet(text, created, likes=0, views=0):
    return {"id": f"t{next(_ids)}", "text": text, "createdAt": created,
            "likeCount": likes, "viewCount": views}


def run_filter(monkeypatch, tweets, mode, since, until, accounts=("acct",),
               per_account=False):
    monkeypatch.setattr(g, "TWITTER_API_KEY", "test-key")
    monkeypatch.setattr(g, "http_get", fake_api(tweets, per_account))
    monkeypatch.setattr(g, "read_accounts", lambda mode="": list(accounts))
    blocks, _ = g.fetch_and_select_tweets(since, mode, until)
    return blocks


# The exact createdAt values from the israel_summary run for 31.8.2026 that shipped
# stale material. Only the 31.8 posts belong in a summary of that session.
REAL_RUN_SAMPLE = [
    tweet("ציוץ מיום המסחר עצמו על הבורסה", "Mon Aug 31 11:03:23 +0000 2026"),
    tweet("עוד ציוץ מיום המסחר על מדד ת\"א", "Mon Aug 31 10:10:21 +0000 2026"),
    tweet("ציוץ מהיום שאחרי הסקירה", "Tue Sep 01 05:12:00 +0000 2026"),
    tweet("ציוץ ישן מיולי על הבורסה", "Sun Jul 26 08:26:17 +0000 2026"),
    tweet("עוד ציוץ ישן מיולי על מניה", "Tue Jul 14 12:47:53 +0000 2026"),
    tweet("ציוץ מלפני שלושה ימים על ריבית", "Sun Aug 30 04:56:52 +0000 2026"),
]


def test_stale_and_next_day_posts_are_dropped_from_a_summary(monkeypatch):
    since, until = window_for("israel_summary", il(2026, 9, 1, 6, 55))
    blocks = run_filter(monkeypatch, REAL_RUN_SAMPLE, "israel_summary", since, until)
    assert "מיום המסחר עצמו" in blocks
    assert "מדד ת\"א" in blocks
    assert "מיולי" not in blocks, "seven-week-old posts reached a one-session summary"
    assert "מהיום שאחרי" not in blocks, "the next day's posts reached the summary"
    assert "מלפני שלושה ימים" not in blocks


def test_promotional_posts_are_dropped_outside_intraday_too(monkeypatch):
    now = il(2026, 8, 20, 8, 30)
    since, until = window_for("daily_prep", now)
    recent = (now - timedelta(hours=2)).strftime("%a %b %d %H:%M:%S +0000 %Y")
    tweets = [
        tweet("Fed minutes land today, futures point higher on the S&P", recent),
        tweet("Huge giveaway! Like & RT to win, winners will be announced", recent),
    ]
    blocks = run_filter(monkeypatch, tweets, "daily_prep", since, until)
    assert "Fed minutes" in blocks
    assert "giveaway" not in blocks.lower()


def test_posts_with_unreadable_timestamps_are_dropped(monkeypatch):
    now = il(2026, 8, 20, 8, 30)
    since, until = window_for("daily_prep", now)
    recent = (now - timedelta(hours=1)).strftime("%a %b %d %H:%M:%S +0000 %Y")
    tweets = [tweet("CPI is due today at 15:30 Israel time", recent),
              tweet("Undated post about an old CPI print", "")]
    blocks = run_filter(monkeypatch, tweets, "daily_prep", since, until)
    assert "due today" in blocks
    assert "Undated" not in blocks


@pytest.mark.parametrize("mode,expected", [
    ("daily_prep", 20), ("daily_summary", 20), ("israel_prep", 20), ("israel_summary", 20),
    ("weekly_summary", 30), ("israel_weekly_summary", 30), ("intraday_update", 40),
])
def test_per_mode_cap_is_applied(monkeypatch, mode, expected):
    monkeypatch.setattr(g, "MAX_TWEETS_ENV_OVERRIDE", "")
    assert g.max_tweets_for(mode) == expected
    now = il(2026, 9, 1, 12, 0)
    since, until = window_for(mode, now)
    inside = (since + timedelta(minutes=5)) if since else now
    stamp = inside.astimezone(g.timezone.utc).strftime("%a %b %d %H:%M:%S +0000 %Y")
    # One account with a raised per-account slice: distinct stories only, so nothing
    # is merged and the test measures the per-mode cap alone.
    monkeypatch.setattr(g, "MAX_TWEETS_PER_ACCOUNT", 60)
    many = [tweet(distinct_story(i), stamp, likes=i) for i in range(60)]
    blocks = run_filter(monkeypatch, many, mode, since, until)
    assert blocks.count("\n\n") + 1 == expected


def test_env_override_still_wins(monkeypatch):
    monkeypatch.setattr(g, "MAX_TWEETS_ENV_OVERRIDE", "7")
    assert g.max_tweets_for("daily_prep") == 7


def test_no_key_is_still_a_clean_skip(monkeypatch):
    monkeypatch.setattr(g, "TWITTER_API_KEY", "")
    blocks, tags = g.fetch_and_select_tweets(il(2026, 9, 1), "daily_prep", None)
    assert blocks == "" and tags == []


# ── P3: near-duplicate collapse and quality filters ──────────────

def test_the_same_story_from_several_accounts_becomes_one_post(monkeypatch):
    now = il(2026, 8, 20, 8, 30)
    since, until = window_for("daily_prep", now)
    recent = (now - timedelta(hours=1)).astimezone(g.timezone.utc).strftime(
        "%a %b %d %H:%M:%S +0000 %Y")
    # One story told four ways, plus one genuinely different story.
    tweets = [
        tweet("$NVDA beats earnings estimates, raises guidance for next quarter", recent),
        tweet("NVDA beats earnings estimates and raises guidance for the next quarter", recent),
        tweet("$NVDA earnings beat estimates, guidance raised for next quarter", recent),
        tweet("Nvidia beats earnings estimates, raises its guidance for next quarter", recent),
        tweet("Oil climbs above eighty dollars on renewed supply disruption worries", recent),
    ]
    blocks = run_filter(monkeypatch, tweets, "daily_prep", since, until)
    posts = [b for b in blocks.split("\n\n") if b.strip()]
    assert len(posts) == 2, f"expected one NVDA story + one oil story, got:\n{blocks}"
    assert "Oil climbs" in blocks


def test_distinct_stories_are_never_merged(monkeypatch):
    now = il(2026, 8, 20, 8, 30)
    since, until = window_for("daily_prep", now)
    recent = (now - timedelta(hours=1)).astimezone(g.timezone.utc).strftime(
        "%a %b %d %H:%M:%S +0000 %Y")
    tweets = [
        tweet("$NVDA beats earnings estimates and raises guidance for next quarter", recent),
        tweet("Fed leaves rates unchanged, Powell signals patience at the press conference", recent),
        tweet("Oil climbs above eighty dollars on renewed supply disruption worries", recent),
        tweet("מדד תל אביב 35 עלה במסחר, מניות הבנקים הובילו את העליות", recent),
    ]
    blocks = run_filter(monkeypatch, tweets, "daily_prep", since, until)
    posts = [b for b in blocks.split("\n\n") if b.strip()]
    assert len(posts) == 4, f"distinct stories were merged:\n{blocks}"


def test_a_corroborated_story_outranks_an_equally_scored_lone_one(monkeypatch):
    now = il(2026, 8, 20, 8, 30)
    since, until = window_for("daily_prep", now)
    recent = (now - timedelta(hours=1)).astimezone(g.timezone.utc).strftime(
        "%a %b %d %H:%M:%S +0000 %Y")
    lone = "Bitcoin holds steady near its recent trading range today"
    carried = "Regional bank discloses unexpected credit losses in commercial property"
    assert g.tweet_score(g.normalize_tweet({"text": lone}, "a")) == \
           g.tweet_score(g.normalize_tweet({"text": carried}, "a")), "fixture must be score-neutral"
    tweets = [
        tweet(lone, recent),
        tweet(carried, recent),
        tweet("A regional bank disclosed unexpected credit losses on commercial property", recent),
        tweet("Regional bank discloses unexpected credit losses across commercial property", recent),
    ]
    blocks = run_filter(monkeypatch, tweets, "daily_prep", since, until)
    posts = [b for b in blocks.split("\n\n") if b.strip()]
    assert len(posts) == 2, f"the three retellings should be one story:\n{blocks}"
    assert "credit losses" in posts[0], f"corroboration did not lift the story:\n{blocks}"


def test_bare_ticker_lists_are_dropped(monkeypatch):
    now = il(2026, 8, 20, 8, 30)
    since, until = window_for("daily_prep", now)
    recent = (now - timedelta(hours=1)).astimezone(g.timezone.utc).strftime(
        "%a %b %d %H:%M:%S +0000 %Y")
    tweets = [
        tweet("$SPY $QQQ $NVDA $TSLA $AAPL $AMD watchlist today", recent),
        tweet("$NVDA $AMD $AVGO $MU semiconductor stocks rally on strong AI demand outlook", recent),
    ]
    blocks = run_filter(monkeypatch, tweets, "daily_prep", since, until)
    assert "watchlist today" not in blocks, "a bare watchlist reached the prompt"
    assert "semiconductor stocks rally" in blocks, "a real chip story was dropped as a list"


def test_very_long_posts_are_trimmed(monkeypatch):
    now = il(2026, 8, 20, 8, 30)
    since, until = window_for("daily_prep", now)
    recent = (now - timedelta(hours=1)).astimezone(g.timezone.utc).strftime(
        "%a %b %d %H:%M:%S +0000 %Y")
    long_text = "The Federal Reserve released its statement and " + ("detail " * 200)
    blocks = run_filter(monkeypatch, [tweet(long_text, recent)], "daily_prep", since, until)
    assert len(blocks) < len(long_text)
    assert blocks.rstrip().endswith("…")
    assert "The Federal Reserve released its statement" in blocks
