"""Staleness is measured against inputs, not the clock (spec 3.3)."""
import os
import time

from program.collect import envelope
from program.collect.views import classify, collect


def test_envelope_carries_provenance():
    env = envelope([1, 2], source="unit-test")
    assert env["ok"] is True and env["error"] is None
    assert env["source"] == "unit-test"
    assert env["data"] == [1, 2]
    assert env["collected_at"]


def test_view_newer_than_its_inputs_is_fresh(tmp_path):
    src = tmp_path / "in.txt"; src.write_text("x", encoding="utf-8")
    view = tmp_path / "out.html"; view.write_text("y", encoding="utf-8")
    os.utime(view, (time.time() + 10, time.time() + 10))
    assert classify(view, [src]) == "FRESH"


def test_view_older_than_an_input_is_stale(tmp_path):
    view = tmp_path / "out.html"; view.write_text("y", encoding="utf-8")
    src = tmp_path / "in.txt"; src.write_text("x", encoding="utf-8")
    os.utime(src, (time.time() + 10, time.time() + 10))
    assert classify(view, [src]) == "STALE"


def test_view_without_declared_inputs_is_unknown_never_fresh(tmp_path):
    view = tmp_path / "hand.md"; view.write_text("y", encoding="utf-8")
    assert classify(view, []) == "UNKNOWN"


def test_missing_view_is_stale(tmp_path):
    assert classify(tmp_path / "absent.html", []) == "STALE"


def test_collect_returns_an_envelope_listing_every_registered_view():
    env = collect()
    assert env["ok"] is True
    names = [v["name"] for v in env["data"]]
    assert "review dashboard" in names
    assert "item tracker" in names
    for v in env["data"]:
        assert v["state"] in {"FRESH", "STALE", "UNKNOWN"}
