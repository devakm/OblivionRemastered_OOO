# alpha51 — release notes

_Compared against `alpha50`._

## File-level changes

- Added: 1
- Removed: 0
- Changed: 8

### Added

- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_KEY.json`

### Changed

- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_ARMO.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_CELL.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_CELLMAP.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_NPC_.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_QUST.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_SCPT.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/Oscuro's_Oblivion_Overhaul.esp`
- `OblivionRemastered/Content/Dev/ObvData/Data/SyncMap/Oscuro's_Oblivion_Overhaul.ini`

## ESP changes — `Oscuro's_Oblivion_Overhaul.esp`

### Armor (ARMO) — +0 -0 ~6

**Changed:**

- `IronBootsGhost` (FormID `01465B`) — "LOC_FN_IronBootsGhost" — `full`: `'Ghostly Iron Boots'` → `'LOC_FN_IronBootsGhost'`
- `IronCuirassGhost` (FormID `01465C`) — "LOC_FN_IronCuirassGhost" — `full`: `'Ghostly Iron Cuirass'` → `'LOC_FN_IronCuirassGhost'`
- `IronGauntletsGhost` (FormID `01465D`) — "LOC_FN_IronGauntletsGhost" — `full`: `'Ghostly Iron Gauntlets'` → `'LOC_FN_IronGauntletsGhost'`
- `IronGreavesGhost` (FormID `01465E`) — "LOC_FN_IronGreavesGhost" — `full`: `'Ghostly Iron Greaves'` → `'LOC_FN_IronGreavesGhost'`
- `IronHelmetGhost` (FormID `01465F`) — "LOC_FN_IronHelmetGhost" — `full`: `'Ghostly Iron Helmet'` → `'LOC_FN_IronHelmetGhost'`
- `IronShieldGhost` (FormID `014660`) — "LOC_FN_IronShieldGhost" — `full`: `'Ghostly Iron Shield'` → `'LOC_FN_IronShieldGhost'`

### Cell (CELL) — +0 -0 ~2

**Changed:**

- `MelusPetiliusBasement` (FormID `006D3F`) — "LOC_FN_MelusPetiliusBasement" — `full`: `"Melus Petilius' Secret Room"` → `'LOC_FN_MelusPetiliusBasement'`
- `DeepCoverCave02` (FormID `015D7D`) — "LOC_FN_DeepCoverCave02" — `full`: `'Deep Cover Caverns'` → `'LOC_FN_DeepCoverCave02'`

### Key (KEYM) — +0 -0 ~79

**Changed:**

