### Requires a UE4SS update

alpha92 needs **"UE4SS new" (v3.0.1-1164)** from the
[UE4SS Nexus page](https://www.nexusmods.com/oblivionremastered/mods/32) (under
**Update files**). Install it over your existing UE4SS **before** you install
alpha92. The older "UE4SS stable" (3.0.1.a) is no longer supported: the alpha92
`RAX` DLL is not safe on it, and the alpha91 `RAX` DLL is not safe on the new one.

- **RAX rebuilt for the new UE4SS.** No change to what RAX does: custom map
  loading and the leveled-spell fix work as before.
- **Fewer crashes after level loads (expected).** The new UE4SS fixes a crash in
  Lua mods that check a game object after a fast travel, a cell change or a save
  load. In testing, repeated fast travel and loading a different save after a long
  session are more stable. Testing continues.
- **Other UE4SS mods:** the UE4SS page warns that some older UE4SS mods may not
  work with "UE4SS new". TesSyncMapInjector v0.1.8 and MagicLoader v2.9 work with it.

### Begone and OOO_REFRFix are now optional test mods

RAX is now the only UE4SS mod installed by default. `Begone` (now log-only: it
suppresses nothing) and `OOO_REFRFix` ship under
`OblivionRemastered\alpha92_test_optional\` with their install tree intact; copy a
mod's folder from `alpha92_test_optional\Binaries\Win64\ue4ss\Mods\` into
`Binaries\Win64\ue4ss\Mods\` to use it.

**Upgrading from alpha91:** installing over alpha91 does **not** remove the old
`Mods\Begone\` and `Mods\OOO_REFRFix\` folders. Delete them unless you want them.

### 21 new item sets, and SyncMap remapping

Ancestral, BladesElite, DaedricPrince, DarkMalachite, Draconis, Dragonborne,
Dread, DremoraElite, DurableSteel, ImagoStorm, Light of Dawn (four sword
variants), Noble, TheBear, UnfinishedAncestral, UnfinishedSteel,
UnfinishedWornSteel, WornAncestral and WornSteel.

About 120 OOO items that borrowed a vanilla mesh in alpha91 now point at their own
set in the SyncMap: for example Dread armor (was Daedric), Noble (was Ebony),
Durable Steel (was Steel), the Ancestral sets (were Amelion), Daedric Prince (was
Daedric and Dremora), Vella's armor (now BlueGlass and DarkMalachite), the Light
of Dawn swords (were Rugdumph's sword) and the enchanted RGlass greaves (now
Drakefired greaves). The Aureus, Drakefired, Eboron, GrayFox and Obsidian sets
were rebuilt.

### Dungeons

**All classic OOO dungeons are now complete.** Gloom Way Cave and Red Gill Cave,
the last two, are finished in alpha92, with their water approved in-game.
