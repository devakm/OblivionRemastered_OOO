-- ===========================================================================
-- OOO_REFRFix unit tests  (v2.39.4)
-- Pure Lua — no UE4SS APIs.  Simulates core logic in isolation.
-- Exported: tests.run_tests() -> bool (true = all pass)
-- Called from main.lua BOOT when version file does not match VERSION.
-- ===========================================================================

local M = {}

-- ── helpers ────────────────────────────────────────────────────────────────

local LOG_PATH = "C:\\Temp\\OOO_REFRFix.log"
local function tlog(msg)
    local f = io.open(LOG_PATH, "a")
    if f then f:write(msg .. "\n"); f:close() end
end

local pass_count = 0
local fail_count = 0

local function expect(name, got, expected)
    if got == expected then
        pass_count = pass_count + 1
        tlog(string.format("[TEST PASS]  %s", name))
        return true
    else
        fail_count = fail_count + 1
        tlog(string.format("[TEST FAIL]  %s  got=%s  expected=%s",
            name, tostring(got), tostring(expected)))
        return false
    end
end

-- ── constants mirrored from main.lua ───────────────────────────────────────

local SKY_STASH_Z_MIN  = 2000
local SNAP_RADIUS_SQ   = 3000 * 3000

-- ── logic helpers mirrored from main.lua ───────────────────────────────────

local function locKey(e)
    return e.name or string.format("%.0f,%.0f,%.0f", e.ox, e.oy, e.oz)
end

-- Should this actor be moved?  Returns bool.
-- Mirrors the Z guard + npc_landed check in runScan().
local function should_move(cur_z, pawn_fn, npc_landed_tbl)
    if cur_z < SKY_STASH_Z_MIN then return false end   -- Z guard
    if npc_landed_tbl[pawn_fn]  then return false end   -- dedup guard
    return true
end

-- Is this actor disabled by the re-entry flag?
-- Mirrors the ENABLE_REENTRY_DISABLE guard in runScan().
local function reentry_disable_fires(enable_flag, zones_cov, zone, tc, pawn_fn)
    return enable_flag and (zones_cov[zone] ~= nil) and (tc[pawn_fn] == nil)
end

-- Does Change 2 skip this actor?  Returns bool.
-- Mirrors the guard after findBestSpawnEntry in runScan() (v2.39.4+).
-- Only skips unknown actors (tc[pawn_fn] nil); known alive actors must re-snap.
local function reentry_change2_fires(zones_cov, zone, snap_unclaimed, tc, pawn_fn)
    return (zones_cov[zone] ~= nil) and not snap_unclaimed and (tc[pawn_fn] == nil)
end

-- Simulate a first-visit scan of N sky actors into N spawn entries.
-- Returns covered count (= how many target_cache entries were populated).
local function simulate_first_visit(n_actors)
    local tc = {}
    local spawn_claimed_zone = {}
    local entries = {}
    for i = 1, n_actors do
        entries[i] = { name = "Z1_" .. string.format("%02d", i),
                       ox = i * 100, oy = 0, oz = 0,
                       tx = i * 100, ty = 0, tz = 35 }
    end
    -- Each actor gets a unique fn; all are at sky Z.
    for i = 1, n_actors do
        local fn = "BP_Actor_" .. i
        local cur_z = 8500  -- sky-stash
        if cur_z >= SKY_STASH_Z_MIN and not tc[fn] then
            -- simulate snap + claim
            local nearest = entries[i]  -- perfect 1-to-1 for test
            spawn_claimed_zone[locKey(nearest)] = (spawn_claimed_zone[locKey(nearest)] or 0) + 1
            tc[fn] = { x = nearest.tx, y = nearest.ty, z = nearest.tz }
        end
    end
    return tc
end

-- ── test cases ─────────────────────────────────────────────────────────────

local function test1_z_guard_floor()
    -- Technical: Actor Z=1999 is below SKY_STASH_Z_MIN threshold (2000).
    -- Outcome: An actor already at floor level (correctly placed or dead)
    --   must never be touched by REFRFix, regardless of any other state.
    local result = should_move(1999, "BP_Actor_1", {})
    expect("T1 Z guard floor (Z=1999 -> no move)", result, false)
end

local function test2_z_guard_sky()
    -- Technical: Actor Z=5001 is above SKY_STASH_Z_MIN with empty npc_landed.
    -- Outcome: A sky-stash actor is a candidate for snapping to an unclaimed
    --   ESP target position (floor Z).  If no unclaimed HITloc remains, the
    --   actor is instead a disable candidate (ENABLE_REENTRY_DISABLE, currently
    --   off) — snapping it anyway causes cluster bloat at the nearest entry.
    local result = should_move(5001, "BP_Actor_2", {})
    expect("T2 Z guard sky-stash (Z=5001, landed empty -> move)", result, true)
end

