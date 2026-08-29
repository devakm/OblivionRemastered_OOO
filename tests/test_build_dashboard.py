"""The dashboard is a static file with no server and no side effects (spec 3)."""
import re
from pathlib import Path

from program import build_dashboard
from program.collect import envelope

OOO = Path(__file__).resolve().parents[1]


def test_failed_envelope_renders_as_an_error_panel_not_an_empty_one():
    env = envelope(None, source="x", ok=False, error="git not found")
    html = build_dashboard.panel("Branches", env, "")
    assert "git not found" in html
    assert "panel-error" in html


def test_page_has_no_absolute_root_links(tmp_path):
    out = build_dashboard.main(out=tmp_path / "dashboard.html")
    html = out.read_text(encoding="utf-8")
    assert not re.search(r'(href|src)="/', html), "must work over file://"


def test_page_names_the_rebuild_command_for_a_stale_view(tmp_path):
    out = build_dashboard.main(out=tmp_path / "dashboard.html")
    html = out.read_text(encoding="utf-8")
    assert "python tools/" in html


def test_generator_writes_nothing_outside_program(tmp_path):
    before = {p: p.stat().st_mtime for p in (OOO / "release").rglob("*") if p.is_file()}
    build_dashboard.main(out=tmp_path / "dashboard.html")
    after = {p: p.stat().st_mtime for p in (OOO / "release").rglob("*") if p.is_file()}
    assert before == after, "collectors must be read-only outside program/"
