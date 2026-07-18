"""Guards for the site's WhatsApp share link (index.html).

The shared message once embedded location.href — whatever URL the sharer was
viewing at that moment. Sharing from a temporary preview/proxy address sent
recipients to a blocked page. These tests lock in the fix: the share link must
always be the canonical public site URL, hardcoded as SITE_URL.
"""
import re
from pathlib import Path

INDEX_HTML = (Path(__file__).resolve().parent.parent / "index.html").read_text(encoding="utf-8")

CANONICAL_URL = "https://doronsh170.github.io/wallstreet-reviews-v2/"


def share_function_body():
    match = re.search(r"function shareWhatsApp\(\)\{.*?\n\}", INDEX_HTML, re.DOTALL)
    assert match, "shareWhatsApp() not found in index.html"
    return match.group(0)


def test_site_url_constant_is_canonical():
    match = re.search(r"const SITE_URL = '([^']+)'", INDEX_HTML)
    assert match, "SITE_URL constant not found in index.html"
    assert match.group(1) == CANONICAL_URL


def test_share_message_uses_site_url():
    assert "SITE_URL" in share_function_body()


def test_share_message_never_uses_dynamic_location():
    body = share_function_body()
    for forbidden in ("location.href", "window.location", "document.URL", "document.location"):
        assert forbidden not in body, (
            f"shareWhatsApp() uses {forbidden}: the shared link must be the fixed "
            "SITE_URL, never the address the sharer happens to be viewing from"
        )


def test_share_button_is_wired():
    assert 'onclick="shareWhatsApp()"' in INDEX_HTML, "the share button lost its onclick handler"


def test_share_uses_wa_me_link():
    # wa.me is the canonical click-to-chat form that works with no phone number;
    # api.whatsapp.com/send is unreliable on both desktop and mobile.
    body = share_function_body()
    assert "https://wa.me/?text=" in body
    assert "api.whatsapp.com" not in body.replace("// The older api.whatsapp.com", "")


def test_share_never_fails_summary_errors_fall_back_to_title_and_link():
    # The button must always produce a working share: if condensing the summary
    # throws on unexpected data, the message degrades to title + site link.
    body = share_function_body()
    assert "try{" in body and "}catch(" in body, "shareWhatsApp() lost its try/catch fallback"
    fallback = re.search(r"\}catch\([^)]*\)\{\s*lines = \[title, '', cta\];", body)
    assert fallback, "the catch branch must rebuild the message as [title, '', cta]"


def test_share_caps_url_length():
    # Browsers/WhatsApp silently reject absurdly long URLs — the message must be
    # trimmed (dropping summary lines, keeping title + link) instead of dying.
    assert "MAX_SHARE_URL_CHARS" in INDEX_HTML
    assert "MAX_SHARE_URL_CHARS" in share_function_body()


def test_published_reviews_are_shareable():
    """Every review currently in data.json must carry what the share message
    needs: a non-empty title and at least one bullet (summariesOf falls back to
    bullets when there is no authored summary)."""
    import json
    data_path = Path(__file__).resolve().parent.parent / "data.json"
    if not data_path.exists():
        return
    data = json.loads(data_path.read_text(encoding="utf-8"))
    keys = ("dailyPrep", "intradayUpdate", "dailySummary", "weeklySummary",
            "israelPrep", "israelSummary", "israelWeeklySummary")
    for key in keys:
        review = data.get(key)
        if not review:
            continue
        assert str(review.get("title", "")).strip(), f"{key}: empty title breaks the share message"
        sections = review.get("sections") or []
        content = str((sections[0] if sections else {}).get("content", ""))
        bullets = [l for l in content.split("\n") if l.strip()]
        assert bullets, f"{key}: no bullets — the share message would be empty"
