#!/usr/bin/env python3
"""
Render the release tracker's index, changelog, and install pages as HTML and
write them into the devnull GitHub Pages repo at:

    X:\\dev\\devnull\\docs\\OOO\\OBR\\

The script DOES NOT commit, push, or otherwise touch git in the devnull repo.
It only writes files. The user is expected to review, then commit and push
manually.

Pages produced:
  - index.html        — landing page with current latest release + download +
                        link to GitHub Releases archive of all historical builds
  - changelog.html    — rolling per-release diff summary, latest first
  - install.html      — install instructions (drawn from docs/installation.md)
  - dependencies.html — dependency reference (drawn from docs/dependencies.md)
  - overview.html     — what OOORS Full is (drawn from docs/overview.md)

All pages link back to <https://github.com/devakm/OblivionRemastered_OOO/releases>
for the actual `.7z` downloads.

Usage:
    python scripts/sync_pages.py                   # DIFF only (writes nothing) - DEFAULT
    python scripts/sync_pages.py --apply           # write pages, skipping DO-NOT-REGENERATE files
    python scripts/sync_pages.py --apply --max-changelog 20
"""

from __future__ import annotations

import argparse
import html
import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFEST_DIR = REPO_ROOT / "manifests"
PER_RELEASE_DOC_DIR = REPO_ROOT / "docs" / "per-release"
DOCS_DIR = REPO_ROOT / "docs"

PAGES_DEST = Path(r"X:/dev/devnull/docs/OOO/OBR")
GITHUB_REPO = "devakm/OblivionRemastered_OOO"
GITHUB_RELEASES_URL = f"https://github.com/{GITHUB_REPO}/releases"

# CSS path is relative to docs/OOO/OBR/, so it goes up two folders.
CSS_HREF = "../../css/devnull-shared.css"

REGEN_MARKER = "DO-NOT-REGENERATE"


def should_skip(dest: Path) -> bool:
    """True if the destination is hand-canonical and must not be overwritten."""
    if not dest.exists():
        return False
    return REGEN_MARKER in dest.read_text(encoding="utf-8", errors="replace")


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=REPO_ROOT, capture_output=True, text=True, check=check)


def list_main_line_tags() -> list[str]:
    """Return all alpha tags reachable from main, sorted oldest → newest."""
    r = git("tag", "--merged", "main", "--sort=v:refname")
    out = []
    for line in r.stdout.splitlines():
        line = line.strip()
        if line:
            out.append(line)
    return out


def latest_main_tag() -> str | None:
    tags = list_main_line_tags()
    return tags[-1] if tags else None


def load_manifest(name: str) -> dict[str, dict[str, object]]:
    p = MANIFEST_DIR / f"{name}.json"
    if not p.exists():
        return {}
    with p.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def total_size(manifest: dict[str, dict[str, object]]) -> int:
    total = 0
    for entry in manifest.values():
        s = entry.get("size", 0)
        assert isinstance(s, int)
        total += s
    return total


def human_size(n: int) -> str:
    f = float(n)
    for unit in ("B", "KiB", "MiB", "GiB"):
        if f < 1024:
            return f"{f:.1f} {unit}" if unit != "B" else f"{int(f)} B"
        f /= 1024
    return f"{f:.1f} TiB"


