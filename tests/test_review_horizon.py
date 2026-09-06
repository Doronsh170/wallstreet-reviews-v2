"""Prep looks forward, summary looks back — enforced in the window, the ranking and
the prompt, not just in the hours a mode collects.

Prep = what is about to happen and what matters before trading.
Summary = what happened and why it mattered.

These tests exist so the two cannot quietly blend back together: a prep that fills up
with yesterday's closing report, or a summary that turns into tomorrow's briefing.
"""
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import pytest

os.environ.setdefault("REVIEW_MODE", "daily_prep")
_saved_argv = sys.argv
sys.argv = [str(Path(__file__).resolve().parent.parent / "gather_review_input.py")]
import gather_review_input as g  # noqa: E402
sys.argv = _saved_argv

ISR = ZoneInfo("Asia/Jerusalem")

PREP = list(g.PREP_MODES)
SUMMARY = list(g.SUMMARY_MODES)
WEEKLY = list(g.WEEKLY_SUMMARY_MODES)
WEEKLY_PREP = list(g.WEEKLY_PREP_MODES)
# The daily briefings keep a "fresh tier" that lets recent news in unconditionally;
# the week-ahead briefings deliberately do not (see prep_fresh_cutoff).
DAILY_PREP = [m for m in PREP if m not in WEEKLY_PREP]

FORWARD_POST = "CPI is due Monday at 15:30, consensus 2.4% — futures are pricing a soft print"
BACKWARD_POST = "Stocks closed sharply lower; the S&P 500 finished down and the Dow tumbled"
FORWARD_HEB = "מדד המחירים צפוי להתפרסם מחר, והמשקיעים יעקבו אחר החלטת בנק ישראל הקרובה"
BACKWARD_HEB = "המסחר ננעל בירידות, מדד ת\"א 35 צנח והבנקים סיכמו יום אדום"


def il(y, m, d, hh=0, mm=0):
    return datetime(y, m, d, hh, mm, tzinfo=ISR)


def stamp(dt):
    return dt.astimezone(timezone.utc).strftime("%a %b %d %H:%M:%S +0000 %Y")


def post(text, when, likes=0, views=0):
    return {"id": f"{text[:12]}{when}", "text": text, "createdAt": stamp(when),
            "likeCount": likes, "viewCount": views}


def norm(text):
    return g.normalize_tweet({"text": text}, "acct")


# ── the signals themselves ───────────────────────────────────────

@pytest.mark.parametrize("text", [
    FORWARD_POST, FORWARD_HEB,
    "Nvidia reports after the close on Wednesday",
    "Powell speaks tomorrow; markets await the rate decision",
    "דוחות הבנקים מתוכננים לשבוע הקרוב",
])
def test_forward_signals_are_recognised(text):
    assert g.FORWARD_SIGNAL_RE.search(text), text


@pytest.mark.parametrize("text", [
    BACKWARD_POST, BACKWARD_HEB,
    "Nvidia beat estimates and the stock surged",
    "המדד ננעל בעליות והמניה זינקה",
])
def test_past_signals_are_recognised(text):
    assert g.PAST_SIGNAL_RE.search(text), text


def test_hebrew_stems_never_match_inside_another_word():
    """The documented 'נפל inside אינפלציה' class of bug — a stem must not fire on a
    longer word that merely contains it."""
    for text in ["האינפלציה נותרה גבוהה", "מעלה את הרף", "הצפיפות בשוק הדיור"]:
        assert not g.PAST_SIGNAL_RE.search(text), text


# ── ranking: the same post is worth opposite amounts ─────────────

@pytest.mark.parametrize("mode", PREP)
def test_prep_prefers_what_has_not_happened(mode):
    forward, backward = norm(FORWARD_POST), norm(BACKWARD_POST)
    assert g.horizon_bonus(forward, mode) > 0
    assert g.horizon_bonus(backward, mode) < 0
    assert g.ranked_score(forward, mode) > g.ranked_score(backward, mode)


