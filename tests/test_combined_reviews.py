import copy
import json
import pytest
import paste_review as pr
from gather_combined_review import combine


def child(mode):
    return {"mode": mode, "expected_title": "כותרת", "first_heading": "נקודות מרכזיות", "review_date": "2026-10-25", "week_range": "26–30.10.2026", "generated_at": "2026-10-25T10:00:00+02:00"}


def setup(mode="wallstreet_weekly_review"):
    prefix = "israel_" if mode == "israel_weekly_review" else ""
    children = [child(prefix + "weekly_summary"), child(prefix + "weekly_prep")]
    prompt, snapshot = combine(mode, ["Summary material", "Preparation material"], children)
    review = {"title": "model title", "sections": [
        {"heading": heading, "summary": [heading + ": תקציר"], "content": "\n".join(f"* נושא מספר {i}: הסבר ממוקד על השוק והמשמעות למשקיעים." for i in range(n))}
        for heading, n in (("סיכום שבועי", 8), ("הכנה לשבוע הקרוב", 4))]}
    return prompt, snapshot, review


@pytest.mark.parametrize("mode", ["wallstreet_weekly_review", "israel_weekly_review"])
def test_combined_retains_both_markets_and_validates_each(mode):
    prompt, snapshot, review = setup(mode)
    result = pr.validate_review(review, snapshot)
    assert "Summary material" in prompt and "Preparation material" in prompt
    assert result["title"] == snapshot["expected_title"]
    assert [s["heading"] for s in result["sections"]] == ["סיכום שבועי", "הכנה לשבוע הקרוב"]
    assert len(result["summary"]) == 2
    assert result["date"] == "2026-10-25"


def test_missing_market_is_rejected():
    _, snapshot, review = setup()
    review["sections"].pop()
    with pytest.raises(ValueError):
        pr.validate_review(review, snapshot)


def test_invalid_second_market_does_not_publish_first(tmp_path, monkeypatch):
    _, snapshot, review = setup()
    review["sections"][1]["content"] = "* נקודה: מעט מדי נקודות להכנה."
    monkeypatch.chdir(tmp_path)
    Path = __import__('pathlib').Path
    Path("raw_review_input.json").write_text(json.dumps(snapshot), encoding="utf-8")
    Path("review_output.json").write_text(json.dumps(review), encoding="utf-8")
    Path("data.json").write_text('{"lastUpdated":"original"}', encoding="utf-8")
    monkeypatch.setattr(pr.sys, "argv", ["paste_review.py"])
    with pytest.raises(ValueError):
        pr.main()
    assert Path("data.json").read_text(encoding="utf-8") == '{"lastUpdated":"original"}'
    assert not Path("archive").exists()
