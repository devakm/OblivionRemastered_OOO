#!/usr/bin/env python3
"""
Create (or update) a GitHub Release for a tag and attach the packaged 7z archive.

DRY-RUN BY DEFAULT. The script prints what it *would* do and exits. Pass
`--for-real` to actually call `gh release` and `git push`.

Workflow per release:
  1. Verify the local tag exists.
  2. Verify dist/<tag>.7z exists (build it first via package_release.py).
  3. Verify docs/per-release/<tag>.md exists (used as release body).
  4. Push the tag to origin (`git push origin <tag>`).
  5. `gh release create <tag> dist/<tag>.7z --title "<tag>" --notes-file docs/per-release/<tag>.md`
     (or `gh release upload <tag> dist/<tag>.7z --clobber` if release exists).

Pre-reqs:
  - `gh` CLI installed and authenticated (`gh auth login`).
  - Remote `origin` set to a GitHub repo you can push to.

Usage:
    python scripts/publish_github.py --tag alpha90              # dry-run
    python scripts/publish_github.py --tag alpha90 --for-real   # real
    python scripts/publish_github.py --tag alpha90 --prerelease # mark as pre-release
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DIST_DIR = REPO_ROOT / "dist"
PER_RELEASE_DOC_DIR = REPO_ROOT / "docs" / "per-release"


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=REPO_ROOT, capture_output=True, text=True, check=check)


def gh(*args: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(["gh", *args], cwd=REPO_ROOT, capture_output=True, text=True, check=check)


def tag_exists(tag: str) -> bool:
    return git("rev-parse", "--verify", "--quiet", f"refs/tags/{tag}", check=False).returncode == 0


def gh_release_exists(tag: str) -> bool:
    r = gh("release", "view", tag, check=False)
    return r.returncode == 0


def run_or_print(cmd: list[str], for_real: bool) -> int:
    if for_real:
        print(f"[publish] EXEC: {' '.join(cmd)}", file=sys.stderr)
        r = subprocess.run(cmd, cwd=REPO_ROOT)
        return r.returncode
    print(f"[publish] DRY: {' '.join(cmd)}", file=sys.stderr)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--tag", required=True, help="release tag to publish (e.g. alpha90)")
    ap.add_argument("--for-real", action="store_true", help="actually invoke git push + gh release")
    ap.add_argument("--prerelease", action="store_true", help="mark as pre-release on GitHub")
    ap.add_argument("--title", help="release title (default: tag name)")
    args = ap.parse_args()

    if not tag_exists(args.tag):
        raise SystemExit(f"local tag does not exist: {args.tag}")

    archive = DIST_DIR / f"{args.tag}.7z"
    if not archive.exists():
        raise SystemExit(
            f"missing archive: {archive}\n"
            f"Run: python scripts/package_release.py --tag {args.tag}"
        )

    notes = PER_RELEASE_DOC_DIR / f"{args.tag}.md"
    if not notes.exists():
        raise SystemExit(f"missing release notes: {notes}")

    if args.for_real and not shutil.which("gh"):
        raise SystemExit("gh CLI not on PATH. Install via: winget install GitHub.cli")

    title = args.title or args.tag

    # Step 1: push tag to origin
    push_cmd = ["git", "push", "origin", args.tag]
    rc = run_or_print(push_cmd, args.for_real)
    if rc != 0:
        return rc

    # Step 2: create or update release
    if args.for_real and gh_release_exists(args.tag):
        upload_cmd = ["gh", "release", "upload", args.tag, str(archive), "--clobber"]
        return run_or_print(upload_cmd, args.for_real)

    create_cmd = [
        "gh", "release", "create", args.tag, str(archive),
        "--title", title,
        "--notes-file", str(notes),
    ]
    if args.prerelease:
        create_cmd.append("--prerelease")
    return run_or_print(create_cmd, args.for_real)


if __name__ == "__main__":
    raise SystemExit(main())
