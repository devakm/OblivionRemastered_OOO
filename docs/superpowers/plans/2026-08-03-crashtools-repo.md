# Crash-Debugging Tooling Repo + RAX Traceability Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Move crash-debugging tools and knowledge into a dedicated private repo with preserved git history, package the knowledge as an auto-loading skill, and make any deployed RAX binary traceable to its source commit.

**Architecture:** A new repo `X:\dev\OblivionRemastered_CrashTools` holds the two Python tools (migrated with `git filter-repo` so their history survives), a `docs/` signature catalog seeded from Claude memory files, and a `skill/` directory deployed by copy into `~/.claude/skills/`. Separately, RAX gains a `CLAUDE.md` and a generated version header so `[RAX] build <sha>` appears in `UE4SS.log`.

**Tech Stack:** Python 3.12 + capstone, git 2.52 + git-filter-repo 2.47, PowerShell 5.1, xmake/C++20 (RAX).

## Global Constraints

- **No dumps in the repo.** `*.dmp` is gitignored. Dumps carry tester PII (Windows username, machine GUID, `LoginId`, save names, Steam paths).
- **Game folder is READ-ONLY.** `C:\games\Steam\steamapps\common\Oblivion Remastered\` — read only, never write. Hook-enforced in other repos; state it in the new `CLAUDE.md` files.
- **Never write a `Co-Authored-By: Claude` trailer or "Generated with Claude Code" line** in any commit message. Inherited from `X:\dev\CLAUDE.md`.
- **Merges must create a merge commit** (`merge.ff = false`); never pass `--ff`/`--ff-only`.
- Repo name is exactly `OblivionRemastered_CrashTools`; skill name is exactly `obr-crash-forensics`.
- Task groups A (tasks 1–6) and B (tasks 7–8) are independent and may be executed and reviewed separately.

---

### Task 1: Capture baseline, then create the repo with preserved history

Migration is only correct if the tools behave identically afterward. Capture the "before" output first — it is the regression test for Task 2.

**Files:**
- Create: `C:\Users\aubre\AppData\Local\Temp\claude\baseline_analyze.txt` (scratch, not committed)
- Create: `X:\dev\OblivionRemastered_CrashTools\` (via clone + filter)

**Interfaces:**
- Produces: a git repo at `X:\dev\OblivionRemastered_CrashTools` containing `tools/analyze_crashdump.py` and `tools/check_crashes.py` with their original commit history.

- [ ] **Step 1: Capture the baseline output of the current tool**

```bash
cd /x/dev/OblivionRemastered_MapClone
py -3 analyze_crashdump.py "X:\tmp\crashlogs\UECC-Windows-156F45DC489F75522E51998F693A866F_0000" 2>/dev/null > "C:\Users\aubre\AppData\Local\Temp\claude\baseline_analyze.txt"
wc -l "C:\Users\aubre\AppData\Local\Temp\claude\baseline_analyze.txt"
```

Expected: a non-empty file (~120 lines) containing `zOOOHaplessVictim01` and `KNOWN CRASH SITE`.

- [ ] **Step 2: Verify the baseline is meaningful**

```bash
grep -c "zOOOHaplessVictim01\|KNOWN CRASH SITE\|Imperial Prison Sewer" "C:\Users\aubre\AppData\Local\Temp\claude\baseline_analyze.txt"
```

Expected: `3` or more. If `0`, stop — the baseline is not valid and the migration cannot be verified.

- [ ] **Step 3: Clone MapClone and filter to just the two tools**

`git filter-repo` requires a fresh clone. `--no-local` forces a real object copy so the source repo is never touched.

```bash
cd /x/dev
git clone --no-local OblivionRemastered_MapClone OblivionRemastered_CrashTools
cd OblivionRemastered_CrashTools
git filter-repo --force \
  --path analyze_crashdump.py \
  --path check_crashes.py \
  --path-rename analyze_crashdump.py:tools/analyze_crashdump.py \
  --path-rename check_crashes.py:tools/check_crashes.py
