"""What has actually shipped, and what the next release is.

Derived from the repository -- tag, manifest and dist archive must all agree
before a version counts as released. The first cut of this dashboard declared
the version in program.yaml and was wrong by a full release within a day of
being written, which is the argument for deriving it.
"""
import re
import subprocess
from pathlib import Path

from . import envelope

OOO = Path(r"X:\dev\OblivionRemastered_OOO")
TAG = re.compile(r"^([a-z]+)(\d+)$")


def next_version(tag: str) -> str:
    """alpha91 -> alpha92. Increments the trailing number, keeps the series."""
    m = TAG.match(tag)
    if not m:
        return "?"
    return f"{m.group(1)}{int(m.group(2)) + 1}"


def _tags() -> list[str]:
    out = subprocess.run(["git", "-C", str(OOO), "tag", "--list", "alpha[0-9]*"],
                         capture_output=True, text=True, timeout=30)
    return [t for t in out.stdout.split() if TAG.match(t)]


def latest_released() -> dict:
    """The highest alpha tag corroborated by a manifest and a dist archive."""
    best = None
    for tag in _tags():
        n = int(TAG.match(tag).group(2))
        has_manifest = (OOO / "manifests" / f"{tag}.json").exists()
        has_archive = (OOO / "dist" / f"{tag}.7z").exists()
        if has_manifest and has_archive and (best is None or n > best["n"]):
            best = {"tag": tag, "n": n, "has_manifest": has_manifest,
                    "has_archive": has_archive}
    return best or {"tag": "?", "n": 0, "has_manifest": False, "has_archive": False}


def collect() -> dict:
    try:
        latest = latest_released()
        data = {"latest": latest, "next": next_version(latest["tag"]),
                "released_count": len(_tags())}
    except (OSError, subprocess.SubprocessError) as exc:
        return envelope(None, source="releases.collect", ok=False, error=str(exc))
    return envelope(data, source="releases.collect")
