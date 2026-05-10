-- ===========================================================================
-- HARD BLOCK: C:\games\Steam\steamapps\common\ is READ-ONLY.
-- The ONLY permitted ops on that path are Get-Content / Select-String reads.
-- NEVER write, edit, copy, move, or patch any file under that path. Ever.
-- Violations: 2026-03-14 (Copy-Item), 2026-03-22 (Set-Content in-place patch)
-- ===========================================================================-- Begone v1.3.18
-- Plugin-agnostic UE4SS actor suppressor for Oblivion Remastered.
--
-- Loads *.json config files from two locations and suppresses actors each time
-- a matching cell loads.  Designed so any mod can ship a JSON config without
-- touching shared Lua scripts.
--
-- Config search order (both scanned; entries from all files are merged):
--   1. ue4ss\Mods\Begone\Config\               (mod-local, for mod developers)
--   2. ..\..\Content\Dev\ObvData\Data\Begone\  (game Data path, for end users)
--
-- Config format  (<anything>.json):
--   {
--     "Plugin": "SomeMod.esp",
--     "Cells": {
--       "L_LevelName16C": [
--         {
--           "name": "BP_SomeActor_C_0",
--           "cls": "BP_SomeActor_C",
--           "actions": ["hide", "collision"]
--         }
--       ]
--     }
--   }
--
-- Supported actions (may be combined in any order):
--   "hide"      → actor:SetActorHiddenInGame(true)
--   "collision" → actor:SetActorEnableCollision(false)
--   "niagara"   → NiagaraComponent:Deactivate()  (kills dynamic-light spawner)
--
-- Cell name key: the 16-char-truncated UE5 streaming level package basename.
-- (e.g. "L_DrownedHopesCa", not "L_DrownedHopesCave")
--
-- Install:
--   Copy Mods/Begone/ to  <game>\OblivionRemastered\Binaries\Win64\ue4ss\Mods\
--   Add to mods.txt:  Begone : 1
--   Drop plugin JSON files in  ue4ss\Mods\Begone\Config\  or in the Data path.
-- ─────────────────────────────────────────────────────────────────────────────

local LOG_PATH = "C:/Temp/Begone.log"

-- Set to true to log every individual SUPR action (useful for diagnosing missed
-- suppressions or wrong actor names).  Set to false for normal play — only
-- BOOT, LOAD, and RESTART lines are written.
local VERBOSE = true

-- Config directories (relative to Binaries\Win64\ working directory)
local CONFIG_DIRS = {
    "ue4ss\\Mods\\Begone\\Config",
    "..\\..\\Content\\Dev\\ObvData\\Data\\Begone",
}

-- Truncate log at boot so each game session starts fresh.
do local f = io.open(LOG_PATH, "w"); if f then f:close() end end

local function log(msg)
    local f = io.open(LOG_PATH, "a")
    if f then f:write(os.date("[%Y-%m-%d %H:%M:%S] ") .. msg .. "\n"); f:close() end
end

-- ─── Minimal JSON parser ─────────────────────────────────────────────────────
-- Handles our fixed schema only: top-level "Plugin" string + "Cells" object.
-- Collapses whitespace so patterns work across original newlines.
-- Supports both "action":"x" (single, backward compat) and "actions":["x","y"].
local function parseConfig(path)
    local f = io.open(path, "r")
    if not f then log("LOAD  ERR  cannot open: " .. path); return nil, nil end
    local text = f:read("*a"); f:close()
    text = text:gsub("%s+", " ")
    local plugin = text:match('"Plugin"%s*:%s*"([^"]+)"') or "unknown"
    local cells = {}
    -- %b[] matches balanced [...] so nested "actions":[...] don't truncate the outer match.
    for level, br_arr in text:gmatch('"(L_[^"]+)"%s*:%s*(%b[])') do
        local arr_str = br_arr:sub(2, -2)  -- strip enclosing [ ]
        cells[level] = {}
        for obj in arr_str:gmatch('%b{}') do
            local name = obj:match('"name"%s*:%s*"([^"]+)"')
            local cls  = obj:match('"cls"%s*:%s*"([^"]+)"')
            if name and cls then
                -- Parse actions: "actions":["a","b"] takes priority; fall back to "action":"a"
                local actions = {}
                local arr = obj:match('"actions"%s*:%s*%[(.-)%]')
                if arr then
                    for a in arr:gmatch('"([^"]+)"') do table.insert(actions, a) end
                else
                    local single = obj:match('"action"%s*:%s*"([^"]+)"')
                    if single then table.insert(actions, single) end
                end
                if #actions > 0 then
                    table.insert(cells[level], {name=name, cls=cls, actions=actions})
                end
            end
        end
    end
    return plugin, cells
