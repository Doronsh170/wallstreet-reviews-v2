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
WEEKLY = list(g.WEEKLY_MODES)

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


@pytest.mark.parametrize("mode", SUMMARY)
def test_summary_prefers_what_already_happened(mode):
    forward, backward = norm(FORWARD_POST), norm(BACKWARD_POST)
    assert g.horizon_bonus(backward, mode) > 0
    assert g.horizon_bonus(forward, mode) < 0
    assert g.ranked_score(backward, mode) > g.ranked_score(forward, mode)


@pytest.mark.parametrize("mode", WEEKLY)
def test_weekly_rewards_the_past_without_punishing_the_future(mode):
    """The weeklies are combined reviews — their preparation block needs forward
    material, so it is never pushed down."""
    assert g.horizon_bonus(norm(BACKWARD_POST), mode) > 0
    assert g.horizon_bonus(norm(FORWARD_POST), mode) == 0


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


@pytest.mark.parametrize("mode", PREP)
def test_recent_material_needs_no_forward_signal(monkeypatch, mode):
    """Inside the fresh tier a post is current news and enters on its own merit."""
    now = il(2026, 9, 7, 8, 0)
    blocks = gather(monkeypatch, [post(BACKWARD_POST, now - timedelta(hours=3))], mode, now)
    assert "closed sharply lower" in blocks


@pytest.mark.parametrize("mode", PREP)
def test_a_prep_never_reaches_past_its_lookback(monkeypatch, mode):
    now = il(2026, 9, 7, 8, 0)
    ancient = now - timedelta(hours=g.PREP_LOOKBACK_HOURS + 24)
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
    ("daily_summary", "closed sharply lower", "CPI is due Monday"),
])
def test_the_top_post_faces_the_right_way(monkeypatch, mode, expected, rejected):
    now = il(2026, 9, 7, 8, 0) if mode == "daily_prep" else il(2026, 9, 8, 7, 0)
    d = g.compute_dates(mode, now, g.FALLBACK_US_HOLIDAYS)
    since, _ = g.compute_tweet_window(mode, now, d)
    when = since + timedelta(hours=2)
    blocks = gather(monkeypatch, [post(BACKWARD_POST, when), post(FORWARD_POST, when)], mode, now)
    first = blocks.split("\n\n")[0]
    assert expected in first, blocks
    assert rejected not in first, blocks


# ── the prompt says it too ───────────────────────────────────────

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


@pytest.mark.parametrize("mode", SUMMARY)
def test_summary_prompt_forbids_becoming_a_briefing(mode):
    text = instructions(mode)
    assert "REVIEW OF A SESSION THAT ENDED" in text
    assert "Do NOT turn this into a briefing" in text
    assert "FORWARD-LOOKING BRIEFING" not in text


@pytest.mark.parametrize("mode", WEEKLY)
def test_weekly_prompt_keeps_the_two_halves_apart(mode):
    text = instructions(mode)
    assert "the two halves must not bleed into each other" in text


@pytest.mark.parametrize("mode", PREP + SUMMARY + WEEKLY)
def test_every_non_intraday_mode_self_checks_its_horizon(mode):
    assert "HORIZON:" in g.get_self_verification(mode)


def test_intraday_prompt_and_checklist_are_untouched():
    now = il(2026, 9, 7, 14, 0)
    text = g.mode_instructions("intraday_update", g.compute_dates("intraday_update", now, []))
    assert "FORWARD-LOOKING BRIEFING" not in text
    assert "REVIEW OF A SESSION THAT ENDED" not in text
    assert "HORIZON:" not in g.get_self_verification("intraday_update")
