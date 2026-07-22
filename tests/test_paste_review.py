"""Tests for paste_review.py — the deterministic validation/publish layer.

This is the most safety-critical file in the pipeline: every regex here runs on
Hebrew text where a substring match can silently corrupt an innocent word
(the documented "נפל inside אינפלציה" class of bugs). These tests lock in the
guard behaviors so new modes and rules can't quietly break the existing ones.
"""
import json
import re

import pytest

import paste_review as pr


def make_result(content, title="כותרת לדוגמה", summary=None):
    result = {"title": title, "sections": [{"heading": "סיכום המסחר", "content": content}]}
    if summary is not None:
        result["summary"] = summary
    return result


def content_of(result):
    return result["sections"][0]["content"]


# ── JSON extraction ──────────────────────────────────────────────

def test_extract_json_tolerates_fences_and_chatter():
    text = 'הנה הסקירה שביקשת:\n```json\n{"title": "א", "n": [1, 2]}\n```\nבהצלחה!'
    assert pr.extract_first_json_object(text) == {"title": "א", "n": [1, 2]}


def test_extract_json_ignores_braces_inside_strings():
    assert pr.extract_first_json_object('{"a": "x } y"} trailing') == {"a": "x } y"}


def test_extract_json_fails_on_truncated_object():
    with pytest.raises(ValueError):
        pr.extract_first_json_object('פתיח {"a": 1')


def test_extract_json_fails_when_no_object():
    with pytest.raises(ValueError):
        pr.extract_first_json_object("אין כאן שום JSON")


# ── Structure enforcement ────────────────────────────────────────

def test_normalize_bullets_unifies_bullet_marks():
    text = "• נקודה ראשונה: תוכן\n- נקודה שנייה: תוכן\n* נקודה שלישית: תוכן"
    lines = pr.normalize_bullets(text).split("\n")
    assert all(l.startswith("* ") for l in lines)


def test_normalize_bullets_adds_bullet_to_ticker_opener():
    text = "* נקודה: תוכן\n$TSLA: המניה עלתה\n* עוד נקודה: תוכן"
    assert "* $TSLA: המניה עלתה" in pr.normalize_bullets(text)


def test_enforce_structure_forces_title_and_merges_sections():
    result = {"title": "כותרת שהצ'אט המציא", "sections": [
        {"heading": "נקודות", "content": "* סיפור ראשון: פרטים"},
        {"heading": "שורה תחתונה", "content": "סיכום קצר של היום"},
    ]}
    out = pr.enforce_structure(result, "סיכום המסחר", "הכותרת הנכונה")
    assert out["title"] == "הכותרת הנכונה"
    assert len(out["sections"]) == 1
    assert out["sections"][0]["heading"] == "סיכום המסחר"
    assert "* בשורה התחתונה: סיכום קצר של היום" in content_of(out)


def test_enforce_structure_fails_without_sections():
    with pytest.raises(ValueError):
        pr.enforce_structure({"title": "א", "sections": []}, "h", "t")


def test_normalize_summary_strips_bullets_and_drops_junk():
    out = pr.normalize_summary(make_result("x", summary=["* נקודה אחת: תקציר", "  - שנייה: תקציר", "", 5]))
    assert out["summary"] == ["נקודה אחת: תקציר", "שנייה: תקציר"]
    out = pr.normalize_summary(make_result("x", summary="לא רשימה"))
    assert "summary" not in out


# ── Text and style fixes ─────────────────────────────────────────

def test_text_fixes_trump_is_current_president():
    out = pr.apply_text_fixes(make_result("הנשיא לשעבר טראמפ הודיע על מכסים חדשים."))
    assert "הנשיא טראמפ הודיע" in content_of(out)
    assert "לשעבר" not in content_of(out)


def test_text_fixes_numeric_spacing():
    out = pr.apply_text_fixes(make_result("המדד עלה 2. 5% והתשואה ירדה 3 %."))
    assert "2.5%" in content_of(out)
    assert "3%." in content_of(out)


