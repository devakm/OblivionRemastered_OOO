# alpha49 — release notes

_Compared against `alpha48`._

## File-level changes

- Added: 0
- Removed: 0
- Changed: 6

### Changed

- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_CELLMAP.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_NPC_.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_QUST.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_SCPT.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/Oscuro's_Oblivion_Overhaul.esp`
- `OblivionRemastered/Content/Dev/ObvData/Data/SyncMap/Oscuro's_Oblivion_Overhaul.ini`

## ESP changes — `Oscuro's_Oblivion_Overhaul.esp`

### Armor (ARMO) — +0 -0 ~17

**Changed:**

- `CMIronBattleShield08OOO` (FormID `001253`) — "LOC_FN_CMIronBattleShield08OOO" — `modl`: `'Armor\\CMBattleShields\\CMBattleShield008.nif'` → `'Armor\\Iron\\Shield.NIF'`
- `YinYangShieldHeavyOOO` (FormID `025BBF`) — "LOC_FN_YinYangShieldHeavyOOO" — `modl`: `'armor\\yin-yangshi\\shield.nif'` → `'Armor\\Chainmail\\Shield.NIF'`
- `YinYangShieldLightOOO` (FormID `025BC0`) — "LOC_FN_YinYangShieldLightOOO" — `modl`: `'armor\\yin-yangshi\\shield.nif'` → `'Armor\\Orcish\\Shield.NIF'`
- `pegasushelmetOOO` (FormID `026C63`) — "LOC_FN_pegasushelmetOOO" — `modl`: `'armor\\Pegasus\\phelmet.nif'` → `'Armor\\AmelionCeremonial\\M\\Helmet.NIF'`
- `pegasusshieldOOO` (FormID `026C64`) — "LOC_FN_pegasusshieldOOO" — `modl`: `'armor\\Pegasus\\pshield.nif'` → `'Armor\\AmelionCeremonial\\Shield.NIF'`
- `EYCCAbootsOOO` (FormID `0392EF`) — "LOC_FN_EYCCAbootsOOO" — `modl`: `'armor\\EY_CCA\\f\\boots.nif'` → `'Armor\\AmelionCeremonial\\M\\Boots.NIF'`
- `EYCCAcuirassOOO` (FormID `0392F0`) — "LOC_FN_EYCCAcuirassOOO" — `modl`: `'armor\\EY_CCA\\f\\cuirass.nif'` → `'Armor\\AmelionCeremonial\\M\\Cuirass.NIF'`
- `EYCCAgauntlesOOO` (FormID `0392F1`) — "LOC_FN_EYCCAgauntlesOOO" — `modl`: `'armor\\EY_CCA\\f\\gauntlet.nif'` → `'Armor\\AmelionCeremonial\\M\\Gauntlets.NIF'`
- `EYCCAgreavesOOO` (FormID `0392F2`) — "LOC_FN_EYCCAgreavesOOO" — `modl`: `'armor\\EY_CCA\\f\\greaves.nif'` → `'Armor\\AmelionCeremonial\\M\\Greaves.NIF'`
- `EYQMABootsOOO` (FormID `0392F3`) — "LOC_FN_EYQMABootsOOO" — `modl`: `'armor\\EY_QMA\\f\\boots.nif'` → `'Armor\\AmelionCeremonial\\M\\Boots.NIF'`
- `EYQMAcuirassOOO` (FormID `0392F4`) — "LOC_FN_EYQMAcuirassOOO" — `modl`: `'armor\\EY_QMA\\f\\cuirass.nif'` → `'Armor\\AmelionCeremonial\\M\\Cuirass.NIF'`
- `EYQMAgauntletsOOO` (FormID `0392F5`) — "LOC_FN_EYQMAgauntletsOOO" — `modl`: `'armor\\EY_QMA\\f\\gauntlet.nif'` → `'Armor\\AmelionCeremonial\\M\\Gauntlets.NIF'`
- `EYQMAgreavesOOO` (FormID `0392F6`) — "LOC_FN_EYQMAgreavesOOO" — `modl`: `'armor\\EY_QMA\\f\\greaves.nif'` → `'Armor\\AmelionCeremonial\\M\\Greaves.NIF'`
- `DreadCuirassOOOv2L` (FormID `06EA3C`) — "LOC_FN_DreadCuirassOOOv2L" — `modl`: `'armor\\Dread Armor\\m\\ooodcuirassm.nif'` → `'Armor\\Daedric\\M\\Cuirass.NIF'`
- `DreadBootsOOOv2L` (FormID `06EA3D`) — "LOC_FN_DreadBootsOOOv2L" — `modl`: `'armor\\Dread Armor\\m\\ooodbootsm.nif'` → `'Armor\\Daedric\\M\\Boots.NIF'`
- `DreadGreavesOOOv2L` (FormID `06EA3F`) — "LOC_FN_DreadGreavesOOOv2L" — `modl`: `'armor\\Dread Armor\\m\\ooodgreavesm.nif'` → `'Armor\\Daedric\\M\\Greaves.NIF'`
- `DreadHelmetOOOv2L` (FormID `06EA40`) — "LOC_FN_DreadHelmetOOOv2L" — `modl`: `'armor\\Dread Armor\\ooodhelmet.nif'` → `'Armor\\Daedric\\M\\Helmet.NIF'`

### Creature (CREA) — +2 -0 ~0

**Added:**

- `SummonAtronachFrost` (FormID `0C8BCA`) — "LOC_FN_SummonAtronachFrost"
- `SummonAtronachStorm` (FormID `0C8BCB`) — "LOC_FN_SummonAtronachStorm"

### Misc Item (MISC) — +0 -0 ~1

**Changed:**

- `GemZEmeraldJephre` (FormID `00C39A`) — "LOC_FN_GemZEmeraldJephre" — `modl`: `'Clutter\\Gems\\RubyFlawless.NIF'` → `'Clutter\\Gems\\EmeraldFlawless.NIF'`

### Weapon (WEAP) — +0 -0 ~3

**Changed:**

- `rdTemplarSwordOOO` (FormID `00C412`) — "LOC_FN_rdTemplarSwordOOO" — `modl`: `'Weapons\\Ebony\\LongSword.NIF'` → `'Weapons\\BlackwaterBlade\\BlackwaterBlade.NIF'`
- `rdTemplarSwordOOO2` (FormID `019D3D`) — "LOC_FN_rdTemplarSwordOOO2" — `modl`: `'Weapons\\Silver\\LongSword.NIF'` → `'Weapons\\BlackwaterBlade\\BlackwaterBlade.NIF'`
- `drlongswordOOO` (FormID `02716B`) — "LOC_FN_drlongswordOOO" — `modl`: `'Weapons\\Silver\\LongSword.NIF'` → `'Weapons\\Silver\\AmelionCeremonialSword.NIF'`

