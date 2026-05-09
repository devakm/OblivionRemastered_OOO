# Release process

End-to-end procedure for publishing a new alpha — or re-publishing an existing one. This is the runbook for **`alpha90`** once its fixup work is done, and for **every future alpha** after that.

## TL;DR

```powershell
# 0. regenerate the two SyncMap variants from the OOO_SyncGen Deluxe source
#    of truth and drop them into the alpha source folder. (See "Step 0" below.)
py -3 scripts/sync_syncmap.py --target "X:\games\Oscuro\Oscuro's_..._alphaNN"

# 1. ingest the source folder (idempotent: --force if you're re-doing an existing tag)
py -3 scripts/ingest_release.py "X:\games\Oscuro\Oscuro's_..._alphaNN" --force

# 2. push the new commit + the new tag
git push origin main
git push origin alphaNN

# 3. publish the GitHub Release with the .7z attached, marked Latest
py -3 scripts/publish_github.py --tag alphaNN --latest --for-real

# 4. regenerate the Pages staging files
py -3 scripts/sync_pages.py

# 5. review + commit + push the devnull repo (manual)
cd X:\dev\devnull
git add docs/OOO/OBR/
git commit -m "OBR: alphaNN release"
git push
```

---

## Step-by-step

### 0. Regenerate the SyncMap variants from the OOO_SyncGen source of truth

OOORS Full ships **two** SyncMap files inside every release:

| File in release | Audience |
|---|---|
| `…\Data\SyncMap\Oscuro's_Oblivion_Overhaul.ini` | Default — **non-Deluxe Edition** owners |
| `…\Data\OptionalPatches\SyncMap - DeluxeEdition\Oscuro's_Oblivion_Overhaul.ini` | **Deluxe Edition** owners |

The two files are derived from a single source of truth maintained outside this repo:

```
X:\mod-tools\OOO_SyncGen\SyncGen\Overrides\Oscuro's_Oblivion_Overhaul_Overrides.ini
```

That source IS the Deluxe variant — it uses Deluxe-DLC asset paths for the items that have a Deluxe analogue:

- `/Game/Forms/items/armor/DEA…` — Deluxe Armor "Order" set
- `/Game/Forms/items/armor/DEM…` — Deluxe Armor "Cataclysm" set
- `/Game/Forms/items/weapons/DEA…` — Deluxe weapons "Order" set
- `/Game/Forms/items/weapons/DEM…` — Deluxe weapons "Cataclysm" set

Each of those Deluxe entries has a commented-out non-Deluxe alternative directly above it. **`scripts/sync_syncmap.py`** reads that source and writes:

- The **Deluxe** target — verbatim copy of the source.
- The **default** target — same file with each Deluxe pair swapped (the previously-commented non-Deluxe line becomes active; the previously-active Deluxe line becomes commented).

```powershell
py -3 scripts/sync_syncmap.py --target "X:\games\Oscuro\Oscuro's_..._alphaNN"
```

Pair-swap rule (the "important restriction"): only triggered when the active line uses `/Game/Forms/items/armor/DEA…` or `/Game/Forms/items/armor/DEM…`. Other commented prose (header `; EditorID:` lines, prose notes, unrelated commented mappings) is left untouched.

Output stats look like:

```
[sync_syncmap]   18 Deluxe-active line(s) found
[sync_syncmap]   18 pair(s) swapped to non-Deluxe
```

If the script reports `Deluxe-active line(s) had no preceding alternative`, a Deluxe entry was added to the source without a commented-out non-Deluxe fallback — fix the source first (the missing fallback is what users without Deluxe will end up with).