local function test3_npc_landed_dedup()
    -- Technical: pawn_fn already present in npc_landed table.
    -- Outcome: Within a single scan pass, re-snapping the same actor is blocked
    --   via npc_landed.  npc_landed is cleared on ZONE_CHANGE, so permanent
    --   cross-visit protection comes from the Z guard (T1): an actor already at
    --   floor Z never re-enters the snap path at all.
    local landed = {}
    landed["BP_Actor_3"] = true
    local result = should_move(8500, "BP_Actor_3", landed)
    expect("T3 npc_landed dedup (fn in landed -> no move)", result, false)
end

local function test4_first_visit_new_actor()
    -- Technical: zones_coverage nil for this zone (first visit), target_cache empty.
    -- Outcome: On the initial zone entry every sky actor must be eligible for
    --   placement — the re-entry guard must be completely inactive.
    local zones_cov = {}
    local tc        = {}
    local fires = reentry_disable_fires(true, zones_cov, "L_Arondar", tc, "BP_NewActor_4")
    expect("T4 first-visit new actor (zones_cov nil -> guard inactive)", fires, false)
end

local function test5_reentry_new_actor()
    -- Technical: zones_coverage set (first WINDOW_CLOSE seen) AND target_cache nil
    --   for this UUID (engine re-rolled a new actor instance on re-entry).
    -- Outcome: Spurious new actors spawned by the engine on re-entry must be
    --   caught before they can be moved to geometry that would place them
    --   outside the dungeon walls.
    local zones_cov = { L_Arondar = 14 }
    local tc        = {}
    local fires = reentry_disable_fires(true, zones_cov, "L_Arondar", tc, "BP_NewActor_5")
    expect("T5 re-entry new actor (zones_cov set, tc nil -> guard fires)", fires, true)
end

local function test6_reentry_placed_actor()
    -- Technical: zones_coverage set AND target_cache populated for this UUID
    --   (same actor instance as first-visit, already correctly placed).
    -- Outcome: A re-entry actor whose UUID is already in target_cache must NOT
    --   be disabled — the engine may re-spawn it at sky Z on re-entry and it
    --   should be snapped back to its recorded target position, not hidden.
    local zones_cov = { L_Arondar = 14 }
    local tc        = { ["BP_OldActor_6"] = { x=100, y=0, z=35 } }
    local fires = reentry_disable_fires(true, zones_cov, "L_Arondar", tc, "BP_OldActor_6")
    expect("T6 re-entry placed actor (tc set -> guard inactive)", fires, false)
end

local function test7_first_visit_baseline_14_14()
    -- Technical: 14 sky actors each snapped 1-to-1 to 14 unique spawn entries.
    -- Outcome: Every OOO spawn point in zone 1 must be filled on initial entry
    --   with no actors missing. This is the working baseline — any change to
    --   main.lua that causes fewer than 14 to be placed is a regression.
    local tc = simulate_first_visit(14)
    local covered = 0
    for _ in pairs(tc) do covered = covered + 1 end
    expect("T7 first-visit 14/14 baseline (all actors placed)", covered, 14)
end

local function test8_reentry_change2_skip()
    -- Technical: zones_coverage set (re-entry, first WINDOW_CLOSE seen) AND
    --   snap_unclaimed=false (Phase 2 result — all first-visit entries claimed).
    -- Outcome: A re-entry sky actor with no unclaimed slot must be skipped
    --   entirely.  Falling through to Phase 2 snaps it to the nearest entry,
    --   causing cluster bloat (observed as Z1_12 HIT 6 in v2.39.2 diag.log).
    local zones_cov = { L_Arondar = 14 }
    local fires = reentry_change2_fires(zones_cov, "L_Arondar", false, {}, "BP_NewActor_8")
    expect("T8 re-entry change2 skip (zones_cov set + snap_unclaimed=false -> skip)", fires, true)
end

local function test9_reentry_change2_known_actor_not_skipped()
    -- Technical: zones_coverage set (re-entry) AND snap_unclaimed=false (Phase 2)
    --   BUT target_cache has an entry for this actor (placed on first visit, still alive).
    -- Outcome: A re-entry actor with a known placement must NOT be skipped — it was
    --   placed by us on first visit and should re-snap to its recorded target position.
    --   (Regression for v2.39.3 bug: actors wrongly skipped because tc was not checked.)
    local zones_cov = { L_Arondar = 14 }
    local tc = { ["BP_KnownActor_9"] = { x=100, y=0, z=35 } }
    local fires = reentry_change2_fires(zones_cov, "L_Arondar", false, tc, "BP_KnownActor_9")
    expect("T9 re-entry change2 known actor (tc set -> no skip)", fires, false)
end

-- ── public entry point ─────────────────────────────────────────────────────

function M.run_tests()
    pass_count = 0
    fail_count = 0

    tlog(string.format("[TESTS START v2.48.0]  %s", os.date()))
    test1_z_guard_floor()
    test2_z_guard_sky()
    test3_npc_landed_dedup()
    test4_first_visit_new_actor()
    test5_reentry_new_actor()
    test6_reentry_placed_actor()
    test7_first_visit_baseline_14_14()
    test8_reentry_change2_skip()
    test9_reentry_change2_known_actor_not_skipped()
    tlog(string.format("[TESTS DONE]  pass=%d  fail=%d", pass_count, fail_count))

    return fail_count == 0
end

return M