def test_style_fixes_rewrite_ticker_opener_with_hebrew_name():
    out = pr.apply_style_fixes(make_result("* $TSLA: המניה עלתה לאחר הדוחות."))
    assert content_of(out).startswith("* מניית טסלה (TSLA): ")


def test_style_fixes_unknown_bare_ticker_untouched():
    # "* AI:" without $ must not be mangled into a stock opener.
    out = pr.apply_style_fixes(make_result("* AI: תחום הבינה המלאכותית ממשיך לרכז עניין."))
    assert content_of(out).startswith("* AI: ")


def test_style_fixes_iso_dates_and_semicolons():
    out = pr.apply_style_fixes(make_result("הדוח יתפרסם ב-2026-07-15; השוק ממתין."))
    c = content_of(out)
    assert "15.7.2026" in c
    assert ";" not in c


def test_intraday_fixes_forbidden_cash_market_phrase():
    out = pr.apply_intraday_fixes(make_result("המסחר במזומן נפתח בעליות."))
    assert "המסחר הרגיל" in content_of(out)
    assert "במזומן" not in content_of(out)


# ── Direction guards ─────────────────────────────────────────────

def test_direction_words_respect_word_boundaries():
    # The documented bug class: "נפל" inside "אינפלציה", "זינק" inside "זינקה",
    # "יורד" inside "יורדות", "עולה" inside "פעולה" — none may register as a claim.
    for word in ("האינפלציה", "זינקה", "יורדות", "פעולה"):
        assert not pr._has_direction_word(word, pr.UP_WORDS + pr.DOWN_WORDS)


def test_market_direction_check_fails_on_wrong_oil_direction():
    # The guard must FAIL (demand a rewrite), never patch the verb in place —
    # the old auto-fix published a bullet whose headline said "נסוג" and body "עלה".
    result = make_result("* הנפט יורד: מחיר הנפט נפל היום בחדות למרות נתוני האינפלציה הגבוהים.")
    with pytest.raises(ValueError):
        pr.market_direction_check(result, {"USO": 1.4, "BNO": 1.1})


def test_market_direction_check_flat_asset_is_warning_only():
    pr.market_direction_check(make_result("הזהב מזנק היום לשיא חדש."), {"GLD": 0.05})


def test_market_direction_check_checks_the_summary_too():
    result = make_result("* הזהב עולה: מחיר הזהב עלה היום.",
                         summary=["הזהב עולה: מחיר הזהב ירד היום בחדות."])
    with pytest.raises(ValueError):
        pr.market_direction_check(result, {"GLD": 2.6})


def test_market_direction_check_splits_mixed_clauses():
    # "הזהב ירד" and "ה-VIX עלה" share one sentence — the gold claim must still
    # be judged on its own clause (this exact pattern slipped through the old guard).
    result = make_result("* הזהב נסוג: מחיר הזהב ירד כ-2.6%, בעוד מדד הפחד עלה בכ-3.3%.")
    with pytest.raises(ValueError):
        pr.market_direction_check(result, {"GLD": 2.6, "VIXY": 3.3})


def test_market_direction_check_matching_direction_passes():
    pr.market_direction_check(make_result("* הנפט מטפס: מחיר הנפט עלה היום בחדות."),
                              {"USO": 1.4, "BNO": 1.1})


def test_market_direction_check_yields_move_inversely_to_tlt():
    # TLT (bond prices) UP means yields DOWN: "התשואות ירדו" is CORRECT then.
    pr.market_direction_check(make_result("* שוק החוב נרגע: תשואות האג\"ח ירדו היום."), {"TLT": 0.5})
    with pytest.raises(ValueError):
        pr.market_direction_check(make_result("* שוק החוב לוחץ: תשואות האג\"ח עלו היום."), {"TLT": 0.5})


def test_market_direction_check_ignores_dollar_amounts():
    # "מיליארד דולר" / "79 דולר לחבית" are prices, not claims about the currency.
    pr.market_direction_check(
        make_result("* הנפט מטפס: מחיר הנפט עלה מעל 79 דולר לחבית על רקע המתיחות."),
        {"USO": 1.4, "BNO": 1.1, "UUP": -0.5})


