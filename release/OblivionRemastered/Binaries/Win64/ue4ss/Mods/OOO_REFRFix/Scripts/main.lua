-- ===========================================================================
-- HARD BLOCK: C:\games\Steam\steamapps\common\ is READ-ONLY.
-- The ONLY permitted ops on that path are Get-Content / Select-String reads.
-- NEVER write, edit, copy, move, or patch any file under that path. Ever.
-- Violations: 2026-03-14 (Copy-Item), 2026-03-22 (Set-Content in-place patch)
-- ===========================================================================-- OOO_REFRFix -- Lua version  (v2.49.0)
-- Corrects stale NPC/creature positions in all OOO shifted cells by scanning
-- for Character/Pawn actors and snapping them to patched ESP target positions.
--
-- WHY THIS EXISTS:
--   The OOO ESP shifts static REFR positions to match cloned Moranda geometry.
--   But NPC/creature actors have stale positions baked into the player's save
--   (UE FArchive format — undecodable, cannot be patched offline).
--   This mod relocates live actors each time the cell loads.
--
-- ROOT CAUSE OF TWO-STEP PROCESS:
--   The save cache overrides ESP even for first-visit cells.  NPC spawn positions
--   are read from the save's ChangedForm data, not re-evaluated from the ESP.
--   => We must move them at runtime after they spawn.
--
-- INSTALL:
--   Copy Scripts\main.lua to:
--   ...\Binaries\Win64\ue4ss\Mods\OOO_REFRFix\Scripts\main.lua
--   Add line to mods.txt:  OOO_REFRFix : 1
--
-- USAGE:
--   Step 1 — Leave MODE = "probe".  Enter zOOOArondar.  Watch UE4SS console or
--            UE4SS.log for [REFRFIX] lines.
--            Confirm "Found N VTESObjectRefComponent instances" and [PROBE] lines.
--   Step 2 — Change MODE = "fix" once probe output looks correct.
--            Re-deploy.  Enter cell.  NPCs/creatures teleport to correct positions.
--   F9     — Manual scan (use after map transition if auto-scan fires too early).
-- ─────────────────────────────────────────────────────────────────────────────

-- ─── Configuration ────────────────────────────────────────────────────────────
-- "probe" → log only, NO actor moves (safe for first run)
-- "fix"   → apply delta once per session per FormID
local MODE = "fix"

-- ─── Own log file ────────────────────────────────────────────────────────────
-- Writes to C:\Temp\OOO_REFRFix.log via standard Lua io, completely bypassing
-- the UE4SS print buffer that gets corrupted by rapid-fire calls from other mods.
-- Each line has an OS timestamp so scans are easy to correlate with game events.
-- The file is appended-to for the entire game session; delete it to reset.
-- print() is still called for the UE4SS console window (may still garble there,
-- but the file log is always clean and that is the authoritative source).
local LOG_PATH = "C:/Temp/OOO_REFRFix.log"
local function log(msg)
    local f = io.open(LOG_PATH, "a")
    if f then
        f:write(os.date("[%Y-%m-%d %H:%M:%S] ") .. msg .. "\n")
        f:close()
    end
end

-- UE5 cm deltas per streaming level name.
-- Matched as substring of actor:GetFullName() (which includes full package path).
-- ORDER MATTERS: check longer patterns (03, 02) before the base name.
-- Deltas: OOO/save-cached position → correct Moranda geometry position.
-- Verified in actor_position_fix.lua (VDoorTeleportMarker confirmed working).
-- ORDER MATTERS: check longer suffixes (03, 02) before the bare name.
-- Deltas computed from backup ESP: shift = (vanilla_Moranda_pos - OOO_pos) in TES4 units,
-- converted to UE5 cm using the TES4→UE5 axis mapping:
--   UE5_X =  TES4_X * 1.4162,  UE5_Y = -TES4_Y * 1.4162,  UE5_Z =  TES4_Z * 1.4162
-- Source: detect_shift(vanilla, backup_OOO) — STAT cluster average across 10–13 matched pairs.
-- These are the same delta applied to statics in the patched ESP.
--
-- IMPORTANT: These deltas are ONLY applied to L_PersistentDungeon actors (NPCs/creatures
-- with stale save-cached OOO positions).  Static geometry in L_Arondar is already at the
-- correct Moranda positions via the patched ESP — applying delta to them again would be wrong.
local LEVEL_DELTAS = {
    -- Arondar (source: Moranda) — large downward shift, NPCs sky-stashed at Z > 3000
    { pattern = "L_Arondar03",    dx =  2027.9, dy =   2982.3, dz = -11527.5 },  -- zOOOArondar03
    { pattern = "L_Arondar02",    dx = -2297.0, dy =   3000.0, dz =  -5741.2 },  -- zOOOArondar02
    { pattern = "L_Arondar",      dx = -2687.2, dy =   2915.0, dz =  -8416.8 },  -- zOOOArondar
    -- Barastas (source: Belda) — large downward shift, NPCs sky-stashed
    { pattern = "L_Baras02",      dx =   462.5, dy =  -3595.7, dz =  -9288.3 },  -- zOOOBarastas02
    { pattern = "L_Baras",        dx =  -288.7, dy =   4081.1, dz =  -8990.4 },  -- zOOOBarastas
    -- Blood Clot Cave (source: Greenmead Cave) — small +Z shift, NPCs below floor
    { pattern = "L_BloodClotCave", dx =    0.0, dy =      0.0, dz =    704.9 },  -- BloodClotCave
    -- Narind (source: Nonungalo) — large downward shift, NPCs sky-stashed
    { pattern = "L_Narid02XXXX",  dx =  3091.6, dy =  11716.5, dz = -10327.0 },  -- zOOONarid02
    { pattern = "L_NarindXXX",    dx =  4986.2, dy =   5088.1, dz =  -9752.9 },  -- zOOONarind
}

-- Absolute UE5 player landing positions derived from XTEL subrecords in the patched ESP.
-- These are the authoritative spawn targets for the player on cell entry — NOT cur+delta.
-- Conversion: UE5_X = TES4_X*1.4162,  UE5_Y = -TES4_Y*1.4162,  UE5_Z = TES4_Z*1.4162
-- Only defined for cells whose exterior door XTEL has been patched by fix_ooo_positions.py.
-- Cells without an entry here will have the player skipped (not moved) — add entry once XTEL is patched.
--   All entries below are generated from fix_ooo_positions.py EXTERIOR_XTEL_FIXES (auto-discovered 3/9/2026).
--   Pick the primary exterior worldspace entry door for each cell (highest TES4 Z = closest to surface).
--   L_Arondar02, L_Arondar03, L_Baras02 : entered only via interior passage doors — player Z
--     should be at interior room height, not sky position → skip (no entry needed).
--   Landing coordinates are the PATCHED ESP XTEL XYZ converted to UE5:
--     ue5_x = tes4_x * 1.4162,  ue5_y = -tes4_y * 1.4162,  ue5_z = tes4_z * 1.4162
local PLAYER_LANDING = {
    -- L_Arondar: main entry 0x0A0076F4   TES4 (-3336.3, -17.4, 787.7)
    ["L_Arondar"]       = { x = -4724.5, y =    24.6, z =  1115.3 },
    -- L_Baras: entry 0x0A00160A         TES4 (-2412.0,  -2.8, 476.6)
    ["L_Baras"]         = { x = -3415.8, y =     3.9, z =   675.0 },
    -- L_BloodClotCave: entry 0x0A016ECD  TES4 (4681.6, -2602.6, 1134.9)
    ["L_BloodClotCave"] = { x =  6630.0, y =  3685.9, z =  1607.2 },
    -- L_NarindXXX: entry 0x0A0023E7     TES4 (2878.0, -3226.3, -1280.0)
    ["L_NarindXXX"]     = { x =  4075.8, y =  4569.1, z = -1812.7 },
    -- L_Narid02XXXX: entry 0x0A0022A8   TES4 (2850.3, -3398.9, -1280.2)
    ["L_Narid02XXXX"]   = { x =  4036.6, y =  4813.6, z = -1813.0 },
}