```

- [ ] **Step 4: Verify history and layout survived**

```bash
cd /x/dev/OblivionRemastered_CrashTools
git log --oneline
ls tools/
git remote -v
```

Expected: log shows the tool commits (`4201983`-equivalent `feat(analyze_crashdump): recognize heap-corruption...` etc. — SHAs change because filter-repo rewrites); `tools/` contains both `.py` files; **no** `origin` remote (filter-repo strips it).

---

### Task 2: Scaffold the repo and fix path assumptions

Two paths break when the scripts move down into `tools/`. Fix them, then prove behavior is unchanged against the Task 1 baseline.

**Files:**
- Create: `X:\dev\OblivionRemastered_CrashTools\.gitignore`
- Create: `X:\dev\OblivionRemastered_CrashTools\README.md`
- Create: `X:\dev\OblivionRemastered_CrashTools\CLAUDE.md`
- Create: `X:\dev\OblivionRemastered_CrashTools\tools\requirements.txt`
- Modify: `X:\dev\OblivionRemastered_CrashTools\tools\analyze_crashdump.py` (`LANDMARK_CACHE`)
- Modify: `X:\dev\OblivionRemastered_CrashTools\tools\check_crashes.py` (`CRASH_DIR` → `--dir`)

**Interfaces:**
- Consumes: repo from Task 1.
- Produces: `check_crashes.py` gains `--dir PATH` (default `X:\games\OBR_CrashDumps`); `analyze_crashdump.py` resolves its landmark cache to `<repo>/work/landmark_cache.json`.

- [ ] **Step 1: Create `.gitignore`**

```gitignore
# Crash dumps are NEVER committed — they contain tester PII
# (Windows username, machine GUID, LoginId, save names, Steam paths).
*.dmp
*.7z

# Scratch, dump staging, generated caches
work/

__pycache__/
*.pyc
.venv/
```

- [ ] **Step 2: Fix the landmark cache path**

The cache currently resolves next to the script. After the move that would be `tools/work/`, which is not the gitignored `work/`. Point it at the repo root.

In `tools/analyze_crashdump.py`, replace:

```python
LANDMARK_CACHE = Path(__file__).resolve().parent / "work" / "landmark_cache.json"
```

with:

```python
# Repo-root work/ (gitignored), not tools/work/
LANDMARK_CACHE = Path(__file__).resolve().parent.parent / "work" / "landmark_cache.json"
```

- [ ] **Step 3: Make the crash directory configurable**

In `tools/check_crashes.py`, change line 25 from a constant to a default. Replace:

```python
CRASH_DIR = Path(r"X:\games\OBR_CrashDumps")
```

with:

```python
DEFAULT_CRASH_DIR = Path(r"X:\games\OBR_CrashDumps")
```

Then in `main()`, add the argument alongside the existing ones:

```python
    parser.add_argument("--dir", type=Path, default=DEFAULT_CRASH_DIR,
                        help="crash-dump directory (default: %(default)s)")
```

and replace the four `CRASH_DIR` uses in `main()` with `args.dir`:

```python
    if not args.dir.is_dir():
        print(f"Crash dump directory not found: {args.dir}", file=sys.stderr)
        sys.exit(1)

    crashes = []
    for d in sorted(args.dir.iterdir()):
```

- [ ] **Step 4: Create `tools/requirements.txt`**

```
capstone>=5.0
```

- [ ] **Step 5: Create `README.md`**

````markdown
# OblivionRemastered_CrashTools

Crash-forensics tooling and knowledge for Oblivion Remastered mod projects
(OOO, MapClone, ItemClone, RAX).

**No crash dumps are ever committed here.** They contain tester PII — Windows
usernames, machine GUIDs, save names, Steam paths. Keep them in `work/`
(gitignored) or outside the repo.

## Tools

| Tool | Use |
|------|-----|
| `tools/check_crashes.py` | Triage: list recent crashes with error messages. `--dir` to point at tester-supplied dumps. |
| `tools/analyze_crashdump.py` | Deep single-dump analysis: modules, registers, symbolicated frames, FormID recovery, landmark lookup. |

## Setup

```bash
py -3 -m pip install -r tools/requirements.txt
```

## Quickstart

```bash
py -3 tools/check_crashes.py --last 3
py -3 tools/analyze_crashdump.py "X:\tmp\crashlogs\UECC-Windows-XXXX_0000"
py -3 tools/analyze_crashdump.py --locate 47241 81157
```

## Skill

`skill/obr-crash-forensics/` is the source of truth for the crash-forensics
skill. Deploy it after every edit:

```powershell
pwsh -File scripts/deploy_skill.ps1
```

## Docs

- `docs/crash-signatures.md` — catalog of known crash sites
- `docs/debugging-workflow.md` — workflow and the limits of each technique
````

- [ ] **Step 6: Create `CLAUDE.md`**

```markdown
# CLAUDE.md — OblivionRemastered_CrashTools

Crash-forensics tooling shared across the Oblivion Remastered mod projects.
Inherits `X:\dev\CLAUDE.md` (no-ff merges; never add a `Co-Authored-By: Claude`
trailer or "Generated with Claude Code" line).

## Hard rules

