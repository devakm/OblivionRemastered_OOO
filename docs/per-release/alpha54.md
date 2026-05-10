# alpha54 — release notes

_Compared against `alpha53`._

## File-level changes

- Added: 1
- Removed: 0
- Changed: 11

### Added

- `OblivionRemastered/Content/Dev/ObvData/Data/OOO_ThePunishedRestored.esp`

### Changed

- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_ACTI.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_ALCH.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_ARMO.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_BOOK.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_CELL.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_CREA.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_ENCH.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_QUST.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_SCPT.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/Oscuro's_Oblivion_Overhaul.esp`
- `OblivionRemastered/Content/Dev/ObvData/Data/SyncMap/Oscuro's_Oblivion_Overhaul.ini`

## ESP changes — `OOO_ThePunishedRestored.esp`

_Initial inventory (no prior version to compare against)._

- **Activator (ACTI):** 22 records
- **Potion / Ingestible (ALCH):** 286 records
- **Ammunition (AMMO):** 172 records
- **Armor (ARMO):** 1717 records
- **Book (BOOK):** 197 records
- **Cell (CELL):** 976 records
- **Class (CLAS):** 36 records
- **Clothing (CLOT):** 620 records
- **Container (CONT):** 652 records
- **Creature (CREA):** 1106 records
- **Combat Style (CSTY):** 185 records
- **Dialogue Topic (DIAL):** 28 records
- **Door (DOOR):** 33 records
- **Effect Shader (EFSH):** 9 records
- **Enchantment (ENCH):** 915 records
- **Faction (FACT):** 143 records
- **Global Variable (GLOB):** 75 records
- **Game Setting (GMST):** 26 records
- **Idle Animation (IDLE):** 57 records
- **Ingredient (INGR):** 141 records
- **Key (KEYM):** 79 records
- **Light (LIGH):** 31 records
- **Leveled Creature List (LVLC):** 1027 records
- **Leveled Item List (LVLI):** 3081 records
- **Leveled Spell List (LVSP):** 37 records
- **Magic Effect (MGEF):** 74 records
- **Misc Item (MISC):** 427 records
- **NPC (NPC_):** 2899 records
- **AI Package (PACK):** 716 records
- **Quest (QUST):** 66 records
- **Race (RACE):** 13 records
- **Script (SCPT):** 636 records
- **Sigil Stone (SGST):** 24 records
- **Skill (SKIL):** 21 records
- **Soul Gem (SLGM):** 30 records
- **Sound (SOUN):** 45 records
- **Spell (SPEL):** 1199 records
- **Static Object (STAT):** 1 records
- **Weapon (WEAP):** 2270 records
- **Worldspace (WRLD):** 27 records

## ESP changes — `Oscuro's_Oblivion_Overhaul.esp`

### Activator (ACTI) — +1 -0 ~0

**Added:**

- `OOOMelusPetiliusLongsword` (FormID `00DDB7`) — "LOC_FN_OOOMelusPetiliusLongsword"

### Armor (ARMO) — +14 -0 ~2

**Added:**

- `NDArmorHeavyShield5` (FormID `000EB0`) — "LOC_FN_NDArmorHeavyShield5"
- `NDArmorHeavyHelmet5` (FormID `000EB1`) — "LOC_FN_NDArmorHeavyHelmet5"
- `NDArmorHeavyGreaves5` (FormID `000EB2`) — "LOC_FN_NDArmorHeavyGreaves5"
- `NDArmorHeavyGauntlets5` (FormID `000EB3`) — "LOC_FN_NDArmorHeavyGauntlets5"
- `NDArmorHeavyCuirass5` (FormID `000EB4`) — "LOC_FN_NDArmorHeavyCuirass5"
- `NDArmorHeavyBoots5` (FormID `000EB5`) — "LOC_FN_NDArmorHeavyBoots5"
- `NDArmorHeavyShield4` (FormID `000EB6`) — "LOC_FN_NDArmorHeavyShield4"
- `NDArmorHeavyHelmet4` (FormID `000EB7`) — "LOC_FN_NDArmorHeavyHelmet4"
- `NDArmorHeavyGreaves4` (FormID `000EB8`) — "LOC_FN_NDArmorHeavyGreaves4"
- `NDArmorHeavyGauntlets4` (FormID `000EB9`) — "LOC_FN_NDArmorHeavyGauntlets4"
- `NDArmorHeavyCuirass4` (FormID `000EBA`) — "LOC_FN_NDArmorHeavyCuirass4"
- `NDArmorHeavyBoots4` (FormID `000EBB`) — "LOC_FN_NDArmorHeavyBoots4"
- `NDArmorHeavyShield3` (FormID `000EBC`) — "LOC_FN_NDArmorHeavyShield3"
- `NDArmorHeavyGreaves3` (FormID `000EBE`) — "LOC_FN_NDArmorHeavyGreaves3"