-- Idempotency: cache of actor fullname → absolute CENTER target {x,y,z}.
-- Always stores the un-scattered entry target so LVLC assignment matching stays
-- consistent. Reset on each ClientRestart so re-entering a cell starts fresh.
local target_cache = {}
-- v2.33.0: scatter offsets stored separately so target_cache holds the CENTER
-- coordinate. Applied at move-time only; does NOT affect spawn_claimed matching.
-- Cleared on ClientRestart alongside target_cache.
local scatter_offset = {}
local scan_count = 0
-- Set to true after the player is first moved to the XTEL landing position.
-- Cleared on ClientRestart. Prevents subsequent scans from snapping the player
-- back to the entrance after they have walked away from it.
local player_landed = false
-- Global flat set of NPC/creature fullnames moved this session.
-- npc_landed[fullname] = true.
-- v2.43.0: Cleared ONLY on ClientRestart (restored from v2.29.0 core).
-- Re-entry actors have fresh UUIDs (KL 91, confirmed v2.41.0 log: first-visit
-- _2147467501 vs re-entry _2147456434). Fresh UUIDs bypass npc_landed naturally,
-- so no per-zone clear is needed. Z < SKY_STASH_Z_MIN remains the primary guard
-- for already-placed floor-level actors across continuous 500ms scans.
local npc_landed = {}
-- Per-zone first-visit coverage. zones_coverage[pattern] = covered_count after first window close.
-- Kept for logging only; suppression removed in v2.37.0 (KL 92).
local zones_coverage    = {}
-- Per-zone spawn-point claim table. spawn_claimed[zone_pattern][locKey] = true.
-- Phase 1 of findBestSpawnEntry skips claimed entries so each spawn point gets
-- at most one actor before extras are distributed via Phase 2.
-- Cleared per-zone on each ZONE_CHANGE; entire table reset on ClientRestart.
local spawn_claimed = {}
-- How many actors have been placed at each spawn entry this zone visit.
-- entry_land_count[pattern][locKey] = n.  Incremented once per unique actor UUID
-- (inside target_cache miss) so the scatter offset is stable for the lifetime of that
-- actor instance.  Cleared per-zone on first-visit ZONE_CHANGE; reset on ClientRestart.
local entry_land_count = {}  -- v2.31.0 (scatter idx; cleared per-zone on ZONE_CHANGE)
-- Feature flag: set true to re-enable diag-era re-entry scan logging (v2.39.5-diag/diag2).
-- Confirmed root cause (KL 94 free-fall). Keep flagged-off; flip to true if re-entry
-- issues regress and we need tick-level ZGUARD/PAWN data again.
local DIAG_REENTRY_LOG = false
-- Feature flag: intercept SendSpellCast to trigger diagnostic dump from controller.
-- Set false when Begone is handling SendSpellCast to avoid duplicate hooks.
local DIAG_SPELL_CAST_HOOK = true
-- Feature flag: append to log instead of truncating at boot.
-- Set true to preserve multi-session detail for cross-session analysis.
local DIAG_PRESERVE_BOOT_LOG = true
-- Per-session diagnostic: log first N getDeltaForActor-rejected pawn fullnames.
local diag_count = 0
-- placement_pending[fn] = {sp=string, tgt={x,y,z}} -- actors we attempted to place this zone visit.
-- Populated on K2_SetActorLocation call; verified via DIAG (SendSpellCast) to confirm landing.
local placement_pending = {}
-- scan_open_at: os.clock() timestamp of the most recent ZONE_CHANGE.
-- runScan() is skipped once (os.clock() - scan_open_at) > SCAN_WINDOW_SECS.
-- Reset on ZONE_CHANGE (re-entry gets its own fresh window) and ClientRestart.
local SCAN_WINDOW_SECS = 45
local scan_open_at     = nil  -- nil = no window active yet (before first zone entry)

-- Character pawn scan class names to try.
-- VTESObjectRefComponent outer-actors are spawn trigger WRAPPERS, not pawns.
-- Actual NPC/creature pawns are ACharacter or APawn subclasses.
-- We try all names until one returns results; unknown ones return nil (safe).
local CHAR_CLASSES = { "Character", "Pawn" }

-- ─── Active cell detection ────────────────────────────────────────────────────
-- Walk world.StreamingLevels and return the delta for whichever L_Arondar*
-- level is currently loaded.  Used for L_PersistentDungeon actors (NPCs spawn
-- into the persistent level before the streaming level becomes visible).
local UEHelpers = require("UEHelpers")

-- ─── Per-spawn-point delta table ─────────────────────────────────────────────
-- Loaded from Scripts/spawn_deltas.lua (generated by work/gen_spawn_deltas.py).
-- Key = lower-24-bit FormID (not used at runtime — table is searched by proximity).
-- Fields per entry: cell (level name), ox/oy/oz (old OOO UE5 position), dx/dy/dz (UE5 delta).
local SPAWN_DELTAS = require("spawn_deltas")

-- Pre-index by cell name for O(n) per-cell search instead of O(total).
local SPAWN_BY_CELL = {}
for _, e in ipairs(SPAWN_DELTAS) do
    if not SPAWN_BY_CELL[e.cell] then SPAWN_BY_CELL[e.cell] = {} end
    table.insert(SPAWN_BY_CELL[e.cell], e)
end

-- How far (UE5 cm) an actor may be from a spawn-point entry and still be matched.
-- Spawn scatter is typically < 200 UU; set conservatively at 3000 UU to handle
-- actors that wandered a bit between spawn and our first scan at +2s.
local SNAP_RADIUS_SQ   = 3000 * 3000
-- v2.25.0: Only actors above this Z are sky-stash stale positions that need moving.
-- Zone-1 floor max ≈ 942. Zone-2 floor max ≈ 2890. Sky-stash min ≈ 8126.
-- v2.51.0: raised back to 5000. At 2000, correctly-placed Z2 actors (Z=2385-2890) exceeded the
-- threshold and were falsely classified FAILED_SKY by VERIFY. 5000 is safely above Z2 floor max
-- (~2890) and well below sky stash (~7000+), so all three zones classify correctly.
local SKY_STASH_Z_MIN  = 5000


local function spawnKey(e)
    return string.format("%.0f,%.0f,%.0f", e.ox, e.oy, e.oz)
end
-- v2.36.0: claim/count key is the entry's name when available, coordinate string otherwise.
-- This ensures log sp=, enforcement, and HITloc coverage counts all use the same key.
local function locKey(e)
    return e.name or spawnKey(e)
end

-- Find the best SPAWN_DELTAS entry for (cx,cy,cz) in two phases:
--   Phase 1: nearest UNCLAIMED entry, NO radius limit — all actors fan out to unique entries.
--            Returns is_unclaimed=true.  Calling code trusts this result at any distance.
--   Phase 2: nearest ANY entry within SNAP_RADIUS_SQ (extra actors once all slots claimed).
--            Returns is_unclaimed=false.

