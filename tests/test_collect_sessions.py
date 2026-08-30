"""Sessions and handoffs are one feed (spec 3.5)."""
from program.collect.sessions import handoffs, parse_list_sessions

SAMPLE = """STARTED          LAST ACTIVE      ID        TITLE / first prompt
------------------------------------------------------------------------------
08-29 09:22      08-29 09:41      7a62b37c  Program control plane design
08-23 15:01      08-23 16:22      06b8a9bb  Noble benchmark closed
"""


def test_parse_list_sessions_reads_rows_not_the_header():
    rows = parse_list_sessions(SAMPLE)
    assert len(rows) == 2
    assert rows[0]["id"] == "7a62b37c"
    assert rows[0]["label"] == "Program control plane design"


def test_handoff_filenames_yield_date_and_set(tmp_path):
    (tmp_path / "handoff-2026-08-23-noble-s1-benchmark-closed.md").write_text("x", encoding="utf-8")
    (tmp_path / "not-a-handoff.md").write_text("x", encoding="utf-8")
    rows = handoffs(tmp_path)
    assert len(rows) == 1
    assert rows[0]["date"] == "2026-08-23"
    assert rows[0]["set_name"] == "noble"


def test_handoffs_are_newest_first(tmp_path):
    for d in ("2026-07-01", "2026-08-23"):
        (tmp_path / f"handoff-{d}-noble-s1-x.md").write_text("x", encoding="utf-8")
    assert handoffs(tmp_path)[0]["date"] == "2026-08-23"
