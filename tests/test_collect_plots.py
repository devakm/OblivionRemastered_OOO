"""Plots are timestamped artifacts, not a view (staged by the MapClone session).

Each run writes a NEW png, so there is nothing to call stale -- the mtime is
the content. The gate_only flag is the point of the panel: a plot that reached
the pre-build gate folder but never the review folder is invisible to review,
which is the bug that prompted this collector.
"""
import os
import time

from program.collect import plots, views


def _png(folder, name, when=None):
    folder.mkdir(parents=True, exist_ok=True)
    p = folder / name
    p.write_bytes(b"\x89PNG\r\n\x1a\n" + b"0" * 2048)
    if when:
        os.utime(p, (when, when))
    return p


def _redirect(monkeypatch, tmp_path):
    review, gate = tmp_path / "plots", tmp_path / "gate"
    review.mkdir(); gate.mkdir()
    monkeypatch.setattr(plots, "REVIEW_DIR", review)
    monkeypatch.setattr(plots, "GATE_DIR", gate)
    return review, gate


def test_plot_in_both_folders_is_not_gate_only(monkeypatch, tmp_path):
    review, gate = _redirect(monkeypatch, tmp_path)
    _png(review, "both.png"); _png(gate, "both.png")
    row = plots.collect()["data"]["plots"][0]
    assert row["name"] == "both.png"
    assert row["gate_only"] is False


def test_plot_only_in_the_gate_folder_is_flagged(monkeypatch, tmp_path):
    review, gate = _redirect(monkeypatch, tmp_path)
    _png(gate, "gateonly.png")
    data = plots.collect()["data"]
    assert data["plots"][0]["gate_only"] is True
    assert data["gate_only_count"] == 1


def test_plot_only_in_review_is_not_flagged(monkeypatch, tmp_path):
    review, gate = _redirect(monkeypatch, tmp_path)
    _png(review, "reviewonly.png")
    assert plots.collect()["data"]["plots"][0]["gate_only"] is False


def test_by_design_single_savers_are_not_flagged_as_anomalies(monkeypatch, tmp_path):
    """plot_water_analysis.py and plot_water_z_analysis.py write only the gate
    copy on purpose. Calling those anomalies buries the one row that is real."""
    review, gate = _redirect(monkeypatch, tmp_path)
    _png(gate, "water_analysis_20260601_abc.png")
    _png(gate, "water_z_analysis_20260823_def.png")
    data = plots.collect()["data"]
    assert data["gate_only_count"] == 2
    assert data["unexpected_count"] == 0


def test_a_single_test_xy_plot_missing_from_review_is_the_real_bug(monkeypatch, tmp_path):
    review, gate = _redirect(monkeypatch, tmp_path)
    _png(gate, "water_xy_gwcz2-t5_actual_20260830_125841.png")
    data = plots.collect()["data"]
    assert data["unexpected_count"] == 1
    assert data["plots"][0]["unexpected"] is True


def test_newest_first(monkeypatch, tmp_path):
    review, gate = _redirect(monkeypatch, tmp_path)
    now = time.time()
    _png(review, "old.png", when=now - 7200)
    _png(review, "new.png", when=now - 60)
    assert [r["name"] for r in plots.collect()["data"]["plots"]] == ["new.png", "old.png"]


def test_links_are_file_uris_so_the_static_page_can_open_them(monkeypatch, tmp_path):
    review, gate = _redirect(monkeypatch, tmp_path)
    _png(review, "a.png")
    assert plots.collect()["data"]["plots"][0]["url"].startswith("file:///")


def test_missing_folders_yield_an_ok_empty_envelope(monkeypatch, tmp_path):
    monkeypatch.setattr(plots, "REVIEW_DIR", tmp_path / "nope")
    monkeypatch.setattr(plots, "GATE_DIR", tmp_path / "also-nope")
    env = plots.collect()
    assert env["ok"] is True and env["data"]["plots"] == []


def test_plots_are_not_registered_as_a_generated_view():
    """Every run writes a new file, so a staleness verdict is meaningless."""
    assert not any("plot" in v["name"].lower() for v in views.VIEWS)


def test_the_real_folders_are_readable():
    """Fixture drift guard against the live MapClone tree."""
    env = plots.collect()
    assert env["ok"] is True
    for r in env["data"]["plots"]:
        assert r["name"].endswith(".png") and r["kb"] >= 0
