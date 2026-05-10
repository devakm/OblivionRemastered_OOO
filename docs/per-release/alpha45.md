# alpha45 — release notes

_Compared against `alpha44`._

## File-level changes

- Added: 0
- Removed: 0
- Changed: 4

### Changed

- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_CELLMAP.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_QUST.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/Oscuro's_Oblivion_Overhaul.esp`
- `OblivionRemastered/Content/Dev/ObvData/Data/SyncMap/Oscuro's_Oblivion_Overhaul.ini`

## ESP changes — `Oscuro's_Oblivion_Overhaul.esp`

**Master list changed:**

- before: ['Oblivion.esm', 'DLCBattlehornCastle.esp', 'DLCMehrunesRazor.esp', 'DLCOrrery.esp', 'DLCSpellTomes.esp', 'DLCThievesDen.esp', 'DLCVileLair.esp', 'Knights.esp', 'AltarESPMain.esp', 'DLCFrostcrag.esp']
- after:  ['Oblivion.esm', 'DLCBattlehornCastle.esp', 'DLCFrostcrag.esp', 'DLCMehrunesRazor.esp', 'DLCOrrery.esp', 'DLCSpellTomes.esp', 'DLCThievesDen.esp', 'DLCVileLair.esp', 'Knights.esp', 'AltarESPMain.esp']

### Armor (ARMO) — +0 -0 ~17

**Changed:**

- `CMIronBattleShield01OOO` (FormID `00124C`) — "LOC_FN_CMIronBattleShield01OOO" — `modl`: `'Armor\\CMBattleShields\\CMBattleShield001.nif'` → `'Armor\\Iron\\Shield.NIF'`
- `CMIronBattleShield02OOO` (FormID `00124D`) — "LOC_FN_CMIronBattleShield02OOO" — `modl`: `'Armor\\CMBattleShields\\CMBattleShield002.nif'` → `'Armor\\Chainmail\\Shield.NIF'`
- `CMIronBattleShield03OOO` (FormID `00124E`) — "LOC_FN_CMIronBattleShield03OOO" — `modl`: `'Armor\\CMBattleShields\\CMBattleShield003.nif'` → `'Armor\\Chainmail\\Shield.NIF'`
- `CMIronBattleShield04OOO` (FormID `00124F`) — "LOC_FN_CMIronBattleShield04OOO" — `modl`: `'Armor\\CMBattleShields\\CMBattleShield004.nif'` → `'Armor\\Steel\\Shield.NIF'`
- `CMIronBattleShield05OOO` (FormID `001250`) — "LOC_FN_CMIronBattleShield05OOO" — `modl`: `'Armor\\CMBattleShields\\CMBattleShield005.nif'` → `'Armor\\Orcish\\Shield.NIF'`
- `CMIronBattleShield06OOO` (FormID `001251`) — "LOC_FN_CMIronBattleShield06OOO" — `modl`: `'Armor\\CMBattleShields\\CMBattleShield006.nif'` → `'Armor\\Chainmail\\Shield.NIF'`
- `CMIronBattleShield07OOO` (FormID `001252`) — "LOC_FN_CMIronBattleShield07OOO" — `modl`: `'Armor\\CMBattleShields\\CMBattleShield007.nif'` → `'Armor\\Ebony\\Shield.NIF'`
- `CMIronBattleShield10OOO` (FormID `001255`) — "LOC_FN_CMIronBattleShield10OOO" — `modl`: `'Armor\\CMBattleShields\\CMBattleShield010.nif'` → `'Armor\\Dwarven\\Shield.NIF'`
- `CMIronBattleShield11OOO` (FormID `001256`) — "LOC_FN_CMIronBattleShield11OOO" — `modl`: `'Armor\\CMBattleShields\\CMBattleShield011.nif'` → `'Armor\\Iron\\Shield.NIF'`
- `DefStaffUnique1OOO` (FormID `002593`) — "LOC_FN_DefStaffUnique1OOO" — `modl`: `'armor\\DefensiveStaves\\staffunique1.nif'` → `'Armor\\Dwarven\\Shield.NIF'`
- `DefStaffUnique2OOO` (FormID `00259B`) — "LOC_FN_DefStaffUnique2OOO" — `modl`: `'armor\\DefensiveStaves\\staffunique2.nif'` → `'Armor\\Orcish\\Shield.NIF'`
- `DefStaffUnique3OOO` (FormID `00259D`) — "LOC_FN_DefStaffUnique3OOO" — `modl`: `'armor\\DefensiveStaves\\staffunique3.nif'` → `'Armor\\Iron\\Shield.NIF'`
- `DefStaffUnique4OOO` (FormID `00259E`) — "LOC_FN_DefStaffUnique4OOO" — `modl`: `'armor\\DefensiveStaves\\ashenstaff.nif'` → `'Armor\\Chainmail\\Shield.NIF'`
- `DefStaffUnique5OOO` (FormID `00259F`) — "LOC_FN_DefStaffUnique5OOO" — `modl`: `'armor\\DefensiveStaves\\elvenstaff.nif'` → `'Armor\\Ebony\\Shield.NIF'`
- `ReguardNobilityOOO` (FormID `01AFCB`) — "LOC_FN_ReguardNobilityOOO" — `modl`: `'armor\\CMRedguardScaled\\RedguardShield.nif'` → `'Armor\\AmelionCeremonial\\Shield.NIF'`
- `CMIronBattleShield08OOOSpecial` (FormID `01C2DD`) — "LOC_FN_CMIronBattleShield08OOOSpecial" — `modl`: `'Armor\\CMBattleShields\\CMBattleShield008.nif'` → `'Armor\\Ebony\\Shield.NIF'`
- `CMOrcNobilityOOO` (FormID `027167`) — "LOC_FN_CMOrcNobilityOOO" — `modl`: `'Armor\\Orcish\\Helmet.NIF'` → `'Armor\\Orcish\\Shield.NIF'`

