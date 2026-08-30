"""Branch state sorted into actions (spec 3.4)."""
from program.collect.repos import bucket, collect


def test_merged_branch_that_still_exists_is_flagged_for_deletion():
    assert bucket({"name": "old", "merged": True, "ahead": 0}) == "merged-undeleted"


def test_open_branch_ahead_of_main_is_unmerged_work():
    assert bucket({"name": "ancestral", "merged": False, "ahead": 5}) == "open-ahead"


def test_branch_with_nothing_to_merge_is_in_sync():
    assert bucket({"name": "tidy", "merged": False, "ahead": 0}) == "in-sync"


def test_unannotated_open_branch_renders_unexplained():
    env = collect(annotations={})
    open_branches = [b for r in env["data"] for b in r["branches"]
                     if b["bucket"] == "open-ahead"]
    assert open_branches, "the survey found open branches; fixture drift if empty"
    assert all(b["intent"] == "unexplained" for b in open_branches)


def test_annotation_supplies_the_intent_git_cannot():
    env = collect(annotations={"ItemClone/ancestral": "Amelion template work"})
    found = [b for r in env["data"] if r["repo"] == "ItemClone"
             for b in r["branches"] if b["name"] == "ancestral"]
    assert found and found[0]["intent"] == "Amelion template work"


def test_collector_reports_a_repo_without_a_remote():
    env = collect()
    plugintools = [r for r in env["data"] if r["repo"] == "PluginTools"]
    assert plugintools and plugintools[0]["has_remote"] is False
