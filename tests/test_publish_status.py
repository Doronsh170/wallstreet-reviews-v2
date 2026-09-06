"""publish_status.json — the publish step's verdict, in Hebrew, as a file.

A rejected review used to explain itself only inside an Actions log. These tests
lock in that every attempt leaves a readable outcome behind, so the admin screen can
show the guard's own message, and that a rejection still never touches data.json.
"""
import json
import subprocess
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent

SNAPSHOT = {
    "mode": "daily_summary",
    "generated_at": "2026-09-01T06:54:39+03:00",
    "expected_title": "סיכום יום המסחר בוול סטריט 🇺🇸 – יום שני, 31.8.2026",
    "first_heading": "סיכום המסחר",
    "review_date": "2026-08-31",
    "title_date_str": "2026-08-31",
    "title_day_name": "שני",
    "week_range": None,
    "etf_pcts": {},
    "ticker_quotes": {},
}

BODY = ("המסחר התאפיין בפעילות ערה סביב הסיפור הזה, על רקע הדיווחים שהתקבלו במהלך היום. "
        "המשמעות למשקיעים היא שצריך לעקוב אחר ההתפתחויות בימים הקרובים.")
HEADS = ["שוק השבבים ממשיך להוביל", "הריבית בכותרות", "הנפט מתייצב",
         "עונת הדוחות נמשכת", "הבנקים מרכזים עניין", "שורה תחתונה"]


def review(n_bullets=6):
    heads = HEADS[:n_bullets - 1] + ["שורה תחתונה"]
    return {
        "title": SNAPSHOT["expected_title"],
        "date": SNAPSHOT["review_date"],
        "summary": [f"{h}: תמצית קצרה של מה שקרה ולמה זה חשוב למשקיע." for h in heads],
        "sections": [{"heading": SNAPSHOT["first_heading"],
                      "content": "\n".join(f"* {h}: {BODY}" for h in heads)}],
    }


@pytest.fixture
def workdir(tmp_path):
    (tmp_path / "raw_review_input.json").write_text(
        json.dumps(SNAPSHOT, ensure_ascii=False), encoding="utf-8")
    (tmp_path / "data.json").write_text(
        json.dumps({"holidays": []}, ensure_ascii=False), encoding="utf-8")
    (tmp_path / "archive").mkdir()
    return tmp_path


def publish(workdir, payload):
    if payload is not None:
        (workdir / "review_output.json").write_text(
            payload if isinstance(payload, str) else json.dumps(payload, ensure_ascii=False),
            encoding="utf-8")
    proc = subprocess.run([sys.executable, str(REPO / "paste_review.py"), "review_output.json"],
                          cwd=workdir, capture_output=True, text=True)
    status_file = workdir / "publish_status.json"
    status = json.loads(status_file.read_text(encoding="utf-8")) if status_file.exists() else None
    return proc, status


def test_success_records_the_published_review(workdir):
    proc, status = publish(workdir, review())
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert status["ok"] is True
    assert status["mode"] == "daily_summary"
    assert status["title"] == SNAPSHOT["expected_title"]
    assert status["bullets"] == 6
    assert status["finishedAt"]
    data = json.loads((workdir / "data.json").read_text(encoding="utf-8"))
    assert data["dailySummary"]["title"] == SNAPSHOT["expected_title"]


def test_rejection_records_the_hebrew_reason_and_leaves_data_alone(workdir):
    before = (workdir / "data.json").read_text(encoding="utf-8")
    # A daily review must have exactly 6 bullets; three is a guard failure.
    proc, status = publish(workdir, review(n_bullets=3))
    assert proc.returncode != 0
    assert status["ok"] is False
    assert status["mode"] == "daily_summary"
    assert status["error"].strip(), "a rejection must say why"
    assert any("֐" <= ch <= "ת" for ch in status["error"]), "the reason must be Hebrew"
    assert (workdir / "data.json").read_text(encoding="utf-8") == before


def test_unparseable_paste_is_reported_not_crashed(workdir):
    proc, status = publish(workdir, "הנה הסקירה שביקשת, בלי JSON בכלל")
    assert proc.returncode != 0
    assert status["ok"] is False
    assert "JSON" in status["error"]


def test_missing_snapshot_is_reported(workdir):
    (workdir / "raw_review_input.json").unlink()
    proc, status = publish(workdir, review())
    assert proc.returncode != 0
    assert status["ok"] is False
    assert "raw_review_input.json" in status["error"]
    # Nothing to read the mode from — the field is present but empty, not missing.
    assert status["mode"] == ""


def test_status_is_replaced_on_every_attempt(workdir):
    _, bad = publish(workdir, review(n_bullets=3))
    _, good = publish(workdir, review())
    assert bad["ok"] is False and good["ok"] is True
    assert good["finishedAt"] >= bad["finishedAt"]
    assert "error" not in good, "a success must not carry the previous failure's reason"
