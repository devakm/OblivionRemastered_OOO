-- OOO_REFRFix -- Lua version  (v1.9.0)
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

-- Idempotency: cache of actor fullname → absolute target {x,y,z}.
-- Set on first move, used on all subsequent scans to move back to same target
-- (handles TES4 engine snap-back) or skip if already there.
-- Reset on each ClientRestart so re-entering a cell starts fresh.
local target_cache = {}
local scan_count = 0
-- Set to true after the player is first moved to the XTEL landing position.
-- Cleared on ClientRestart. Prevents subsequent scans from snapping the player
-- back to the entrance after they have walked away from it.
local player_landed = false
-- Set of NPC/creature actor fullnames that have already been moved this cell visit.
-- Once moved, we never touch them again (same logic as player_landed).
-- Cleared on ClientRestart.
local npc_landed = {}

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
local SNAP_RADIUS_SQ = 3000 * 3000

-- Find the SPAWN_DELTAS entry nearest to (cx,cy,cz) within SNAP_RADIUS_SQ.
-- Returns the entry table (with tx/ty/tz patched target) or nil if nothing is close enough.
local function findBestSpawnEntry(cell_name, cx, cy, cz)
    local entries = SPAWN_BY_CELL[cell_name]
    if not entries then return nil end
    local best_e = nil
    local best_d = SNAP_RADIUS_SQ + 1
    for _, e in ipairs(entries) do
        local ddx = cx - e.ox
        local ddy = cy - e.oy
        local ddz = cz - e.oz
        local d2  = ddx*ddx + ddy*ddy + ddz*ddz
        if d2 < best_d then
            best_d = d2
            best_e = e
        end
    end
    return best_e, best_d
end

local function getActiveCellDelta()
    local world = UEHelpers.GetWorld()
    if not world or not world:IsValid() then return nil end
    local ok, levels = pcall(function() return world.StreamingLevels end)
    if not ok or not levels then return nil end
    for i = 1, #levels do
        local ok_l, lvl = pcall(function() return levels[i] end)
        if ok_l and lvl then
            local ok_iv, iv = pcall(function() return lvl:IsValid() end)
            if ok_iv and iv then
            local ok_p, pkg = pcall(function()
                return lvl.PackageNameToLoad:ToString()
            end)
            if ok_p and pkg then
                local base = pkg:match("[^/]+$") or pkg
                -- Match against LEVEL_DELTAS (longer suffixes first)
                for _, entry in ipairs(LEVEL_DELTAS) do
                    if base == entry.pattern then
                        return entry
                    end
                end
            end
            end  -- ok_iv
        end  -- ok_l
    end
    return nil
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