def md_to_simple_html(md: str) -> str:
    """Markdown -> HTML for our per-release docs and handwritten docs/*.md.
    Supports headings, lists, paragraphs, code spans, links, bold, italic,
    fenced code blocks, and pipe tables. External (http/https) links get
    target=_blank rel=noopener. NOT a general-purpose Markdown renderer."""
    lines = md.splitlines()
    out: list[str] = []
    in_ul = False
    i = 0
    n = len(lines)

    def flush_ul():
        nonlocal in_ul
        if in_ul:
            out.append("</ul>")
            in_ul = False

    def render_inline(s: str) -> str:
        s = html.escape(s)
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", s)

        def link_sub(m: "re.Match[str]") -> str:
            text, url = m.group(1), m.group(2)
            if url.startswith(("http://", "https://")):
                return f'<a href="{url}" target="_blank" rel="noopener">{text}</a>'
            return f'<a href="{url}">{text}</a>'

        return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link_sub, s)

    def is_table_sep(s: str) -> bool:
        return bool(re.match(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$", s))

    def split_row(s: str) -> list[str]:
        s = s.strip()
        if s.startswith("|"):
            s = s[1:]
        if s.endswith("|"):
            s = s[:-1]
        return [c.strip() for c in s.split("|")]

    while i < n:
        line = lines[i]

        if re.match(r"^```(\S*)\s*$", line):
            flush_ul()
            code_lines: list[str] = []
            i += 1
            while i < n and not re.match(r"^```\s*$", lines[i]):
                code_lines.append(lines[i])
                i += 1
            i += 1  # skip the closing fence
            out.append(f"<pre><code>{html.escape('\n'.join(code_lines))}</code></pre>")
            continue

        if line.lstrip().startswith("|") and i + 1 < n and is_table_sep(lines[i + 1]):
            flush_ul()
            headers = split_row(line)
            i += 2  # consume header + separator
            rows: list[list[str]] = []
            # Body rows run until a non-pipe line. Two adjacent tables must be
            # separated by a blank line, or the second is absorbed into the first.
            while i < n and lines[i].lstrip().startswith("|"):
                rows.append(split_row(lines[i]))
                i += 1
            thead = "".join(f"<th>{render_inline(h)}</th>" for h in headers)
            tbody = "".join(
                "<tr>" + "".join(f"<td>{render_inline(c)}</td>" for c in row) + "</tr>"
                for row in rows
            )
            out.append(f"<table><thead><tr>{thead}</tr></thead><tbody>{tbody}</tbody></table>")
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            flush_ul()
            level = len(m.group(1))
            out.append(f"<h{level}>{render_inline(m.group(2))}</h{level}>")
            i += 1
            continue

        if line.startswith("- "):
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{render_inline(line[2:])}</li>")
            i += 1
            continue

        if line.strip() == "":
            flush_ul()
            out.append("")
            i += 1
            continue

        flush_ul()
        out.append(f"<p>{render_inline(line)}</p>")
        i += 1

    flush_ul()
    return "\n".join(out)


def page_shell(title: str, body_html: str, active_nav: str = "") -> str:
    nav_links = [
        ("index.html", "Home"),
        ("overview.html", "Overview"),
        ("new-Items.html", "New Items"),
        ("changelog.html", "Changelog"),
        ("install.html", "Install"),
        ("dependencies.html", "Dependencies"),
    ]
    nav_html = " | ".join(
        f'<a href="{href}"{" class=\"highlight-text\"" if name == active_nav else ""}>{name}</a>'
        for href, name in nav_links
    )
    nav_html += f' | <a href="{GITHUB_RELEASES_URL}">Downloads (GitHub Releases)</a>'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" href="{CSS_HREF}">
</head>
<body>
  <div class="container">
    <header>
      <h1>Oscuro's Oblivion Overhaul Remastered FULL (OOORF)</h1>
      <p class="subtitle">Release Tracker</p>
    </header>
    <nav>{nav_html}</nav>
    {body_html}
    <footer>
      <p>Source: <a href="https://github.com/{GITHUB_REPO}">github.com/{GITHUB_REPO}</a> · Releases: <a href="{GITHUB_RELEASES_URL}">GitHub Releases</a></p>
    </footer>
  </div>
</body>
</html>
"""


def render_index(latest_tag: str, all_tags: list[str]) -> str:
    latest_manifest = load_manifest(latest_tag)
    file_count = len(latest_manifest)
    total_bytes = total_size(latest_manifest)

    body = f"""
    <div class="update">
      <p><span class="date">Latest:</span> <strong>{html.escape(latest_tag)}</strong> · {file_count} files · {human_size(total_bytes)} total</p>
      <p><a href="{GITHUB_RELEASES_URL}/tag/{html.escape(latest_tag)}">Download {html.escape(latest_tag)}.7z</a> · <a href="changelog.html#{html.escape(latest_tag)}">What changed</a></p>
    </div>

    <h2>About this site</h2>
    <p>Every alpha / beta / release build of <strong>Oscuro's Oblivion Overhaul Remastered FULL</strong> is tracked in the
       <a href="https://github.com/{GITHUB_REPO}">OblivionRemastered_OOO</a> repo, with a per-release manifest of every file
       (SHA-256 + size) so you can see exactly what changed between any two builds. Install archives are published as
       <a href="{GITHUB_RELEASES_URL}">GitHub Releases</a>.</p>

    <h2>Quick links</h2>
    <ul>
      <li><a href="install.html">Install instructions</a> for the latest release</li>
      <li><a href="dependencies.html">Required dependencies</a> (OBSE, UE4SS, MagicLoader, etc.)</li>
      <li><a href="changelog.html">Full changelog</a> ({len(all_tags)} releases)</li>
      <li><a href="overview.html">What OOORS Full bundles</a></li>
    </ul>

    <h2>All releases</h2>
    <p>Listed newest first. Each links to its GitHub Release page (with download) and its diff summary.</p>
    <ul>
"""
    for tag in reversed(all_tags):
        body += (
            f'      <li><a href="{GITHUB_RELEASES_URL}/tag/{html.escape(tag)}">{html.escape(tag)}</a> · '
            f'<a href="changelog.html#{html.escape(tag)}">changes</a></li>\n'
        )
    body += "    </ul>\n"

    return page_shell("OOORS Full — Release Tracker", body, active_nav="Home")


def render_changelog(all_tags: list[str], max_entries: int) -> str:
    body = "<h2>Per-release changes</h2>\n"
    body += "<p>Newest first. Click a release name in the index to jump to it.</p>\n"

    tags_to_show = list(reversed(all_tags))
    if max_entries > 0:
        tags_to_show = tags_to_show[:max_entries]

    for tag in tags_to_show:
        doc_path = PER_RELEASE_DOC_DIR / f"{tag}.md"
        body += f'<hr><h2 id="{html.escape(tag)}">{html.escape(tag)}</h2>\n'
        body += f'<p><a href="{GITHUB_RELEASES_URL}/tag/{html.escape(tag)}">Download</a></p>\n'
        if not doc_path.exists():
            body += f'<p><em>No diff doc for {html.escape(tag)}.</em></p>\n'
            continue
        md = doc_path.read_text(encoding="utf-8")
        # Strip the top-level h1 from the per-release doc since we render our own h2 above.
        md = re.sub(r"^#\s+.*\n", "", md, count=1)
        body += md_to_simple_html(md)

    return page_shell("OOORS Full — Changelog", body, active_nav="Changelog")


def render_doc_page(slug: str, nav_label: str, title_suffix: str) -> str:
    src = DOCS_DIR / f"{slug}.md"
    if not src.exists():
        body = f"<p><em>{slug}.md not found in repo docs/. Add it to populate this page.</em></p>"
    else:
        body = md_to_simple_html(src.read_text(encoding="utf-8"))
    return page_shell(f"OOORS Full — {title_suffix}", body, active_nav=nav_label)


def main() -> int:
    import difflib

    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true",
                    help="write pages (skips any file containing the DO-NOT-REGENERATE "
                         "marker); default is diff-only, writes nothing")
    ap.add_argument("--max-changelog", type=int, default=0,
                    help="cap the changelog to N most-recent releases (0 = all)")
    args = ap.parse_args()

    all_tags = list_main_line_tags()
    if not all_tags:
        raise SystemExit("no main-line tags found in repo. Run backfill_history.py first.")
    latest = all_tags[-1]
    print(f"[sync_pages] {len(all_tags)} tags, latest = {latest}", file=sys.stderr)

    pages = {
        "index.html": render_index(latest, all_tags),
        "changelog.html": render_changelog(all_tags, args.max_changelog),
        "install.html": render_doc_page("installation", "Install", "Install"),
        "dependencies.html": render_doc_page("dependencies", "Dependencies", "Dependencies"),
        "overview.html": render_doc_page("overview", "Overview", "Overview"),
    }

    if not args.apply:
        any_diff = False
        for name, content in pages.items():
            dest = PAGES_DEST / name
            current = dest.read_text(encoding="utf-8", errors="replace") if dest.exists() else ""
            diff = "".join(difflib.unified_diff(
                current.splitlines(keepends=True),
                content.splitlines(keepends=True),
                fromfile=f"a/{name}", tofile=f"b/{name}",
            ))
            if diff:
                any_diff = True
                marked = " [DO-NOT-REGENERATE - would be skipped by --apply]" if should_skip(dest) else ""
                print(f"\n===== {name}{marked} =====")
                print(diff)
        if not any_diff:
            print("[sync_pages] no differences against the live pages.", file=sys.stderr)
        print("[sync_pages] diff-only (default). Re-run with --apply to write UNMARKED files.",
              file=sys.stderr)
        return 0

    PAGES_DEST.mkdir(parents=True, exist_ok=True)
    for name, content in pages.items():
        dest = PAGES_DEST / name
        if should_skip(dest):
            print(f"[sync_pages] SKIP {dest} (DO-NOT-REGENERATE marker present)", file=sys.stderr)
            continue
        dest.write_text(content, encoding="utf-8")
        print(f"[sync_pages] wrote {dest} ({len(content)} bytes)", file=sys.stderr)

    print(f"[sync_pages] done. Review under {PAGES_DEST}, then commit + push the devnull repo.",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