@pytest.mark.parametrize("mode", SUMMARY + WEEKLY)
def test_summary_prefers_what_already_happened(mode):
    forward, backward = norm(FORWARD_POST), norm(BACKWARD_POST)
    assert g.horizon_bonus(backward, mode) > 0
    assert g.horizon_bonus(forward, mode) < 0
    assert g.ranked_score(backward, mode) > g.ranked_score(forward, mode)


@pytest.mark.parametrize("mode", WEEKLY)
def test_a_weekly_ranks_exactly_like_a_daily_summary(mode):
    """A weekly review is a summary. It gets no exception: forward-looking material is
    penalised there just as it is in a daily summary."""
    for text in (FORWARD_POST, BACKWARD_POST, FORWARD_HEB, BACKWARD_HEB):
        assert g.horizon_bonus(norm(text), mode) == g.horizon_bonus(norm(text), "daily_summary")
    assert g.horizon_bonus(norm(FORWARD_POST), mode) < 0


def test_intraday_ranking_is_unchanged():
    for text in (FORWARD_POST, BACKWARD_POST):
        assert g.horizon_bonus(norm(text), "intraday_update") == 0.0


# ── the window: reach back, but only for what points forward ─────

def fake_api(posts):
    class R:
        ok = True
        status_code = 200

        @staticmethod
        def json():
            return {"tweets": posts}

    return lambda *a, **k: R()


def gather(monkeypatch, posts, mode, now):
    monkeypatch.setattr(g, "TWITTER_API_KEY", "test-key")
    monkeypatch.setattr(g, "http_get", fake_api(posts))
    monkeypatch.setattr(g, "read_accounts", lambda mode="": ["acct"])
    d = g.compute_dates(mode, now, g.FALLBACK_US_HOLIDAYS)
    since, until = g.compute_tweet_window(mode, now, d)
    blocks, _ = g.fetch_and_select_tweets(since, mode, until, g.prep_fresh_cutoff(mode, now))
    return blocks


@pytest.mark.parametrize("mode", PREP)
def test_a_friday_post_about_a_monday_release_reaches_mondays_prep(monkeypatch, mode):
    """The user's own example: old material stays eligible when it points at an event
    that is still ahead."""
    monday = il(2026, 9, 7, 8, 0)
    friday = il(2026, 9, 4, 16, 0)
    blocks = gather(monkeypatch, [post(FORWARD_POST, friday)], mode, monday)
    assert "CPI is due Monday" in blocks


@pytest.mark.parametrize("mode", PREP)
def test_an_old_backward_looking_post_still_does_not_reach_a_prep(monkeypatch, mode):
    """Widening the reach must not reopen the stale-content hole P0 closed."""
    monday = il(2026, 9, 7, 8, 0)
    friday = il(2026, 9, 4, 16, 0)
    blocks = gather(monkeypatch, [post(BACKWARD_POST, friday)], mode, monday)
    assert "closed sharply lower" not in blocks


@pytest.mark.parametrize("mode", DAILY_PREP)
def test_recent_material_needs_no_forward_signal(monkeypatch, mode):
    """Inside the fresh tier a post is current news and enters on its own merit."""
    now = il(2026, 9, 7, 8, 0)
    blocks = gather(monkeypatch, [post(BACKWARD_POST, now - timedelta(hours=3))], mode, now)
    assert "closed sharply lower" in blocks


@pytest.mark.parametrize("mode", PREP)
def test_a_prep_never_reaches_past_its_lookback(monkeypatch, mode):
    now = il(2026, 9, 7, 8, 0)
    lookback = (g.WEEKLY_PREP_LOOKBACK_HOURS if mode in WEEKLY_PREP
                else g.PREP_LOOKBACK_HOURS)
    ancient = now - timedelta(hours=lookback + 24)
    blocks = gather(monkeypatch, [post(FORWARD_POST, ancient)], mode, now)
    assert "CPI is due Monday" not in blocks, "a forward signal must not buy unlimited age"