def test_market_direction_check_leaves_unrelated_text_alone():
    pr.market_direction_check(make_result("* מניות הבנקים יורדות: הסקטור הפיננסי נחלש היום."),
                              {"USO": 1.4})


def test_ticker_sign_flip_fails_publish():
    result = make_result("* מניית טסלה (TSLA): המניה זינקה היום לאחר דוח חזק.")
    with pytest.raises(ValueError):
        pr.ticker_direction_check(result, {"TSLA": {"pct": -2.5}})


def test_ticker_matching_direction_passes():
    result = make_result("* מניית טסלה (TSLA): המניה זינקה היום לאחר דוח חזק.")
    pr.ticker_direction_check(result, {"TSLA": {"pct": 2.5}})


def test_ticker_flat_quote_is_warning_only():
    # A claim against a ~flat quote is usually a real pre/after-market move.
    result = make_result("* מניית טסלה (TSLA): המניה זינקה היום לאחר דוח חזק.")
    pr.ticker_direction_check(result, {"TSLA": {"pct": -0.1}})


def test_ticker_sign_flip_downgraded_for_weekly():
    result = make_result("* מניית טסלה (TSLA): המניה זינקה השבוע לאחר דוח חזק.")
    pr.ticker_direction_check(result, {"TSLA": {"pct": -2.5}}, hard_fail=False)


# ── Tense guard, links, dedupe ───────────────────────────────────

def test_pre_market_tense_guard_only_before_open_and_only_daily_prep(monkeypatch):
    monkeypatch.setattr(pr, "is_before_us_market_open", lambda now: True)
    out = pr.apply_pre_market_tense_guard(make_result("השוק נפתח הבוקר בעליות."), "daily_prep")
    assert "השוק צפוי להיפתח" in content_of(out)
    out = pr.apply_pre_market_tense_guard(make_result("השוק נפתח הבוקר בעליות."), "daily_summary")
    assert "השוק נפתח הבוקר" in content_of(out)


def test_strip_links_removes_markdown_and_bare_urls():
    result = make_result("* חדשות: פרטים נוספים [כתבה](https://example.com/a) בהמשך https://t.co/xyz סוף.")
    c = content_of(pr.strip_links_from_result(result))
    assert "http" not in c
    assert "כתבה" not in c
    assert "פרטים נוספים" in c and "סוף" in c


def test_dedupe_removes_exact_duplicate_bullets():
    result = make_result("* נקודה אחת: טקסט\n* נקודה שנייה: אחר\n*  נקודה אחת:  טקסט")
    c = content_of(pr.dedupe_exact_review_lines(result))
    assert c.count("נקודה אחת") == 1
    assert "נקודה שנייה" in c


# ── Final validation ─────────────────────────────────────────────

def good_hebrew_content(n=6):
    return "\n".join(f"* נושא מספר {i}: תיאור אנליטי של ההתפתחות ומשמעותה למשקיע." for i in range(1, n + 1))


def test_hard_validation_passes_clean_review():
    pr.hard_content_validation(make_result(good_hebrew_content()))


def test_hard_validation_rejects_tweet_meta_phrases():
    with pytest.raises(ValueError):
        pr.hard_content_validation(make_result(good_hebrew_content() + "\n* עוד: לפי הציוץ המניה עלתה."))


def test_hard_validation_rejects_verification_layer_leak():
    with pytest.raises(ValueError):
        pr.hard_content_validation(make_result(good_hebrew_content() + "\n* נפט: לפי נתוני Finnhub המחיר עלה."))


def test_hard_validation_rejects_non_hebrew_review():
    with pytest.raises(ValueError):
        pr.hard_content_validation(make_result("\n".join(f"* point {i}: english only text." for i in range(6)),
                                               title="english title"))


def test_hard_validation_rejects_too_few_bullets():
    with pytest.raises(ValueError):
        pr.hard_content_validation(make_result(good_hebrew_content(4)), min_bullets=5)


# ── Length enforcement ───────────────────────────────────────────

