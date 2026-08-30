"""Phase 9 zone validation is human-gated progress, not a staleness verdict."""
from program.collect import views
from program.collect.maps import cave_of, pending_cells, zones

TABLE = """
| Mark | Meaning |
| ---- | ------- |
| ✓ MM-DD | Confirmed in-game on that 2026 date. |
| Cell | Donor | W | P1 | P3 | Notes |
|------|-------|---|----|----|-------|
| Blood Clot Cave (BloodClotCave)   | GreenmeadCave  | Y | ✓ | ✓ | **VERIFIED 2026-05-26** |
| Gloom Way Cave (GloomWayCave)     | CrayfishCave05 | Y | · | ⏳ 08-23 | Awaiting in-game. |
| Gloom Way Cave (GloomWayCave02)   | CrayfishCave04 | Y | · | ⏳ 08-23 | Awaiting in-game. |
| Red Gill Cave (RedGillCaverns)    | FloodedMine    | Y | · | ⏳ 08-23 | Awaiting in-game. |
"""


def _doc(tmp_path):
    p = tmp_path / "tracker.md"
    p.write_text(TABLE, encoding="utf-8")
    return p


def test_legend_rows_are_not_mistaken_for_zones(tmp_path):
    names = [z["cell"] for z in zones(_doc(tmp_path))]
    assert all("Mark" not in n and "MM-DD" not in n for n in names)
    assert len(names) == 4


def test_confirmed_and_pending_are_distinguished(tmp_path):
    rows = zones(_doc(tmp_path))
    by = {z["edid"]: z["state"] for z in rows}
    assert by["BloodClotCave"] == "confirmed"
    assert by["GloomWayCave"] == "pending"
    assert by["RedGillCaverns"] == "pending"


def test_pending_cells_are_the_rows_still_awaiting(tmp_path):
    edids = [z["edid"] for z in pending_cells(_doc(tmp_path))]
    assert set(edids) == {"GloomWayCave", "GloomWayCave02", "RedGillCaverns"}


def test_zones_group_into_caves():
    assert cave_of("Gloom Way Cave (GloomWayCave02)") == "Gloom Way Cave"
    assert cave_of("Red Gill Cave (RedGillCaverns)") == "Red Gill Cave"


def test_missing_tracker_yields_no_rows(tmp_path):
    assert zones(tmp_path / "absent.md") == []


def test_the_tracker_is_not_registered_as_a_generated_view():
    """It has no generator -- every row is validated by a human in-game, so a
    freshness verdict on it would be a category error."""
    assert not any("phase9" in str(v["path"]) or "phase 9" in v["name"].lower()
                   for v in views.VIEWS)


def test_recent_activity_is_not_mojibake():
    """git_narrative emits UTF-8; decoding it with the Windows locale default
    turned every em-dash into 'a-hat-euro'. Guard the round trip."""
    from program.collect import maps
    env = maps.collect()
    for line in env["data"]["recent"]:
        assert "â€" not in line, f"mis-decoded UTF-8: {line}"


def test_the_real_tracker_parses():
    """Fixture drift guard: the live tracker must still be readable."""
    from program.collect.maps import TRACKER
    if TRACKER.exists():
        rows = zones(TRACKER)
        assert rows, "the live tracker parsed to zero zones -- format drift"
        assert all(z["edid"] for z in rows)