- `DarkFirstMateKey` (FormID `002D6D`) — "LOC_FN_DarkFirstMateKey" — `full`: `'Rusted Iron Key'` → `'LOC_FN_DarkFirstMateKey'`
- `RoselarKey` (FormID `0043B9`) — "LOC_FN_RoselarKey" — `full`: `'Rosulas Key'` → `'LOC_FN_RoselarKey'`
- `Regulusterentiuskey` (FormID `00445F`) — "LOC_FN_Regulusterentiuskey" — `full`: `'Plain Silver Key'` → `'LOC_FN_Regulusterentiuskey'`
- `MelusPetiliusChestKeyOOO` (FormID `00528B`) — "LOC_FN_MelusPetiliusChestKeyOOO" — `full`: `'Melus Petilius Old Key'` → `'LOC_FN_MelusPetiliusChestKeyOOO'`
- `HonmundKeyOOO` (FormID `005DE7`) — "LOC_FN_HonmundKeyOOO" — `full`: `'Small Golden Key'` → `'LOC_FN_HonmundKeyOOO'`
- `HafidhollowlegOOO` (FormID `005DE9`) — "LOC_FN_HafidhollowlegOOO" — `full`: `'Small Rusted Key'` → `'LOC_FN_HafidhollowlegOOO'`
- `LyraRosentiaKeyOOO` (FormID `005DF1`) — "LOC_FN_LyraRosentiaKeyOOO" — `full`: `'Tiny Ornate Key'` → `'LOC_FN_LyraRosentiaKeyOOO'`
- `ArrianaValgaKeyOOO` (FormID `0067FB`) — "LOC_FN_ArrianaValgaKeyOOO" — `full`: `'Tiny Steel Key'` → `'LOC_FN_ArrianaValgaKeyOOO'`
- `EugalBeletteKeyOOO` (FormID `0067FF`) — "LOC_FN_EugalBeletteKeyOOO" — `full`: `'Stained Key'` → `'LOC_FN_EugalBeletteKeyOOO'`
- `FrancoisMotierreKeyOOO` (FormID `006800`) — "LOC_FN_FrancoisMotierreKeyOOO" — `full`: `'Small Ornate Key'` → `'LOC_FN_FrancoisMotierreKeyOOO'`
- `TalasmasKeyOOO` (FormID `006801`) — "LOC_FN_TalasmasKeyOOO" — `full`: `'Small Sticky Key'` → `'LOC_FN_TalasmasKeyOOO'`
- `VilenaDontonKeyOOO` (FormID `006804`) — "LOC_FN_VilenaDontonKeyOOO" — `full`: `'Tiny Engraved Key'` → `'LOC_FN_VilenaDontonKeyOOO'`
- `HannibalTravenKeyOOO` (FormID `006D42`) — "LOC_FN_HannibalTravenKeyOOO" — `full`: `"Hannibal Traven's Shiny Key"` → `'LOC_FN_HannibalTravenKeyOOO'`
- `DovynArensChestKeyOOO` (FormID `00743E`) — "LOC_FN_DovynArensChestKeyOOO" — `full`: `'Blackened Key'` → `'LOC_FN_DovynArensChestKeyOOO'`
- `DulgroShugsChestKeyOOO` (FormID `007440`) — "LOC_FN_DulgroShugsChestKeyOOO" — `full`: `'Dented Small Iron Key'` → `'LOC_FN_DulgroShugsChestKeyOOO'`
- `RajhansChestKeyOOO` (FormID `00794B`) — "LOC_FN_RajhansChestKeyOOO" — `full`: `"Ra'Jhan's Tiny Key"` → `'LOC_FN_RajhansChestKeyOOO'`
- `InielSintavsChestKeyOOO` (FormID `00813E`) — "LOC_FN_InielSintavsChestKeyOOO" — `full`: `"Iniel Sintav's Small Key"` → `'LOC_FN_InielSintavsChestKeyOOO'`
- `KastusSintavsChestKeyOOO` (FormID `00813F`) — "LOC_FN_KastusSintavsChestKeyOOO" — `full`: `"Kastus Sintav's Tiny Key"` → `'LOC_FN_KastusSintavsChestKeyOOO'`
- `MarinusCatiotusChestKeyOOO` (FormID `008141`) — "LOC_FN_MarinusCatiotusChestKeyOOO" — `full`: `"Marinus' Iron Key"` → `'LOC_FN_MarinusCatiotusChestKeyOOO'`
- `RodericPierranesChestKeyOOO` (FormID `008142`) — "LOC_FN_RodericPierranesChestKeyOOO" — `full`: `"Roderic Pierrane's Jeweled Key"` → `'LOC_FN_RodericPierranesChestKeyOOO'`

_…59 more changed omitted (see JSON for full list)_

### Script (SCPT) — +1 -0 ~0

**Added:**

- `GhostEffectScript` (FormID `0B9922`)

### Spell (SPEL) — +8 -0 ~0

**Added:**

- `ZZWolfSummonPlayer` (FormID `025165`) — "Jephre's Forest Guardian"
- `ZZWolfTundraSummonPlayer` (FormID `025BCD`) — "Jephre's Tundra Guardian"
- `ZZLionSummonPlayer` (FormID `025BCE`) — "Jephre's Fangs"
- `ZZLionSnowSummonPlayer` (FormID `025BD0`) — "Jephre's Arctic Claws"
- `ZZLeopardSnowSummonPlayer` (FormID `025BD2`) — "Jephre's White Shadow"
- `ZZLeopardSummonPlayer` (FormID `025BD4`) — "Jephre's Jungle Guardian"
- `ZZBoarSummonPlayer` (FormID `025BD6`) — "Jephre's Tusks"
- `ZZDeerSummonPlayer` (FormID `025BDB`) — "Jephre's Pride"

