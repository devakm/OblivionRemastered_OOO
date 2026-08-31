"""The dashboard must disclose its own staleness.

It is a static snapshot that only tells the truth when regenerated. Every
other view here gets a staleness verdict; without this the dashboard was the
one artifact that could silently go stale while looking current -- a user
read a 45-minute-old page as live and asked why new plots were missing.
"""
import re
from datetime import datetime
from pathlib import Path

from program import build_dashboard


def test_page_carries_a_machine_readable_generation_stamp(tmp_path):
    out = build_dashboard.main(out=tmp_path / "d.html")
    html = out.read_text(encoding="utf-8")
    m = re.search(r'id=age data-gen="([^"]+)"', html)
    assert m, "no generation stamp -- the page cannot disclose its own age"
    datetime.fromisoformat(m.group(1))          # parses, so JS can too


def test_page_names_the_command_that_refreshes_it(tmp_path):
    out = build_dashboard.main(out=tmp_path / "d.html")
    html = out.read_text(encoding="utf-8")
    assert "py -3 -m program.build_dashboard" in html


def test_the_stamp_reflects_the_generation_time_not_a_constant():
    a = build_dashboard.self_age(now=datetime(2026, 8, 31, 12, 29, 39))
    b = build_dashboard.self_age(now=datetime(2026, 8, 31, 13, 10, 3))
    assert a != b
    assert "2026-08-31T12:29:39" in a and "2026-08-31T13:10:03" in b


def test_age_script_is_inline_and_makes_no_external_request(tmp_path):
    """Static and self-contained: reading the clock is not a side effect, and
    the page still never runs a generator."""
    out = build_dashboard.main(out=tmp_path / "d.html")
    html = out.read_text(encoding="utf-8")
    assert "<script>" in html
    assert not re.search(r'(src|href)="https?://', html), "must stay offline"
    for forbidden in ("fetch(", "XMLHttpRequest", "import("):
        assert forbidden not in html
