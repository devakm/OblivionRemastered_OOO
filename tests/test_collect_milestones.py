"""A claim without a registered check is never green (spec 3.6)."""
from program.collect import milestones


def test_unregistered_check_kind_is_unverified_not_met():
    state = milestones.evaluate({"id": "x", "claim": "c", "check": {"kind": "invented"}})
    assert state == "UNVERIFIED"


def test_criterion_with_no_check_at_all_is_unverified():
    assert milestones.evaluate({"id": "x", "claim": "c"}) == "UNVERIFIED"


def test_passing_check_is_met(monkeypatch):
    monkeypatch.setitem(milestones.CHECKS, "always", lambda c: True)
    assert milestones.evaluate({"id": "x", "claim": "c", "check": {"kind": "always"}}) == "MET"


def test_failing_check_is_contradicted(monkeypatch):
    monkeypatch.setitem(milestones.CHECKS, "never", lambda c: False)
    assert milestones.evaluate(
        {"id": "x", "claim": "c", "check": {"kind": "never"}}) == "CONTRADICTED"


def test_failing_check_on_unfinished_work_is_pending_not_contradicted(monkeypatch):
    """Not-yet-done is remaining work, not a lie. Red is reserved for a
    milestone asserted DONE whose evidence denies it."""
    monkeypatch.setitem(milestones.CHECKS, "never", lambda c: False)
    assert milestones.evaluate({"id": "x", "claim": "c", "check": {"kind": "never"}},
                               claimed_done=False) == "PENDING"


def test_a_done_milestone_with_failing_evidence_still_contradicts():
    """The gate keeps its teeth: alpha91 is declared done, so if its manifest
    ever vanished the dashboard must say CONTRADICTED, not PENDING."""
    env = milestones.collect()
    done = [m for m in env["data"]["milestones"] if m["status"] == "done"]
    assert done, "fixture drift: no milestone is declared done"
    for m in done:
        for c in m["criteria"]:
            assert c["state"] in {"MET", "CONTRADICTED", "UNVERIFIED"}
            assert c["state"] != "PENDING"


def test_manifest_check_finds_a_real_tag():
    assert milestones.CHECKS["manifest_exists"]({"tag": "alpha90"}) is True
    assert milestones.CHECKS["manifest_exists"]({"tag": "no-such-tag"}) is False


def test_collect_reports_unmet_criteria_for_the_next_milestone():
    env = milestones.collect()
    assert env["ok"] is True
    nxt = env["data"]["next"]
    assert "name" in nxt and isinstance(nxt["unmet"], list)
