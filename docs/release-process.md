# Release process

End-to-end procedure for publishing a new alpha — or re-publishing an existing one. This is the v2 runbook (current architecture). For the architecture rationale see [`v2-design.md`](v2-design.md).

## TL;DR

```powershell
# 1. Edit release/ in place. Drop new binaries (paks, ESPs, DLLs) into the
#    correct release/OblivionRemastered/... paths. Update text files (JSON,
#    INI, Lua, etc.) directly. The repo is the staging tree.

# 2. Cut the release end-to-end (regenerates SyncMap, hashes, parses ESPs,
#    updates co-files, writes per-release diff doc, commits, tags, packages,
#    pushes, creates the GitHub Release).
py -3 scripts/release.py alphaNN --latest --for-real

# 3. Refresh the GitHub Pages staging.
py -3 scripts/sync_pages.py

# 4. Review + commit + push the devnull Pages repo (manual).
cd X:\dev\devnull
git add docs/OOO/OBR/
git commit -m "OBR: alphaNN release"
git push
```

---

## What `release.py` does, step by step

When you run `py -3 scripts/release.py alphaNN --latest --for-real`, in order:

| # | Step | Output |
|---|------|--------|
| 0 | **Check SyncMap drift** via `sync_syncmap.py diff-check`. Reads OOO_SyncGen source, compares to `release/`'s two SyncMap files. If drift detected: aborts with "review with `diff-show`, then re-run with `--syncmap-fix-approved`." If `--syncmap-fix-approved` is set: invokes `sync_syncmap.py diff-fix` to regenerate. | Drift report on stderr; possibly updates `release/OblivionRemastered/Content/Dev/ObvData/Data/SyncMap/...` and `.../OptionalPatches/SyncMap - DeluxeEdition/...`. |
| 1 | Validate working tree — no uncommitted changes outside `release/`, `manifests/`, `docs/per-release/`. Aborts if the tag already exists (unless `--force`). | (no output if clean) |
| 2 | Hash every file in `release/` (text + gitignored binaries; skips `*.md` co-files and `*.records/` directories). | `manifests/alphaNN.json` |
| 3 | Parse every ESP/ESM in `release/` via Wrye Bash. | `<esp>.records/_meta.json` + `<esp>.records/<TYPE>.json` for each record type. |
| 4 | For every binary in `release/`, append (or replace) its row in the sibling `<binary>.md` co-file with this tag's SHA + size + GitHub URLs. The `★` marker on each row is recomputed pairwise so it stays correct. | `<binary>.md` updated. |
| 5 | Diff vs the previous tag's manifest + `.records/` bundles. File-level changes (added / removed / changed paths) plus per-ESP content diff (added / removed / changed records, with leveled-list entry detail and cell ref-count deltas). | `docs/per-release/alphaNN.md` |
| 6 | `git add -A release/ manifests/ docs/per-release/`, commit (subject = `alphaNN`), tag. | new commit on `main`, tag `alphaNN`. |
| 7 | Build `dist/alphaNN.7z` from `release/` EXCLUDING `*.md` co-files and `*.records/` directories. | `dist/alphaNN.7z` |
| 8 | (`--for-real` only) `git push origin main`, `git push origin alphaNN`, `gh release create alphaNN dist/alphaNN.7z --title alphaNN --notes-file docs/per-release/alphaNN.md --latest`. | New GitHub Release attached to `alphaNN`. |

Without `--for-real` step 8 is printed but not executed. Always **dry-run first** with `--for-real` omitted to confirm the plan.

## Common patterns

### Brand-new alpha, becomes the current build

```powershell
py -3 scripts/release.py alpha91 --latest --for-real
```

`--latest` flips the new release into the displayed Latest slot on the GitHub Releases page (auto-demoting whatever was previously Latest to a regular release).

### Backfilling an old alpha that pre-dates the current Latest

```powershell
py -3 scripts/release.py alpha75-fixup --prerelease --for-real
```

`--prerelease` keeps GitHub from auto-promoting it to Latest.

### Re-running an already-tagged release (e.g. after a bug fix)

```powershell
py -3 scripts/release.py alphaNN --latest --for-real --force
```

`--force` deletes the local tag, re-runs the pipeline, re-creates the tag at the new commit. Step 8 then force-pushes the tag and uses `gh release upload --clobber` to replace the asset.

### Local-only dry build (no push, no GitHub Release)

```powershell
py -3 scripts/release.py alphaNN
```

No `--for-real` — produces commit + tag + `dist/alphaNN.7z` locally, then prints what step 8 *would* do. Inspect `dist/alphaNN.7z` before deciding to publish.

### Plan-only inspection (no FS or git changes)

```powershell
py -3 scripts/release.py alphaNN --dry-run
```

Walks every step and prints what it would do. Useful for sanity-checking before a real run.