| Rule | Detail |
|------|--------|
| **No dumps in git** | `*.dmp` is gitignored. Crash dumps contain tester PII (Windows username, machine GUID, `LoginId`, save names, Steam paths). Never commit one, not even "temporarily". |
| **Game install is READ-ONLY** | `C:\games\Steam\steamapps\common\Oblivion Remastered\` is read-only. `analyze_crashdump.py` reads the shipping exe for disassembly — reads only, never writes. |
| **Skill source of truth is here** | Edit `skill/obr-crash-forensics/SKILL.md`, then run `scripts/deploy_skill.ps1`. Never edit the deployed copy in `~/.claude/skills/` directly — it is overwritten. |

## Layout

| Path | Role |
|------|------|
| `tools/analyze_crashdump.py` | Deep dump analysis; `KNOWN_CRASH_SITES` lives here (keyed by faulting RVA). |
| `tools/check_crashes.py` | Recent-crash triage; `--dir` for tester dumps. |
| `skill/obr-crash-forensics/` | Skill source; deployed by copy. |
| `docs/crash-signatures.md` | Human-readable expansion of the signature catalog. |
| `docs/debugging-workflow.md` | Workflow + technique limits. |
| `work/` | Gitignored: dumps, landmark cache, scratch. |

## Adding a crash signature

When a dump is fully diagnosed, add it in **both** places:
1. `KNOWN_CRASH_SITES` in `tools/analyze_crashdump.py`, keyed by faulting RVA.
2. A section in `docs/crash-signatures.md` with mechanism and evidence.
```

- [ ] **Step 7: Verify the tools still behave identically**

```bash
cd /x/dev/OblivionRemastered_CrashTools
py -3 tools/analyze_crashdump.py "X:\tmp\crashlogs\UECC-Windows-156F45DC489F75522E51998F693A866F_0000" 2>/dev/null > "C:\Users\aubre\AppData\Local\Temp\claude\after_analyze.txt"
diff "C:\Users\aubre\AppData\Local\Temp\claude\baseline_analyze.txt" "C:\Users\aubre\AppData\Local\Temp\claude\after_analyze.txt" && echo "IDENTICAL"
```

Expected: `IDENTICAL`. (The landmark cache rebuilds on first run — that message goes to stderr and is excluded.) If the diff is non-empty, fix before continuing.

- [ ] **Step 8: Verify `--dir` works and the cache landed in the right place**

```bash
py -3 tools/check_crashes.py --dir "X:\tmp\crashlogs" --last 2
ls work/landmark_cache.json && git status --short
```

Expected: crash listing prints; `work/landmark_cache.json` exists; `git status` does **not** list `work/` or the cache.

- [ ] **Step 9: Commit**

```bash
git add .gitignore README.md CLAUDE.md tools/requirements.txt tools/analyze_crashdump.py tools/check_crashes.py
git commit -m "feat: scaffold CrashTools repo; repo-root cache path, --dir for triage"
```

---

### Task 3: Port crash knowledge into the signature catalog

**Files:**
- Create: `X:\dev\OblivionRemastered_CrashTools\docs\crash-signatures.md`
- Create: `X:\dev\OblivionRemastered_CrashTools\docs\debugging-workflow.md`

**Interfaces:**
- Consumes: repo from Task 2.
- Produces: docs referenced by `SKILL.md` in Task 4.

- [ ] **Step 1: Create `docs/crash-signatures.md`**

```markdown
# Known crash signatures

All RVAs are for game build **1.512.105** (`OblivionRemastered-Win64-Shipping.exe`).
`tools/analyze_crashdump.py` recognizes these automatically via `KNOWN_CRASH_SITES`,
keyed by faulting RVA. When adding a signature, update both that dict and this file.

## 1. `exe+2dc0356` — null TES-object → UE-actor lookup

**Mechanism:** `mov eax,[rcx+8]` on a null object. Reached from the pairing-command
dispatch at `exe+4899ca2`, inside the Altar reverse-pairing session.

**Identifying evidence:** GameThread; `SecondsSinceLoadingScreen: 0`; faults reading
a small offset (`0x8`); frame `exe+4899ca5` references the strings
`"Begin Reverse Pairing Session - FrameNumber: %lu"` and `"SeamlessTravelHandlers"`.

**FormID recoverable:** **Yes.** The pairing command payload
(`{u32 formid, u32 pad, u32 opcode}`) sits on the GameThread stack, reachable via
the crashed `RDX`/`R14`. The runtime FormID's top byte is the plugin's load-order
index and varies per user; the low 6 hex digits identify the record.

**First seen:** 2026-07-12 — OOO `zOOOHaplessVictim01` (`07DDB4`), a persistent
ACHR on the Lake Rumare shore by the Imperial Prison Sewer exit. Persistent refs
are paired on every load regardless of player position.

## 2. `exe+331b38c` — null component during post-pairing teardown

**Mechanism:** iterating an actor's component array (`rdi = [rcx+0x88]`, count
`[rcx+0x90]`); element `r14 = components[i]` is null, faulting on `[r14]`.
Reached from the `Release_Oblivion` teardown at `exe+4899d01` — one call *later*
in the same pairing function as signature 1.

**Identifying evidence:** GameThread; same pairing function; fault address `0x0`.

**FormID recoverable:** **No.** Verified by scanning the full dumped stack, not just
registers. By teardown the actor is already half-destroyed. A dump with this
signature **cannot name a mod record** — do not attribute one from it.

**First seen:** 2026-07-19.

## 3. `exe+e0c8ca` — heap corruption in the binned allocator

**Mechanism:** Unreal's binned small-block allocator popping a free list;
`rsi` (free-list head) is a poisoned pointer (observed `0x40000000`), faulting on
`mov rax,[rsi]`. **The allocator is the victim, not the cause** — a bad write
elsewhere poisoned the heap and this later allocation tripped over it.

**Identifying evidence:** often a worker thread rather than GameThread; fault
address is a page-aligned mid-range pointer rather than a small null+offset.
`analyze_crashdump.py` flags both conditions as `NOTE:` lines even at unknown RVAs.

**FormID recoverable:** **No.** The corruptor is long gone from the stack.
Diagnose by in-game bisection and dynamic analysis, not dump forensics.

**First seen:** 2026-08-02, reproducible in the Fort Nikel interior, on two
different characters (dev and alpha tester) — which rules out save-state
corruption and any single user's mod list.

**Investigation status (open).** Ruled out by static analysis: unmapped SyncMap
objects, malformed `XAAG`/`XACN` pairing data, GUID collisions, chest loot trees,
custom meshes, and cooked paks — OOO ships **no** cooked asset for Fort Nikel at
all, only ESP records and SyncMap lines pairing onto vanilla assets. A RAX LVSP
theory was refuted on base rate: that code path runs for every leveled-spell
caster game-wide, so it cannot explain a crash localized to one small, rarely
changed zone (Fort Nikel content last changed in alpha57).
```