-- ─── Main scan ────────────────────────────────────────────────────────────────
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
local function runScan()
    scan_count = scan_count + 1

    -- Gate: check active cell FIRST, before any FindAllOf calls.
    local persistent_delta = getActiveCellDelta()
    if not persistent_delta then
        log(string.format("#%d SKIP", scan_count))
        print(string.format("\n[REFRFIX] #%d SKIP", scan_count))
        return
    end

    log(string.format("SCAN #%d  cell=%s  dx=%.1f dy=%.1f dz=%.1f",
        scan_count, persistent_delta.pattern,
        persistent_delta.dx, persistent_delta.dy, persistent_delta.dz))

    -- Pass 1: DISABLED (v1.6.3)
    -- The patched ESP already positions all VTESObjectRefComponent actors (statics, containers,
    -- etc.) at the correct Moranda geometry positions. Applying the cluster delta on top moved
    -- them to wrong positions far beneath the dungeon. NPCs/creatures are handled in Pass 2.
    local comps = {}
    local fa1_err = false
    local matched, moved, skipped, errors = 0, 0, 0, 0
    log(string.format("  REFR  pass1=DISABLED (ESP handles static REFR positions)"))

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
    local pawn_scanned, pawn_matched, pawn_moved, pawn_skip = 0, 0, 0, 0
    for _, cls in ipairs(CHAR_CLASSES) do
        local ok_fa, pawns = pcall(function() return FindAllOf(cls) end)
        if not ok_fa or not pawns or #pawns == 0 then goto nextcls end
        pawn_scanned = pawn_scanned + #pawns

        for _, pawn in ipairs(pawns) do
            if not pawn or not pawn:IsValid() then goto nextpawn end

            -- Player: handle with XTEL absolute landing target, not cluster delta.
            if player_char and pawn == player_char then
                if player_landed then
                    plyr_status = "ok_at_tgt"
                    -- Already placed this cell visit — never move the player again.
                    log("  PLYR  already landed this visit, skip")
                    goto nextpawn
                end
                local landing = PLAYER_LANDING[persistent_delta.pattern]
                if not landing then
                    plyr_status = "no_xtel"
                    log("  PLYR  no XTEL data for this cell, skip")
                    goto nextpawn
                end
                local ok_ploc, ploc = pcall(function() return pawn:K2_GetActorLocation() end)
                if not ok_ploc or not ploc then plyr_status = "no_loc"; goto nextpawn end
                local ddx = ploc.X - landing.x
                local ddy = ploc.Y - landing.y
                local ddz = ploc.Z - landing.z
                if (ddx*ddx + ddy*ddy + ddz*ddz) < (200*200) then
                    player_landed = true
                    plyr_status = "ok_at_tgt"
                    log(string.format("  PLYR  at landing (%.0f,%.0f,%.0f)  skip", ploc.X, ploc.Y, ploc.Z))
                else
                    local ok_set = pcall(function()
                        pawn:K2_SetActorLocation({X=landing.x, Y=landing.y, Z=landing.z}, false, {}, true)
                    end)
                    if ok_set then
                        pawn_moved = pawn_moved + 1
                        player_landed = true
                        plyr_status = "moved"
                        log(string.format("  PLYR  moved (%.0f,%.0f,%.0f)->(%.0f,%.0f,%.0f)",
                            ploc.X, ploc.Y, ploc.Z, landing.x, landing.y, landing.z))
                    else
                        errors = errors + 1
                        plyr_status = "err"
                        log("  PLYR  K2_SetActorLocation failed")
                    end
                end
                goto nextpawn
            end

            local delta2, pawn_fn = getDeltaForActor(pawn, persistent_delta)
            if not delta2 then goto nextpawn end
            if pawn_fn and pawn_fn:find("Controller", 1, true) then goto nextpawn end

            -- Skip if already moved this cell visit (prevents TES4 snap-back fight).
            if npc_landed[pawn_fn] then
                pawn_skip = pawn_skip + 1
                goto nextpawn
            end

            local ok_cur0, cur0 = pcall(function() return pawn:K2_GetActorLocation() end)
            if not ok_cur0 or not cur0 then goto nextpawn end
            if math.abs(cur0.X) < 5 and math.abs(cur0.Y) < 5 and math.abs(cur0.Z) < 5 then
                goto nextpawn
            end

            pawn_matched = pawn_matched + 1

            -- Find nearest spawn-point entry (no radius limit for metrics).
            local snap_e, snap_d = findBestSpawnEntry(persistent_delta.pattern, cur0.X, cur0.Y, cur0.Z)
            local snap_dist = snap_e and math.sqrt(snap_d) or -1

            -- Compute absolute target:
            --   SNAP match  → tgt = (tx, ty, tz) directly (patched ESP pos, CS-verified).
            --                  Applied regardless of Z — handles floor-level actors (e.g. BloodClotCave).
            --   No snap + Z >= 3000 → cluster-average fallback (sky-stash: Arondar/Barastas/Narind).
            --   No snap + Z <  3000 → skip (actor already at correct geometry position per ESP).
            local tgt_x, tgt_y, tgt_z
            local match_tag
            if snap_e and snap_d <= SNAP_RADIUS_SQ then
                tgt_x = snap_e.tx
                tgt_y = snap_e.ty
                tgt_z = snap_e.tz
                match_tag = string.format("SNAP gap=%.0f", snap_dist)
            else
                -- No spawn-point entry: guard fallback with Z threshold.
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
                target_cache[key] = { x = tgt_x, y = tgt_y, z = tgt_z }
            end
            local tgt = target_cache[key]

            -- Short class name for logging.
            local short_cls = (pawn_fn:match("BP_([^%._]+)") or pawn_fn:match("([^%.:%s]+)%s*$") or "?"):sub(1, 24)
            -- Spawn-point origin for logging.
            local sp_str = snap_e and string.format("(%.0f,%.0f,%.0f)", snap_e.ox, snap_e.oy, snap_e.oz) or "none"

            -- Check idempotency: already at target?
            local ddx = cur0.X - tgt.x
            local ddy = cur0.Y - tgt.y
            local ddz = cur0.Z - tgt.z
            local dist_to_tgt = math.sqrt(ddx*ddx + ddy*ddy + ddz*ddz)

            if dist_to_tgt < 50 then
                pawn_skip = pawn_skip + 1
                npc_landed[pawn_fn] = true
                log(string.format("  NPC  %-24s  cur=(%.0f,%.0f,%.0f)  sp=%s  %s  tgt=(%.0f,%.0f,%.0f)  dist_to_tgt=%.0f  SKIP",
                    short_cls, cur0.X, cur0.Y, cur0.Z, sp_str, match_tag, tgt.x, tgt.y, tgt.z, dist_to_tgt))
                goto nextpawn
            end

            -- Move.
            if MODE == "probe" then
                log(string.format("  NPC  %-24s  cur=(%.0f,%.0f,%.0f)  sp=%s  %s  tgt=(%.0f,%.0f,%.0f)  dist_to_tgt=%.0f  PROBE",
                    short_cls, cur0.X, cur0.Y, cur0.Z, sp_str, match_tag, tgt.x, tgt.y, tgt.z, dist_to_tgt))
                pawn_moved = pawn_moved + 1
                npc_landed[pawn_fn] = true
            else
                local ok_set = pcall(function()
                    pawn:K2_SetActorLocation({X=tgt.x, Y=tgt.y, Z=tgt.z}, false, {}, true)
                end)
                if ok_set then
                    pawn_moved = pawn_moved + 1
                    npc_landed[pawn_fn] = true
                    log(string.format("  NPC  %-24s  cur=(%.0f,%.0f,%.0f)  sp=%s  %s  tgt=(%.0f,%.0f,%.0f)  dist_to_tgt=%.0f  MOVED",
                        short_cls, cur0.X, cur0.Y, cur0.Z, sp_str, match_tag, tgt.x, tgt.y, tgt.z, dist_to_tgt))
                else
                    errors = errors + 1
                    log(string.format("  NPC  %-24s  cur=(%.0f,%.0f,%.0f)  %s  ERR K2_SetActorLocation",
                        short_cls, cur0.X, cur0.Y, cur0.Z, match_tag))
                end
            end

            ::nextpawn::
        end
        ::nextcls::
    end

    -- File log: verbose PLYR + PAWN counts
    log(string.format("  PAWN  scanned=%d  matched=%d  moved=%d  skip=%d",
        pawn_scanned, pawn_matched, pawn_moved, pawn_skip))

    -- Summary: verbose DONE line to file, single compact line to UE4SS console.
    local notes = ""
    if plyr_status ~= "ok_at_tgt" and plyr_status ~= "moved" then notes = notes .. " plyr=" .. plyr_status end
    if errors > 0 then notes = notes .. string.format(" ERR=%d", errors) end
    if fa1_err then notes = notes .. " FA1ERR" end
    local summary = string.format("#%-3d  %-12s  R:n=%d m=%d mv=%d sk=%d  P:n=%d m=%d mv=%d sk=%d%s",
        scan_count, persistent_delta.pattern,
        #comps, matched, moved, skipped,
        pawn_scanned, pawn_matched, pawn_moved, pawn_skip,
        notes)
    log("DONE " .. summary)
    print("\n[REFRFIX] " .. summary)
