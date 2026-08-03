# Crash-debugging tooling: dedicated repo + RAX traceability

**Date:** 2026-08-03
**Status:** Approved design, pending implementation plan

## Problem

Crash-debugging capability for Oblivion Remastered mods is scattered across three
repos and two machine-local stores, with no single owner:

| What | Where it lives today | Problem |
|------|---------------------|---------|
| `analyze_crashdump.py`, `check_crashes.py` | `OblivionRemastered_MapClone/` | Used to debug **OOO** and **RAX** crashes, but owned by the map-cloning repo |
| Crash signatures, workflows, hard-won limits | Claude per-project memory files | Machine-local, not version-controlled, not shareable, not reviewable |
| Engine/tool domain knowledge | `~/.claude/skills/oblivion-remastered-modding/` | Same — personal, outside git |
| RAX build identity | nowhere | The deployed `main.dll` cannot be traced to a source commit |

The RAX gap is not hypothetical. During the 2026-08-02 Fort Nikel investigation,
RAX source was analyzed at length with **no way to confirm the running
`main.dll` (dated 2025-08-30) was built from it**, and the alpha tester's copy was
a third, separately unverifiable binary.

## Goals

1. One home for crash-debugging tools and knowledge, owned by no single mod project.
2. Knowledge that is version-controlled, reviewable, and auto-loads into any repo.
3. Any RAX binary in a dump or log identifies its exact source commit.

## Non-goals

- **Allocator-validation feature in RAX.** Instrumenting UE's binned pools from a
  DLL is a genuine research task and gets its own spec once RAX is trackable.
- **Storing crash dumps.** See "No dumps" below.
- Refactoring MapClone or OOO beyond updating pointers to the moved tools.

## Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Tool home | New repo `X:\dev\OblivionRemastered_CrashTools` | Debugging is cross-cutting; matches `OblivionRemastered_<Thing>` convention |
| Contents | Tools + knowledge, **no dumps** | Dumps carry tester PII (Windows username, machine GUID, `LoginId`, save names, Steam paths) and are large (49 MB for one UE4SS dump) |
| Knowledge form | Skill in repo, deployed to `~/.claude/skills/` | Version-controlled source of truth that still auto-triggers in every repo |
| Migration | Preserve git history | Keeps authorship and evolution of the three tool commits |
| Visibility | Private for now | Flip to public later once the no-dumps discipline is proven |
| RAX scope | Traceability only | Version stamping is itself a debugging concern; the allocator feature is separate |

## Architecture

```
OblivionRemastered_CrashTools/
├── CLAUDE.md                     # repo rules; inherits X:\dev\CLAUDE.md
├── README.md                     # what this is, quickstart
├── .gitignore                    # work/, *.dmp, *.7z, __pycache__
├── tools/
│   ├── analyze_crashdump.py      # deep single-dump analysis
│   ├── check_crashes.py          # recent-crash triage
│   └── requirements.txt          # capstone
├── skill/
│   └── obr-crash-forensics/
│       └── SKILL.md              # deployed to ~/.claude/skills/
├── docs/
│   ├── crash-signatures.md       # catalog of known crash sites
│   └── debugging-workflow.md     # workflow + limits of each technique
├── scripts/
│   └── deploy_skill.ps1          # idempotent copy → ~/.claude/skills/
└── work/                         # gitignored: dumps, scratch
```

### Component: `tools/`

`analyze_crashdump.py` moves unchanged in behavior. Two adjustments:

- `check_crashes.py`'s hardcoded `CRASH_DIR = X:\games\OBR_CrashDumps` becomes a
  `--dir` argument defaulting to that path, so tester-supplied dumps
  (e.g. `X:\tmp\crashlogs`) work without editing the script.
- Default paths that point into sibling repos (`DEFAULT_RECORDS_DIR`,
  `DEFAULT_SYNCMAP`) stay as defaults but are already CLI-overridable. They are
  the one accepted coupling: the FormID lookup is OOO-specific by nature.

