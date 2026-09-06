"""Browser test for admin.html — the whole publishing flow against a mock Worker.

Drives the real page in Chromium: choose a review, gather, copy, paste, publish.
Skipped automatically where Playwright/Chromium is not installed (CI runs the rest).
"""
import json
import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

import pytest

pytest.importorskip("playwright.sync_api", reason="playwright not installed")
from playwright.sync_api import sync_playwright  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
CHROMIUM_PATHS = [
    "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
    "/opt/pw-browsers/chromium/chrome-linux/chrome",
]
PASSWORD = "correct-horse-battery-staple"
RAW_MATERIAL = "אתה כותב סקירה פיננסית בעברית.\n\n@acct: $NVDA beats\n"
TITLE = "נקודות חשובות לקראת פתיחת המסחר בוול סטריט 🇺🇸 – יום שני, 7.9.2026"


class MockWorker(BaseHTTPRequestHandler):
    """Stands in for worker.js: same routes, same auth, same JSON shapes."""

    calls = []
    gather_polls = 0
    publish_polls = 0
    publish_fails = False
    published = False
    verdict = {}
    has_auth_check = True     # False simulates an older deployed Worker

    def log_message(self, *a):
        pass

    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Authorization, Content-Type")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")

    def _send(self, code, body):
        payload = json.dumps(body).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self._cors()
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def _authed(self):
        return self.headers.get("Authorization") == f"Bearer {PASSWORD}"

    def do_GET(self):
        if not self._authed():
            return self._send(401, {"error": "unauthorized"})
        if self.path == "/auth-check":
            if not type(self).has_auth_check:
                return self._send(404, {"error": "not found"})
            return self._send(200, {"ok": True})
        if self.path.startswith("/status"):
            cls = type(self)
            if "workflow=publish" in self.path:
                cls.publish_polls += 1
                if cls.publish_polls == 1:
                    return self._send(200, {"state": "queued"})
                state = "failure" if cls.publish_fails else "success"
            else:
                cls.gather_polls += 1
                # First poll still queued, then success — the real thing behaves so.
                state = "queued" if cls.gather_polls == 1 else "success"
            return self._send(200, {"state": state, "id": 99, "url": "http://run"})
        if self.path == "/result":
            cls = type(self)
            if not cls.published:
                return self._send(200, {"ok": True, "finishedAt": "2026-09-01T05:00:00+03:00",
                                        "title": "סקירה קודמת"})
            return self._send(200, dict(cls.verdict, finishedAt="2026-09-07T09:00:00+03:00"))
        if self.path == "/raw":
            return self._send(200, {"content": RAW_MATERIAL, "mode": "daily_prep",
                                    "title": TITLE, "generatedAt": "2026-09-07T06:00:00+03:00"})
        return self._send(404, {"error": "not found"})

    def do_POST(self):
        if not self._authed():
            return self._send(401, {"error": "unauthorized"})
        length = int(self.headers.get("Content-Length") or 0)
        body = json.loads(self.rfile.read(length) or "{}")
        type(self).calls.append((self.path, body))
        if self.path == "/gather":
            return self._send(200, {"ok": True, "mode": body.get("mode"), "after": 98})
        if self.path == "/publish":
            type(self).published = True
            return self._send(200, {"ok": True, "after": 98})
        return self._send(404, {"error": "not found"})