-- v2.41.0 (KL 97): sort key only — nearest entry ignoring claimed state.
-- Used to pre-rank sky-stash actors so closer-match actors claim entries first.
local function nearestEntryDist(active_cell, cx, cy, cz)
    local entries = SPAWN_BY_CELL[active_cell]
    if not entries then return math.huge end
    local best_d = math.huge
    for _, e in ipairs(entries) do
        local d2 = (cx-e.ox)^2 + (cy-e.oy)^2 + (cz-e.oz)^2
        if d2 < best_d then best_d = d2 end
    end
    return best_d
end

local function findBestSpawnEntry(active_cell, cx, cy, cz)
    local entries = SPAWN_BY_CELL[active_cell]
    if not entries then return nil, SNAP_RADIUS_SQ + 1, false end
    -- Phase 1: nearest entry with room left (count < e.max, default 3).
    -- Multiple actors from the same LVLC pick-one REFR share a sky-stash cluster
    -- and should all land at the same spawn entry; count-based claiming allows this.
    local zone_claimed = spawn_claimed[active_cell] or {}
    local best_e, best_d = nil, math.huge
    for _, e in ipairs(entries) do
        if (zone_claimed[locKey(e)] or 0) < (e.max or 1) then
            local d2 = (cx-e.ox)^2 + (cy-e.oy)^2 + (cz-e.oz)^2
            if d2 < best_d then best_d = d2; best_e = e end
        end
    end
    if best_e then return best_e, best_d, true end
    -- Phase 2 (v2.43.0): nearest entry STILL under max= cap within SNAP_RADIUS_SQ.
    -- If all in-radius entries are at max → returns nil → caller uses FALLBACK delta.
    -- Prevents entrance-cluster bloat (e.g. Z1_12=4 actors observed in v2.41.0 log).
    best_d = SNAP_RADIUS_SQ + 1
    for _, e in ipairs(entries) do
        if (zone_claimed[locKey(e)] or 0) < (e.max or 1) then
            local d2 = (cx-e.ox)^2 + (cy-e.oy)^2 + (cz-e.oz)^2
            if d2 < best_d then best_d = d2; best_e = e end
        end
    end
    return best_e, best_d, false
end

local function getActiveCellDelta()
    local world = UEHelpers.GetWorld()
    if not world or not world:IsValid() then return nil end
    local ok, levels = pcall(function() return world.StreamingLevels end)
    if not ok or not levels then return nil end
    -- v2.2.0: build a set of loaded basenames first, then check LEVEL_DELTAS in
    -- priority order (longest suffix first).  This guarantees L_Arondar02 wins
    -- over L_Arondar when both are simultaneously resident in StreamingLevels,
    -- regardless of their array index.  Iterating StreamingLevels first (v2.1.0)
    -- was non-deterministic and caused zone 2 to be misidentified as zone 1.
    local loaded = {}
    for i = 1, #levels do
        local ok_l, lvl = pcall(function() return levels[i] end)
        if ok_l and lvl then
            local ok_iv, iv = pcall(function() return lvl:IsValid() end)
            if ok_iv and iv then
                local ok_vis, vis = pcall(function() return lvl.bIsVisible end)
                if ok_vis and vis then
                    local ok_p, pkg = pcall(function()
                        return lvl.PackageNameToLoad:ToString()
                    end)
                    if ok_p and pkg then
                        local base = pkg:match("[^/]+$") or pkg
                        loaded[base] = true
                    end
                end
            end
        end
    end
    local best = nil
    for _, entry in ipairs(LEVEL_DELTAS) do
        if loaded[entry.pattern] then best = entry; break end
    end
    -- v2.28.0: L_Arondar03 never unloads after zone-3 visit. If player is above Z=-1000
    -- (zone-3 floor ≈ -3001 UE5; zone-1 floor ≈ 35 UE5), they are not in zone 3 →
    -- reduce to L_Arondar02 so the existing block below can further reduce to L_Arondar.
    if best and best.pattern == "L_Arondar03" then
        local ok_ctrl, pc = pcall(function() return UEHelpers.GetPlayerController() end)
        if ok_ctrl and pc and pc:IsValid() then
            local ok_pw, pw = pcall(function() return pc:K2_GetPawn() end)
            if ok_pw and pw and pw:IsValid() then
                local ok_l, loc = pcall(function() return pw:K2_GetActorLocation() end)
                if ok_l and loc and loc.Z > -1000 then
                    for _, e in ipairs(LEVEL_DELTAS) do
                        if e.pattern == "L_Arondar02" and loaded[e.pattern] then best = e; break end
                    end
                end
            end
        end
    end
    -- v2.24.0: Z-override moved here so ALL callers (LoopAsync + runScan) agree on zone.
    -- L_Arondar02 never unloads, so after returning to zone 1 it still wins priority.
    -- If player is at zone-1 floor height (Z < 1500), return L_Arondar entry instead.
    if best and best.pattern == "L_Arondar02" then
        local ok_ctrl, pc = pcall(function() return UEHelpers.GetPlayerController() end)
        if ok_ctrl and pc and pc:IsValid() then
            local ok_pw, pw = pcall(function() return pc:K2_GetPawn() end)
            if ok_pw and pw and pw:IsValid() then
                local ok_l, loc = pcall(function() return pw:K2_GetActorLocation() end)
                if ok_l and loc and loc.Z < 1500 then
                    for _, e in ipairs(LEVEL_DELTAS) do
                        if e.pattern == "L_Arondar" and loaded[e.pattern] then return e end
                    end
                end
            end
        end
    end
    return best
end

-- ─── Delta lookup ─────────────────────────────────────────────────────────────
-- Returns (delta_entry, fullname_string) or (nil, fullname_string).
-- ONLY matches L_PersistentDungeon actors (NPCs/creatures with stale save positions).
-- L_Arondar actors (static geometry) are ALREADY at correct Moranda positions via the
-- patched ESP — we must NOT apply the delta to them again.
local function getDeltaForActor(actor, persistent_delta)
    local ok, fullname = pcall(function() return actor:GetFullName() end)
    if not ok or not fullname then return nil, nil end
    -- Skip door teleport markers.
    if fullname:find("TeleportMarker", 1, true) then return nil, fullname end
    -- Skip the player character — handled separately in Pass 2.
    if fullname:find("PlayerCharacter", 1, true) then return nil, fullname end
    -- Only match actors in L_PersistentDungeon.
    if not fullname:find("L_PersistentDungeon", 1, true) then return nil, fullname end
    -- NOTE: do NOT filter by VerticalSlice path. OOO uses TesSyncMapInjector to
    -- reuse vanilla UE5 NPC blueprints (e.g. BP_Degil_C, BP_Thoronir_C) as skins
    -- for OOO marauders/creatures. These actors genuinely need to be moved.
    if persistent_delta then
        return persistent_delta, fullname
    end
    return nil, fullname
end

