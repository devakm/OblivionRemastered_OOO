# alpha28 — release notes

_Compared against `alpha27`._

## File-level changes

- Added: 0
- Removed: 1
- Changed: 6

### Removed

- `OblivionRemastered/Content/Dev/ObvData/Data/SyncMap/archive/Oscuro's_Oblivion_Overhaul_alpha26.ini`

### Changed

- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_AMMO.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_ARMO.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_CREA.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_NPC_.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/Oscuro's_Oblivion_Overhaul.esp`
- `OblivionRemastered/Content/Dev/ObvData/Data/SyncMap/Oscuro's_Oblivion_Overhaul.ini`

## ESP changes — `Oscuro's_Oblivion_Overhaul.esp`

### Cell (CELL) — +2 -0 ~0

**Added:**

- `MelusPetilusHouse` (FormID `025E28`) — "LOC_FN_MelusPetilusHouse"
- `MelusPetiliusBasement` (FormID `006D3F`) — "Melus Petilius' Secret Room"

### Creature (CREA) — +0 -0 ~2

**Changed:**

- `OOOGuarMount` (FormID `02EFD4`) — "LOC_FN_OOOGuarMount" — `full`: `'Guaroache'` → `'LOC_FN_OOOGuarMount'`
- `OOOGuarPropMount` (FormID `02EFE0`) — "LOC_FN_OOOGuarMount" — `full`: `'Guaroache'` → `'LOC_FN_OOOGuarMount'`

### Leveled Creature List (LVLC) — +0 -0 ~3

**Changed:**

- `SELL1BaliwogDementia100` (FormID `011B8D`) — - entry: level 1 × 1 → `000EDA`
- `SELL2Undead100` (FormID `03B815`) — - entry: level 1 × 1 → `0037F6`; - entry: level 10 × 1 → `0037F6`
- `OOOSELL2Undead100Pack` (FormID `004CFF`) — - entry: level 1 × 1 → `0037F6`

### Leveled Item List (LVLI) — +1 -0 ~6

**Added:**

- `OOOSELL4LootZealotMedium10` (FormID `00DDC4`)

**Changed:**

- `LL1LootGold100` (FormID `014931`) — + entry: level 1 × 3 → `0054AF`; + entry: level 4 × 3 → `0054B0`; + entry: level 6 × 4 → `0054B1`; + entry: level 8 × 4 → `0054B2`; + entry: level 10 × 4 → `0054B3`; + entry: level 12 × 5 → `0054B4`; + entry: level 14 × 5 → `0054B5`; + entry: level 16 × 5 → `0054A7`; + entry: level 18 × 6 → `0054A8`; + entry: level 20 × 6 → `0054A9`; + entry: level 22 × 6 → `0054AA`; + entry: level 24 × 7 → `0054AB`; + entry: level 26 × 7 → `0054AC`; + entry: level 28 × 7 → `0054AD`; + entry: level 30 × 7 → `0054AE`; - entry: level 1 × 10 → `0054AF`; - entry: level 4 × 10 → `0054B0`; - entry: level 6 × 10 → `0054B1`; - entry: level 8 × 10 → `0054B2`; - entry: level 10 × 10 → `0054B3`; - entry: level 12 × 10 → `0054B4`; - entry: level 14 × 10 → `0054B5`; - entry: level 16 × 10 → `0054A7`; - entry: level 18 × 10 → `0054A8`; - entry: level 20 × 10 → `0054A9`; - entry: level 22 × 10 → `0054AA`; - entry: level 24 × 10 → `0054AB`; - entry: level 26 × 10 → `0054AC`; - entry: level 28 × 10 → `0054AD`; - entry: level 30 × 10 → `0054AE`
- `LL1LootScroll1Novice100` (FormID `08AE51`) — + entry: level 1 × 1 → `0011DC`
- `LL1LootScroll2Apprentice100` (FormID `08AE52`) — + entry: level 1 × 1 → `0011DD`
- `LL1LootScroll3Journeyman100` (FormID `08AE53`) — + entry: level 1 × 1 → `0011DD`
- `SQ02LL0NPCWeapon0MagicClaymoreLvl100` (FormID `181C66`) — + entry: level 5 × 1 → `02B586`
- `OOOLoot0All02` (FormID `00DDC1`) — `edid`: `'OOOLoot0All05'` → `'OOOLoot0All02'`

### Leveled Spell List (LVSP) — +2 -0 ~4

**Added:**

- `LL2Valen100new` (FormID `00DDF2`)
- `LL2ArgonianBlackMarsh100new` (FormID `00DDF3`)

**Changed:**