@pytest.mark.parametrize("mode", SUMMARY)
def test_a_summary_window_did_not_widen(mode):
    """Only prep gained reach; a summary still covers just its own session."""
    now = il(2026, 9, 7, 7, 0)
    since, until = g.compute_tweet_window(mode, now, g.compute_dates(mode, now, g.FALLBACK_US_HOLIDAYS))
    assert until is not None
    assert (until - since) == timedelta(hours=24)
    assert g.prep_fresh_cutoff(mode, now) is None


# ── no blending, end to end through the selection ────────────────

@pytest.mark.parametrize("mode,expected,rejected", [
    ("daily_prep", "CPI is due Monday", "closed sharply lower"),
    ("israel_prep", "CPI is due Monday", "closed sharply lower"),
    ("daily_summary", "closed sharply lower", "CPI is due Monday"),
    ("israel_summary", "closed sharply lower", "CPI is due Monday"),
    ("weekly_summary", "closed sharply lower", "CPI is due Monday"),
    ("israel_weekly_summary", "closed sharply lower", "CPI is due Monday"),
])
def test_the_top_post_faces_the_right_way(monkeypatch, mode, expected, rejected):
    now = il(2026, 9, 7, 8, 0) if mode in PREP else il(2026, 9, 8, 7, 0)
    d = g.compute_dates(mode, now, g.FALLBACK_US_HOLIDAYS)
    since, until = g.compute_tweet_window(mode, now, d)
    when = (until - timedelta(hours=1)) if until else (now - timedelta(hours=1))
    blocks = gather(monkeypatch, [post(BACKWARD_POST, when), post(FORWARD_POST, when)], mode, now)
    first = blocks.split("\n\n")[0]
    assert expected in first, blocks
    assert rejected not in first, blocks


# ── the prompt says it too ───────────────────────────────────────

def dates(mode, now):
    return g.compute_dates(mode, now, g.FALLBACK_US_HOLIDAYS)


def instructions(mode):
    now = il(2026, 9, 7, 8, 0)
    return g.mode_instructions(mode, g.compute_dates(mode, now, g.FALLBACK_US_HOLIDAYS))


@pytest.mark.parametrize("mode", PREP)
def test_prep_prompt_states_the_forward_priority(mode):
    text = instructions(mode)
    assert "FORWARD-LOOKING BRIEFING" in text
    assert "have NOT been published yet" in text
    assert "PRICING IN" in text
    assert "REVIEW OF A SESSION THAT ENDED" not in text


@pytest.mark.parametrize("mode", SUMMARY + WEEKLY)
def test_summary_prompt_forbids_becoming_a_briefing(mode):
    text = instructions(mode)
    assert "REVIEW OF A SESSION THAT ENDED" in text
    assert "Do NOT turn this into a briefing" in text
    assert "FORWARD-LOOKING BRIEFING" not in text


@pytest.mark.parametrize("mode", WEEKLY)
def test_weekly_prompt_has_no_preparation_block(mode):
    """The combined weekly is gone: no 'coming week' block, and the only forward-looking
    sentence allowed is inside the closing bottom line."""
    text = instructions(mode)
    for banned in ("PREPARATION points", "השבוע הקרוב במאקרו", "דוחות בשבוע הקרוב",
                   "prepares the reader", "COMING week"):
        assert banned not in text, f"{mode} still carries: {banned}"
    assert "Do NOT write a preparation block" in text


@pytest.mark.parametrize("mode", WEEKLY)
def test_weekly_title_no_longer_promises_a_preparation_half(mode):
    now = il(2026, 9, 6, 9, 0)
    d = g.compute_dates(mode, now, g.FALLBACK_US_HOLIDAYS)
    title = g.build_expected_title(mode, d["title_day_name"], d["title_date_str"],
                                   d["week_range"], d["time_str"])
    assert "הכנה" not in title, title
    assert "סיכום שבוע המסחר" in title