class Static(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def do_GET(self):
        name = self.path.lstrip("/").split("?")[0] or "admin.html"
        target = REPO / name
        if not target.is_file() or REPO not in target.resolve().parents:
            self.send_response(404); self.end_headers(); return
        data = target.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


def serve(handler, port):
    srv = HTTPServer(("127.0.0.1", port), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


@pytest.fixture(scope="module")
def servers():
    site = serve(Static, 8811)
    worker = serve(MockWorker, 8812)
    yield "http://127.0.0.1:8811/admin.html", "http://127.0.0.1:8812"
    site.shutdown()
    worker.shutdown()


def setup_page(page, site, worker, password=PASSWORD):
    """Fills the setup card and waits for the connection test to actually pass."""
    page.goto(site)
    page.fill("#wurl", worker)
    page.fill("#wpass", password)
    page.click("#saveSetup")
    page.wait_for_selector("#chooseCard:not([hidden])", timeout=20000)


def drive_raw(servers, body):
    """Like drive(), but leaves the setup card alone for the tests that drive it."""
    return _run(servers, body, setup=False)


def drive(servers, body, password=PASSWORD):
    """Runs body(page) against a fresh browser, past a successful setup.

    In a worker thread on purpose: pytest 9 runs each test inside an asyncio loop and
    the Playwright sync API refuses to start there.
    """
    return _run(servers, body, setup=True, password=password)


def _run(servers, body, setup=True, password=PASSWORD):
    site, worker = servers
    MockWorker.calls.clear()
    MockWorker.gather_polls = 0
    MockWorker.publish_polls = 0
    MockWorker.published = False
    box = {}

    def run():
        try:
            with sync_playwright() as pw:
                try:
                    # This image ships a Chromium build that may not match the
                    # installed Playwright's expected revision — point at it directly.
                    exe = next((p for p in CHROMIUM_PATHS if os.path.exists(p)), None)
                    browser = pw.chromium.launch(executable_path=exe) if exe else pw.chromium.launch()
                except Exception as exc:
                    box["skip"] = f"chromium unavailable: {exc}"
                    return
                ctx = browser.new_context(permissions=["clipboard-read", "clipboard-write"])
                page = ctx.new_page()
                try:
                    if setup:
                        setup_page(page, site, worker, password)
                    body(page)
                finally:
                    ctx.close()
                    browser.close()
        except BaseException as exc:      # re-raised on the test's thread below
            box["error"] = exc

    thread = threading.Thread(target=run)
    thread.start()
    thread.join(180)
    if thread.is_alive():
        raise AssertionError("browser flow timed out")
    if "skip" in box:
        pytest.skip(box["skip"])
    if "error" in box:
        raise box["error"]


def test_defaults_are_wall_street_morning(servers):
    def body(page):
        assert page.get_attribute('[data-market="us"]', "aria-pressed") == "true"
        assert page.get_attribute('[data-kind="prep"]', "aria-pressed") == "true"
    drive(servers, body)


def test_weekly_is_split_into_summary_and_prep(servers):
    """Weekly summary and weekly prep are separate reviews, so they are separate
    buttons — in both markets."""
    def body(page):
        for market, summary_mode, prep_mode in [("us", "weekly_summary", "weekly_prep"),
                                                ("il", "israel_weekly_summary", "israel_weekly_prep")]:
            page.click(f'[data-market="{market}"]')
            assert page.is_enabled('[data-kind="weeklySummary"]')
            assert page.is_enabled('[data-kind="weeklyPrep"]')
            page.click('[data-kind="weeklyPrep"]')
            page.click("#gatherBtn")
            page.wait_for_selector("#gatherStatus.ok", timeout=40000)
            assert MockWorker.calls[-1] == ("/gather", {"mode": prep_mode})
            page.click('[data-kind="weeklySummary"]')
            page.click("#gatherBtn")
            page.wait_for_selector("#gatherStatus.ok", timeout=40000)
            assert MockWorker.calls[-1] == ("/gather", {"mode": summary_mode})
    drive(servers, body)


def test_a_stored_pre_split_choice_does_not_break_the_screen(servers):
    """"weekly" was a valid stored choice before the split; it must not leave the
    screen with nothing selected and the gather button dead."""
    def body(page):
        page.evaluate("localStorage.setItem('md.kind','weekly')")
        page.reload()
        page.wait_for_selector("#chooseCard:not([hidden])")
        assert page.get_attribute('[data-kind="prep"]', "aria-pressed") == "true"
        assert page.is_enabled("#gatherBtn")
    drive(servers, body)


def test_israel_has_no_intraday_option(servers):
    def body(page):
        assert page.is_enabled('[data-kind="intraday"]')
        page.click('[data-market="il"]')
        assert page.is_disabled('[data-kind="intraday"]'), "Tel Aviv has no intraday mode"
        assert page.is_enabled('[data-kind="weeklySummary"]')
        assert page.is_enabled('[data-kind="weeklyPrep"]')
    drive(servers, body)


def test_switching_to_israel_off_intraday_falls_back(servers):
    def body(page):
        page.click('[data-kind="intraday"]')
        page.click('[data-market="il"]')
        assert page.get_attribute('[data-kind="prep"]', "aria-pressed") == "true"
    drive(servers, body)


def test_last_choice_is_remembered(servers):
    def body(page):
        page.click('[data-market="il"]')
        page.click('[data-kind="weeklyPrep"]')
        page.reload()
        page.wait_for_selector("#chooseCard:not([hidden])")
        assert page.get_attribute('[data-market="il"]', "aria-pressed") == "true"
        assert page.get_attribute('[data-kind="weeklyPrep"]', "aria-pressed") == "true"
    drive(servers, body)


def test_full_flow_gather_copy_publish(servers):
    def body(page):
        # Steps 2 and 3 stay locked until there is material.
        assert page.get_attribute("#chatCard", "data-off") is not None
        assert page.get_attribute("#publishCard", "data-off") is not None

        page.click('[data-kind="close"]')
        page.click("#gatherBtn")
        page.wait_for_selector("#gatherStatus.ok", timeout=40000)

        assert MockWorker.calls[0] == ("/gather", {"mode": "daily_summary"})
        assert TITLE in page.inner_text("#readyBox")
        assert page.get_attribute("#chatCard", "data-off") is None
        assert page.get_attribute("#publishCard", "data-off") is None

        page.click("#copyBtn")
        page.wait_for_function(
            "document.getElementById('copyBtn').textContent.includes('\u05d4\u05d5\u05e2\u05ea\u05e7')")
        assert page.evaluate("navigator.clipboard.readText()") == RAW_MATERIAL

        reply = '```json\n{"title":"x","sections":[]}\n```'
        page.fill("#paste", reply)
        page.click("#publishBtn")
        page.wait_for_selector("#pubStatus.ok", timeout=40000)
        assert "\u05d1\u05d0\u05d5\u05d5\u05d9\u05e8" in page.inner_text("#pubStatus")
        assert MockWorker.calls[-1] == ("/publish", {"content": reply})
    drive(servers, body)


def test_publish_without_text_is_refused(servers):
    def body(page):
        page.eval_on_selector("#publishCard", "el => el.removeAttribute('data-off')")
        page.click("#publishBtn")
        page.wait_for_selector("#pubStatus.bad")
        assert "\u05d4\u05d3\u05d1\u05e7" in page.inner_text("#pubStatus")
        assert not any(c[0] == "/publish" for c in MockWorker.calls)
    drive(servers, body)


def open_setup(servers, body, url=None, password=PASSWORD):
    """Drives the setup card without expecting the connection test to pass."""
    site, worker = servers

    def inner(page):
        page.goto(site)
        page.fill("#wurl", url if url is not None else worker)
        page.fill("#wpass", password)
        page.click("#saveSetup")
        body(page)

    drive_raw(servers, inner)


def test_a_wrong_password_is_caught_at_setup_not_at_the_first_gather(servers):
    """The setup card used to dismiss without checking anything, so the first sign of
    trouble was a failed gather reported as "wrong password" whatever the cause."""
    def body(page):
        page.wait_for_selector("#setupStatus.bad", timeout=20000)
        text = page.inner_text("#setupStatus")
        assert "הסיסמה נדחתה" in text, text
        assert "ADMIN_PASSWORD" in text, "must point at the secret to compare against"
        assert not page.is_hidden("#setupCard"), "setup must stay open on failure"
        assert page.evaluate("localStorage.getItem('md.pass')") is None, \
            "a rejected passphrase must not be left stored"
    open_setup(servers, body, password="wrong")


def test_an_unreachable_server_is_not_reported_as_a_password_problem(servers):
    def body(page):
        page.wait_for_selector("#setupStatus.bad", timeout=25000)
        text = page.inner_text("#setupStatus")
        assert "לא הצלחתי להגיע לשרת" in text, text
        assert "סיסמה" not in text
    open_setup(servers, body, url="https://127.0.0.1:9/nope")


def test_a_stale_worker_deployment_says_so(servers):
    """Auth passes but /auth-check is missing — the deployed Worker predates it."""
    MockWorker.has_auth_check = False
    try:
        def body(page):
            page.wait_for_selector("#setupStatus.bad", timeout=20000)
            text = page.inner_text("#setupStatus")
            assert "הגרסה שפרוסה ישנה" in text, text
            assert "wrangler deploy" in text
        open_setup(servers, body)
    finally:
        MockWorker.has_auth_check = True


def test_a_url_without_https_is_refused_before_any_request(servers):
    def body(page):
        page.wait_for_selector("#setupStatus.bad", timeout=10000)
        assert "https://" in page.inner_text("#setupStatus")
        assert not any(c[0] == "/auth-check" for c in MockWorker.calls)
    open_setup(servers, body, url="market-desk-admin.sh6doron.workers.dev")


def test_plain_http_to_a_remote_host_is_refused(servers):
    """The passphrase must not travel in the clear to anything but a local server."""
    def body(page):
        page.wait_for_selector("#setupStatus.bad", timeout=10000)
        assert "https://" in page.inner_text("#setupStatus")
    open_setup(servers, body, url="http://market-desk-admin.sh6doron.workers.dev")


def test_a_pasted_passphrase_with_stray_whitespace_still_connects(servers):
    """The reported failure: a byte-exact compare against a hand-pasted secret, where
    an invisible trailing newline reads as a wrong password."""
    def body(page):
        page.wait_for_selector("#chooseCard:not([hidden])", timeout=20000)
        assert page.evaluate("localStorage.getItem('md.pass')") == PASSWORD
    open_setup(servers, body, password=f"  {PASSWORD}\n")


def test_a_url_with_stray_whitespace_still_connects(servers):
    site, worker = servers

    def body(page):
        page.wait_for_selector("#chooseCard:not([hidden])", timeout=20000)
    open_setup(servers, body, url=f"  {worker}/  ")


def test_a_successful_setup_leaves_no_error_showing(servers):
    def body(page):
        page.wait_for_selector("#chooseCard:not([hidden])", timeout=20000)
        assert page.is_hidden("#setupCard")
        assert "on" not in (page.get_attribute("#setupStatus", "class") or "")
    open_setup(servers, body)


GUARD_REASON = ("סתירת כיוון: הסקירה כותבת שמניית NVDA עלתה, "
                "אבל בנתוני האיסוף היא ירדה ב-2.4%. בקש מהצ׳אט לתקן.")


def test_guard_rejection_shows_its_hebrew_reason(servers):
    """A rejected review must explain itself on screen, not in an Actions log."""
    MockWorker.publish_fails = True
    MockWorker.verdict = {"ok": False, "mode": "daily_summary", "error": GUARD_REASON}

    def body(page):
        page.click("#gatherBtn")
        page.wait_for_selector("#gatherStatus.ok", timeout=40000)
        reply = '{"title":"x","sections":[]}'
        page.fill("#paste", reply)
        page.click("#publishBtn")
        page.wait_for_selector("#pubStatus.bad", timeout=60000)
        shown = page.inner_text("#pubStatus")
        assert GUARD_REASON in shown, shown
        # The pasted text stays put so it can be corrected and sent again.
        assert page.input_value("#paste") == reply
    try:
        drive(servers, body)
    finally:
        MockWorker.publish_fails = False
        MockWorker.verdict = {}


def test_success_shows_the_published_title(servers):
    MockWorker.publish_fails = False
    MockWorker.verdict = {"ok": True, "mode": "daily_summary", "title": TITLE, "bullets": 6}

    def body(page):
        page.click("#gatherBtn")
        page.wait_for_selector("#gatherStatus.ok", timeout=40000)
        page.fill("#paste", '{"title":"x","sections":[]}')
        page.click("#publishBtn")
        page.wait_for_selector("#pubStatus.ok", timeout=60000)
        shown = page.inner_text("#pubStatus")
        assert "באוויר" in shown and TITLE in shown, shown
    try:
        drive(servers, body)
    finally:
        MockWorker.verdict = {}
