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