- [ ] **Step 2: Create `docs/debugging-workflow.md`**

```markdown
# Crash-debugging workflow

## 1. Triage

```bash
py -3 tools/check_crashes.py --last 3
py -3 tools/check_crashes.py --dir "X:\tmp\crashlogs"    # tester-supplied
```

## 2. Deep analysis

```bash
py -3 tools/analyze_crashdump.py "<UECC folder>"
```

Reports: error and crashed thread, session timing (`SecondsSinceLoadingScreen: 0`
means the crash happened during a load), non-standard modules, registers,
symbolicated frames with referenced strings, recovered FormIDs resolved against
the OOO inventory, and nearest landmarks for the player position.

Requires a **same-build** local exe; the tool verifies via PE timestamp and
refuses to disassemble on mismatch rather than print misleading RVAs.

## 3. Attribution

A recovered FormID's low 6 hex digits identify the record; the top byte is the
plugin's load-order index and **varies per user** — confirm against their
`plugins.txt` before naming a mod.

## Limits of each technique

These are expensive lessons. Respect them before spending a play-test session.

| Technique | Limit |
|-----------|-------|
| **PageHeap / Application Verifier** | Only instruments the **NT heap**. UE5 sub-allocates from its own binned pools via VirtualAlloc, so page heap is **blind to the allocator that actually gets poisoned**. The switches that would reroute allocations (`-ansimalloc`, `-stompmalloc`, `-binnedmalloc`) are **stripped from this shipping build** — verified absent from the exe's strings. |
| **Bisection** | Unreliable for **heap corruption**. Removing any object shifts allocation layout and can mask the bug without fixing it. "Removing X stops the crash" is not evidence that X is the cause. |
| **`pcall` in UE4SS Lua** | Does **not** catch native access violations. Guard UObjects with `if obj and obj:IsValid()` before any member call. |
| **Minidump module lists** | Show only native DLLs. **Lua mods never appear** — enumerate `ue4ss\Mods\*\enabled.txt` separately to know what was actually loaded. |
| **Heap-corruption stacks** | Name the *victim* allocation, never the corruptor. Do not attribute a record from one. |

## Adding a new signature

1. Diagnose the dump fully.
2. Add an entry to `KNOWN_CRASH_SITES` in `tools/analyze_crashdump.py`, keyed by
   faulting RVA, with a description stating whether a FormID is recoverable.
3. Add a section to `docs/crash-signatures.md`.
4. Re-run the tool on the dump and confirm it prints `*** KNOWN CRASH SITE ***`.
```

- [ ] **Step 3: Verify the docs match the tool's actual behavior**

```bash
cd /x/dev/OblivionRemastered_CrashTools
grep -c "0x2dc0356\|0x331b38c\|0xe0c8ca" tools/analyze_crashdump.py
```

Expected: `3` — every RVA documented in `crash-signatures.md` exists in `KNOWN_CRASH_SITES`.

- [ ] **Step 4: Commit**

```bash
git add docs/
git commit -m "docs: crash signature catalog and debugging workflow"
```

---

### Task 4: Author and deploy the skill

