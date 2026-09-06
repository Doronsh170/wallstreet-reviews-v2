"""Regression fixtures for the scheduled-date failures found in review.

A weekly_prep passed every guard while stating: CPI on Thursday 10.9 (BLS publishes
August CPI on Friday 11.9, and Thursday 10.9 is PPI), Oracle reporting Wednesday 9.9
(Oracle's IR set Thursday 10.9 after the close), a Bank of Israel decision on 7.9 (the
last one was 1.9, cutting to 3.25%, and the next is 21.10), and Q2 bank reports as
"due" in the 7-11.9 week when both had already reported in August.

Two of those are decidable inside this script and are now hard failures: a weekday that
does not match its date, and a date that contradicts the calendar the run gathered.
Whether the calendar itself is right is not decidable here — the model verifies that
against the publishing body before writing, and the check merely records what was
claimed so a bad date can be traced afterwards.
"""
import json
import subprocess
import sys
from pathlib import Path

import pytest

import paste_review as pr

REPO = Path(__file__).resolve().parent.parent

# The real week: Mon 7.9 (Labor Day) .. Fri 11.9.2026.
WEEK_SNAPSHOT = {
    "mode": "weekly_prep",
    "generated_at": "2026-09-06T09:00:00+03:00",
    "expected_title": "לקראת שבוע המסחר בוול סטריט 🇺🇸 – 07/09–11/09/2026",
    "first_heading": "לקראת השבוע",
    "review_date": "2026-09-07",
    "title_date_str": "2026-09-07",
    "title_day_name": "שני",
    "week_range": "07/09–11/09/2026",
    "etf_pcts": {},
    "ticker_quotes": {},
    "scheduled": {
        "macro": [
            {"event": "CPI YoY", "date": "2026-09-11", "time_il": "15:30"},
            {"event": "PPI MoM", "date": "2026-09-10", "time_il": "15:30"},
        ],
        "earnings": [
            {"event": "ORCL", "date": "2026-09-10", "time_il": ""},
            {"event": "ADBE", "date": "2026-09-10", "time_il": ""},
        ],
    },
}


def review(*bullets, heading="לקראת השבוע"):
    return {"title": WEEK_SNAPSHOT["expected_title"], "date": "2026-09-07",
            "summary": [f"נקודה {i}: תמצית" for i, _ in enumerate(bullets)],
            "sections": [{"heading": heading, "content": "\n".join(f"* {b}" for b in bullets)}]}


def check(result, snapshot=None, mode="weekly_prep"):
    pr.scheduled_event_check(result, snapshot or WEEK_SNAPSHOT, mode)


# ── the weekday/date contradiction ───────────────────────────────

def test_cpi_on_the_wrong_weekday_is_rejected():
    """BLS publishes August CPI on Friday 11.9. Calling 11.9 a Thursday is a contradiction
    the script can see on its own."""
    with pytest.raises(ValueError, match="סתירה בין יום לתאריך"):
        check(review("מדד המחירים לצרכן: המדד יתפרסם ביום חמישי, 11.9, בשעה 15:30."))


def test_the_error_message_names_the_actual_weekday_and_the_official_source():
    with pytest.raises(ValueError) as e:
        check(review("מדד המחירים לצרכן: המדד יתפרסם ביום חמישי, 11.9, בשעה 15:30."))
    message = str(e.value)
    assert "יום שישי" in message, "must say what day 11.9 really is"
    assert "BLS" in message and "בנק ישראל" in message
    assert "הסר את האירוע" in message, "omission must be offered as the fallback"


def test_a_correct_weekday_passes():
    check(review("מדד המחירים לצרכן: המדד יתפרסם ביום שישי, 11.9, בשעה 15:30.",
                 "מדד המחירים ליצרן: יתפרסם ביום חמישי, 10.9, בשעה 15:30."))


def test_bank_of_israel_decision_on_a_wrong_weekday_is_rejected():
    """The next decision after 1.9.2026 is 21.10.2026, a Wednesday. Writing it as a
    Monday is caught here; that it is 21.10 at all is the prompt's job."""
    israel = dict(WEEK_SNAPSHOT, mode="israel_weekly_prep", scheduled={"macro": [], "earnings": []})
    with pytest.raises(ValueError, match="סתירה בין יום לתאריך"):
        check(review("החלטת הריבית: בנק ישראל יפרסם את ההחלטה ביום שני, 21.10."),
              israel, "israel_weekly_prep")


def test_an_impossible_date_is_rejected():
    with pytest.raises(ValueError, match="תאריך לא תקין"):
        check(review("מדד המחירים לצרכן: יתפרסם ביום שישי, 31.9."))


# ── contradicting the gathered calendar ──────────────────────────

def test_cpi_moved_off_the_gathered_calendar_date_is_rejected():
    """A source post said Wednesday, the gathered calendar said otherwise. The calendar
    beats the post — and the official source beats them both."""
    with pytest.raises(ValueError, match="סותר את לוח האירועים"):
        check(review("מדד המחירים לצרכן: המדד יתפרסם ב-10.9 בשעה 15:30."))