end

-- ─── Auto-scan on cell load ────────────────────────────────────────────────────
-- ClientRestart fires when the pawn respawns (= new cell entered).
-- Scan at 5s / 10s / 20s to catch actors that spawn late.
local restartSeq = 0

RegisterHook("/Script/Engine.PlayerController:ClientRestart", function()
    restartSeq = restartSeq + 1
    local seq = restartSeq
    -- Reset target cache: new cell load means actors respawn at save positions
    target_cache = {}
    player_landed = false
    npc_landed = {}
    log(string.format("RESTART #%d cache cleared", seq))
    print(string.format("\n[REFRFIX] RESTART #%d cache cleared", seq))

    for _, ms in ipairs({2000, 5000, 10000, 20000, 30000}) do
        LoopAsync(ms, function()
            if restartSeq == seq then
                runScan()
            end
            return false  -- fire once, don't loop
        end)
    end
end)

-- ─── Diagnostic dump (F8) ────────────────────────────────────────────────────
-- Logs EVERY Character/Pawn actor with: class name, full path, XYZ, and exact
-- distance to the nearest spawn-point entry (unlimited radius).
-- Use this to find where the actual Arondar marauders are and how far they are
-- from spawn-point entries in SPAWN_DELTAS — without moving anything.
RegisterKeyBind(Key.F8, function()
    log("=== F8 DIAG DUMP ===")
    print("\n[REFRFIX] F8 DIAG DUMP")
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

            -- nearest spawn-point distance (no radius limit)
            local entries = SPAWN_BY_CELL[cell]
            local best_d = math.huge
            if entries then
                for _, e in ipairs(entries) do
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
end)

-- ─── Manual trigger ───────────────────────────────────────────────────────────
RegisterKeyBind(Key.F9, function()
    log("F9 manual scan")
    print("\n[REFRFIX] F9 manual scan")
    runScan()
end)

-- ─── Startup ──────────────────────────────────────────────────────────────────
local total_spawn_entries = 0
for _, v in pairs(SPAWN_BY_CELL) do total_spawn_entries = total_spawn_entries + #v end
log(string.format("BOOT   v1.9.0  mode=%s  entries=%d  cells=%d  F8=diag  F9=scan",
    MODE, total_spawn_entries, (function() local n=0; for _ in pairs(SPAWN_BY_CELL) do n=n+1 end; return n end)()))
print(string.format("\n[REFRFIX] BOOT v1.9.0  mode=%s  F8=diag  F9=scan", MODE))