end

-- ─── Config loader ───────────────────────────────────────────────────────────
-- Scans both CONFIG_DIRS for *.json, merges all entries into one table.
local function loadAllConfigs()
    local combined = {}
    local n_cfg = 0
    for _, dir in ipairs(CONFIG_DIRS) do
        local p = io.popen(string.format('dir /b /a-d "%s\\*.json" 2>nul', dir))
        if p then
            for fname in p:lines() do
                local plugin, cells = parseConfig(dir .. "\\" .. fname)
                if cells then
                    local n_cells = 0
                    for level, entries in pairs(cells) do
                        if not combined[level] then combined[level] = {} end
                        for _, e in ipairs(entries) do table.insert(combined[level], e) end
                        n_cells = n_cells + 1
                    end
                    log(string.format("LOAD  %-46s  plugin=%-38s  cells=%d",
                        fname, plugin, n_cells))
                    n_cfg = n_cfg + 1
                end
            end
            p:close()
        end
    end
    local n_levels, n_entries = 0, 0
    for _, v in pairs(combined) do n_levels = n_levels + 1; n_entries = n_entries + #v end
    log(string.format("BOOT  configs=%d  levels=%d  entries=%d", n_cfg, n_levels, n_entries))
    return combined
end

local SUPPRESS   = loadAllConfigs()
local UEHelpers  = require("UEHelpers")
local restartSeq = 0
local logged_done = {}  -- fn..":"..action → true; log-dedup only (NOT an action gate)
local runSuppressPass  -- forward declared

-- ─── World path probe ────────────────────────────────────────────────────────
-- Reads StreamingLevels, returns two sorted pipe-separated strings:
--   vis = only bIsVisible=true interior levels (short basename)
--   all = all interior levels; loaded-but-invisible prefixed with [H]
local function getAllInteriorLevels()
    local ok1, world = pcall(function() return UEHelpers.GetWorld() end)
    if not (ok1 and world and world:IsValid()) then return nil, nil end
    local ok2, slevels = pcall(function() return world.StreamingLevels end)
    if not (ok2 and slevels) then return nil, nil end
    local vis_list, all_list = {}, {}
    for i = 1, #slevels do
        local sl = slevels[i]
        if sl and sl:IsValid() then
            local ok4, pkg = pcall(function() return sl.PackageNameToLoad:ToString() end)
            if ok4 and pkg and (
                pkg:find("/Maps/Interiors/", 1, true) or
                pkg:find("L_DrownedHopesCa0", 1, true)
            ) then
                local short = pkg:match("([^/]+)$") or pkg
                local ok3, vis = pcall(function() return sl.bIsVisible end)
                local is_vis = ok3 and vis
                table.insert(all_list, is_vis and short or ("[H]"..short))
                if is_vis then table.insert(vis_list, short) end
            end
        end
    end
    table.sort(vis_list); table.sort(all_list)
    local v = #vis_list > 0 and table.concat(vis_list, "|") or "NONE"
    local a = #all_list > 0 and table.concat(all_list, "|") or "NONE"
    return v, a
end