@pytest.mark.parametrize("mode", WEEKLY)
def test_weekly_web_search_may_not_build_a_look_ahead(mode):
    now = il(2026, 9, 6, 9, 0)
    d = g.compute_dates(mode, now, g.FALLBACK_US_HOLIDAYS)
    policy = g.get_macro_checklist(mode, d["date_str"], d["week_range"])
    assert "no preparation part" in policy.lower() or "NO preparation part" in policy
    assert "bottom-line point" in policy


@pytest.mark.parametrize("mode", PREP + SUMMARY + WEEKLY)
def test_every_non_intraday_mode_self_checks_its_horizon(mode):
    assert "HORIZON:" in g.get_self_verification(mode)


def test_intraday_prompt_and_checklist_are_untouched():
    now = il(2026, 9, 7, 14, 0)
    text = g.mode_instructions("intraday_update", g.compute_dates("intraday_update", now, []))
    assert "FORWARD-LOOKING BRIEFING" not in text
    assert "REVIEW OF A SESSION THAT ENDED" not in text
    assert "HORIZON:" not in g.get_self_verification("intraday_update")


# ── the week-ahead briefings ─────────────────────────────────────

@pytest.mark.parametrize("mode", WEEKLY_PREP)
def test_a_week_ahead_briefing_demands_a_forward_signal_from_everything(monkeypatch, mode):
    """There is no "today's news" on a quiet Sunday, so a week-ahead briefing has no
    fresh tier: every post must point at the week ahead, however recent it is."""
    sunday = il(2026, 9, 6, 9, 0)
    assert g.prep_fresh_cutoff(mode, sunday) == sunday
    recent_recap = post(BACKWARD_POST, sunday - timedelta(hours=2))
    recent_ahead = post(FORWARD_POST, sunday - timedelta(hours=2))
    blocks = gather(monkeypatch, [recent_recap, recent_ahead], mode, sunday)
    assert "CPI is due Monday" in blocks
    assert "closed sharply lower" not in blocks, "a recap reached a week-ahead briefing"


@pytest.mark.parametrize("mode", WEEKLY_PREP)
def test_a_week_ahead_briefing_reaches_across_the_weekend(mode):
    sunday = il(2026, 9, 6, 9, 0)
    since, until = g.compute_tweet_window(mode, sunday, dates(mode, sunday))
    assert since == sunday - timedelta(hours=g.WEEKLY_PREP_LOOKBACK_HOURS)
    assert since < il(2026, 9, 2, 12, 0), "must reach back into the week that ended"
    assert until is None


@pytest.mark.parametrize("mode", WEEKLY_PREP)
def test_a_week_ahead_briefing_targets_the_COMING_week(mode):
    """Run on a Sunday, the summary covers the week that ended and the prep the next
    one. The two must never point at the same days."""
    sunday = il(2026, 9, 6, 9, 0)
    prep = dates(mode, sunday)
    summary_mode = ("weekly_summary" if mode == "weekly_prep" else "israel_weekly_summary")
    summary = dates(summary_mode, sunday)
    assert prep["week_range"] == "07/09–11/09/2026"
    assert summary["week_range"] == "31/08–04/09/2026"
    assert prep["week_range"] != summary["week_range"]
    assert prep["review_date"] > summary["review_date"]


def test_the_coming_week_is_always_the_next_monday_to_friday():
    # Sunday, Saturday, midweek and Monday itself all resolve to a full Mon-Fri ahead.
    for day, expected_monday in [(il(2026, 9, 6), "2026-09-07"),    # Sunday
                                 (il(2026, 9, 5), "2026-09-07"),    # Saturday
                                 (il(2026, 9, 9), "2026-09-14"),    # Wednesday
                                 (il(2026, 9, 7), "2026-09-14")]:   # Monday, week underway
        monday, friday = g.get_next_week_range(day)
        assert monday.strftime("%Y-%m-%d") == expected_monday
        assert monday.weekday() == 0 and friday.weekday() == 4