-- ─── Shared move logic ────────────────────────────────────────────────────────
-- Applies delta to actor using target_cache.  Returns: "moved", "skipped", or "error".
local function applyDelta(actor, fullname, delta, scan_n, tag)
    if fullname:find("Controller", 1, true) then return "skip_ctrl" end

    local ok_loc, cur = pcall(function() return actor:K2_GetActorLocation() end)
    if not ok_loc or not cur then return "error" end

    -- Skip actors that haven't been placed yet (world origin = uninitialized).
    -- Moving them would cache a poisoned target of (0,0,0)+delta.
    if math.abs(cur.X) < 5 and math.abs(cur.Y) < 5 and math.abs(cur.Z) < 5 then
        return "skipped"
    end

    local key = fullname
    local is_new = (target_cache[key] == nil)
    local tgt = target_cache[key]
    if tgt == nil then
        tgt = { x = cur.X + delta.dx, y = cur.Y + delta.dy, z = cur.Z + delta.dz }
        target_cache[key] = tgt
    end

    local ddx = cur.X - tgt.x
    local ddy = cur.Y - tgt.y
    local ddz = cur.Z - tgt.z
    if MODE == "fix" and (ddx*ddx + ddy*ddy + ddz*ddz) < 2500.0 then
        return "skipped"
    end

    if MODE == "probe" then
        log(string.format("PROBE %-4s  cell=%-14s  cur=(%.1f, %.1f, %.1f)  ->  want=(%.1f, %.1f, %.1f)",
            tag, delta.pattern, cur.X, cur.Y, cur.Z, tgt.x, tgt.y, tgt.z))
        return "probed"
    end

    local ok_set, err = pcall(function()
        return actor:K2_SetActorLocation({ X = tgt.x, Y = tgt.y, Z = tgt.z }, false, {}, true)
    end)
    if ok_set then
        if is_new then
            local short = (fullname:match("([^%.:%s]+)%s*$") or fullname):sub(1, 60)
            log(string.format("  MOVE  %-4s  %-60s  (%.0f,%.0f,%.0f)->(%.0f,%.0f,%.0f)",
                tag, short, cur.X, cur.Y, cur.Z, tgt.x, tgt.y, tgt.z))
        end
        return "moved"
    else
        log(string.format("  ERR   K2_SetActorLocation failed  tag=%s  reason=%s", tag, tostring(err)))
        return "error"
    end
end