**Files:**
- Create: `X:\dev\OblivionRemastered_CrashTools\skill\obr-crash-forensics\SKILL.md`
- Create: `X:\dev\OblivionRemastered_CrashTools\scripts\deploy_skill.ps1`

**Interfaces:**
- Consumes: docs from Task 3.
- Produces: `~/.claude/skills/obr-crash-forensics/SKILL.md` on disk.

- [ ] **Step 1: Create `skill/obr-crash-forensics/SKILL.md`**

The frontmatter `description` is what triggers the skill — it must name the
concrete artifacts a user will mention.

````markdown
---
name: obr-crash-forensics
description: Use when analyzing an Oblivion Remastered crash — a UECC crash-dump folder, UEMinidump.dmp, CrashContext.runtime-xml, a UE4SS crash_*.dmp, or a tester-reported CTD. Covers triage, deep dump analysis, FormID attribution, and the limits of PageHeap/bisection for heap corruption.
---

# Oblivion Remastered crash forensics

Tools live in `X:\dev\OblivionRemastered_CrashTools`.

## Triage first

```bash
py -3 X:\dev\OblivionRemastered_CrashTools\tools\check_crashes.py --last 3
py -3 X:\dev\OblivionRemastered_CrashTools\tools\check_crashes.py --dir "X:\tmp\crashlogs"
```

## Then deep analysis

```bash
py -3 X:\dev\OblivionRemastered_CrashTools\tools\analyze_crashdump.py "<UECC folder>"
```

Also: `--locate X Y` names a TES4 worldspace position via nearest map markers.

## Known signatures (build 1.512.105)

| RVA | Meaning | FormID recoverable? |
|-----|---------|---------------------|
| `exe+2dc0356` | Null TES-object → UE-actor lookup in pairing dispatch | **Yes** — payload on GameThread stack |
| `exe+331b38c` | Null component in post-pairing teardown | **No** — actor already half-destroyed |
| `exe+e0c8ca` | Heap corruption in UE's binned allocator | **No** — allocator is the victim |

Detail: `docs/crash-signatures.md`. The tool recognizes all three automatically.

## Rules that prevent wasted work

- **A heap-corruption stack names the victim, never the corruptor.** Never
  attribute a mod record from one.
- **Bisection lies for heap corruption.** Removing any object perturbs allocation
  layout and can mask the bug. "Removing X fixed it" is not causation.
- **PageHeap cannot see UE's binned pools** — it only instruments the NT heap, and
  this shipping build strips `-ansimalloc`/`-stompmalloc`. Do not spend a
  play-test session on it.
- **`pcall` does not catch native access violations** in UE4SS Lua hooks.
- **Lua mods are invisible in minidump module lists** — enumerate
  `ue4ss\Mods\*\enabled.txt` separately.
- **A FormID's top byte is load-order dependent.** Confirm against the user's
  `plugins.txt` before naming a mod; only the low 6 hex digits identify the record.

## Adding a signature

Update `KNOWN_CRASH_SITES` in `tools/analyze_crashdump.py` **and**
`docs/crash-signatures.md`, then re-run the tool to confirm recognition.
````

- [ ] **Step 2: Create `scripts/deploy_skill.ps1`**

Copy rather than symlink — symlink creation is blocked on this machine without developer mode.

```powershell
[CmdletBinding()]
param()

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$source   = Join-Path $repoRoot 'skill\obr-crash-forensics'
$target   = Join-Path $env:USERPROFILE '.claude\skills\obr-crash-forensics'

if (-not (Test-Path -LiteralPath $source)) {
    throw "Skill source not found: $source"
}

New-Item -ItemType Directory -Path $target -Force | Out-Null
Copy-Item -Path (Join-Path $source '*') -Destination $target -Recurse -Force

Write-Host "Deployed skill -> $target" -ForegroundColor Green
Get-ChildItem -LiteralPath $target | ForEach-Object { Write-Host "  $($_.Name)" }
```

- [ ] **Step 3: Run the deploy script**

```bash
pwsh -File /x/dev/OblivionRemastered_CrashTools/scripts/deploy_skill.ps1
```

Expected: `Deployed skill -> C:\Users\aubre\.claude\skills\obr-crash-forensics` and `SKILL.md` listed.

- [ ] **Step 4: Verify the deployed skill is valid and idempotent**

```bash
head -4 ~/.claude/skills/obr-crash-forensics/SKILL.md
pwsh -File /x/dev/OblivionRemastered_CrashTools/scripts/deploy_skill.ps1
ls ~/.claude/skills/
```

Expected: frontmatter shows `name: obr-crash-forensics`; second run succeeds without error; both `obr-crash-forensics` and the pre-existing `oblivion-remastered-modding` are present.

- [ ] **Step 5: Commit**

```bash
cd /x/dev/OblivionRemastered_CrashTools
git add skill/ scripts/
git commit -m "feat: obr-crash-forensics skill and deploy script"
```