@pytest.mark.parametrize("mode", WEEKLY_PREP)
def test_a_week_ahead_briefing_is_titled_and_headed_as_a_prep(mode):
    sunday = il(2026, 9, 6, 9, 0)
    d = dates(mode, sunday)
    title = g.build_expected_title(mode, d["title_day_name"], d["title_date_str"],
                                   d["week_range"], d["time_str"])
    assert title.startswith("לקראת שבוע המסחר")
    assert "07/09–11/09/2026" in title
    assert g.EXPECTED_FIRST_HEADING[mode] == "לקראת השבוע"


@pytest.mark.parametrize("mode", WEEKLY_PREP)
def test_a_week_ahead_briefing_is_calendar_first(mode):
    text = instructions(mode)
    assert "CALENDAR-FIRST BRIEFING" in text
    assert "not a precondition" in text
    assert "FIVE STRONG POINTS BEAT EIGHT PADDED ONES" in text
    # It must never become a forecast or a recap.
    assert "Never predict an" in text
    assert "Do NOT recap the week that ended" in text or "no recap of the week that ended" in text


@pytest.mark.parametrize("mode", WEEKLY_PREP)
def test_a_week_ahead_briefing_survives_a_silent_sunday(mode):
    """X is a complement, not a precondition: with zero posts the prompt must still tell
    the model to build the briefing, not to bail out."""
    sunday = il(2026, 9, 6, 9, 0)
    d = dates(mode, sunday)
    block = g.build_paste_block(mode, d, "t", "", "econ", "check", "", "", sunday, "earnings")
    assert "calendar-first" in block
    assert "Do NOT invent a narrative" in block
    assert "אין מספיק חומר מהמקורות" not in block, "must not bail out like the Israeli dailies"


def test_the_weekly_prep_prompt_carries_the_earnings_calendar():
    sunday = il(2026, 9, 6, 9, 0)
    d = dates("weekly_prep", sunday)
    block = g.build_paste_block("weekly_prep", d, "t", "", "ECONBLOCK", "check", "", "",
                                sunday, "EARNINGSBLOCK")
    assert "EARNINGSBLOCK" in block and "ECONBLOCK" in block


@pytest.mark.parametrize("mode", WEEKLY_PREP)
def test_a_week_ahead_briefing_self_checks_the_prep_horizon(mode):
    checks = g.get_self_verification(mode)
    assert "HORIZON: every point has an UPCOMING event" in checks


# ── claims stay inside what the sources support ──────────────────

@pytest.mark.parametrize("mode", PREP + WEEKLY_PREP)
def test_prep_prompts_forbid_claims_wider_than_the_sources(mode):
    """Calendar coverage is never complete, so "there is no X" is a claim the review
    cannot support. Both corrected phrasings are shown to the model verbatim."""
    text = instructions(mode)
    assert "CLAIM ONLY WHAT YOUR SOURCES SUPPORT" in text
    assert "absence of evidence is not evidence of absence" in text
    assert "האירועים המרכזיים של השבוע מרוכזים בחמישי ושישי" in text
    assert "לא זוהו אירועי מאקרו מהותיים בלוחות שאומתו לשבוע הקרוב" in text


@pytest.mark.parametrize("mode", PREP + WEEKLY_PREP)
def test_prep_prompts_put_verification_before_writing(mode):
    """Checking dates is the model's job, done up front — not work handed to the reader
    after the review exists."""
    text = instructions(mode)
    assert "VERIFY BEFORE YOU WRITE" in text
    assert "before drafting a single bullet" in text
    assert "Do NOT write the\nreview first" in text


@pytest.mark.parametrize("mode", PREP + WEEKLY_PREP)
def test_prep_self_check_covers_dates_and_scope(mode):
    checks = g.get_self_verification(mode)
    assert "VERIFIED DATES:" in checks
    assert "SCOPED CLAIMS:" in checks
