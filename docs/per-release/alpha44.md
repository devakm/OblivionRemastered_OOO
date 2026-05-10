# alpha44 — release notes

_Compared against `alpha43`._

## File-level changes

- Added: 0
- Removed: 0
- Changed: 5

### Changed

- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_BOOK.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_CELL.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_CELLMAP.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_SPELL.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/Oscuro's_Oblivion_Overhaul.esp`

## ESP changes — `Oscuro's_Oblivion_Overhaul.esp`

**Master list changed:**

- before: ['Oblivion.esm', 'DLCBattlehornCastle.esp', 'DLCMehrunesRazor.esp', 'DLCOrrery.esp', 'DLCSpellTomes.esp', 'DLCThievesDen.esp', 'DLCVileLair.esp', 'Knights.esp', 'AltarESPMain.esp']
- after:  ['Oblivion.esm', 'DLCBattlehornCastle.esp', 'DLCMehrunesRazor.esp', 'DLCOrrery.esp', 'DLCSpellTomes.esp', 'DLCThievesDen.esp', 'DLCVileLair.esp', 'Knights.esp', 'AltarESPMain.esp', 'DLCFrostcrag.esp']

### Cell (CELL) — +131 -0 ~7

**Added:**

- `BrumaMagesGuildBasement` (FormID `003AAC`) — "LOC_FN_BrumaMagesGuildBasement"
- `BravilMagesGuild2ndFloor` (FormID `00A2BC`) — "LOC_FN_BravilMagesGuild2ndFloor"
- `FyrelightCave` (FormID `014987`) — "LOC_FN_FyrelightCave"
- `UnmarkedCave01` (FormID `014991`) — "LOC_FN_UnmarkedCave01"
- `EchoCave03` (FormID `014995`) — "LOC_FN_EchoCave03"
- `KingscrestCavern` (FormID `01499B`) — "LOC_FN_KingscrestCavern"
- `PotholeCaverns` (FormID `0149AD`) — "LOC_FN_PotholeCaverns"
- `DerelictMine` (FormID `015C33`) — "LOC_FN_DerelictMine"
- `AbandonedMine` (FormID `015C3D`) — "LOC_FN_AbandonedMine"
- `FortMagia` (FormID `015E1D`) — "LOC_FN_FortMagia"
- `FortIstirus` (FormID `015E21`) — "LOC_FN_FortIstirus"
- `FortCuptor` (FormID `015E22`) — "LOC_FN_FortCuptor"
- `FortRayles` (FormID `015E31`) — "LOC_FN_FortRayles"
- `DasekMoor` (FormID `015E3B`) — "LOC_FN_DasekMoor"
- `FortStrand01` (FormID `015E3C`) — "LOC_FN_FortStrand01"
- `PillagedMine` (FormID `015E45`) — "LOC_FN_PillagedMine"
- `ICImperialLegionHQMessHall` (FormID `015E97`) — "LOC_FN_ICImperialLegionHQMessHall"
- `Miscarcand02` (FormID `0160A3`) — "LOC_FN_Miscarcand02"
- `ICImperialLegionWatchTowerSW` (FormID `016327`) — "LOC_FN_ICImperialLegionWatchTowerSW"
- `ICImperialLegionWatchTowerN` (FormID `016328`) — "LOC_FN_ICImperialLegionWatchTowerN"

_…111 more added omitted (see JSON for full list)_

**Changed:**

- `LeyawiinTheDividingLine` (FormID `030538`) — "LOC_FN_LeyawiinTheDividingLine" — `full`: `'The Dividing Line'` → `'LOC_FN_LeyawiinTheDividingLine'`
- `BravilCastlePrivateQuartersNorthWing` (FormID `031A50`) — "LOC_FN_BravilCastlePrivateQuartersNorthWing" — `full`: `"Castle Bravil Lord's Manor North Wing"` → `'LOC_FN_BravilCastlePrivateQuartersNorthWing'`
- `zOOONarind` (FormID `002158`) — "LOC_FN_Narind" — `full`: `'Narind'` → `'LOC_FN_Narind'`
- `zOOONarid02` (FormID `002159`) — "LOC_FN_Narind02" — `full`: `'Narind Vadosel'` → `'LOC_FN_Narind02'`
- `Yeleri03` (FormID `0028E2`) — "LOC_FN_Yeleri03" — `full`: `'Yeleri Verasdel'` → `'LOC_FN_Yeleri03'`
- `DrownedHopesCave02` (FormID `017645`) — "LOC_FN_DrownedHopesCave02" — `full`: `"Silent Lament's Hollow"` → `'LOC_FN_DrownedHopesCave02'`
- `OOOWasteCell` (FormID `02AEEE`) — "LOC_FN_OOOWasteCell" — `full`: `"OOO's Waste Cell"` → `'LOC_FN_OOOWasteCell'`

### Container (CONT) — +6 -0 ~0

**Added:**

- `DarkAntoinettaChest` (FormID `0693D3`) — "LOC_FN_DarkAntoinettaChest"
- `LapBrewer` (FormID `001BA3`) — "Still"
- `LapSecretGrapeBarrel` (FormID `00208A`) — "Secret, No Lookie!"
- `LapGrapeSmushingBarrel` (FormID `002572`) — "Grape Barrel"
- `LapWineMakingMachine` (FormID `002A6B`) — "Apple Press"
- `LapKeg` (FormID `003479`) — "Keg"

### Leveled Item List (LVLI) — +3 -0 ~1

**Added:**

- `LL0Book1Cheap50` (FormID `0A497C`)
- `LL0Book2Common50` (FormID `0A497D`)
- `LL0Book3Valuable50` (FormID `0A497E`)

**Changed:**

- `LL0Book4Rare50` (FormID `0A497F`) — + entry: level 1 × 1 → `024587`

### Worldspace (WRLD) — +25 -0 ~0

**Added:**

- `?` (FormID `01C319`)
- `?` (FormID `01C31A`)
- `?` (FormID `01C31B`)
- `?` (FormID `01C31C`)
- `?` (FormID `01C31D`)
- `?` (FormID `02525F`)
- `?` (FormID `02C107`)
- `?` (FormID `02C109`)
- `?` (FormID `02C10A`)
- `?` (FormID `02C10B`)
- `?` (FormID `02C10C`)
- `?` (FormID `02C10D`)
- `?` (FormID `02C10E`)
- `?` (FormID `02C10F`)
- `?` (FormID `02C5E4`)
- `?` (FormID `03633E`)
- `?` (FormID `038D48`)
- `?` (FormID `03CA6F`)
- `?` (FormID `03E50A`)
- `?` (FormID `03F551`)

_…5 more added omitted (see JSON for full list)_