`KNOWN_CRASH_SITES` stays **in code** (it is executable data, keyed by faulting
RVA). `docs/crash-signatures.md` is the human-readable expansion, not a
duplicate: it explains mechanism, evidence, and how to add a new entry.

### Component: `skill/obr-crash-forensics/SKILL.md`

Auto-triggers on crash-dump work in any repo. Contents:

- When to reach for triage vs deep analysis.
- The three known signatures (summary + pointer to `docs/crash-signatures.md`).
- The analysis workflow.
- **Technique limits** — the expensive lessons, stated as rules:
  - `pcall` does not catch native access violations in UE4SS Lua hooks.
  - PageHeap/AppVerifier cannot see UE's binned pools; this shipping build
    strips `-ansimalloc`/`-stompmalloc`, so there is no way to route UE
    allocations onto the NT heap.
  - Bisection results are unreliable for heap corruption — removing any object
    perturbs allocation layout and can mask a bug without fixing it.
  - Lua mods never appear in minidump module lists; enumerate
    `ue4ss\Mods\*\enabled.txt` separately.

### Component: `scripts/deploy_skill.ps1`

Copies `skill/obr-crash-forensics/` → `~/.claude/skills/obr-crash-forensics/`.
Copy rather than symlink: symlink creation is blocked on this machine without
developer mode. Idempotent; safe to re-run after every skill edit. Deploying is
a manual step, documented in `README.md` and `CLAUDE.md`.

### Component: `docs/`

- `crash-signatures.md` — one section per known crash site: faulting RVA, game
  build, mechanism, what evidence identifies it, whether a FormID is
  recoverable, and first-seen date. Seeded from the existing memory files.
- `debugging-workflow.md` — triage → deep analysis → attribution, plus the
  technique-limits table above in long form.

## Migration plan

1. Create the new repo with history preserved for `analyze_crashdump.py` and
   `check_crashes.py` (git subtree/filter-repo from MapClone), then restructure
   into `tools/`.
2. Remove both tools from MapClone; replace the `CLAUDE.md` crash-dumps row with
   a pointer to the new repo.
3. Port the four crash memory files into `docs/crash-signatures.md`; reduce the
   memory entries to thin pointers.
4. Author `SKILL.md`; deploy it; verify it triggers.

Migration is complete when analyzing an existing dump from the new repo
reproduces the same output as before the move.

## RAX traceability

Three changes to `X:\dev\RAX` (currently: one "Initial import" commit, no
`CLAUDE.md`, no version stamping; `.gitignore` and remote are already correct):

1. **`CLAUDE.md`** — build commands (`build_release.ps1` / `build_debug.ps1`),
   deploy target, game-folder-read-only rule, no-binaries-in-git rule. Inherits
   the workspace-root merge and commit-authorship rules.
2. **Version stamping** — the build generates `version.generated.h` containing
   the git short SHA and a dirty flag; `mod_main` logs `[RAX] build <sha>` at
   init so it lands in `UE4SS.log`. Generated header is gitignored.
3. **Commit discipline** — real commits per change from here on.

Verification: build RAX, launch, confirm `[RAX] build <sha>` appears in
`UE4SS.log` and matches `git rev-parse --short HEAD`.

## Risks

| Risk | Mitigation |
|------|-----------|
| A dump is committed by accident, leaking tester PII | `.gitignore` excludes `*.dmp`; repo starts private; no-dumps rule stated in `CLAUDE.md` |
| Deployed skill drifts from repo source | Deploy script is idempotent and documented; re-run after edits |
| History-preserving migration is fiddly | If `filter-repo` proves troublesome, fall back to copy + provenance note — history remains visible in MapClone's log |
| Tools break after the move (path assumptions) | Migration is not complete until an existing dump re-analyzes identically |

## Open follow-ups (not this spec)

- RAX allocator-validation feature — own spec.
- Whether `RE-UE4SS` should become a submodule rather than 2,959 vendored files.
- Whether to flip the repo public.
