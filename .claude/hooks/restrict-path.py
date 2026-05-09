#!/usr/bin/env python3
"""
Claude Code PreToolUse hook for the OblivionRemastered_OOO release tracker.

Model: deny-list, not allow-list. This project legitimately reads from
multiple roots (game install, source release folders, sister projects) and
writes to several roots (this repo, the devnull GitHub Pages repo).

Hard-blocked WRITES (any tool that writes to these paths is rejected):
  - C:\\games\\Steam\\steamapps\\common\\Oblivion Remastered\\  (game install)
  - X:\\games\\Oscuro\\                                         (source release folders)

For Bash commands, we look for *write-shaped* invocations (cp/mv/rm/Set-Content/etc.)
that target a denied root. Pure reads against denied roots are allowed.

For Write/Edit/MultiEdit/NotebookEdit, any file_path under a denied root is rejected.

Exit code 2 = hard block (Claude Code will not execute the tool).
Exit code 0 = allow.
"""

from __future__ import annotations

import json
import re
import sys

# Roots that must NEVER be written to. Lowercase, normalised to backslashes.
DENY_WRITE_ROOTS = (
    r"c:\games\steam\steamapps\common\oblivion remastered",
    r"x:\games\oscuro",
)

# Bash / PowerShell verbs that indicate a write. If any of these appear in a
# command alongside a denied path, the command is blocked.
WRITE_VERB_PATTERNS = (
    re.compile(r"\b(cp|mv|rm|tee|dd|touch|mkdir|rmdir|chmod|chown|ln)\b", re.IGNORECASE),
    re.compile(r"\b(xcopy|robocopy|move|del|erase|ren|attrib|takeown|icacls)\b", re.IGNORECASE),
    re.compile(r"\b(Copy-Item|Move-Item|Remove-Item|New-Item|Rename-Item)\b"),
    re.compile(r"\b(Set-Content|Add-Content|Out-File|Set-Acl)\b"),
    # Shell redirect: `>` or `>>` not preceded by `-`/`=` (so `->`, `=>`, and
    # `2>&1`-style fd dupes don't match) followed by space + target token.
    re.compile(r"(?<![-=])>>?\s+\S"),
    re.compile(r"\|\s*tee\b", re.IGNORECASE),
)


def normalise(path: str) -> str:
    """Return a canonical lowercase backslash form for path comparison."""
    s = path.strip().strip("\"'")
    s = s.replace("/", "\\").lower()
    # Convert /x/foo (Git Bash) to x:\foo
    if len(s) >= 3 and s[0] == "\\" and s[2] == "\\":
        drive = s[1]
        rest = s[3:]
        s = f"{drive}:\\{rest}"
    return s


def under_denied_root(path: str) -> str | None:
    """If `path` lies under a denied root, return that root; else None."""
    n = normalise(path)
    for root in DENY_WRITE_ROOTS:
        if n.startswith(root):
            return root
    return None


_PATH_RE = re.compile(r'[A-Za-z]:[\\/][^\s"\'`|;&<>\n]+')
_GITBASH_PATH_RE = re.compile(r'/[a-zA-Z]/[^\s"\'`|;&<>\n]+')


def find_paths(text: str) -> list[str]:
    out = list(_PATH_RE.findall(text))
    out.extend(_GITBASH_PATH_RE.findall(text))
    return out


def looks_like_write(cmd: str) -> bool:
    return any(p.search(cmd) for p in WRITE_VERB_PATTERNS)


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    tool_name = data.get("tool_name", "")
    tool_input = data.get("tool_input", {})
    reason: str | None = None

    if tool_name == "Bash":
        cmd = tool_input.get("command", "")
        if looks_like_write(cmd):
            for path in find_paths(cmd):
                root = under_denied_root(path)
                if root:
                    reason = (
                        f"command appears to write to a deny-listed root ({root}). "
                        f"Offending path in command: {path}"
                    )
                    break

    elif tool_name in ("Write", "Edit", "MultiEdit", "NotebookEdit"):
        fp = tool_input.get("file_path", "")
        root = under_denied_root(fp)
        if root:
            reason = f"file path lies under deny-listed root ({root}): {fp}"

    if reason:
        print(f"[restrict-path] BLOCKED: {reason}", file=sys.stderr)
        sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