**Important:** the target folder lives under `X:\games\Oscuro\` which the project's `restrict-path.py` hook flags as read-only. `sync_syncmap.py` itself is benign (it's just file I/O), but to actually run it against a source folder you'll need to invoke it **from your own shell**, not via a Claude tool call. Claude can dry-run the script with `--target work\_syncmap_test --dry-run` for verification, but should not write into the source folder directly.

To preview without modifying the source folder:

```powershell
py -3 scripts/sync_syncmap.py --target "work\_syncmap_test" --show-unmatched
diff "X:\mod-tools\OOO_SyncGen\SyncGen\Overrides\Oscuro's_Oblivion_Overhaul_Overrides.ini" "work\_syncmap_test\OblivionRemastered\Content\Dev\ObvData\Data\SyncMap\Oscuro's_Oblivion_Overhaul.ini"
```

### 1. Ingest the source folder

```powershell
py -3 scripts/ingest_release.py "X:\games\Oscuro\Oscuro's_Oblivion_Remastered_Shivering_Full_alphaNN"
```

What this does (in order):

- Hashes every file in the source folder → writes `manifests/alphaNN.json`.
- Diffs vs the previous tag's manifest → writes `docs/per-release/alphaNN.md`.
- Wipes `release/` and copies **only text files** (`.json`, `.ini`, `.lua`, `.md`, `.txt`, etc.) from the source folder into `release/`.
- Builds `dist/alphaNN.7z` from the **full** source folder (text + binary). Skips this step if `dist/alphaNN.7z` already exists — pass `--force` to rebuild.
- Stages `release/`, `manifests/`, `docs/per-release/` → commits → tags `alphaNN`.

**If the tag already exists** (you're re-publishing): pass `--force`. It will delete the old tag, rebuild the archive, and re-create the tag pointing at the new commit.

```powershell
py -3 scripts/ingest_release.py "X:\games\Oscuro\Oscuro's_..._alphaNN" --force
```

**If you only want to update the archive** without re-doing the commit (e.g. you blew away `dist/` by accident): use `package_release.py` standalone:

```powershell
py -3 scripts/package_release.py --source "X:\games\Oscuro\Oscuro's_..._alphaNN" --name alphaNN
```

### 2. Push the commit + tag

```powershell
git push origin main
git push origin alphaNN
```

If you're force-re-tagging an existing release (step 1 with `--force`), you also need:

```powershell
git push origin alphaNN --force
```

Force-push of a tag is acceptable here only because tags in this repo are 1:1 with releases — they don't get rebased. **Do not force-push `main`.**

### 3. Publish the GitHub Release

For a brand-new alpha that should become the displayed **Latest** release:

```powershell
py -3 scripts/publish_github.py --tag alphaNN --latest --for-real
```

`--latest` flips this release into the "Latest" slot on the Releases page. GitHub automatically demotes whatever was previously Latest to a regular release.

For an alpha that should be a historical / pre-release entry (e.g. backfilling an old version that's not the current build):

```powershell
py -3 scripts/publish_github.py --tag alphaNN --prerelease --for-real
```

Without `--for-real`, the script prints what it would do but doesn't call `gh`. Always dry-run first.

**If the release already exists** (you're re-publishing): the script detects this and runs `gh release upload <tag> dist/<tag>.7z --clobber` instead of `gh release create`, which replaces the asset on the existing release page.

### 4. Refresh Pages staging

```powershell
py -3 scripts/sync_pages.py
```

This rewrites `X:\dev\devnull\docs\OOO\OBR\{index,changelog,install,dependencies,overview}.html`. The new release shows up in the index and changelog automatically (script reads the live tag list).

### 5. Commit + push the devnull repo (manual)

`sync_pages.py` deliberately does not touch git in the devnull repo — review first, then commit:

```powershell
cd X:\dev\devnull
git status                        # should show docs/OOO/OBR/*.html modified
git diff docs/OOO/OBR/index.html  # eyeball the new release entry
git add docs/OOO/OBR/
git commit -m "OBR: publish alphaNN"
git push
```

GitHub Pages auto-rebuilds within ~1 minute. The new release is then visible at <https://devakm.github.io/devnull/docs/OOO/OBR/>.

---

## Special case: variant branches (`alpha32nex` and friends)

Variants live on `variants/<tagname>` branches off their parent tag. Their `docs/per-release/<tag>.md` is committed on that branch, NOT on `main`. So when you're checked out on `main` and try to publish a variant, the notes file isn't in your working tree.

`publish_github.py` falls back to `git show <tag>:docs/per-release/<tag>.md` automatically (introduced after the `alpha32nex` snag during the initial backfill publish). No manual action needed — but if you ever do this by hand:

```powershell
git show alpha32nex:docs/per-release/alpha32nex.md > work\_notes\alpha32nex.md
gh release create alpha32nex dist\alpha32nex.7z --title alpha32nex --notes-file work\_notes\alpha32nex.md --prerelease
```

Variants almost always get `--prerelease` since they're side-channels, not the main line.

To ingest a NEW variant (e.g. some future `alpha95nex`):

```powershell
git checkout -b variants/alpha95nex alpha95
py -3 scripts/ingest_release.py "X:\games\Oscuro\Oscuro's_..._alpha95nex"
git checkout main
```

(`backfill_history.py` does this automatically when run from scratch — it's only manual when you're adding one variant after the fact.)

---

## Latest vs Pre-release: who gets which flag

| Situation | Flag |
|-----------|------|
| New alpha just shipped, becomes the current build | `--latest` |
| Hot-fix re-issue of the current alpha | `--latest` (replaces existing) |
| Backfilling a historical alpha that pre-dates the current Latest | `--prerelease` |
| Variant branch (alpha32nex etc.) | `--prerelease` |
| Experimental side build for testers | `--prerelease` |

`--latest` and `--prerelease` are mutually exclusive in `gh release`. If you don't pass either, GitHub uses semver-ish heuristics, which can be surprising — be explicit.

---

## Common mistakes

| Mistake | Symptom | Fix |
|---------|---------|-----|
| Forgot to push the tag before `gh release create` | `gh` errors with "tag not found" | `git push origin <tag>` then retry |
| Force-pushed `main` instead of just the tag | History rewrite, anyone who cloned the repo will need to re-clone | Use `git push origin <tag> --force`, never `git push origin main --force` |
| Re-ran `ingest_release.py` without `--force` on an existing tag | Aborts with "tag already exists" | Add `--force` |
| Edited a file in `docs/`, `scripts/`, or `release/` mid-ingest | Ingest aborts with "working tree has uncommitted changes outside …" | Commit or stash unrelated edits first |
| Built `dist/<tag>.7z` from the wrong source | Manifest SHA-256s won't match the archive contents | Always ingest from the canonical `X:\games\Oscuro\Oscuro's_..._alphaNN` folder |
| Marked a backfill as `--latest` instead of `--prerelease` | GitHub now shows an old build as "Latest" | `gh release edit <tag> --prerelease` to demote |
| Ran `sync_pages.py` and then committed both repos in the wrong order | The devnull repo links to a tag that hasn't been pushed yet | Always: ingest → push tag → create Release → THEN sync_pages → THEN commit devnull |

---

## What to do for `alpha90` specifically

This is the procedure once `alpha90`'s fixup is done. (Right now `alpha90` exists as a tag and as a built `.7z`, but there is **no GitHub Release** for it yet — that was deliberately deferred.)

1. Apply your fixes to the source folder at `X:\games\Oscuro\Oscuro's_Oblivion_Remastered_Shivering_Full_alpha90\`.
2. Re-ingest with `--force` (overwrites the existing tag + commit + archive):
   ```powershell
   py -3 scripts/ingest_release.py "X:\games\Oscuro\Oscuro's_..._alpha90" --force
   ```
3. Push the new commit and force-push the tag:
   ```powershell
   git push origin main
   git push origin alpha90 --force
   ```
4. Publish as the new Latest:
   ```powershell
   py -3 scripts/publish_github.py --tag alpha90 --latest --for-real
   ```
5. Refresh + push Pages:
   ```powershell
   py -3 scripts/sync_pages.py
   cd X:\dev\devnull
   git add docs/OOO/OBR/
   git commit -m "OBR: publish alpha90 (current Latest)"
   git push
   ```

After this, `alpha90` will show with the green "Latest" badge on the Releases page; all 88 historical alphas remain marked Pre-release.