**Changed:**

- `RedDragonShieldHeavyOOO` (FormID `025BB9`) — "LOC_FN_RedDragonShieldHeavyOOO" — `modl`: `'armor\\reddragonsh\\shield.nif'` → `'Armor\\Orcish\\Shield.NIF'`
- `RedDragonShieldLightOOO` (FormID `025BBA`) — "LOC_FN_RedDragonShieldLightOOO" — `modl`: `'armor\\reddragonsh\\shield.nif'` → `'Armor\\Orcish\\Shield.NIF'`

### Book (BOOK) — +0 -0 ~2

**Changed:**

- `ZNoteSkingradDisturbances` (FormID `014244`) — "LOC_FN_ZNoteSkingradDisturbances" — `edid`: `'ZNoteSingradDisturbances'` → `'ZNoteSkingradDisturbances'`; `full`: `'LOC_FN_ZNoteSingradDisturbances'` → `'LOC_FN_ZNoteSkingradDisturbances'`
- `ZNoteSkingradDisturbancesPU` (FormID `022786`) — "LOC_FN_ZNoteSkingradDisturbancesPU" — `edid`: `'ZNoteSingradDisturbancesPU'` → `'ZNoteSkingradDisturbancesPU'`; `full`: `'LOC_FN_ZNoteSingradDisturbancesPU'` → `'LOC_FN_ZNoteSkingradDisturbancesPU'`

### Cell (CELL) — +0 -0 ~1

**Changed:**

- `UnderpallCave05` (FormID `03E22F`) — "LOC_FN_UnderpallCave05" — `full`: `'Underpall Reflecting Chamber'` → `'LOC_FN_UnderpallCave05'`

### Creature (CREA) — +0 -0 ~10

**Changed:**

- `OOOSECreatureBeetle` (FormID `000EDA`) — "LOC_FN_OOOSECreatureBeetle" — `full`: `'Shalk Beetle'` → `'LOC_FN_OOOSECreatureBeetle'`
- `OOOSECreatureOoze2` (FormID `0037F5`) — "LOC_FN_OOOSECreatureOoze2" — `full`: `'Red Fungus'` → `'LOC_FN_OOOSECreatureOoze2'`
- `OOOSECreatureOoze3` (FormID `0037F6`) — "LOC_FN_OOOSECreatureOoze3" — `full`: `'Necrotic Sludge'` → `'LOC_FN_OOOSECreatureOoze3'`
- `CreatureOgreZ1` (FormID `0089F0`) — "LOC_FN_CreatureOgreZ1" — `full`: `'Ravenous Ogre'` → `'LOC_FN_CreatureOgreZ1'`
- `DeadZombieOOOCorpse` (FormID `01C2F9`) — "LOC_FN_DeadZombieOOOCorpse" — `full`: `'Rotten Corpse'` → `'LOC_FN_DeadZombieOOOCorpse'`
- `DeadSkeleton3` (FormID `032660`) — "LOC_FN_DeadSkeleton3" — `full`: `'Skeleton'` → `'LOC_FN_DeadSkeleton3'`
- `OOOSEErrorScalon` (FormID `058A20`) — "LOC_FN_OOOSEErrorScalon" — `full`: `'Well-Fed Scalon'` → `'LOC_FN_OOOSEErrorScalon'`
- `OOOSEMiriliElytra3` (FormID `07140C`) — "LOC_FN_OOOSEMiriliElytra3" — `full`: `"Mirili's Elytra"` → `'LOC_FN_OOOSEMiriliElytra3'`
- `OOOSEMiriliElytra4` (FormID `07140D`) — "LOC_FN_OOOSEMiriliElytra4" — `full`: `"Mirili's Elytra"` → `'LOC_FN_OOOSEMiriliElytra4'`
- `OOOSEMiriliBaliwog1` (FormID `071410`) — "LOC_FN_OOOSEMiriliBaliwog1" — `full`: `"Mirili's Baliwog"` → `'LOC_FN_OOOSEMiriliBaliwog1'`

