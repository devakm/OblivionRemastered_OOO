"""The map tracker reports outstanding cells, not a bare UNKNOWN."""
from program.collect.maps import pending_cells

TABLE = """
| Cell | Donor | W | P1 | P3 | Notes |
|------|-------|---|----|----|-------|
| Blood Clot Cave (BloodClotCave)   | GreenmeadCave  | Y | ✓ | ✓ | **VERIFIED 2026-05-26** |
| Gloom Way Cave (GloomWayCave)     | CrayfishCave05 | Y | · | ⏳ 08-23 | Awaiting in-game. |
| Red Gill Cave (RedGillCaverns)    | FloodedMine    | Y | · | ⏳ 08-23 | Awaiting in-game. |
"""


def test_pending_cells_are_the_rows_still_awaiting(tmp_path):
    doc = tmp_path / "tracker.md"
    doc.write_text(TABLE, encoding="utf-8")
    rows = pending_cells(doc)
    names = [r["cell"] for r in rows]
    assert "Gloom Way Cave (GloomWayCave)" in names
    assert "Red Gill Cave (RedGillCaverns)" in names


def test_verified_rows_are_not_reported_as_pending(tmp_path):
    doc = tmp_path / "tracker.md"
    doc.write_text(TABLE, encoding="utf-8")
    assert all("Blood Clot" not in r["cell"] for r in pending_cells(doc))


def test_missing_tracker_yields_no_rows(tmp_path):
    assert pending_cells(tmp_path / "absent.md") == []


def test_the_real_tracker_parses():
    """Fixture drift guard: the live tracker must still be readable."""
    from program.collect.maps import TRACKER
    if TRACKER.exists():
        for r in pending_cells(TRACKER):
            assert r["cell"] and isinstance(r["cell"], str)