-- v1.9.0: extended to all 8 OOO shifted cells (Arondar/Barastas/BloodClotCave/Narind).
--         Z guard moved inside fallback branch so snap matches work at any Z (BloodClotCave).
--         spawn_deltas.lua regenerated with no Z_MIN filter (all floor-level actors included).
-- v1.8.0: spawn_deltas stores tx/ty/tz (direct patched ESP target) instead of ox+dx.
--         LVLC-only filter via parsed LVLC FormID set; exact FormID pairing backup<->patched.
-- v1.7.3: per-actor NPC log line with cur/spawn-origin/gap/target/dist_to_tgt;
--         absolute tgt = (ox+dx, oy+dy, oz+dz) not cur+delta when snap matched
-- v1.7.2: revert VerticalSlice filter (SyncMap reuses city-NPC blueprints as OOO creature skins)
-- v1.7.1: filter out VerticalSlice/L_PersistentDungeon city NPCs (Degil, Thoronir, etc.)
-- v1.7.0: per-spawn-point delta via findBestSpawnEntry / SPAWN_DELTAS (generated from ESPs)
-- v1.6.4: Z-threshold guard for NPCs (skip if Z < 3000 = already in Moranda space)
-- v1.6.3: disable Pass 1 (ESP handles all static REFR positions); add npc_landed set
-- v1.6.2: move player XTEL teleport back inside pawn loop (FindAllOf called before teleport)
-- v1.6.1: add player_landed flag to prevent snap-back after first correct placement
-- v1.6.0: player uses absolute XTEL landing target (not cluster delta); skip PlayerCharacter from Pass 1
-- v1.5.9: verbose file log (SCAN/REFR/PLYR/PAWN/DONE + per-actor MOVE on first encounter)
--         log() writes to file only; single print() per scan keeps UE4SS.log clean
-- v1.5.8: log() writes to C:\Temp\OOO_REFRFix.log, bypasses UE4SS print buffer
-- v1.5.7: prepend \n to every print() so REFRFIX always starts on a fresh line
-- v1.5.6: collapsed to ONE print() per scan to prevent log-line jumbling when
-- other mods (NaturalBodyMorph, etc.) fire many rapid-fire print() calls that
-- overflow the UE4SS log buffer and corrupt line terminators for all mods.
-- v2.49.0: Post-scan greedy redistribution — fill vacant entries from surplus clusters.
-- Donors: placement_pending actors whose assigned entry has spawn_claimed count > 1.
-- Vacancies: spawn entries with claimed count == 0 (and max > 0).
-- Greedy: each iteration picks the (donor, vacancy) pair with minimum 2D distance
-- (donor.from_xy → vacancy origin XY).  Preserves total actor count invariant.
local function runQCRedistribute(zone_sc, entries)
    if not entries then return 0 end
    local vacant = {}
    for _, e in ipairs(entries) do
        if (zone_sc[locKey(e)] or 0) == 0 and (e.max or 1) > 0 then
            vacant[#vacant+1] = e
        end
    end
    if #vacant == 0 then return 0 end
    local donors = {}
    for fn, p in pairs(placement_pending) do
        if p.entry_key and p.pawn_obj and (zone_sc[p.entry_key] or 0) > 1 then
            donors[#donors+1] = { fn=fn, p=p }
        end
    end
    if #donors == 0 then return 0 end
    local reassigned = 0
    while #vacant > 0 and #donors > 0 do
        local best_sq, bvi, bdi = math.huge, 1, 1
        for vi, v in ipairs(vacant) do
            for di, d in ipairs(donors) do
                local sq = (d.p.from_x - v.ox)^2 + (d.p.from_y - v.oy)^2
                if sq < best_sq then best_sq=sq; bvi=vi; bdi=di end
            end
        end
        local bv = table.remove(vacant, bvi)
        local bd = table.remove(donors, bdi)
        local old_k, new_k = bd.p.entry_key, locKey(bv)
        zone_sc[old_k] = (zone_sc[old_k] or 1) - 1
        zone_sc[new_k] = (zone_sc[new_k] or 0) + 1
        local ok = pcall(function()
            bd.p.pawn_obj:K2_SetActorLocation({X=bv.tx, Y=bv.ty, Z=bv.tz}, false, {}, true)
        end)
        if ok then
            reassigned = reassigned + 1
            bd.p.entry_key = new_k; bd.p.sp = new_k
            bd.p.tgt = { x=bv.tx, y=bv.ty, z=bv.tz }
            target_cache[bd.fn] = { x=bv.tx, y=bv.ty, z=bv.tz }
            scatter_offset[bd.fn] = nil
            log(string.format("  QC_SNAP  %-8s  dist=%.0f  from=(%.0f,%.0f)  tgt=(%.0f,%.0f,%.0f)",
                new_k, math.sqrt(best_sq), bd.p.from_x, bd.p.from_y, bv.tx, bv.ty, bv.tz))
            if (zone_sc[old_k] or 0) <= 1 then
                for i = #donors, 1, -1 do
                    if donors[i].p.entry_key == old_k then table.remove(donors, i) end
                end
            end
        else
            zone_sc[old_k] = (zone_sc[old_k] or 0) + 1
            zone_sc[new_k] = (zone_sc[new_k] or 1) - 1
            log(string.format("  QC_ERR  %s  K2_SetActorLocation failed", new_k))
        end
    end
    return reassigned
end

local function runScan()
    scan_count = scan_count + 1

    -- Gate: check active cell FIRST, before any FindAllOf calls.
    local persistent_delta = getActiveCellDelta()
    if not persistent_delta then
        log(string.format("#%d SKIP", scan_count))
        print(string.format("\n[REFRFIX] #%d SKIP", scan_count))
        return
    end

    -- Pass 1: DISABLED (v1.6.3)
    local comps = {}
    local fa1_err = false
    local matched, moved, skipped, errors = 0, 0, 0, 0

    -- Detect player pawn once before the loop (no teleport here — teleport happens inside
    -- the loop on the already-fetched list to avoid invalidating GUObjectArray state).
    local player_char = nil
    local plyr_status = "missing"
    do
        local ok_ctrl, pc = pcall(function() return UEHelpers.GetPlayerController() end)
        if ok_ctrl and pc and pc:IsValid() then
            local ok_p, p = pcall(function() return pc:K2_GetPawn() end)
            if ok_p and p and p:IsValid() then player_char = p end
        end
        if not player_char then
            local ok_pcs, pcs = pcall(function() return FindAllOf("PlayerController") end)
            if ok_pcs and pcs then
                for _, ctrl in ipairs(pcs) do
                    if ctrl and ctrl:IsValid() then
                        local ok_p, p = pcall(function() return ctrl:K2_GetPawn() end)
                        if ok_p and p and p:IsValid() then player_char = p; break end
                    end
                end
            end
        end
    end
    if not player_char then log("  PLYR  player pawn not found") end

    -- Pass 2: Character/Pawn actors (NPC/creature meshes + player).
    -- NOTE: GetPlayerCharacter() and GetPlayerPawn() are nil in OBR UE4SS.
    -- FindAllOf is called HERE so the list is fetched before any teleport.
    local pawn_scanned, pawn_matched, pawn_moved, pawn_skip, pawn_landed = 0, 0, 0, 0, 0
    -- Per-zone idempotency tables; keyed by zone pattern so each zone entry is independent.
    local zone = persistent_delta.pattern
    if not spawn_claimed[zone] then spawn_claimed[zone] = {} end
    local zone_sc  = spawn_claimed[zone]
    -- v2.41.0 (KL 97): Collect eligible sky-stash pawns, sort by distance to nearest
    -- spawn entry, then assign in sorted order.  Actors closest to their natural entry
    -- claim it first — prevents greedy-order theft across spawn clusters (e.g. zone-2).
    local pawn_list = {}
    local fn_seen   = {}
    for _, cls in ipairs(CHAR_CLASSES) do
        local ok_fa, pawns = pcall(function() return FindAllOf(cls) end)
        if not ok_fa or not pawns or #pawns == 0 then goto nextcls end
        pawn_scanned = pawn_scanned + #pawns
        for _, pawn in ipairs(pawns) do
            if not pawn or not pawn:IsValid() then goto np_c end
            -- Player: handle inline with XTEL target, then skip from NPC list.
            if player_char and pawn == player_char then
                if player_landed then
                    plyr_status = "ok_at_tgt"
                    log("  PLYR  already landed this visit, skip")
                else
                    local landing = PLAYER_LANDING[persistent_delta.pattern]
                    if not landing then
                        plyr_status = "no_xtel"; log("  PLYR  no XTEL data for this cell, skip")
                    else
                        local ok_ploc, ploc = pcall(function() return pawn:K2_GetActorLocation() end)
                        if not ok_ploc or not ploc then plyr_status = "no_loc"
                        else
                            local ddx=ploc.X-landing.x; local ddy=ploc.Y-landing.y; local ddz=ploc.Z-landing.z
                            if (ddx*ddx+ddy*ddy+ddz*ddz) < (200*200) then
                                player_landed=true; plyr_status="ok_at_tgt"
                                log(string.format("  PLYR  at landing (%.0f,%.0f,%.0f)  skip",ploc.X,ploc.Y,ploc.Z))
                            else
                                local ok_set=pcall(function()
                                    pawn:K2_SetActorLocation({X=landing.x,Y=landing.y,Z=landing.z},false,{},true)
                                end)
                                if ok_set then
                                    pawn_moved=pawn_moved+1; player_landed=true; plyr_status="moved"
                                    log(string.format("  PLYR  moved (%.0f,%.0f,%.0f)->(%.0f,%.0f,%.0f)",
                                        ploc.X,ploc.Y,ploc.Z,landing.x,landing.y,landing.z))
                                else
                                    errors=errors+1; plyr_status="err"
                                    log("  PLYR  K2_SetActorLocation failed")
                                end
                            end
                        end
                    end
                end
                goto np_c
            end
            local delta2, pawn_fn = getDeltaForActor(pawn, persistent_delta)
            if not delta2 then
                if diag_count < 15 then
                    local has_pd = pawn_fn and (pawn_fn:find("L_PersistentDungeon",1,true) and "PD" or "no_PD") or "nil_fn"
                    log(string.format("  DIAG  [%s] %s", has_pd, (pawn_fn or "(nil)"):sub(1,100)))
                    diag_count = diag_count + 1
                end
                goto np_c
            end
            if pawn_fn and pawn_fn:find("Controller", 1, true) then goto np_c end
            if npc_landed[pawn_fn] then pawn_landed = pawn_landed + 1; goto np_c end
            if fn_seen[pawn_fn] then goto np_c end
            local ok_c0, cur0 = pcall(function() return pawn:K2_GetActorLocation() end)
            if not ok_c0 or not cur0 then goto np_c end
            if math.abs(cur0.X)<5 and math.abs(cur0.Y)<5 and math.abs(cur0.Z)<5 then goto np_c end
            if cur0.Z < SKY_STASH_Z_MIN then
                pawn_skip = pawn_skip + 1
                -- Log first encounter: actor already at floor level, not sky-stashed.
                local d0 = nearestEntryDist(persistent_delta.pattern, cur0.X, cur0.Y, cur0.Z)
                local sn0 = (pawn_fn:match("([^%.:%s]+)%s*$") or "?"):sub(1,48)
                log(string.format("  NPC_FLOOR  %-48s  cur=(%.0f,%.0f,%.0f)  dist_to_nearest=%.0f",
                    sn0, cur0.X, cur0.Y, cur0.Z, d0 < math.huge and math.sqrt(d0) or -1))
                npc_landed[pawn_fn] = true  -- suppress re-logging on subsequent scans
                goto np_c
            end
            fn_seen[pawn_fn] = true
            table.insert(pawn_list, {pawn=pawn, fn=pawn_fn, delta2=delta2, cur0=cur0,
                sort_d = nearestEntryDist(zone, cur0.X, cur0.Y, cur0.Z)})
            ::np_c::
        end
        ::nextcls::
    end
    table.sort(pawn_list, function(a, b) return a.sort_d < b.sort_d end)
    for _, c in ipairs(pawn_list) do
        local pawn, pawn_fn, delta2, cur0 = c.pawn, c.fn, c.delta2, c.cur0
        pawn_matched = pawn_matched + 1

            -- Find nearest spawn-point entry within the active zone only (v2.9.0).
            local snap_e, snap_d, snap_unclaimed = findBestSpawnEntry(persistent_delta.pattern, cur0.X, cur0.Y, cur0.Z)
            local snap_dist = snap_e and math.sqrt(snap_d) or -1


            -- v2.10.0: XY-only rescue snap for actors displaced to wrong-zone height by a prior
            -- incorrect assignment (e.g. zone1 actor moved to zone2 geometry Z≈2437–2890).
            -- 3D SNAP fails because Z offset (~6000) >> SNAP_RADIUS (3000).  XY-only proximity
            -- finds the correct own-zone entry ignoring the stale Z.
            -- Threshold: Z in [1200, 4000) — above zone1 max floor (941), below sky-stash (~8000).
            -- XY rescue also prefers unclaimed entries
            local xy_rescue = false
            if not (snap_e and snap_d <= SNAP_RADIUS_SQ) and cur0.Z >= 1200 and cur0.Z < 4000 then
                local r_entries = SPAWN_BY_CELL[persistent_delta.pattern]
                if r_entries then
                    local best_e2, best_d2 = nil, SNAP_RADIUS_SQ + 1
                    -- Phase 1: entry has room (count < e.max)
                    for _, e in ipairs(r_entries) do
                        if (zone_sc[locKey(e)] or 0) < (e.max or 1) then
                            local d2 = (cur0.X - e.ox)^2 + (cur0.Y - e.oy)^2
                            if d2 < best_d2 then best_d2 = d2; best_e2 = e end
                        end
                    end
                    -- Phase 2: any
                    if not best_e2 then
                        for _, e in ipairs(r_entries) do
                            local d2 = (cur0.X - e.ox)^2 + (cur0.Y - e.oy)^2
                            if d2 < best_d2 then best_d2 = d2; best_e2 = e end
                        end
                    end
                    if best_e2 and best_d2 <= SNAP_RADIUS_SQ then
                        snap_e = best_e2; snap_d = best_d2; xy_rescue = true
                    end
                end
            end

            -- Compute absolute target:
            --   SNAP     → tgt = (tx, ty, tz) exactly from nearest own-zone entry (3D match).
            --   XY_SNAP  → same, from XY-only rescue for actors at wrong-zone geometry height.
            --   No snap + Z >= 3000 → cluster-average fallback (sky-stash: Arondar/Barastas/Narind).
            --   No snap + Z <  3000 → skip (actor already at correct geometry position per ESP).
            local tgt_x, tgt_y, tgt_z
            local match_tag
            if snap_e and (snap_unclaimed or snap_d <= SNAP_RADIUS_SQ or xy_rescue) then
                tgt_x = snap_e.tx
                tgt_y = snap_e.ty
                tgt_z = snap_e.tz
                match_tag = xy_rescue
                    and string.format("XY_SNAP gap=%.0f", math.sqrt(snap_d))
                    or  (snap_d > SNAP_RADIUS_SQ
                         and string.format("SNAP_FAR gap=%.0f", snap_dist)
                         or  string.format("SNAP gap=%.0f", snap_dist))
            else
                -- No snap available.  Guard fallback with Z threshold.
                -- Actors at geometry floor (Z < 3000) are correctly placed by patched ESP.
                if cur0.Z < 3000 then
                    pawn_skip = pawn_skip + 1
                    npc_landed[pawn_fn] = true
                    goto nextpawn
                end
                tgt_x = cur0.X + delta2.dx
                tgt_y = cur0.Y + delta2.dy
                tgt_z = cur0.Z + delta2.dz
                if snap_e then
                    match_tag = string.format("FALLBACK gap=%.0f>%.0f", snap_dist, math.sqrt(SNAP_RADIUS_SQ))
                else
                    match_tag = "FALLBACK no_entries"
                end
            end

            -- Idempotency via target_cache (absolute target, not cur-relative).
            local key = pawn_fn
            if target_cache[key] == nil then
                -- v2.31.0: scatter actors sharing a spawn entry — apply once per UUID so
                -- the offset is fixed for the lifetime of this instance.
                if snap_e and not xy_rescue then
                    local sk = locKey(snap_e)
                    local zone_ec = entry_land_count[zone] or {}
                    zone_ec[sk] = (zone_ec[sk] or 0) + 1
                    entry_land_count[zone] = zone_ec
                    local idx = zone_ec[sk] - 1  -- 0-based; idx=0 → exact target
                    if idx > 0 then
                        -- v2.35.0: random ±50 UU, min 40 UU from center to avoid
                        -- overlapping actor idx=0 (~31 UU capsule radius).
                        -- center stays in target_cache so LVLC matching is unaffected.
                        local sc_dx, sc_dy
                        repeat
                            sc_dx = math.random(-50, 50)
                            sc_dy = math.random(-50, 50)
                        until (sc_dx*sc_dx + sc_dy*sc_dy) >= 1600  -- >=40 UU from center
                        scatter_offset[key] = { dx = sc_dx, dy = sc_dy }
                        match_tag = match_tag .. string.format(" sc=(%d,%d)", sc_dx, sc_dy)
                    end
                end
                target_cache[key] = { x = tgt_x, y = tgt_y, z = tgt_z }
            end
            -- Count-based claim: allows up to e.max actors per entry (default 3).
            if snap_e then zone_sc[locKey(snap_e)] = (zone_sc[locKey(snap_e)] or 0) + 1 end
            local tgt = target_cache[key]
            -- v2.33.0: apply scatter offset at move-time (kept separate from target_cache).
            local _so = scatter_offset[key]
            local act_x = tgt.x + (_so and _so.dx or 0)
            local act_y = tgt.y + (_so and _so.dy or 0)
            -- v2.34.0: show actual placement position only when scattered; center otherwise.
            local act_str = _so and string.format("  act=(%.0f,%.0f)", act_x, act_y) or ""

            -- v2.26.0: label = "BP_Glarthir_C_42@L_Arondar_LevelInstance_1" — the
            -- level-instance suffix shows which zone owns the actor so cross-zone
            -- contamination is immediately visible in the log. "@PD" = PersistentDungeon.
            local inst_name  = (pawn_fn:match("%.([^%.:%s]+)%s*$") or pawn_fn:match("([^%.:%s]+)%s*$") or "?")
            local inst_level = pawn_fn:match("(L_[^%.]+_LevelInstance_%d+)") or "PD"
            local short_cls  = (inst_name .. "@" .. inst_level):sub(1, 56)
            -- Spawn-point origin for logging.
            local sp_str = snap_e and (snap_e.name or string.format("(%.0f,%.0f,%.0f)", snap_e.ox, snap_e.oy, snap_e.oz)) or "none"

            -- Check idempotency: already at target (scattered position)?
            local ddx = cur0.X - act_x
            local ddy = cur0.Y - act_y
            local ddz = cur0.Z - tgt.z
            local dist_to_tgt = math.sqrt(ddx*ddx + ddy*ddy + ddz*ddz)

            if dist_to_tgt < 50 then
                pawn_skip = pawn_skip + 1
                npc_landed[pawn_fn] = true
                log(string.format("  NPC  %-24s  cur=(%.0f,%.0f,%.0f)  sp=%s  %s  tgt=(%.0f,%.0f,%.0f)%s  dist_to_tgt=%.0f  SKIP",
                    short_cls, cur0.X, cur0.Y, cur0.Z, sp_str, match_tag, tgt.x, tgt.y, tgt.z, act_str, dist_to_tgt))
                goto nextpawn
            end

            -- Move.
            if MODE == "probe" then
                log(string.format("  NPC  %-24s  cur=(%.0f,%.0f,%.0f)  sp=%s  %s  tgt=(%.0f,%.0f,%.0f)%s  dist_to_tgt=%.0f  PROBE",
                    short_cls, cur0.X, cur0.Y, cur0.Z, sp_str, match_tag, tgt.x, tgt.y, tgt.z, act_str, dist_to_tgt))
                pawn_moved = pawn_moved + 1
                npc_landed[pawn_fn] = true
            else
                local ok_set = pcall(function()
                    pawn:K2_SetActorLocation({X=act_x, Y=act_y, Z=tgt.z}, false, {}, true)
                end)
                if ok_set then
                    pawn_moved = pawn_moved + 1
                    npc_landed[pawn_fn] = true
                    placement_pending[pawn_fn] = { sp = sp_str, tgt = { x = tgt.x, y = tgt.y, z = tgt.z },
                        from_x    = cur0.X, from_y = cur0.Y,
                        entry_key = snap_e and locKey(snap_e) or nil,
                        pawn_obj  = pawn }
                    log(string.format("  NPC  %-24s  cur=(%.0f,%.0f,%.0f)  sp=%s  %s  tgt=(%.0f,%.0f,%.0f)%s  dist_to_tgt=%.0f  MOVED",
                        short_cls, cur0.X, cur0.Y, cur0.Z, sp_str, match_tag, tgt.x, tgt.y, tgt.z, act_str, dist_to_tgt))
                else
                    errors = errors + 1
                    log(string.format("  NPC  %-24s  cur=(%.0f,%.0f,%.0f)  %s  ERR K2_SetActorLocation",
                        short_cls, cur0.X, cur0.Y, cur0.Z, match_tag))
                end
            end

            ::nextpawn::
    end  -- pawn_list (sorted)

    -- v2.50.0: Displacement recovery — re-snap actors that physics-displaced after initial
    -- snap (wrong surface loaded before cell collision settled, typically on scan #1 only).
    -- Two-scan delay: first observation marks eligible; second checks dist and re-snaps once.
    local disp_n = 0
    for fn, p in pairs(placement_pending) do
        if p.resnap_done == nil then
            p.resnap_done = false   -- first observation: too soon, physics not yet settled
        elseif p.resnap_done == false then
            p.resnap_done = true    -- attempt once regardless of outcome
            if p.pawn_obj and p.pawn_obj:IsValid() then
                local ok_l, loc = pcall(function() return p.pawn_obj:K2_GetActorLocation() end)
                if ok_l and loc and loc.Z < SKY_STASH_Z_MIN then
                    local dist = math.sqrt((loc.X-p.tgt.x)^2+(loc.Y-p.tgt.y)^2+(loc.Z-p.tgt.z)^2)
                    if dist > 500 then
                        local ok_set = pcall(function()
                            p.pawn_obj:K2_SetActorLocation(
                                {X=p.tgt.x, Y=p.tgt.y, Z=p.tgt.z}, false, {}, true)
                        end)
                        local sn = (fn:match("([^%.:%s]+)%s*$") or fn):sub(1,44)
                        log(string.format("  DISP_RECOV  %-10s  sp=%-8s  dist=%.0f  Z=%.0f  tgt=(%.0f,%.0f,%.0f)  %s",
                            ok_set and "RESNAP" or "RESNAP_ERR", p.sp, dist, loc.Z,
                            p.tgt.x, p.tgt.y, p.tgt.z, sn))
                        disp_n = disp_n + 1
                        if ok_set then pawn_moved = pawn_moved + 1 end
                    end
                end
            end
        end
    end

    -- v2.49.0: QC redistribution — fill vacant entries from surplus clusters.
    local qc_entries = SPAWN_BY_CELL[persistent_delta.pattern]
    if qc_entries then
        local qc_n = runQCRedistribute(zone_sc, qc_entries)
        if qc_n > 0 then
            pawn_moved = pawn_moved + qc_n
            log(string.format("  QC_REDIST  cell=%s  reassigned=%d", persistent_delta.pattern, qc_n))
        end
    end

    -- Log when something moved. With DIAG_REENTRY_LOG, also log every re-entry tick
    -- (v2.39.5-diag2 behaviour — exposes pawn_scanned on no-op scans for free-fall diagnosis).
    local is_reentry_scan = zones_coverage[persistent_delta.pattern] ~= nil
    if pawn_moved > 0 or (DIAG_REENTRY_LOG and is_reentry_scan) then
        local reentry_tag = (DIAG_REENTRY_LOG and is_reentry_scan) and "  [REENTRY]" or ""
        log(string.format("SCAN #%d  cell=%s%s", scan_count, persistent_delta.pattern, reentry_tag))
        log(string.format("  PAWN  scanned=%d  matched=%d  moved=%d  skip=%d  landed=%d",
            pawn_scanned, pawn_matched, pawn_moved, pawn_skip, pawn_landed))
        local notes = ""
        if plyr_status ~= "ok_at_tgt" and plyr_status ~= "moved" then notes = notes .. " plyr=" .. plyr_status end
        if errors > 0 then notes = notes .. string.format(" ERR=%d", errors) end
        local summary = string.format("#%-3d  %-12s  P:n=%d m=%d mv=%d sk=%d ld=%d%s",
            scan_count, persistent_delta.pattern,
            pawn_scanned, pawn_matched, pawn_moved, pawn_skip, pawn_landed, notes)
        log("DONE " .. summary)
        print("\n[REFRFIX] " .. summary)
    end
    return pawn_moved
end

-- ─── Auto-scan on cell load ────────────────────────────────────────────────────
-- v2.17.0: Continuous 500ms probe loop mirroring Begone architecture.
-- v2.43.0: Continuous 500ms scan loop — no window, no WINDOW_CLOSE.
-- Fires every 500ms whenever an OOO cell is active. npc_landed dedup prevents
-- re-moving actors already placed this session (cleared only on ClientRestart).
-- spawn_claimed + entry_land_count cleared per ZONE_CHANGE for fresh Phase 1.
-- Late-streamers (distant rooms) are caught automatically as they appear.
local restartSeq   = 0
local last_pattern = nil

LoopAsync(500, function()
    local delta   = getActiveCellDelta()
    local pattern = delta and delta.pattern or nil
    if pattern ~= last_pattern then
        last_pattern = pattern
        if pattern then
            -- Clear per-zone state so Phase 1 claims start fresh on each zone entry.
            -- v2.46.0: npc_landed is NOT cleared here (reverts v2.45.0 change).
            -- Clearing it caused batch-2 actors (proximity-triggered Z2 spawns seen
            -- in Z1 context) to bypass dedup and get recycled as Z2 placements,
            -- producing log HITs that were invisible in-game (wrong physics context).
            -- npc_landed is cleared only on ClientRestart (global, session-scoped).
            spawn_claimed[pattern]    = {}
            entry_land_count[pattern] = {}
            placement_pending         = {}
            scan_open_at              = os.clock()
        end
        log(string.format("ZONE_CHANGE  new=%s  window=%.0fs", pattern or "nil", SCAN_WINDOW_SECS))
        print(string.format("\n[REFRFIX] ZONE_CHANGE  new=%s", pattern or "nil"))
    end
    if pattern then
        local elapsed = scan_open_at and (os.clock() - scan_open_at) or 0
        if elapsed <= SCAN_WINDOW_SECS then
            runScan()
        else
            -- Window closed: suppress scan to prevent re-processing settled actors.
            -- NPC_FLOOR logging still fires for any truly-new floor arrivals if window re-opens.
        end
    end
    return false
end)

RegisterHook("/Script/Engine.PlayerController:ClientRestart", function()
    restartSeq = restartSeq + 1
    -- Force zone re-detect and cache reset on loading-screen cell entry
    last_pattern      = nil
    target_cache      = {}
    scatter_offset    = {}  -- v2.33.0
    npc_landed        = {}
    spawn_claimed     = {}
    entry_land_count  = {}  -- v2.31.0
    zones_coverage    = {}
    player_landed     = false
    diag_count        = 0
    placement_pending = {}
    scan_open_at      = nil
    log(string.format("RESTART #%d  probe reset", restartSeq))
    print(string.format("\n[REFRFIX] RESTART #%d probe reset", restartSeq))
end)

-- ─── Diagnostic dump (F8 / SendSpellCast) ──────────────────────────────────
-- Logs EVERY Character/Pawn actor with: class name, full path, XYZ, and exact
-- distance to the nearest spawn-point entry (unlimited radius).
local function runDiagDump()
    log("=== DIAG DUMP ===")
    print("\n[REFRFIX] DIAG DUMP")
    local persistent_delta = getActiveCellDelta()
    if not persistent_delta then
        log("  no active Arondar cell, abort")
        return
    end
    local cell = persistent_delta.pattern
    log(string.format("  active cell: %s", cell))

    local total = 0
    for _, cls in ipairs(CHAR_CLASSES) do
        local ok_fa, pawns = pcall(function() return FindAllOf(cls) end)
        if not ok_fa or not pawns then goto nextcls_diag end
        for _, pawn in ipairs(pawns) do
            if not pawn or not pawn:IsValid() then goto nextpawn_diag end
            total = total + 1

            -- class name
            local cls_name = cls
            local ok_c, klass = pcall(function() return pawn:GetClass() end)
            if ok_c and klass and klass:IsValid() then
                local ok_n, n = pcall(function() return klass:GetName() end)
                if ok_n and n then cls_name = n end
            end

            -- full path (last 80 chars)
            local ok_fn, fn = pcall(function() return pawn:GetFullName() end)
            if not ok_fn or not fn then fn = "(no fullname)" end
            local path_60 = fn:sub(-80)

            -- location
            local ok_loc, loc = pcall(function() return pawn:K2_GetActorLocation() end)
            if not ok_loc or not loc then
                log(string.format("  [%d] %s  path=...%s  loc=ERR", total, cls_name, path_60))
                goto nextpawn_diag
            end

            -- nearest spawn-point distance (global search, no radius limit)
            local best_d = math.huge
            for _, cell_entries in pairs(SPAWN_BY_CELL) do
                for _, e in ipairs(cell_entries) do
                    local ddx = loc.X - e.ox
                    local ddy = loc.Y - e.oy
                    local ddz = loc.Z - e.oz
                    local d2  = ddx*ddx + ddy*ddy + ddz*ddz
                    if d2 < best_d then best_d = d2 end
                end
            end
            local dist_str = (best_d == math.huge) and "no_entries" or string.format("%.0f", math.sqrt(best_d))

            log(string.format("  [%d] %-40s  Z=%-8.0f  snap_dist=%-8s  ...%s",
                total, cls_name, loc.Z, dist_str, path_60))
            ::nextpawn_diag::
        end
        ::nextcls_diag::
    end
    log(string.format("=== DIAG END  total=%d ===", total))
    print(string.format("\n[REFRFIX] DIAG done, %d actors logged to %s", total, LOG_PATH))
    -- Verify actors we attempted to place this zone visit.
    local np = 0; for _ in pairs(placement_pending) do np=np+1 end
    log(string.format("=== PLACEMENT VERIFY  n=%d ===", np))
    local nv,nf,nd,nm = 0,0,0,0
    for fn, p in pairs(placement_pending) do
        local loc2 = nil
        for _, cls2 in ipairs(CHAR_CLASSES) do
            local ok2,pws2 = pcall(function() return FindAllOf(cls2) end)
            if ok2 and pws2 then for _, pw2 in ipairs(pws2) do
                if pw2 and pw2:IsValid() then
                    local ok3,fn3 = pcall(function() return pw2:GetFullName() end)
                    if ok3 and fn3==fn then
                        local ok4,l4 = pcall(function() return pw2:K2_GetActorLocation() end)
                        if ok4 and l4 then loc2=l4 end; break
                    end
                end
            end end
            if loc2 then break end
        end
        local sn = (fn:match("([^%.:%s]+)%s*$") or fn):sub(1,44)
        if not loc2 then
            nm=nm+1; log(string.format("  VERIFY  MISSING     sp=%-8s  %s", p.sp, sn))
        else
            local dist = math.sqrt((loc2.X-p.tgt.x)^2+(loc2.Y-p.tgt.y)^2+(loc2.Z-p.tgt.z)^2)
            local st = dist<200 and "VERIFIED" or (loc2.Z>=SKY_STASH_Z_MIN and "FAILED_SKY" or "DISPLACED")
            if st=="VERIFIED" then nv=nv+1 elseif st=="FAILED_SKY" then nf=nf+1 else nd=nd+1 end
            log(string.format("  VERIFY  %-10s  sp=%-8s  dist=%5.0f  Z=%7.0f  tgtZ=%7.0f  %s",
                st, p.sp, dist, loc2.Z, p.tgt.z, sn))
        end
    end
    log(string.format("=== VERIFY DONE  verified=%d  failed=%d  displaced=%d  missing=%d ===",nv,nf,nd,nm))
end
RegisterKeyBind(Key.F8, function() runDiagDump() end)

-- ─── Manual trigger ───────────────────────────────────────────────────────────
RegisterKeyBind(Key.F9, function()
    log("F9 manual scan")
    print("\n[REFRFIX] F9 manual scan")
    runScan()
end)

-- ─── Controller diagnostic trigger (SendSpellCast) ───────────────────────────
-- Player spell cast fires the diagnostic dump without needing keyboard access.
-- Set DIAG_SPELL_CAST_HOOK = false when Begone has SEND_SPELL_CAST_ENABLED = true.
if DIAG_SPELL_CAST_HOOK then
    RegisterHook("/Script/Altar.VPairedPawn:SendSpellCast", function(self)
        local ok_fn, fn = pcall(function() return self:get():GetFullName() end)
        if not (ok_fn and fn and fn:find("BP_OblivionPlayerCharacter_C", 1, true)) then return end
        runDiagDump()
    end)
end

-- ─── Startup ──────────────────────────────────────────────────────────────────
-- Truncate the log at boot unless DIAG_PRESERVE_BOOT_LOG is set.
if not DIAG_PRESERVE_BOOT_LOG then
    local f = io.open(LOG_PATH, "w"); if f then f:close() end
end

-- ─── Boot-time unit tests (Phase 9-C) ────────────────────────────────────────
-- Run tests.lua once per version bump; skip silently on subsequent boots.
local VERSION = "v2.51.0"
do
    local last_ver = ""
    local ok_f, last_f = pcall(function()
        return io.open("C:\\Temp\\OOO_REFRFix_tests_last.txt", "r")
    end)
    if ok_f and last_f then
        last_ver = last_f:read("*l") or ""
        last_f:close()
    end
    if last_ver ~= VERSION then
        local ok_t, tests = pcall(function() return require("tests") end)
        if ok_t and tests and tests.run_tests() then
            local wf = io.open("C:\\Temp\\OOO_REFRFix_tests_last.txt", "w")
            if wf then wf:write(VERSION); wf:close() end
            log("[TESTS PASSED " .. VERSION .. "]")
        else
            log("[TESTS FAILED " .. VERSION .. " -- check log for details]")
        end
    end
end

local total_spawn_entries = 0
for _, v in pairs(SPAWN_BY_CELL) do total_spawn_entries = total_spawn_entries + #v end
log(string.format("BOOT   %s  mode=%s  entries=%d  cells=%d  F8=diag  F9=scan",
    VERSION, MODE, total_spawn_entries, (function() local n=0; for _ in pairs(SPAWN_BY_CELL) do n=n+1 end; return n end)()))
print(string.format("\n[REFRFIX] BOOT %s  mode=%s  F8=diag  F9=scan", VERSION, MODE))
