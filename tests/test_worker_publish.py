"""What the Worker does with a paste — in particular, a paste it has seen before.

Re-publishing identical text used to write an EMPTY commit: the Contents API happily
makes one, but no file changed, so `on: push: paths: [review_output.json]` never
matched and no run was ever created. The admin screen then waited out its whole
six-minute budget for a run that could not arrive — the "why is this so slow?" report.
Unchanged content must dispatch the workflow instead, so the guards re-run and the
screen gets a verdict either way.
"""
import json
import shutil
import subprocess
from pathlib import Path

import pytest

PROBE = Path(__file__).resolve().parent / "worker_publish_probe.mjs"
REVIEW = json.dumps(
    {"title": "כותרת", "sections": [{"heading": "נקודות מרכזיות", "content": "* נקודה: משפט."}]},
    ensure_ascii=False,
)


def run_publish(pasted, on_branch):
    node = shutil.which("node") or "/opt/node22/bin/node"
    if not Path(node).exists():
        pytest.skip("node not installed")
    out = subprocess.run([node, str(PROBE), pasted, on_branch],
                         capture_output=True, text=True, timeout=60)
    assert out.returncode == 0, out.stderr
    return json.loads(out.stdout)


def test_new_content_is_committed_and_not_dispatched():
    r = run_publish(REVIEW, '{"title": "סקירה קודמת", "sections": []}')
    assert r["status"] == 200
    assert r["body"]["unchanged"] is False
    assert r["committed"] == 1, "a changed review must be committed — the push fires the run"
    assert r["dispatched"] == 0


def test_identical_content_dispatches_instead_of_an_empty_commit():
    """The reported hang: the same JSON sent twice."""
    r = run_publish(REVIEW, REVIEW)
    assert r["status"] == 200
    assert r["body"]["unchanged"] is True
    assert r["committed"] == 0, "an empty commit creates no run — the screen would hang"
    assert r["dispatched"] == 1, "the guards must be re-run over the content already there"
    assert r["dispatch_body"] == {"ref": "main"}


def test_identical_content_still_reports_the_run_to_wait_for():
    """`after` is what the screen polls against; the dispatch path must return it too."""
    r = run_publish(REVIEW, REVIEW)
    assert r["body"]["after"] == 4242


def test_whitespace_around_an_otherwise_identical_paste_is_not_a_change():
    r = run_publish(f"\n  {REVIEW}  \n", REVIEW)
    assert r["committed"] == 0 and r["dispatched"] == 1


def test_a_first_ever_publish_has_nothing_to_compare_against():
    r = run_publish(REVIEW, "__missing__")
    assert r["committed"] == 1 and r["dispatched"] == 0


def test_raw_material_is_still_refused_before_either_path():
    r = run_publish("אתה כותב סקירה פיננסית בעברית לאתר. {\"sections\": []}", REVIEW)
    assert r["status"] == 400
    assert "חומר הגלם" in r["body"]["error"]
    assert r["committed"] == 0 and r["dispatched"] == 0