def test_bullet_length_daily_requires_exactly_six():
    pr.bullet_length_check(make_result(good_hebrew_content(6)), "daily_prep")
    for n in (5, 7, 9):
        with pytest.raises(ValueError):
            pr.bullet_length_check(make_result(good_hebrew_content(n)), "daily_prep")


def test_bullet_length_weekly_range_eight_to_ten():
    pr.bullet_length_check(make_result(good_hebrew_content(9)), "weekly_summary")
    with pytest.raises(ValueError):
        pr.bullet_length_check(make_result(good_hebrew_content(6)), "weekly_summary")
    with pytest.raises(ValueError):
        pr.bullet_length_check(make_result(good_hebrew_content(12)), "weekly_summary")


def test_bullet_length_rejects_overlong_daily_bullet():
    long_bullet = "* נקודה ארוכה: " + "מילה " * (pr.MAX_BULLET_WORDS + 5)
    content = "\n".join([long_bullet] + [f"* נקודה {i}: תיאור קצר." for i in range(5)])
    with pytest.raises(ValueError):
        pr.bullet_length_check(make_result(content), "daily_summary")


def test_bullet_length_intraday_and_israel_are_free():
    pr.bullet_length_check(make_result("* עדכון יחיד: אין מספיק עדכונים משמעותיים."), "intraday_update")
    pr.bullet_length_check(make_result(good_hebrew_content(3)), "israel_prep")


# ── Archive ──────────────────────────────────────────────────────

def archived_entries(path):
    return json.loads(path.read_text(encoding="utf-8"))["entries"]


def test_archive_appends_and_replaces_republished_review(tmp_path, monkeypatch):
    monkeypatch.setattr(pr, "ARCHIVE_DIR", tmp_path / "archive")
    review = {"title": "כותרת א", "date": "2026-07-12",
              "sections": [{"heading": "h", "content": "* א: ב"}]}
    path = pr.archive_review("daily_prep", review, "2026-07-12T10:00:00+03:00")
    assert path.name == "2026-07.json"
    assert len(archived_entries(path)) == 1

    # A fix-round re-publish (same mode + title) replaces, not duplicates.
    pr.archive_review("daily_prep", review, "2026-07-12T10:20:00+03:00")
    entries = archived_entries(path)
    assert len(entries) == 1
    assert entries[0]["publishedAt"] == "2026-07-12T10:20:00+03:00"

    # Two intraday runs differ in title (it carries the run time) → both kept, newest first.
    intraday1 = dict(review, title="עדכון ביניים, 12:00")
    intraday2 = dict(review, title="עדכון ביניים, 15:00")
    pr.archive_review("intraday_update", intraday1, "2026-07-12T12:00:00+03:00")
    pr.archive_review("intraday_update", intraday2, "2026-07-12T15:00:00+03:00")
    entries = archived_entries(path)
    assert len(entries) == 3
    assert entries[0]["review"]["title"] == "עדכון ביניים, 15:00"


def test_archive_index_lists_months_newest_first(tmp_path, monkeypatch):
    monkeypatch.setattr(pr, "ARCHIVE_DIR", tmp_path / "archive")
    review = {"title": "א", "date": "2026-07-12", "sections": [{"heading": "h", "content": "* א: ב"}]}
    pr.archive_review("daily_prep", review, "2026-07-12T10:00:00+03:00")
    pr.archive_review("daily_prep", dict(review, title="ב", date="2026-08-03"), "2026-08-03T10:00:00+03:00")
    index = json.loads((tmp_path / "archive" / "index.json").read_text(encoding="utf-8"))
    assert index["months"] == ["2026-08", "2026-07"]


def test_archive_falls_back_to_publish_month_when_date_missing(tmp_path, monkeypatch):
    monkeypatch.setattr(pr, "ARCHIVE_DIR", tmp_path / "archive")
    review = {"title": "א", "sections": [{"heading": "h", "content": "* א: ב"}]}
    path = pr.archive_review("daily_prep", review, "2026-07-12T10:00:00+03:00")
    assert path.name == "2026-07.json"
