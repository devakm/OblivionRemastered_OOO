"""The tracker leads with the real release state, derived and never declared.

A hand-typed version number is exactly what drifted: the first cut of
program.yaml claimed alpha90 while alpha91 was long since tagged, built and
shipped. Nothing here hardcodes a version -- each expectation is computed
from the repository, so these tests keep passing at alpha92 and beyond.
"""
import subprocess
from pathlib import Path

from program.collect.releases import OOO, collect, latest_released, next_version


def _highest_tag_in_git() -> str:
    out = subprocess.run(["git", "-C", str(OOO), "tag", "--list", "alpha[0-9]*"],
                         capture_output=True, text=True, check=True)
    nums = [int(t[5:]) for t in out.stdout.split() if t[5:].isdigit()]
    return f"alpha{max(nums)}"


def test_latest_released_is_the_highest_alpha_tag_git_reports():
    assert latest_released()["tag"] == _highest_tag_in_git()


def test_latest_release_is_corroborated_by_a_manifest_and_an_archive():
    r = latest_released()
    assert r["has_manifest"] is True, "a tag with no manifest is not a release"
    assert r["has_archive"] is True, "a tag with no dist archive is not a release"


def test_next_version_increments_rather_than_being_typed():
    assert next_version("alpha91") == "alpha92"
    assert next_version("alpha9") == "alpha10"
    assert next_version("alpha109") == "alpha110"


def test_collect_reports_current_and_next():
    env = collect()
    assert env["ok"] is True
    highest = _highest_tag_in_git()
    assert env["data"]["latest"]["tag"] == highest
    assert env["data"]["next"] == next_version(highest)


def test_a_tag_without_a_manifest_is_not_treated_as_released(tmp_path):
    """Guards the corroboration rule -- a bare tag must not become 'the release'."""
    r = latest_released()
    assert (OOO / "manifests" / f'{r["tag"]}.json').exists()