---

### Task 5: Retire the tools from MapClone

**Files:**
- Delete: `X:\dev\OblivionRemastered_MapClone\analyze_crashdump.py`
- Delete: `X:\dev\OblivionRemastered_MapClone\check_crashes.py`
- Modify: `X:\dev\OblivionRemastered_MapClone\CLAUDE.md` (Crash Dumps row)

**Interfaces:**
- Consumes: working repo from Tasks 2–4 (do not run this task until Task 2 Step 7 printed `IDENTICAL`).

- [ ] **Step 1: Confirm the new repo works before deleting anything**

```bash
cd /x/dev/OblivionRemastered_CrashTools
py -3 tools/analyze_crashdump.py "X:\tmp\crashlogs\UECC-Windows-BB25F3494CAFA73F055CE6AC6CA9DAB1_0000" 2>/dev/null | grep -c "KNOWN CRASH SITE"
```

Expected: `1`. If `0`, **stop** — do not delete the MapClone copies.

- [ ] **Step 2: Remove the tools from MapClone**

```bash
cd /x/dev/OblivionRemastered_MapClone
git rm analyze_crashdump.py check_crashes.py
```

- [ ] **Step 3: Update the MapClone `CLAUDE.md` pointer**

Replace the entire `**Crash Dumps**` table row with:

```markdown
| **Crash Dumps** | `X:\games\OBR_CrashDumps` — always check latest dumps when user reports a crash. Tooling now lives in **`X:\dev\OblivionRemastered_CrashTools`**: `tools/check_crashes.py` (triage, `--dir` for tester dumps) and `tools/analyze_crashdump.py` (deep analysis: modules, registers, symbolicated frames, FormID recovery, `--locate X Y` landmark lookup). Signature catalog: that repo's `docs/crash-signatures.md`. |
```

- [ ] **Step 4: Verify no dangling references remain**

```bash
cd /x/dev/OblivionRemastered_MapClone
grep -rn "analyze_crashdump\|check_crashes" --include="*.md" --include="*.py" . | grep -v "^./.git/" | grep -v OblivionRemastered_CrashTools
```

Expected: no output (every remaining mention points at the new repo).

- [ ] **Step 5: Commit**

```bash
git add -A analyze_crashdump.py check_crashes.py CLAUDE.md
git commit -m "refactor: move crash tooling to OblivionRemastered_CrashTools"
```

---

### Task 6: Thin the memory files and create the private remote

**Files:**
- Modify: `C:\Users\aubre\.claude\projects\X--dev-OblivionRemastered-OOO\memory\project_crashdump_pairing_formid.md`
- Modify: `C:\Users\aubre\.claude\projects\X--dev-OblivionRemastered-OOO\memory\project_pairing_teardown_ctd.md`
- Modify: `C:\Users\aubre\.claude\projects\X--dev-OblivionRemastered-OOO\memory\project_fortnikel_heap_corruption_ctd.md`
- Modify: `C:\Users\aubre\.claude\projects\X--dev-OblivionRemastered-OOO\memory\project_hapless_victim_ctd.md`

- [ ] **Step 1: Reduce each memory file body to a pointer**

Keep each file's frontmatter unchanged. Replace the body of the three signature
files with a one-line pointer, e.g. for `project_pairing_teardown_ctd.md`:

```markdown
Signature 2 (`exe+331b38c`, null component in post-pairing teardown, no FormID
recoverable). Full detail now lives in
`X:\dev\OblivionRemastered_CrashTools\docs\crash-signatures.md`; the tool
recognizes it automatically via `KNOWN_CRASH_SITES`.
```

Leave `project_fortnikel_heap_corruption_ctd.md`'s **open investigation state**
(cross-character repro, ruled-out hypotheses, next steps) in memory — it is live
working context, not settled reference. Point only its signature description at the docs.

- [ ] **Step 2: Update `project_crashdump_pairing_formid.md` tool paths**

Replace every `X:\dev\OblivionRemastered_MapClone\analyze_crashdump.py` and
`check_crashes.py` reference with `X:\dev\OblivionRemastered_CrashTools\tools\...`.

- [ ] **Step 3: Verify no memory file points at the old location**

```bash
grep -rn "MapClone.*analyze_crashdump\|MapClone.*check_crashes" "C:\Users\aubre\.claude\projects\X--dev-OblivionRemastered-OOO\memory\"
```

Expected: no output.

- [ ] **Step 4: Create the private GitHub remote and push**

```bash
cd /x/dev/OblivionRemastered_CrashTools
gh repo create OblivionRemastered_CrashTools --private --source=. --remote=origin
git push -u origin main
```

- [ ] **Step 5: Verify the remote is private and dump-free**