---

## Variants (`alpha32nex`-style branches)

Variants live on `variants/<tag>` branches off their parent tag. To ingest a new variant:

```powershell
git checkout -b variants/alpha95nex alpha95
py -3 scripts/release.py alpha95nex --prerelease --for-real
git checkout main
```

`publish_github.py` (which `release.py` invokes internally for step 8) automatically falls back to `git show <tag>:docs/per-release/<tag>.md` when the notes file isn't in the working tree — so variant branches that don't have other tags' notes locally work without manual intervention.

---

## Latest vs Pre-release

| Situation | Flag |
|-----------|------|
| New alpha just shipped, becomes the current build | `--latest` |
| Hot-fix re-issue of the current alpha | `--latest` (replaces existing) |
| Backfilling a historical alpha that pre-dates the current Latest | `--prerelease` |
| Variant branch (`alpha32nex` etc.) | `--prerelease` |
| Experimental side build for testers | `--prerelease` |

`--latest` and `--prerelease` are mutually exclusive in `gh release`. Always pass one or the other; otherwise GitHub picks based on tag ordering, which can be surprising.

---

## Skipping steps for special cases

| Flag | When to use |
|------|-------------|
| `--skip-syncmap` | Skip the SyncMap drift check entirely. Use only when you're sure (e.g. you've manually managed both files and don't want any check). Most of the time you don't want this — the drift check is read-only and harmless. |
| `--syncmap-fix-approved` | If the drift check reports drift, apply `sync_syncmap.py diff-fix` and continue (instead of aborting). You should have inspected the drift via `sync_syncmap.py diff-show` first. Without this flag, drift halts the release. |
| `--skip-records` | You want to skip parsing ESPs entirely (e.g. the Wrye Bash checkout is broken and you want to ship anyway). The release will lack the per-ESP content diff in its notes; everything else still runs. |

---

## Refreshing the GitHub Pages site

`scripts/sync_pages.py` writes HTML into `X:\dev\devnull\docs\OOO\OBR\`. It does NOT commit or push the devnull repo — review first, then commit manually:

```powershell
py -3 scripts/sync_pages.py

cd X:\dev\devnull
git status                        # should show docs/OOO/OBR/*.html modified
git diff docs/OOO/OBR/index.html  # eyeball the new release entry
git add docs/OOO/OBR/
git commit -m "OBR: publish alphaNN"
git push
```

GitHub Pages auto-rebuilds within ~1 minute. The new release is then visible at <https://devakm.github.io/devnull/docs/OOO/OBR/>.

---

## Fetching a historical binary

For testing or comparison — pull a binary that shipped with a specific past release without downloading the whole `.7z` manually:

```powershell
# fetch one specific binary for a specific tag, default dest = work/historical/<tag>/...
py -3 scripts/fetch_binary.py --tag alpha75 release/.../Oscuro's_Oblivion_Overhaul.esp

# fetch every binary that has a .md co-file row for a tag
py -3 scripts/fetch_binary.py --tag alpha75 --all

# show what would be fetched, no downloads
py -3 scripts/fetch_binary.py --tag alpha75 --all --list

# fetch and overwrite the working-tree binary in place
py -3 scripts/fetch_binary.py --tag alpha75 release/.../Foo.pak --into-place
```

The `.7z` is cached at `work/_release_cache/<tag>.7z` so multiple fetches per tag re-use one download. SHA-256 is verified against the `.md` co-file's recorded value; mismatch aborts loudly.

---

## Common mistakes

| Mistake | Symptom | Fix |
|---------|---------|-----|
| Forgot to drop a binary into `release/` before running release.py | Binary's `.md` co-file gets no new row, archive missing the file | Drop the binary in, re-run with `--force` |
| Edited a tracked file in another part of the repo mid-release | release.py aborts: "working tree has uncommitted changes outside …" | Commit or stash unrelated edits first |
| Re-ran release.py without `--force` on an existing tag | Aborts: "tag X already exists" | Add `--force` |
| Force-pushed `main` instead of just the tag | Rewrites public history; collaborators have to re-clone | Use `git push origin <tag> --force-with-lease`, never `git push origin main --force` casually |
| Built `dist/<tag>.7z` from the wrong release/ contents | Manifest SHAs won't match the archive bytes | release.py builds atomically from current release/; always run as a single command, don't manually splice |
| Marked an old backfill as `--latest` instead of `--prerelease` | GitHub now shows an old build as "Latest" | `gh release edit <tag> --prerelease` to demote, then re-run release.py for the actual current with `--latest` |
| Ran `sync_pages.py` and pushed devnull before pushing the OOORS repo's tag | Pages links to a tag that doesn't exist on origin yet | Always: `release.py --for-real` (which pushes tag) → THEN `sync_pages.py` → THEN commit/push devnull |