-- Dumps ALL streaming level PackageNameToLoad values to the log (diagnostic only).
-- Call on [CHANGED] events to capture the raw path when zone 2 fails to detect.
local function dumpAllPackages()
    local ok1, world = pcall(function() return UEHelpers.GetWorld() end)
    if not (ok1 and world and world:IsValid()) then return end
    local ok2, slevels = pcall(function() return world.StreamingLevels end)
    if not (ok2 and slevels) then return end
    local pkgs = {}
    for i = 1, #slevels do
        local sl = slevels[i]
        if sl and sl:IsValid() then
            local ok4, pkg = pcall(function() return sl.PackageNameToLoad:ToString() end)
            local ok3, vis = pcall(function() return sl.bIsVisible end)
            if ok4 and pkg and pkg ~= "" then
                local vis_flag = (ok3 and vis) and "V" or "H"
                table.insert(pkgs, vis_flag .. pkg)
            end
        end
    end
    table.sort(pkgs)
    log("[PKG_DUMP] " .. (#pkgs > 0 and table.concat(pkgs, "  ") or "(empty)"))
end

-- Converts a pipe-separated vis string into a set table: { name=true, ... }
local function toSet(pipe_str)
    local s = {}
    if pipe_str and pipe_str ~= "NONE" then
        for name in pipe_str:gmatch("[^|]+") do s[name] = true end
    end
    return s
end

-- Returns a sorted array of keys in cur that are absent from prev.
local function setDiff(cur, prev)
    local new = {}
    for k in pairs(cur) do if not prev[k] then table.insert(new, k) end end
    table.sort(new)
    return new
end

local function probeLog(tag, vis, all)
    log(string.format("PROBE [%s]  vis=%s  all=%s", tag, vis or "NONE", all or "NONE"))
end

-- ─── Probe loop ──────────────────────────────────────────────────────────────
-- Runs every 1s via outer LoopAsync (do NOT call LoopAsync inside probeLoop —
-- that would spawn an extra chain each tick, causing exponential runaway).
-- [CHANGED]: visible interior set grew — fires targeted suppress for new zones.
local last_set      = {}
local last_vis_str  = "NONE"

-- ─── Water state tracker ─────────────────────────────────────────────────────
-- Declared here so probeLoop() can reference them (must be in lexical scope
-- before the function is defined; Lua locals are not visible before declaration).
local is_underwater    = false
local in_water_cave   = false
local in_WaterBodyLake = false   -- player overlapping WaterBodyLake (unconditional)
local in_VWaterVolume  = false   -- player overlapping VWaterVolume (unconditional)

-- Caves known to contain VWaterVolume actors (enables the interior water check).
local WATER_CAVES = {
    ["L_DrownedHopesCa"]   = true,
    ["L_DrownedHopesCa02"] = true,
}

local function probeLoop()
    local vis, all = getAllInteriorLevels()
    local vis_str  = vis or "NONE"
    local cur_set  = toSet(vis)
    local newly    = setDiff(cur_set, last_set)
    local changed  = vis_str ~= last_vis_str

    if changed then
        probeLog("CHANGED", vis, all)
        dumpAllPackages()
        last_set     = cur_set
        last_vis_str = vis_str
        -- Update water-cave state.
        if vis_str == "NONE" then
            in_water_cave = false
            is_underwater = false
        end
        for _, z in ipairs(newly) do
            if WATER_CAVES[z] then in_water_cave = true end
        end
        if #newly > 0 then
            logged_done = {}
            local zones = newly  -- capture for closures
            for _, ms in ipairs({500, 2000, 5000}) do
                LoopAsync(ms, function() runSuppressPass(zones, VERBOSE); return false end)
            end
        end
    end
end
LoopAsync(1000, function() probeLoop(); return false end)

-- ─── Suppress pass ───────────────────────────────────────────────────────────
-- zone_list: array of short zone names to process.
-- nil is a safety fallback only — callers must pass the current visible zone list.
-- Actions are always applied (idempotent). logged_done only deduplicates log output.
local function getEntries(zone_list)
    if not zone_list then
        local all = {}
        for _, entries in pairs(SUPPRESS) do
            for _, e in ipairs(entries) do table.insert(all, e) end
        end
        return all
    end
    local result = {}
    for _, z in ipairs(zone_list) do
        if SUPPRESS[z] then
            for _, e in ipairs(SUPPRESS[z]) do table.insert(result, e) end
        end
    end
    return result
end

runSuppressPass = function(zone_list, verbose)
    local entries = getEntries(zone_list)
    if #entries == 0 then return end
    local nc_map  = {}
    local plc_map = {}
    local function buildMap(cls, dest)
        local ok, all = pcall(function() return FindAllOf(cls) end)
        if not (ok and all) then return end
        for _, comp in ipairs(all) do
            if comp and comp:IsValid() then
                local ok2, ofn = pcall(function() return comp:GetOwner():GetFullName() end)
                if ok2 and ofn then
                    if not dest[ofn] then dest[ofn] = {} end
                    table.insert(dest[ofn], comp)
                end
            end
        end
    end
    buildMap("NiagaraComponent",    nc_map)
    buildMap("PointLightComponent", plc_map)
    buildMap("SpotLightComponent",  plc_map)
    buildMap("RectLightComponent",  plc_map)

    for _, e in ipairs(entries) do
        local ok_fa, actors = pcall(function() return FindAllOf(e.cls) end)
        if ok_fa and actors then
            for _, actor in ipairs(actors) do
                if actor and actor:IsValid() then
                    local ok_fn, fn = pcall(function() return actor:GetFullName() end)
                    local _ms, _me
                    if ok_fn then _ms, _me = fn:find(e.name, 1, true) end
                    if _ms and not fn:sub(_me+1, _me+1):match("[%w]") then
                        if verbose and not logged_done[fn .. ":match"] then
                            log(string.format("  MATCH %-42s  fn=%s", e.name, fn))
                            logged_done[fn .. ":match"] = true
                        end
                        for _, action in ipairs(e.actions) do
                            local key = fn .. ":" .. action
                            if action == "hide" then
                                local ok = pcall(function() actor:SetActorHiddenInGame(true) end)
                                if verbose and not logged_done[key] then
                                    log(string.format("  SUPR  %-9s  %-42s  %s", "hide", e.name, ok and "OK" or "ERR"))
                                    logged_done[key] = true
                                end
                            elseif action == "collision" then
                                local ok = pcall(function() actor:SetActorEnableCollision(false) end)
                                if verbose and not logged_done[key] then
                                    log(string.format("  SUPR  %-9s  %-42s  %s", "collision", e.name, ok and "OK" or "ERR"))
                                    logged_done[key] = true
                                end
                            elseif action == "niagara" then
                                local n_nc, n_plc = 0, 0
                                local ncs = nc_map[fn]
                                if ncs then
                                    for _, nc in ipairs(ncs) do
                                        if nc and nc:IsValid() then pcall(function() nc:Deactivate() end); n_nc = n_nc + 1 end
                                    end
                                end
                                local plcs = plc_map[fn]
                                if plcs then
                                    for _, plc in ipairs(plcs) do
                                        if plc and plc:IsValid() then
                                            if not pcall(function() plc:SetIntensity(0.0) end) then
                                                pcall(function() plc.bVisible = false end)
                                            end
                                            n_plc = n_plc + 1
                                        end
                                    end
                                end
                                if verbose and not logged_done[key] then
                                    log(string.format("  SUPR  %-9s  %-42s  OK (nc=%d si=%d)", "niagara", e.name, n_nc, n_plc))
                                    logged_done[key] = true
                                end
                            end
                        end
                    end
                end
            end
        end
    end
end

-- ─── Periodic re-suppress ────────────────────────────────────────────────────
-- Full-scan fallback every 30s; covers zones that reload outside a CHANGED event.
-- IMPORTANT: only suppresses the currently-visible zones — never fires globally.
local function periodicSuppress(seq)
    if restartSeq ~= seq then return end
    local ok_p, pawn = pcall(function() return UEHelpers.GetPlayerCharacter() end)
    if ok_p and pawn and pawn:IsValid() then
        local vis, _ = getAllInteriorLevels()
        local cur_zones = {}
        if vis and vis ~= "NONE" then
            for name in vis:gmatch("[^|]+") do
                if SUPPRESS[name] then table.insert(cur_zones, name) end
            end
        end
        if #cur_zones > 0 then
            logged_done = {}
            runSuppressPass(cur_zones, false)
        end
    end
end

-- Confirmed working UE4SS API for class name (FindSpellHook v5.9).
local function get_cls(actor_param)
    local ok, cls = pcall(function()
        return actor_param:get():GetClass():GetFName():ToString()
    end)
    return ok and tostring(cls) or "?"
end

local overlap_hooks_registered = false

-- ─── Action hook: spell cast ─────────────────────────────────────────────────
-- Fires on VPairedPawn:SendSpellCast for every pawn (player + NPCs).
-- Filtered to BP_OblivionPlayerCharacter_C only.
-- Logs: ACTION [spell]  pos=X=... Y=... Z=...
RegisterHook("/Script/Altar.VPairedPawn:SendSpellCast", function(self)
    local ok_fn, fn = pcall(function() return self:get():GetFullName() end)
    if not (ok_fn and fn and fn:find("BP_OblivionPlayerCharacter_C", 1, true)) then return end
    local pos_str = "pos=unknown"
    local ok_loc, loc = pcall(function() return self:get():K2_GetActorLocation() end)
    if ok_loc and loc then
        pos_str = string.format("X=%.1f Y=%.1f Z=%.1f", loc.X, loc.Y, loc.Z)
    end
    local ok_ws, depth = pcall(function()
        local ws = FindFirstOf("WaterSubsystem")
        if ws and ws:IsValid() then return ws:GetCameraUnderwaterDepth() end
        return "no_ws"
    end)
    local depth_str = ok_ws and tostring(depth) or "ERR"
    -- Update is_underwater from depth (-1.0 = above water, >0 = submerged).
    -- Works in both interior and exterior; replaces WeatherControl as source of truth.
    if ok_ws and type(depth) == "number" then
        is_underwater = depth > 0
    end
    local overlaps = {}
    if in_WaterBodyLake then table.insert(overlaps, "WaterBodyLake") end
    if in_VWaterVolume  then table.insert(overlaps, "VWaterVolume") end
    log(string.format("ACTION [SendSpellCast]  %s  underwater=%s  depth=%s  overlap=%s",
        pos_str, tostring(is_underwater), depth_str, #overlaps > 0 and table.concat(overlaps, ",") or "none"))
    probeLoop()  -- force zone-change check in hook context (bIsVisible accurate here)
end)

-- ─── Action hooks: water (exterior only) ───────────────────────────────────
-- BP_WeatherControl only exists in exterior world — these won't fire inside caves.
-- OnCameraUnderWater: fires once when camera crosses below water surface.
-- OnCameraOverWater:  fires once when camera comes back above water surface.
local function waterPos(self)
    local ok, loc = pcall(function() return self:get():K2_GetActorLocation() end)
    if ok and loc then return string.format("X=%.1f Y=%.1f Z=%.1f", loc.X, loc.Y, loc.Z) end
    return "pos=unknown"
end
pcall(function()
    RegisterHook("/Game/Art/FX/_Shared/Blueprints/BP_WeatherControl.BP_WeatherControl_C:OnCameraUnderWater", function(self)
        is_underwater = true
        log(string.format("ACTION [OnCameraUnderWater]  %s", waterPos(self)))
    end)
end)
pcall(function()
    RegisterHook("/Game/Art/FX/_Shared/Blueprints/BP_WeatherControl.BP_WeatherControl_C:OnCameraOverWater", function(self)
        is_underwater = false
        log(string.format("ACTION [OnCameraOverWater]  %s", waterPos(self)))
    end)
end)

-- ─── Hook ────────────────────────────────────────────────────────────────────
-- 6 full-scan passes at increasing intervals cover the initial cell load.
-- probeLoop [CHANGED] handles subsequent zone transitions with targeted passes.
RegisterHook("/Script/Engine.PlayerController:ClientRestart", function()
    restartSeq = restartSeq + 1
    local seq = restartSeq
    logged_done  = {}
    last_set     = {}      -- reset: next [CHANGED] fires on full initial vis set
    last_vis_str = "NONE"
    is_underwater    = false  -- clear stale exterior water state on cell transition
    in_water_cave    = false  -- probeLoop will re-set if entering a water cave
    in_WaterBodyLake = false
    in_VWaterVolume  = false
    log(string.format("RESTART  seq=%d", seq))
    -- Register overlap hooks once (deferred 1s to avoid pawn-spawn crash window).
    if not overlap_hooks_registered then
        LoopAsync(1000, function()
            if overlap_hooks_registered then return false end
            pcall(function()
                RegisterHook("/Game/Dev/PlayerBlueprints/BP_OblivionPlayerCharacter.BP_OblivionPlayerCharacter_C:ReceiveActorBeginOverlap",
                    function(_, other_actor)
                        local cls = get_cls(other_actor)
                        if cls == "WaterBodyLake" then in_WaterBodyLake = true end
                        if cls == "VWaterVolume"  then in_VWaterVolume  = true end
                        if not in_water_cave then return end
                        if cls == "VWaterVolume" or cls == "WaterBodyLake" then
                            is_underwater = true
                            probeLog("water_enter", cls, nil)
                        end
                    end)
                RegisterHook("/Game/Dev/PlayerBlueprints/BP_OblivionPlayerCharacter.BP_OblivionPlayerCharacter_C:ReceiveActorEndOverlap",
                    function(_, other_actor)
                        local cls = get_cls(other_actor)
                        if cls == "WaterBodyLake" then in_WaterBodyLake = false end
                        if cls == "VWaterVolume"  then in_VWaterVolume  = false end
                        if not in_water_cave then return end
                        if cls == "VWaterVolume" or cls == "WaterBodyLake" then
                            is_underwater = false
                            probeLog("water_exit", cls, nil)
                        end
                    end)
            end)
            overlap_hooks_registered = true
            return false
        end)
    end
    local vis, all = getAllInteriorLevels()
    probeLog("restart", vis, all)
    for _, ms in ipairs({500, 2000, 5000, 10000, 20000, 30000}) do
        LoopAsync(ms, function()
            if restartSeq ~= seq then return false end
            local v, _ = getAllInteriorLevels()
            local zones = {}
            if v and v ~= "NONE" then
                for name in v:gmatch("[^|]+") do
                    if SUPPRESS[name] then table.insert(zones, name) end
                end
            end
            runSuppressPass(#zones > 0 and zones or nil, true)
            return false
        end)
    end
    LoopAsync(30000, function() periodicSuppress(seq); return false end)
end)