```bash
gh repo view devakm/OblivionRemastered_CrashTools --json isPrivate,name
git ls-files | grep -ci "\.dmp$"
```

Expected: `"isPrivate": true`; the `.dmp` count is `0`.

---

### Task 7: Give RAX a CLAUDE.md

**Files:**
- Create: `X:\dev\RAX\CLAUDE.md`

- [ ] **Step 1: Create `X:\dev\RAX\CLAUDE.md`**

```markdown
# CLAUDE.md — RAX (Remastered Adjustments & eXtensions)

UE4SS C++ mod providing two independent fixes, both registered in
`OOO_Core_Fixes/src/mod_main.cpp` → `on_unreal_init()`:

| Fix | Source | What it does |
|-----|--------|--------------|
| `lvsp` | `OOO_Core_Fixes/src/lvsp/lvsp_fix.cpp` | Works around a vanilla bug with NPCs whose spell list contains a leveled spell (LVSP). **Global** — runs for every such caster in every cell, not just custom maps. |
| `rax` | `OOO_Core_Fixes/src/rax/asset_registry_fix.cpp` | Custom-map / asset-registry loading. The reason custom maps load at all. |

Inherits `X:\dev\CLAUDE.md` (no-ff merges; never add a `Co-Authored-By: Claude`
trailer or "Generated with Claude Code" line).

## Hard rules

| Rule | Detail |
|------|--------|
| **Game install is READ-ONLY** | `C:\games\Steam\steamapps\common\Oblivion Remastered\` — never write, copy, or patch anything under it. Deploying a build is the user's action, not Claude's. |
| **No binaries in git** | `.gitignore` excludes `Binaries/`, `Intermediates/`, `*.pdb`, `*.obj`. Never commit a built `main.dll`. |
| **Real commits per change** | The repo began as a single "Initial import". Every change from here gets its own descriptive commit. |

## Build

```powershell
.\build_release.ps1     # Game__Shipping__Win64
.\build_debug.ps1
```

Requires Visual Studio 2022 (Desktop development with C++), a Windows 10/11 SDK,
and `xmake`. Output: `Binaries\Game__Shipping__Win64\OOO_Core_Fixes\OOO_Core_Fixes.dll`,
deployed by the user as `ue4ss\Mods\RAX\dlls\main.dll`.

## Build identity

`build_common.ps1` generates `OOO_Core_Fixes/src/common/version.generated.h`
(gitignored) containing the git short SHA. `mod_main.cpp` logs
`[RAX] build <sha>` at init, so `UE4SS.log` and any crash investigation can map a
running DLL back to its source commit. **Never hand-edit the generated header.**

## Layout note

`RE-UE4SS/` is a vendored copy of the UE4SS source this mod builds against
(~2,959 files), not a submodule.
```

- [ ] **Step 2: Verify the documented facts are accurate**

```bash
cd /x/dev/RAX
grep -n "lvsp::Initialize\|rax::Initialize" OOO_Core_Fixes/src/mod_main.cpp
ls build_release.ps1 build_debug.ps1
git ls-files | grep -ci "\.dll$"
```

Expected: both `Initialize()` calls found; both scripts exist; DLL count is `0`.

- [ ] **Step 3: Commit**

```bash
git add CLAUDE.md
git commit -m "docs: add CLAUDE.md with build, deploy and hard rules"
```

---

### Task 8: Stamp the build with its git SHA

Closes the gap that made it impossible to confirm a deployed `main.dll` matched the source under analysis.

**Files:**
- Modify: `X:\dev\RAX\.gitignore`
- Modify: `X:\dev\RAX\build_common.ps1:169` (insert generation before `$targetName`)
- Modify: `X:\dev\RAX\OOO_Core_Fixes\src\mod_main.cpp`

**Interfaces:**
- Produces: `OOO_Core_Fixes/src/common/version.generated.h` defining `RAX_BUILD_SHA` (a string literal); consumed by `mod_main.cpp`.

- [ ] **Step 1: Gitignore the generated header**

Append to `X:\dev\RAX\.gitignore`:

```gitignore
# Generated at build time by build_common.ps1
OOO_Core_Fixes/src/common/version.generated.h
```

- [ ] **Step 2: Generate the header during the build**

In `build_common.ps1`, inside `Invoke-OooCoreFixesBuild`, insert immediately
after the `vcRedist` reporting block (currently ending line 169 with `}`) and
before `$targetName = 'OOO_Core_Fixes'`:

```powershell
    # --- build identity -----------------------------------------------------
    # Stamp the git SHA into a generated header so a deployed DLL can be traced
    # back to its source commit (logged at init as "[RAX] build <sha>").
    $sha = & git -C $ProjectRoot rev-parse --short HEAD 2>$null
    if (-not $sha) { $sha = 'unknown' }
    $dirty = & git -C $ProjectRoot status --porcelain 2>$null
    if ($dirty) { $sha = "$sha-dirty" }

    $versionHeader = Join-Path $ProjectRoot 'OOO_Core_Fixes\src\common\version.generated.h'
    @(
        '// Generated by build_common.ps1 - DO NOT EDIT, DO NOT COMMIT.',
        '#pragma once',
        ('#define RAX_BUILD_SHA "{0}"' -f $sha)
    ) | Set-Content -LiteralPath $versionHeader -Encoding UTF8

    Write-OkLine "Build identity: $sha"
```

- [ ] **Step 3: Log the build identity at init**

In `OOO_Core_Fixes/src/mod_main.cpp`, replace the whole file with:

```cpp
#include "Mod/CppUserModBase.hpp"
#include <DynamicOutput/DynamicOutput.hpp>

#include "lvsp/lvsp_fix.h"
#include "rax/asset_registry_fix.h"

// Generated by build_common.ps1. Falls back when building without the script.
#if __has_include("common/version.generated.h")
    #include "common/version.generated.h"
#else
    #define RAX_BUILD_SHA "unknown"
#endif

namespace {

class RAXMod : public RC::CppUserModBase {
public:
    RAXMod()
    {
        ModName = STR("RAX");
        ModVersion = STR("1.1");
        ModDescription = STR("Remastered Adjustments & eXtensions");
        ModAuthors = STR("Antrix");
    }

    auto on_unreal_init() -> void override
    {
        RC::Output::send(STR("[RAX] build {}\n"), STR(RAX_BUILD_SHA));

        lvsp_fix::lvsp::Initialize();
        lvsp_fix::rax::Initialize();
    }
};

} // namespace

#define MY_MOD_API __declspec(dllexport)

extern "C" {

MY_MOD_API RC::CppUserModBase* start_mod()
{
    return new RAXMod();
}

MY_MOD_API void uninstall_mod(RC::CppUserModBase* mod)
{
    delete mod;
}

}
```

- [ ] **Step 4: Build and verify the header is generated correctly**

```bash
cd /x/dev/RAX
pwsh -File build_release.ps1
cat OOO_Core_Fixes/src/common/version.generated.h
git rev-parse --short HEAD
```

Expected: build succeeds; the header's `RAX_BUILD_SHA` matches `git rev-parse --short HEAD` (with a `-dirty` suffix if the tree has uncommitted changes).

- [ ] **Step 5: Verify the generated header is not tracked**

```bash
git status --short
```

Expected: `version.generated.h` does **not** appear.

- [ ] **Step 6: Verify the log line at runtime**

Deploy the built DLL (user action — Claude must not write to the game folder), launch the game, then:

```bash
grep -i "\[RAX\] build" "C:\games\Steam\steamapps\common\Oblivion Remastered\OblivionRemastered\Binaries\Win64\ue4ss\UE4SS.log"
```

Expected: a line like `[RAX] build 9681f51` matching the built commit. **This is the acceptance test for the whole task** — from here on, any dump or log identifies the exact RAX source.

- [ ] **Step 7: Commit**

```bash
git add .gitignore build_common.ps1 OOO_Core_Fixes/src/mod_main.cpp
git commit -m "feat: stamp git SHA into build, log [RAX] build <sha> at init"
```

---

## Self-review

**Spec coverage:**

| Spec requirement | Task |
|---|---|
| New repo `OblivionRemastered_CrashTools` | 1 |
| History-preserving migration | 1 |
| No dumps / PII (`.gitignore`, private) | 2, 6 |
| `check_crashes.py` configurable dir | 2 |
| `KNOWN_CRASH_SITES` stays in code; docs are the expansion | 3 |
| `crash-signatures.md`, `debugging-workflow.md` | 3 |
| Skill in repo + deploy script | 4 |
| Technique limits captured in the skill | 4 |
| Remove tools from MapClone, update pointer | 5 |
| Memory files thinned to pointers | 6 |
| Private remote | 6 |
| RAX `CLAUDE.md` | 7 |
| RAX version stamping | 8 |
| RAX commit discipline | 7 (stated), 8 (practiced) |
| Migration verified by identical re-analysis | 2 Step 7 |

**Placeholders:** none — every step contains literal content or a runnable command.

**Consistency:** `RAX_BUILD_SHA` is defined in Task 8 Step 2 and consumed in Step 3 under the same name. `LANDMARK_CACHE` (Task 2 Step 2) and `.gitignore`'s `work/` (Step 1) agree on repo-root `work/`. `DEFAULT_CRASH_DIR`/`--dir` (Task 2 Step 3) match the README and skill usage.

**Known risk:** Task 2 Step 7 assumes byte-identical output. If the landmark cache rebuild alters ordering, compare with `diff <(sort ...)` instead and note it — but ordering is deterministic (markers sorted by distance, cells by grid distance), so identical output is expected.