- `LL2ArgonianBlackMarsh100` (FormID `007786`) — + entry: level 1 × 1 → `0A936D`; - entry: level 1 × 1 → `007755`; - entry: level 1 × 1 → `007756`; - entry: level 1 × 1 → `007758`; - entry: level 1 × 1 → `00775A`; - entry: level 1 × 1 → `00775C`; - entry: level 1 × 1 → `00775E`; - entry: level 1 × 1 → `007760`; - entry: level 1 × 1 → `007762`; - entry: level 1 × 1 → `007764`; - entry: level 1 × 1 → `007766`; - entry: level 1 × 1 → `007768`; - entry: level 1 × 1 → `00776A`; - entry: level 1 × 1 → `00776C`; - entry: level 1 × 1 → `00776E`; - entry: level 1 × 1 → `007770`; - entry: level 1 × 1 → `007772`; - entry: level 1 × 1 → `007774`; - entry: level 1 × 1 → `007776`; - entry: level 1 × 1 → `007778`; - entry: level 1 × 1 → `00777A`; - entry: level 1 × 1 → `00777C`; - entry: level 1 × 1 → `00777E`; - entry: level 1 × 1 → `007780`; - entry: level 1 × 1 → `007782`; - entry: level 1 × 1 → `007784`
- `LL2CreatureImpCrazed100` (FormID `02F4FE`) — - entry: level 1 × 1 → `028D59`; - entry: level 1 × 1 → `028D5F`; - entry: level 1 × 1 → `02F9EA`; - entry: level 1 × 1 → `02F9EB`
- `LL2CreatureImpMystical100` (FormID `02F500`) — + entry: level 1 × 1 → `0A97A9`; - entry: level 1 × 1 → `028D5B`; - entry: level 1 × 1 → `028D5D`; - entry: level 1 × 1 → `028D61`; - entry: level 1 × 1 → `02F9ED`; - entry: level 1 × 1 → `02F9EF`; - entry: level 1 × 1 → `02F9F1`; - entry: level 1 × 1 → `02F9F3`
- `LL2AmazonLvl100` (FormID `03BFDF`) — + entry: level 1 × 1 → `03C3FB`; - entry: level 1 × 1 → `03BFCD`; - entry: level 1 × 1 → `03BFCF`; - entry: level 1 × 1 → `03BFD1`; - entry: level 1 × 1 → `03BFD3`; - entry: level 1 × 1 → `03BFD5`; - entry: level 1 × 1 → `03BFD7`; - entry: level 1 × 1 → `03BFD9`; - entry: level 1 × 1 → `03BFDB`; - entry: level 1 × 1 → `03BFDD`; - entry: level 1 × 1 → `03D414`; - entry: level 1 × 1 → `03D416`; - entry: level 1 × 1 → `03D418`; - entry: level 1 × 1 → `03D41A`; - entry: level 1 × 1 → `03E2E5`; - entry: level 1 × 1 → `03E2E6`; - entry: level 1 × 1 → `03E2E8`; - entry: level 1 × 1 → `03E2EA`; - entry: level 1 × 1 → `03E2EC`; - entry: level 1 × 1 → `03E2EE`; - entry: level 1 × 1 → `03E2F0`; - entry: level 1 × 1 → `03E2F2`; - entry: level 1 × 1 → `03E2F4`; - entry: level 1 × 1 → `03E2F6`; - entry: level 1 × 1 → `03E2F8`; - entry: level 1 × 1 → `03E2FA`; - entry: level 1 × 1 → `03E2FC`; - entry: level 1 × 1 → `03E2FE`; - entry: level 1 × 1 → `03E306`; - entry: level 1 × 1 → `03E310`

### NPC (NPC_) — +6 -0 ~81

**Added:**

- `ConjurerXGuardianBossFemaleBreton` (FormID `00DDF6`) — "LOC_FN_ConjurerXGuardianBossFemaleBreton"
- `ConjurerXGuardianBossFemaleBreton2` (FormID `00DDF7`) — "LOC_FN_ConjurerXGuardianBossFemaleBreton2"
- `ConjurerXGuardianBossFemaleBreton3` (FormID `00DDF8`) — "LOC_FN_ConjurerXGuardianBossFemaleBreton3"
- `ConjurerXGuardianBossFemaleHighElf` (FormID `00DDF9`) — "LOC_FN_ConjurerXGuardianBossFemaleHighElf"
- `ConjurerXGuardianBossFemaleHighElf2` (FormID `00DDFA`) — "LOC_FN_ConjurerXGuardianBossFemaleHighElf2"
- `ConjurerXGuardianBossFemaleHighElf3` (FormID `00DDFB`) — "LOC_FN_ConjurerXGuardianBossFemaleHighElf3"

**Changed:**