def test_oracle_moved_off_its_calendar_date_is_rejected():
    """Oracle's IR set Thursday 10.9 after the close; 9.9 was the invented date."""
    with pytest.raises(ValueError, match="סותר את לוח האירועים"):
        check(review("דוחות: מניית אורקל (ORCL) מדווחת ב-9.9 אחרי הסגירה."))


def test_matching_the_gathered_calendar_passes():
    check(review("דוחות: מניית אורקל (ORCL) מדווחת ב-10.9 אחרי הסגירה.",
                 "מדד המחירים לצרכן: יתפרסם ב-11.9 בשעה 15:30."))


def test_an_event_absent_from_the_calendar_is_left_alone():
    """Nothing to compare against is not the same as a contradiction — the printed
    report is what surfaces those for a human."""
    check(review("נאום הפד: יו\"ר הפד ידבר ב-9.9 בשעה 17:00."))


# ── scope ────────────────────────────────────────────────────────

@pytest.mark.parametrize("mode", ["daily_summary", "weekly_summary",
                                  "israel_summary", "intraday_update"])
def test_summaries_are_not_subject_to_the_prep_schedule_check(mode):
    """A summary describes what happened; this guard is about scheduled events."""
    check(review("סיכום: המדד פורסם ביום חמישי, 11.9."), mode=mode)


@pytest.mark.parametrize("mode", list(pr.PREP_MODES))
def test_every_prep_mode_is_covered(mode):
    with pytest.raises(ValueError):
        check(review("אירוע: מתפרסם ביום חמישי, 11.9."), mode=mode)


# ── end to end through the real publish path ─────────────────────

@pytest.fixture
def workdir(tmp_path):
    (tmp_path / "raw_review_input.json").write_text(
        json.dumps(WEEK_SNAPSHOT, ensure_ascii=False), encoding="utf-8")
    (tmp_path / "data.json").write_text('{"holidays": []}', encoding="utf-8")
    (tmp_path / "archive").mkdir()
    return tmp_path


def publish(workdir, result):
    (workdir / "review_output.json").write_text(
        json.dumps(result, ensure_ascii=False), encoding="utf-8")
    proc = subprocess.run([sys.executable, str(REPO / "paste_review.py"), "review_output.json"],
                          cwd=workdir, capture_output=True, text=True)
    status = json.loads((workdir / "publish_status.json").read_text(encoding="utf-8"))
    return proc, status


BODY = "האירוע מרכז את תשומת הלב של המשקיעים לקראת השבוע, והתוצאה תשפיע על תמחור הריבית."


def four_bullets(first):
    return review(first,
                  f"מדד המחירים ליצרן: יתפרסם ביום חמישי, 10.9, בשעה 15:30. {BODY}",
                  f"דוחות השבוע: מניית אדובי (ADBE) מדווחת ב-10.9 אחרי הסגירה. {BODY}",
                  f"שורה תחתונה: יום שישי מכריע את השבוע. {BODY}")


def test_a_wrong_date_fails_the_publish_and_leaves_the_site_untouched(workdir):
    before = (workdir / "data.json").read_text(encoding="utf-8")
    proc, status = publish(workdir, four_bullets(
        f"מדד המחירים לצרכן: המדד יתפרסם ביום חמישי, 11.9, בשעה 15:30. {BODY}"))
    assert proc.returncode != 0
    assert status["ok"] is False
    assert "סתירה בין יום לתאריך" in status["error"]
    assert (workdir / "data.json").read_text(encoding="utf-8") == before


def test_the_corrected_dates_publish(workdir):
    proc, status = publish(workdir, four_bullets(
        f"מדד המחירים לצרכן: המדד יתפרסם ביום שישי, 11.9, בשעה 15:30. {BODY}"))
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert status["ok"] is True
    data = json.loads((workdir / "data.json").read_text(encoding="utf-8"))
    assert data["weeklyPrep"]["title"] == WEEK_SNAPSHOT["expected_title"]


def test_the_publish_log_records_the_claims_without_assigning_manual_work(workdir):
    """The listing is a trace for debugging a bad date later, not a checklist the
    publisher has to work through on every review — verification happens in the model,
    before the review is written."""
    proc, _ = publish(workdir, four_bullets(
        f"מדד המחירים לצרכן: המדד יתפרסם ביום שישי, 11.9, בשעה 15:30. {BODY}"))
    assert "SCHEDULE-CHECK" in proc.stdout
    assert "ביום שישי, 11.9" in proc.stdout
    assert "ביום חמישי, 10.9" in proc.stdout
    assert "לתיעוד" in proc.stdout
    assert "ודא כל אחד" not in proc.stdout, "must not read as a manual to-do"
    assert "⚠️" not in proc.stdout.split("Scheduled-event check")[1].split("──")[0]

