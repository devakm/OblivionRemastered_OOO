# OOO_REFRFix — Lua version

## What this does

Corrects stale NPC/creature positions for alpha testers in OOO cells such as Arondar. This is NOT needed if you are starting a new save file. It is only needed if playing with a save file that was started using an earlier alpha version.

**Root cause**: Steam save files use UE FArchive chunk format (`0x9E2A83C1`) — permanently
undecodable offline. The save's `ChangedForm` data caches NPC spawn positions from before the
OOO ESP shift, overriding the corrected ESP values even on first visit. This mod relocates live
actors at runtime after they spawn.

**Method**: `FindAllOf("VTESObjectRefComponent")` → read `SourceFormID` → match actor's level
path against known Arondar map names → call `K2_SetActorLocation` with the precomputed UE5 delta.

## Prerequisites

- UE4SS v3.0+ installed in game directory
- `OOO_PositionFix.esp` + IoStore containers deployed (static statics must already be correct)

## Deploy

This UE4SS installation activates mods via `enabled.txt` (not `mods.txt`).
The `enabled.txt` file is already present in this folder — just copy the whole directory:

```powershell
$game = "C:\games\Steam\steamapps\common\Oblivion Remastered\OblivionRemastered\Binaries\Win64\ue4ss\Mods"

# Deploy (overwrites prior version if present)
Copy-Item -Recurse -Force ue4ss_mods\OOO_REFRFix_Lua "$game\OOO_REFRFix"
```

The mod is now installed at `Mods\OOO_REFRFix\` with `enabled.txt` present → auto-enabled at next game launch.

## Testing workflow

### Step 1 — Probe mode (default)

Leave `MODE = "probe"` in `Scripts\main.lua`.  Deploy and enter **zOOOArondar**.

Check `UE4SS.log` (in `Binaries\Win64\ue4ss\`) or the UE4SS console for the following:

```
[REFRFIX] OOO_REFRFix (Lua v1.0) loaded. mode=probe ...
[REFRFIX] ClientRestart (seq=1) — scans scheduled at +5s / +10s / +20s
[REFRFIX] === Scan #1  mode=probe ===
[REFRFIX] Found N VTESObjectRefComponent instances total
[REFRFIX] [PROBE] fid=007065  cell=L_Arondar  cur=(X, Y, Z)  want=(X', Y', Z')
...
[REFRFIX] Scan #1 done: matched=M moved=0 already_fixed=0 errors=0
```

**If `FindAllOf` returns nil**: `VTESObjectRefComponent` is the wrong class name.
Run the following in the UE4SS Lua console to enumerate class names containing "TES" or "REF":

```lua
local names = {}
FindAllOf("Object"):ForEach(function(obj)
    local n = obj:GetClass():GetName()
    if n:find("TES") or n:find("Ref") or n:find("VTES") then
        names[n] = true
    end
end)
for k in pairs(names) do print(k) end
```

Or check the `.usmap` file with UAssetGUI to confirm the correct short class name.

**If matched=0 but instances>0**: The actor's `GetFullName()` doesn't contain `L_Arondar`.
Add this debug line after `getDeltaForActor` returns nil and log `fullname` to see the actual path.

### Step 2 — Fix mode

Once probe shows correct `[PROBE]` lines with expected positions:

1. Edit `Scripts\main.lua` line 39: change `local MODE = "probe"` → `local MODE = "fix"`
2. Re-deploy
3. Enter zOOOArondar — NPCs/creatures should teleport to correct geometry positions

Press **F9** for a manual rescan if the auto-scan at 5s fires before all actors have spawned.

## Deltas applied

| Cell | Level | UE5 delta (cm) |
|------|-------|----------------|
| zOOOArondar   | L_Arondar   | X=−5943.2, Y=+1897.5, Z=+2058.3 |
| zOOOArondar02 | L_Arondar02 | X=−4053.9, Y=+1621.9, Z=+2118.4 |
| zOOOArondar03 | L_Arondar03 | X=−8139.7, Y=−1431.9, Z=+2105.9 |

Coordinate mapping: `UE5_X = TES4_Z`, `UE5_Y = −TES4_X`, `UE5_Z = −TES4_Y`

## Context: relationship to actor_position_fix

The `actor_position_fix` mod (already deployed) handles:

- `VDoorTeleportMarker` — door XTEL destinations, fixed at actor creation via `NotifyOnNewObject`

This mod (`OOO_REFRFix`) adds:

- `VTESObjectRefComponent` scan via `FindAllOf` at 5s/10s/20s after cell load (post-spawn)
- Targets NPC/creature spawn positions that were baked into the save cache at wrong coordinates

**Critical finding from actor_position_fix**: NPCs/creatures spawn into the persistent level (NOT
`L_Arondar`) 25ms **before** `L_Arondar` appears in StreamingLevels. This means:

1. Our level-name pattern matching may fail (actors' `GetFullName()` won't contain "L_Arondar")
2. The [DIAG] lines in probe output will reveal the actual actor path format
3. If level-matching fails, FormID-based detection (lookup table from ESP data) is needed

**Delta discrepancy note**: `actor_position_fix` uses entrance delta (-2648, +2914, -8537) for
VDoorTeleportMarker. This mod uses the ESP-derived ue5_delta (-5943, +1897, +2058) for general
REFRs. These are different objects with different individual OOO offsets — both can be correct.
The ESP deltas from `fix_ooo_positions.py` are confirmed correct for statics (in-game test 3/6/2026).