- `ConjurerZGuardianBossFemaleBreton2` (FormID `003F14`) — "LOC_FN_ConjurerZGuardianBossFemaleBreton2" — `full`: `'Astral Mistress'` → `'LOC_FN_ConjurerZGuardianBossFemaleBreton2'`
- `ConjurerZGuardianBossFemaleHighElf2` (FormID `003F15`) — "LOC_FN_ConjurerZGuardianBossFemaleHighElf2" — `full`: `'Astral Mistress'` → `'LOC_FN_ConjurerZGuardianBossFemaleHighElf2'`
- `ConjurerZGuardianBossMaleBreton2` (FormID `003F16`) — "LOC_FN_ConjurerZGuardianBossMaleBreton2" — `full`: `'Astral Lord'` → `'LOC_FN_ConjurerZGuardianBossMaleBreton2'`
- `ConjurerZGuardianBossMaleHighElf2` (FormID `003F17`) — "LOC_FN_ConjurerZGuardianBossMaleHighElf2" — `full`: `'Astral Lord'` → `'LOC_FN_ConjurerZGuardianBossMaleHighElf2'`
- `ConjurerZGuardianFemaleBreton2` (FormID `003F18`) — "LOC_FN_ConjurerZGuardianFemaleBreton2" — `full`: `'Guardian of Oblivion'` → `'LOC_FN_ConjurerZGuardianFemaleBreton2'`
- `ConjurerZGuardianFemaleHighElf1` (FormID `003F19`) — "LOC_FN_ConjurerZGuardianFemaleHighElf1" — `full`: `'Guardian of Oblivion'` → `'LOC_FN_ConjurerZGuardianFemaleHighElf1'`
- `ConjurerZGuardianMaleBreton1` (FormID `003F1A`) — "LOC_FN_ConjurerZGuardianMaleBreton1" — `full`: `'Guardian of Oblivion'` → `'LOC_FN_ConjurerZGuardianMaleBreton1'`
- `ConjurerZGuardianMaleHighElf2` (FormID `003F1B`) — "LOC_FN_ConjurerZGuardianMaleHighElf2" — `full`: `'Guardian of Oblivion'` → `'LOC_FN_ConjurerZGuardianMaleHighElf2'`
- `ArgonianSmugglerFighter1` (FormID `007229`) — "LOC_FN_ArgonianSmugglerFighter1" — `full`: `'Black Marsh Smuggler'` → `'LOC_FN_ArgonianSmugglerFighter1'`
- `ArgonianSmugglerFighter2` (FormID `007235`) — "LOC_FN_ArgonianSmugglerFighter2" — `full`: `'Black Marsh Smuggler'` → `'LOC_FN_ArgonianSmugglerFighter2'`
- `ArgonianSmugglerFighter3` (FormID `007746`) — "LOC_FN_ArgonianSmugglerFighter3" — `full`: `'Black Marsh Smuggler'` → `'LOC_FN_ArgonianSmugglerFighter3'`
- `ArgonianSmugglerFighter4` (FormID `007747`) — "LOC_FN_ArgonianSmugglerFighter4" — `full`: `'Black Marsh Smuggler'` → `'LOC_FN_ArgonianSmugglerFighter4'`
- `ArgonianSmugglerFighter5` (FormID `007748`) — "LOC_FN_ArgonianSmugglerFighter5" — `full`: `'Black Marsh Smuggler'` → `'LOC_FN_ArgonianSmugglerFighter5'`
- `ArgonianSmugglerFighter6` (FormID `007749`) — "LOC_FN_ArgonianSmugglerFighter6" — `full`: `'Black Marsh Smuggler'` → `'LOC_FN_ArgonianSmugglerFighter6'`
- `ArgonianSmugglerFighter7` (FormID `00774A`) — "LOC_FN_ArgonianSmugglerFighter7" — `full`: `'Black Marsh Smuggler'` → `'LOC_FN_ArgonianSmugglerFighter7'`
- `ArgonianSmugglerFighter8` (FormID `00774B`) — "LOC_FN_ArgonianSmugglerFighter8" — `full`: `'Black Marsh Smuggler'` → `'LOC_FN_ArgonianSmugglerFighter8'`
- `ArgonianSmugglerFighterMale1` (FormID `00774C`) — "LOC_FN_ArgonianSmugglerFighterMale1" — `full`: `'Black Marsh Smuggler'` → `'LOC_FN_ArgonianSmugglerFighterMale1'`
- `ArgonianSmugglerFighterMale2` (FormID `00774D`) — "LOC_FN_ArgonianSmugglerFighterMale2" — `full`: `'Black Marsh Smuggler'` → `'LOC_FN_ArgonianSmugglerFighterMale2'`
- `ArgonianSmugglerFighterMale3` (FormID `00774E`) — "LOC_FN_ArgonianSmugglerFighterMale3" — `full`: `'Black Marsh Smuggler'` → `'LOC_FN_ArgonianSmugglerFighterMale3'`
- `ArgonianSmugglerFighterMale4` (FormID `00774F`) — "LOC_FN_ArgonianSmugglerFighterMale4" — `full`: `'Black Marsh Smuggler'` → `'LOC_FN_ArgonianSmugglerFighterMale4'`

_…61 more changed omitted (see JSON for full list)_