### Cell (CELL) — +228 -0 ~2

**Added:**

- `ChorrolNorthernGoodsAndTrade` (FormID `000807`) — "LOC_FN_ChorrolNorthernGoodsAndTrade"
- `ChorrolRenoitsBooks` (FormID `000808`) — "LOC_FN_ChorrolRenoitsBooks"
- `ChorrolFireAndSteel` (FormID `000809`) — "LOC_FN_ChorrolFireAndSteel"
- `ChorrolFrancoisMotierresHouse` (FormID `000824`) — "LOC_FN_ChorrolFrancoisMotierresHouse"
- `ChorrolTheOakandCrosierTavern` (FormID `000D77`) — "LOC_FN_ChorrolTheOakandCrosierTavern"
- `BrittlerockCave` (FormID `002E3D`) — "LOC_FN_BrittlerockCave"
- `BloodcrustCavern` (FormID `003990`) — "LOC_FN_BloodcrustCavern"
- `CheydinhalFightersGuildBasement` (FormID `00691B`) — "LOC_FN_CheydinhalFightersGuildBasement"
- `AnvilCastleDiningHallandServantQuarters` (FormID `007947`) — "LOC_FN_AnvilCastleDiningHallandServantQuarters"
- `AnvilFightersGuildDinningHall` (FormID `0097B4`) — "LOC_FN_AnvilFightersGuildDinningHall"
- `AnvilMagesGuildLivingQuarters` (FormID `0097B5`) — "LOC_FN_AnvilMagesGuildLivingQuarters"
- `BravilFightersGuildBasement` (FormID `00A2B9`) — "LOC_FN_BravilFightersGuildBasement"
- `FortRedman01` (FormID `00B239`) — "LOC_FN_FortRedman01"
- `FortTeleman02` (FormID `00C087`) — "LOC_FN_FortTeleman02"
- `WarehouseClothes` (FormID `010551`) — "LOC_FN_WarehouseClothes"
- `MossRockCavern` (FormID `014983`) — "LOC_FN_MossRockCavern"
- `FingerbowlCave` (FormID `014984`) — "LOC_FN_FingerbowlCave"
- `SandstoneCavern` (FormID `014985`) — "LOC_FN_SandstoneCavern"
- `RockmilkCave` (FormID `01498E`) — "LOC_FN_RockmilkCave"
- `GreenmeadCave` (FormID `014996`) — "LOC_FN_GreenmeadCave"

_…208 more added omitted (see JSON for full list)_

**Changed:**

- `BrumaFightersGuild` (FormID `0302ED`) — "LOC_FN_BrumaFightersGuild" — `full`: `'Bruma Fighters Guild'` → `'LOC_FN_BrumaFightersGuild'`
- `ICWaterfrontMarieElenaCaptainsCabin` (FormID `03ED42`) — "LOC_FN_ICWaterfrontMarieElenaCaptainsCabin" — `full`: `"Marie Elena Captain's Cabin"` → `'LOC_FN_ICWaterfrontMarieElenaCaptainsCabin'`

### Quest (QUST) — +30 -0 ~0

**Added:**

- `MG17Ambush` (FormID `00C03B`) — "LOC_FN_MG17Ambush"
- `DABoethia` (FormID `0146A3`) — "LOC_FN_DABoethia"
- `DAClavicusVile` (FormID `0146A4`) — "LOC_FN_DAClavicusVile"
- `DAHircine` (FormID `0146A5`) — "LOC_FN_DAHircine"
- `DAMalacath` (FormID `0146A6`) — "LOC_FN_DAMalacath"
- `DAMephala` (FormID `0146A7`) — "LOC_FN_DAMephala"
- `DAMeridia` (FormID `0146A8`) — "LOC_FN_DAMeridia"
- `DANamira` (FormID `0146A9`) — "LOC_FN_DANamira"
- `DANocturnal` (FormID `0146AA`) — "LOC_FN_DANocturnal"
- `DAPeryite` (FormID `0146AB`) — "LOC_FN_DAPeryite"
- `DASanguine` (FormID `0146AC`) — "LOC_FN_DASanguine"
- `DAVaermina` (FormID `0146AE`) — "LOC_FN_DAVaermina"
- `MQ05` (FormID `01E727`) — "LOC_FN_MQ05"
- `TGStolenGoods` (FormID `01EE46`) — "LOC_FN_TGStolenGoods"
- `MG04Restore` (FormID `02D32B`) — "LOC_FN_MG04Restore"
- `FGD05Oreyn` (FormID `02D71B`) — "LOC_FN_FGD05Oreyn"
- `MS27` (FormID `02E5BE`) — "LOC_FN_MS27"
- `MS26` (FormID `035CA8`) — "LOC_FN_MS26"
- `TG07Lex` (FormID `036334`) — "LOC_FN_TG07Lex"
- `MS02` (FormID `03636F`) — "LOC_FN_MS02"

_…10 more added omitted (see JSON for full list)_