### Enchantment (ENCH) — +7 -0 ~0

**Added:**

- `EnWeapZPAOL` (FormID `00DE0D`)
- `OOOHFEnchArmorShield` (FormID `00DE0E`)
- `OOOHFEnchArmorBoots` (FormID `00DE0F`)
- `OOOHFEnchArmorCuirass` (FormID `00DE10`)
- `OOOHFEnchArmorHelmet` (FormID `00DE11`)
- `OOOHFEnchArmorGauntlets` (FormID `00DE12`)
- `OOOHFEnchArmorGreaves` (FormID `00DE13`)

### Leveled Item List (LVLI) — +1 -1 ~253

**Added:**

- `OOOSELootStaff50Greater` (FormID `08DDB7`)

**Removed:**

- `OOOSELootStaff50Greater` (FormID `00DDB7`)

**Changed:**

- `AyleidLootboxWeaponsUnleveledLow` (FormID `001711`) — + entry: level 1 × 1 → `003F84`; + entry: level 1 × 1 → `003F86`; + entry: level 1 × 1 → `003F8A`; + entry: level 1 × 1 → `003F8B`; + entry: level 1 × 1 → `0513A0`; + entry: level 1 × 10 → `002AE0`; - entry: level 1 × 2 → `02686E`
- `AyleidLootboxWeaponsUnleveledMed` (FormID `001712`) — + entry: level 1 × 1 → `002AE2`; + entry: level 1 × 1 → `003F83`; + entry: level 1 × 1 → `003F84`; + entry: level 1 × 1 → `003F85`; + entry: level 1 × 1 → `003F86`; + entry: level 1 × 1 → `003F88`; + entry: level 1 × 1 → `003F89`; + entry: level 1 × 1 → `003F8A`; + entry: level 1 × 1 → `003F8B`; + entry: level 1 × 1 → `00D3E1`; + entry: level 1 × 1 → `0513A0`; + entry: level 1 × 5 → `002AE1`; + entry: level 1 × 10 → `002AE0`; - entry: level 1 × 2 → `02686E`
- `AyleidLootboxWeaponsUnleveledAll` (FormID `001713`) — + entry: level 1 × 1 → `002AE2`; + entry: level 1 × 1 → `003F82`; + entry: level 1 × 1 → `003F83`; + entry: level 1 × 1 → `003F84`; + entry: level 1 × 1 → `003F86`; + entry: level 1 × 1 → `003F87`; + entry: level 1 × 1 → `003F88`; + entry: level 1 × 1 → `003F8A`; + entry: level 1 × 1 → `003F8B`; + entry: level 1 × 1 → `00D3E1`; + entry: level 1 × 1 → `0513A0`; + entry: level 1 × 1 → `0513A9`; + entry: level 1 × 5 → `002AE1`; + entry: level 1 × 10 → `002AE0`; - entry: level 1 × 2 → `02686E`
- `AyleidLootboxWeaponsUnleveledHighAll` (FormID `001714`) — + entry: level 1 × 1 → `002AE2`; + entry: level 1 × 1 → `003F82`; + entry: level 1 × 1 → `003F83`; + entry: level 1 × 1 → `003F84`; + entry: level 1 × 1 → `003F86`; + entry: level 1 × 1 → `003F87`; + entry: level 1 × 1 → `003F88`; + entry: level 1 × 1 → `003F8A`; + entry: level 1 × 1 → `003F8B`; + entry: level 1 × 1 → `00D3E1`; + entry: level 1 × 1 → `0513A0`; + entry: level 1 × 1 → `0513A9`; + entry: level 1 × 5 → `002AE1`; + entry: level 1 × 10 → `002AE0`; - entry: level 1 × 2 → `02686E`
- `AyleidLootboxWeaponsNecro` (FormID `001715`) — + entry: level 9 × 1 → `003F8B`; + entry: level 10 × 1 → `003F86`; + entry: level 14 × 1 → `003F8A`; + entry: level 15 × 1 → `0513A0`; + entry: level 15 × 10 → `002AE0`; + entry: level 16 × 1 → `003F84`; + entry: level 18 × 1 → `003F86`; + entry: level 18 × 1 → `003F89`; + entry: level 18 × 1 → `003F8B`; + entry: level 20 × 1 → `003F85`; + entry: level 20 × 1 → `003F88`; + entry: level 20 × 5 → `002AE1`; + entry: level 22 × 1 → `003F83`; + entry: level 22 × 1 → `003F8A`; + entry: level 22 × 1 → `0513A0`; + entry: level 23 × 1 → `003F84`; + entry: level 23 × 10 → `002AE0`; + entry: level 25 × 1 → `002AE2`; + entry: level 25 × 1 → `00D3E1`; + entry: level 26 × 1 → `003F86`; + entry: level 26 × 1 → `003F89`; + entry: level 26 × 1 → `003F8B`; + entry: level 28 × 1 → `003F85`; + entry: level 28 × 1 → `003F87`; + entry: level 28 × 1 → `003F88`; + entry: level 28 × 5 → `002AE1`; + entry: level 30 × 1 → `003F82`; + entry: level 30 × 1 → `0513A9`; - entry: level 1 × 2 → `02686E`
- `AyleidLootboxWeaponsConjBoss` (FormID `001716`) — + entry: level 9 × 1 → `003F8B`; + entry: level 10 × 1 → `003F86`; + entry: level 14 × 1 → `003F8A`; + entry: level 15 × 1 → `0513A0`; + entry: level 15 × 10 → `002AE0`; + entry: level 16 × 1 → `003F84`; + entry: level 18 × 1 → `003F86`; + entry: level 18 × 1 → `003F8B`; + entry: level 20 × 1 → `003F88`; + entry: level 20 × 5 → `002AE1`; + entry: level 22 × 1 → `003F83`; + entry: level 22 × 1 → `003F8A`; + entry: level 22 × 1 → `0513A0`; + entry: level 23 × 1 → `003F84`; + entry: level 23 × 10 → `002AE0`; + entry: level 25 × 1 → `002AE2`; + entry: level 25 × 1 → `00D3E1`; + entry: level 26 × 1 → `003F86`; + entry: level 26 × 1 → `003F8B`; + entry: level 28 × 1 → `003F87`; + entry: level 28 × 1 → `003F88`; + entry: level 28 × 5 → `002AE1`; + entry: level 30 × 1 → `003F82`; + entry: level 30 × 1 → `0513A9`; - entry: level 1 × 2 → `02686E`
- `AyleidLootboxWeaponsVamp` (FormID `001717`) — + entry: level 9 × 1 → `003F8B`; + entry: level 10 × 1 → `003F86`; + entry: level 14 × 1 → `003F8A`; + entry: level 15 × 1 → `0513A0`; + entry: level 15 × 10 → `002AE0`; + entry: level 16 × 1 → `003F84`; + entry: level 18 × 1 → `003F86`; + entry: level 18 × 1 → `003F8B`; + entry: level 20 × 1 → `003F88`; + entry: level 20 × 5 → `002AE1`; + entry: level 22 × 1 → `003F83`; + entry: level 22 × 1 → `003F8A`; + entry: level 22 × 1 → `0513A0`; + entry: level 23 × 1 → `003F84`; + entry: level 23 × 10 → `002AE0`; + entry: level 25 × 1 → `002AE2`; + entry: level 25 × 1 → `00D3E1`; + entry: level 26 × 1 → `003F86`; + entry: level 26 × 1 → `003F8B`; + entry: level 28 × 1 → `003F87`; + entry: level 28 × 1 → `003F88`; + entry: level 28 × 5 → `002AE1`; + entry: level 30 × 1 → `003F82`; + entry: level 30 × 1 → `0513A9`; - entry: level 1 × 2 → `02686E`
- `AyleidLootboxWeaponsConj` (FormID `001718`) — + entry: level 9 × 1 → `003F8B`; + entry: level 10 × 1 → `003F86`; + entry: level 14 × 1 → `003F8A`; + entry: level 15 × 1 → `0513A0`; + entry: level 15 × 10 → `002AE0`; + entry: level 16 × 1 → `003F84`; + entry: level 18 × 1 → `003F86`; + entry: level 18 × 1 → `003F8B`; + entry: level 20 × 1 → `003F88`; + entry: level 20 × 5 → `002AE1`; + entry: level 22 × 1 → `003F83`; + entry: level 22 × 1 → `003F8A`; + entry: level 22 × 1 → `0513A0`; + entry: level 23 × 1 → `003F84`; + entry: level 23 × 10 → `002AE0`; + entry: level 25 × 1 → `002AE2`; + entry: level 25 × 1 → `00D3E1`; + entry: level 26 × 1 → `003F86`; + entry: level 26 × 1 → `003F8B`; + entry: level 28 × 1 → `003F87`; + entry: level 28 × 1 → `003F88`; + entry: level 28 × 5 → `002AE1`; + entry: level 30 × 1 → `003F82`; + entry: level 30 × 1 → `0513A9`; - entry: level 1 × 2 → `02686E`
- `AyleidLootboxWeaponsConjSmall` (FormID `001719`) — + entry: level 9 × 1 → `003F8B`; + entry: level 10 × 1 → `003F86`; + entry: level 14 × 1 → `003F8A`; + entry: level 15 × 1 → `0513A0`; + entry: level 15 × 10 → `002AE0`; + entry: level 16 × 1 → `003F84`; + entry: level 18 × 1 → `003F86`; + entry: level 18 × 1 → `003F8B`; + entry: level 20 × 5 → `002AE1`; + entry: level 23 × 1 → `0513A0`; + entry: level 23 × 10 → `002AE0`; + entry: level 25 × 1 → `002AE2`; - entry: level 1 × 2 → `02686E`
- `AyleidLootboxWeaponsConjBossSmall` (FormID `00171A`) — + entry: level 9 × 1 → `003F8B`; + entry: level 10 × 1 → `003F86`; + entry: level 14 × 1 → `003F8A`; + entry: level 15 × 1 → `0513A0`; + entry: level 15 × 10 → `002AE0`; + entry: level 16 × 1 → `003F84`; + entry: level 18 × 1 → `003F86`; + entry: level 18 × 1 → `003F8B`; + entry: level 20 × 5 → `002AE1`; + entry: level 23 × 1 → `0513A0`; + entry: level 23 × 10 → `002AE0`; + entry: level 25 × 1 → `002AE2`; - entry: level 1 × 2 → `02686E`
- `AyleidLootboxWeaponsMarauderBoss` (FormID `00171B`) — + entry: level 9 × 1 → `003F8B`; + entry: level 10 × 1 → `003F86`; + entry: level 14 × 1 → `003F8A`; + entry: level 15 × 1 → `0513A0`; + entry: level 15 × 10 → `002AE0`; + entry: level 16 × 1 → `003F84`; + entry: level 18 × 1 → `003F86`; + entry: level 18 × 1 → `003F8B`; + entry: level 20 × 1 → `003F88`; + entry: level 20 × 5 → `002AE1`; + entry: level 22 × 1 → `003F83`; + entry: level 22 × 1 → `003F8A`; + entry: level 22 × 1 → `0513A0`; + entry: level 23 × 1 → `003F84`; + entry: level 23 × 10 → `002AE0`; + entry: level 25 × 1 → `002AE2`; + entry: level 25 × 1 → `00D3E1`; + entry: level 26 × 1 → `003F86`; + entry: level 26 × 1 → `003F8B`; + entry: level 28 × 1 → `003F87`; + entry: level 28 × 1 → `003F88`; + entry: level 28 × 5 → `002AE1`; + entry: level 30 × 1 → `003F82`; + entry: level 30 × 1 → `0513A9`; - entry: level 1 × 2 → `02686E`
- `AyleidLootboxWeaponsMarauder` (FormID `00171C`) — + entry: level 9 × 1 → `003F8B`; + entry: level 10 × 1 → `003F86`; + entry: level 14 × 1 → `003F8A`; + entry: level 15 × 1 → `0513A0`; + entry: level 15 × 10 → `002AE0`; + entry: level 16 × 1 → `003F84`; + entry: level 18 × 1 → `003F86`; + entry: level 20 × 1 → `003F88`; + entry: level 20 × 5 → `002AE1`; + entry: level 22 × 1 → `003F83`; + entry: level 22 × 1 → `003F8A`; + entry: level 22 × 1 → `0513A0`; + entry: level 23 × 1 → `003F84`; + entry: level 23 × 10 → `002AE0`; + entry: level 25 × 1 → `002AE2`; + entry: level 25 × 1 → `00D3E1`; + entry: level 26 × 1 → `003F86`; + entry: level 26 × 1 → `003F89`; + entry: level 26 × 1 → `003F8B`; + entry: level 28 × 1 → `003F85`; + entry: level 28 × 1 → `003F87`; + entry: level 28 × 1 → `003F88`; + entry: level 28 × 5 → `002AE1`; + entry: level 30 × 1 → `003F82`; + entry: level 30 × 1 → `0513A9`; - entry: level 1 × 2 → `02686E`
- `AyleidLootboxWeaponsMarauderSmall` (FormID `00171D`) — + entry: level 9 × 1 → `003F8B`; + entry: level 10 × 1 → `003F86`; + entry: level 14 × 1 → `003F8A`; + entry: level 15 × 10 → `002AE0`; + entry: level 16 × 1 → `003F84`; + entry: level 18 × 1 → `003F86`; + entry: level 18 × 1 → `003F8B`; + entry: level 20 × 5 → `002AE1`; + entry: level 22 × 1 → `003F8A`; + entry: level 23 × 10 → `002AE0`; + entry: level 25 × 1 → `002AE2`; - entry: level 1 × 2 → `02686E`
- `AyleidLootboxWeaponsMarauderBossSmall` (FormID `00171E`) — + entry: level 9 × 1 → `003F8B`; + entry: level 10 × 1 → `003F86`; + entry: level 14 × 1 → `003F8A`; + entry: level 15 × 10 → `002AE0`; + entry: level 16 × 1 → `003F84`; + entry: level 18 × 1 → `003F86`; + entry: level 18 × 1 → `003F8B`; + entry: level 20 × 5 → `002AE1`; + entry: level 22 × 1 → `003F8A`; + entry: level 23 × 10 → `002AE0`; + entry: level 25 × 1 → `002AE2`; - entry: level 1 × 2 → `02686E`
- `AyleidLootboxWeaponsNecroBoss` (FormID `00171F`) — + entry: level 9 × 1 → `003F8B`; + entry: level 10 × 1 → `003F86`; + entry: level 14 × 1 → `003F8A`; + entry: level 15 × 1 → `0513A0`; + entry: level 15 × 10 → `002AE0`; + entry: level 16 × 1 → `003F84`; + entry: level 18 × 1 → `003F86`; + entry: level 18 × 1 → `003F8B`; + entry: level 20 × 1 → `003F88`; + entry: level 20 × 5 → `002AE1`; + entry: level 22 × 1 → `003F83`; + entry: level 22 × 1 → `003F8A`; + entry: level 22 × 1 → `0513A0`; + entry: level 23 × 1 → `003F84`; + entry: level 23 × 10 → `002AE0`; + entry: level 25 × 1 → `002AE2`; + entry: level 25 × 1 → `00D3E1`; + entry: level 26 × 1 → `003F86`; + entry: level 26 × 1 → `003F8B`; + entry: level 28 × 1 → `003F87`; + entry: level 28 × 1 → `003F88`; + entry: level 28 × 5 → `002AE1`; + entry: level 30 × 1 → `003F82`; + entry: level 30 × 1 → `0513A9`; - entry: level 1 × 2 → `02686E`
- `AyleidLootboxWeaponsNecroSmall` (FormID `001720`) — + entry: level 9 × 1 → `003F8B`; + entry: level 10 × 1 → `003F86`; + entry: level 14 × 1 → `003F8A`; + entry: level 15 × 1 → `0513A0`; + entry: level 15 × 10 → `002AE0`; + entry: level 16 × 1 → `003F84`; + entry: level 18 × 1 → `003F86`; + entry: level 18 × 1 → `003F8B`; + entry: level 20 × 5 → `002AE1`; + entry: level 23 × 1 → `0513A0`; + entry: level 23 × 10 → `002AE0`; + entry: level 25 × 1 → `002AE2`; - entry: level 1 × 2 → `02686E`
- `AyleidLootboxWeaponsNecroBossSmall` (FormID `001721`) — + entry: level 9 × 1 → `003F8B`; + entry: level 10 × 1 → `003F86`; + entry: level 14 × 1 → `003F8A`; + entry: level 15 × 1 → `0513A0`; + entry: level 15 × 10 → `002AE0`; + entry: level 16 × 1 → `003F84`; + entry: level 18 × 1 → `003F86`; + entry: level 18 × 1 → `003F8B`; + entry: level 20 × 5 → `002AE1`; + entry: level 23 × 1 → `0513A0`; + entry: level 23 × 10 → `002AE0`; + entry: level 25 × 1 → `002AE2`; - entry: level 1 × 2 → `02686E`
- `AyleidHalberdGreatMaceCombo` (FormID `003256`) — + entry: level 1 × 1 → `003F82`; - entry: level 1 × 2 → `02686E`
- `AyleidGreatmace` (FormID `003F82`) — + entry: level 1 × 1 → `0025CF`; + entry: level 1 × 1 → `0025D1`; + entry: level 1 × 1 → `0025D2`; + entry: level 1 × 1 → `0025D3`; + entry: level 1 × 1 → `0025D4`; + entry: level 1 × 1 → `0025D5`; + entry: level 1 × 1 → `0025D6`; + entry: level 1 × 1 → `051356`; - entry: level 1 × 2 → `02686E`
- `AyleidBattleAxe` (FormID `003F83`) — + entry: level 1 × 1 → `0016C7`; + entry: level 1 × 1 → `0016C8`; + entry: level 1 × 1 → `0016DF`; + entry: level 1 × 1 → `0016E0`; + entry: level 1 × 1 → `0016E2`; + entry: level 1 × 1 → `051384`; + entry: level 1 × 1 → `051385`; - entry: level 1 × 2 → `02686E`

_…233 more changed omitted (see JSON for full list)_

### Magic Effect (MGEF) — +0 -0 ~1

**Changed:**

- `REDG` (FormID `00188A`) — "LOC_FN_REDG" — `modl`: `None` → `'MagicEffects\\mysticism.nif'`

### NPC (NPC_) — +0 -1 ~0

**Removed:**

- `Carandial` (FormID `00A108`) — "LOC_FN_Carandial"

### Script (SCPT) — +1 -0 ~0

**Added:**

- `7HeavenFuryLongswordScript` (FormID `07DDB8`)

### Weapon (WEAP) — +0 -0 ~1

**Changed:**

- `WeapSeverianSilverDaikatana` (FormID `033EFF`) — "LOC_FN_WeapSeverianSilverDaikatana" — `modl`: `'Weapons\\SeverianKatana\\silverdaikatana.nif'` → `'Weapons\\Akaviri weapon\\LongSword.NIF'`

