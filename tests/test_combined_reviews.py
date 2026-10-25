import copy
import json
import pytest
import paste_review as pr
from gather_combined_review import combine


def child(mode):
    return {"mode": mode, "expected_title": "כותרת", "first_heading": "נקודות מרכזיות", "review_date": "2026-10-25", "week_range": "26–30.10.2026", "generated_at": "2026-10-25T10:00:00+02:00"}


def setup(mode="combined_weekly_prep"):
    suffix = "prep" if mode.endswith("prep") else "summary"
    children = [child("israel_weekly_" + suffix), child("weekly_" + suffix)]
    prompt, snapshot = combine(mode, ["Israel material", "US material"], children)
    n = 4 if suffix == "prep" else 8
    review = {"title": "model title", "sections": [
        {"heading": heading, "summary": [heading + ": תקציר"], "content": "\n".join(f"* נושא מספר {i}: הסבר ממוקד על השוק והמשמעות למשקיעים." for i in range(n))}
        for heading in ("ישראל", "וול סטריט")]}
    return prompt, snapshot, review


@pytest.mark.parametrize("mode", ["combined_weekly_prep", "combined_weekly_summary"])
def test_combined_retains_both_markets_and_validates_each(mode):
    prompt, snapshot, review = setup(mode)
    result = pr.validate_review(review, snapshot)
    assert "Israel material" in prompt and "US material" in prompt
    assert result["title"] == snapshot["expected_title"]
    assert [s["heading"] for s in result["sections"]] == ["ישראל", "וול סטריט"]
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
