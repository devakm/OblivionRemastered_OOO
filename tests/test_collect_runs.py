"""The run ledger: orphans must surface to the next session (spec 3.2)."""
import json

from program.collect import runs


def _write(repo, records):
    led = repo / ".claude"; led.mkdir(parents=True, exist_ok=True)
    (led / "runs.jsonl").write_text(
        "".join(json.dumps(r) + "\n" for r in records), encoding="utf-8")


def test_finished_record_is_done(tmp_path):
    rec = {"id": "a", "pid": 1, "proc_started": "t0", "ended": "2026-08-29T10:00:00"}
    assert runs.status_of(rec) == "done"


def test_live_process_with_matching_start_time_is_running(tmp_path, monkeypatch):
    monkeypatch.setattr(runs, "proc_start", lambda pid: "t0")
    rec = {"id": "a", "pid": 4242, "proc_started": "t0", "ended": None}
    assert runs.status_of(rec) == "running"


def test_dead_process_is_orphaned_not_running(monkeypatch):
    monkeypatch.setattr(runs, "proc_start", lambda pid: None)
    rec = {"id": "a", "pid": 4242, "proc_started": "t0", "ended": None}
    assert runs.status_of(rec) == "orphaned"


def test_recycled_pid_cannot_impersonate_a_live_job(monkeypatch):
    monkeypatch.setattr(runs, "proc_start", lambda pid: "DIFFERENT")
    rec = {"id": "a", "pid": 4242, "proc_started": "t0", "ended": None}
    assert runs.status_of(rec) == "orphaned"


def test_record_without_a_pid_is_orphaned_when_unfinished(monkeypatch):
    """A background subagent has no process handle -- the case that bit us."""
    rec = {"id": "a", "pid": None, "proc_started": None, "ended": None,
           "kind": "agent", "purpose": "Extend approved_territory"}
    assert runs.status_of(rec) == "orphaned"


def test_sweep_marks_dead_records_and_keeps_their_purpose(tmp_path, monkeypatch):
    monkeypatch.setattr(runs, "proc_start", lambda pid: None)
    _write(tmp_path, [{"id": "a", "pid": 9, "proc_started": "t0", "ended": None,
                       "purpose": "Extend approved_territory to original/ masks"}])
    assert runs.sweep(tmp_path) == 1
    line = json.loads((tmp_path / ".claude/runs.jsonl").read_text().splitlines()[-1])
    assert line["status"] == "orphaned"
    assert line["purpose"] == "Extend approved_territory to original/ masks"


def test_append_creates_the_ledger(tmp_path):
    runs.append(tmp_path, {"id": "z", "purpose": "p"})
    assert (tmp_path / ".claude/runs.jsonl").exists()
