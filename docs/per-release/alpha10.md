# alpha10 — release notes

_Compared against `alpha09`._

## File-level changes

- Added: 2
- Removed: 0
- Changed: 3

### Added

- `Content/Dev/ObvData/Data/Oscuro's_Oblivion_Overhaul137.esp`
- `Content/Dev/ObvData/Data/Oscuro's_Oblivion_Overhaul137ESM.esp`

### Changed

- `Content/Dev/ObvData/Data/OOO_NewCreatureComps.esp`
- `Content/Dev/ObvData/Data/OOO_NewCreatures03.esp`
- `Content/Dev/ObvData/Data/Oscuro's_Oblivion_Overhaul.esp`

## ESP changes — `OOO_GameSettings.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewArmor.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewArmor03.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewArmorComps.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewArmorOdds.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewChestComps.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewChests.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewChests03.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewChests2.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewCreatureComps.esp`

**Master list changed:**

- before: ['Oblivion.esm', "Oscuro's_Oblivion_Overhaul.esp"]
- after:  ['Oblivion.esm', 'Knights.esp', "Oscuro's_Oblivion_Overhaul.esp"]

### Creature (CREA) — +57 -0 ~0

**Added:**

- `CreatureMudCrab` (FormID `000B7F`) — "LOC_FN_CreatureMudCrab"
- `CreatureXivilaiNOSUMMON` (FormID `000FE2`) — "LOC_FN_CreatureXivilaiNOSUMMON"
- `CreatureXivilaiWeaponNOSUMMON` (FormID `000FE3`) — "LOC_FN_CreatureXivilaiWeaponNOSUMMON"
- `CreatureTroll` (FormID `002DBC`) — "LOC_FN_CreatureTroll"
- `CreatureGoblin5Warlord` (FormID `00AB71`) — "LOC_FN_CreatureGoblin5Warlord"
- `CreatureGoblin5WarlordArcher` (FormID `00ABD1`) — "LOC_FN_CreatureGoblin5WarlordArcher"
- `CreatureOgre` (FormID `00C20D`) — "LOC_FN_CreatureOgre"
- `CreatureSheep` (FormID `0151DD`) — "LOC_FN_CreatureSheep"
- `CreatureWraith2GloomWeapon` (FormID `01E5EB`) — "LOC_FN_CreatureWraith2GloomWeapon"
- `CreatureAtronachFlame` (FormID `01E5EF`) — "LOC_FN_CreatureAtronachFlame"
- `CreatureWraith0Faded` (FormID `01E5F3`) — "LOC_FN_CreatureWraith0Faded"
- `CreatureDog` (FormID `01E5F5`) — "LOC_FN_CreatureDog"
- `CreatureWolfTimber` (FormID `01E5F6`) — "LOC_FN_CreatureWolfTimber"
- `CreatureMountainLion` (FormID `01E5FA`) — "LOC_FN_CreatureMountainLion"
- `CreatureMinotaurLordWeapon` (FormID `01E648`) — "LOC_FN_CreatureMinotaurLordWeapon"
- `CreatureImp` (FormID `01E649`) — "LOC_FN_CreatureImp"
- `CreatureSpriggan` (FormID `01E64B`) — "LOC_FN_CreatureSpriggan"
- `CreatureSpiderDaedra` (FormID `01E64C`) — "LOC_FN_CreatureSpiderDaedra"
- `CreatureXivilaiWeapon` (FormID `01E64D`) — "LOC_FN_CreatureXivilaiWeapon"
- `CreatureGoblin1` (FormID `01FCB1`) — "LOC_FN_CreatureGoblin1"

_…37 more added omitted (see JSON for full list)_

## ESP changes — `OOO_NewCreatures01.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewCreatures02.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewCreatures03.esp`

### Creature (CREA) — +0 -65 ~121

**Removed:**

- `CreatureMudCrab` (FormID `000B7F`) — "Mud Crab"
- `CreatureXivilaiNOSUMMON` (FormID `000FE2`) — "Xivilai"
- `CreatureXivilaiWeaponNOSUMMON` (FormID `000FE3`) — "Xivilai"
- `CreatureMinotaur3` (FormID `009D6B`) — "LOC_FN_CreatureMinotaur3"
- `CreatureMinotaur4` (FormID `009D6C`) — "LOC_FN_CreatureMinotaur4"
- `CreatureMinotaur1Weapon` (FormID `009D6D`) — "LOC_FN_CreatureMinotaur1Weapon"
- `CreatureMinotaur2Weapon` (FormID `009D6E`) — "LOC_FN_CreatureMinotaur2Weapon"
- `CreatureMinotaur4Weapon` (FormID `009D6F`) — "LOC_FN_CreatureMinotaur4Weapon"
- `CreatureGoblin5Warlord` (FormID `00AB71`) — "Goblin Warlord"
- `CreatureGoblin5WarlordArcher` (FormID `00ABD1`) — "Goblin Warlord"
- `CreatureMinotaur2` (FormID `00B9ED`) — "LOC_FN_CreatureMinotaur2"
- `CreatureOgre` (FormID `00C20D`) — "LOC_FN_CreatureOgre"
- `CreatureSheep` (FormID `0151DD`) — "LOC_FN_CreatureSheep"
- `CreatureWraith2GloomWeapon` (FormID `01E5EB`) — "Gloom Wraith"
- `CreatureAtronachFlame` (FormID `01E5EF`) — "LOC_FN_CreatureAtronachFlame"
- `CreatureWraith0Faded` (FormID `01E5F3`) — "Faded Wraith"
- `CreatureDog` (FormID `01E5F5`) — "LOC_FN_CreatureDog"
- `CreatureWolfTimber` (FormID `01E5F6`) — "Timber Wolf"
- `CreatureMountainLion` (FormID `01E5FA`) — "Mountain Lion"
- `CreatureMinotaur3Weapon` (FormID `01E647`) — "LOC_FN_CreatureMinotaur3Weapon"

_…45 more removed omitted (see JSON for full list)_

**Changed:**

- `CreatureXivilaiWeaponAyleidNOSUMMON` (FormID `004E38`) — "LOC_FN_CreatureXivilaiWeapon" — `full`: `'Xivilai'` → `'LOC_FN_CreatureXivilaiWeapon'`
- `CreatureWolf1` (FormID `007FB9`) — "LOC_FN_CreatureWolf" — `full`: `'Wolf'` → `'LOC_FN_CreatureWolf'`
- `CreatureWolf2` (FormID `007FBA`) — "LOC_FN_CreatureWolf" — `full`: `'Wolf'` → `'LOC_FN_CreatureWolf'`
- `CreatureWolf3` (FormID `007FBB`) — "LOC_FN_CreatureWolf" — `full`: `'Wolf'` → `'LOC_FN_CreatureWolf'`
- `CreatureWolfTimber1` (FormID `007FCB`) — "LOC_FN_CreatureWolfTimber" — `full`: `'Timber Wolf'` → `'LOC_FN_CreatureWolfTimber'`
- `CreatureWolfTimber2` (FormID `007FCC`) — "LOC_FN_CreatureWolfTimber" — `full`: `'Timber Wolf'` → `'LOC_FN_CreatureWolfTimber'`
- `CreatureWolfTimber3` (FormID `007FCD`) — "LOC_FN_CreatureWolfTimber" — `full`: `'Timber Wolf'` → `'LOC_FN_CreatureWolfTimber'`
- `CreatureGoblin4Shamana` (FormID `0084E6`) — "LOC_FN_CreatureGoblin4Shaman" — `full`: `'Goblin Shaman'` → `'LOC_FN_CreatureGoblin4Shaman'`
- `CreatureGoblin4Shamanc` (FormID `0084E7`) — "LOC_FN_CreatureGoblin4Shaman" — `full`: `'Goblin Shaman'` → `'LOC_FN_CreatureGoblin4Shaman'`
- `CreatureGoblin5Warlorda` (FormID `0084E8`) — "LOC_FN_CreatureGoblin5Warlord" — `full`: `'Goblin Warlord'` → `'LOC_FN_CreatureGoblin5Warlord'`
- `CreatureGoblin5Warlordab` (FormID `0084E9`) — "LOC_FN_CreatureGoblin5Warlord" — `full`: `'Goblin Warlord'` → `'LOC_FN_CreatureGoblin5Warlord'`
- `CreatureGoblin5WarlordArchera` (FormID `0084EA`) — "LOC_FN_CreatureGoblin5WarlordArcher" — `full`: `'Goblin Warlord'` → `'LOC_FN_CreatureGoblin5WarlordArcher'`
- `CreatureGoblin5WarlordArcherab` (FormID `0084EB`) — "LOC_FN_CreatureGoblin5WarlordArcher" — `full`: `'Goblin Warlord'` → `'LOC_FN_CreatureGoblin5WarlordArcher'`
- `CreatureMountainLion1` (FormID `0084FD`) — "LOC_FN_CreatureMountainLion" — `full`: `'Mountain Lion'` → `'LOC_FN_CreatureMountainLion'`
- `CreatureMountainLion2` (FormID `0084FE`) — "LOC_FN_CreatureMountainLion" — `full`: `'Mountain Lion'` → `'LOC_FN_CreatureMountainLion'`
- `CreatureMountainLion3` (FormID `0084FF`) — "LOC_FN_CreatureMountainLion" — `full`: `'Mountain Lion'` → `'LOC_FN_CreatureMountainLion'`
- `CreatureMudCrab1` (FormID `0089E9`) — "LOC_FN_CreatureMudCrab" — `full`: `'Mud Crab'` → `'LOC_FN_CreatureMudCrab'`
- `CreatureMudCrab2` (FormID `0089EA`) — "LOC_FN_CreatureMudCrab" — `full`: `'Mud Crab'` → `'LOC_FN_CreatureMudCrab'`
- `CreatureMudCrab3` (FormID `0089EB`) — "LOC_FN_CreatureMudCrab" — `full`: `'Mud Crab'` → `'LOC_FN_CreatureMudCrab'`
- `CreatureSpriggan1` (FormID `0089F5`) — "LOC_FN_CreatureSpriggan" — `full`: `'Spriggan'` → `'LOC_FN_CreatureSpriggan'`

_…101 more changed omitted (see JSON for full list)_

## ESP changes — `OOO_NewCreatures04Special.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewMiscItems.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewNPCs03.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewNPCs04Special.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewRobesComp.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewWeaponComps.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewWeapons01.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewWeapons03.esp`

_No record-level changes detected._

## ESP changes — `Oscuro's_Oblivion_Overhaul.esp`

### Cell (CELL) — +4 -0 ~0

**Added:**

- `Nonungalo` (FormID `0A04E9`) — "LOC_FN_Nonungalo"
- `GreenmeadCave03` (FormID `0A7954`) — "LOC_FN_GreenmeadCave03"
- `GraveGroundCave` (FormID `01630A`) — "Grave Ground Cave"
- `ThunderingSteps02` (FormID `03A070`) — "Thundering Howl Caverns"

### Creature (CREA) — +3 -0 ~215

**Added:**

- `DeadZombieOOOCorpse` (FormID `01C2F9`) — "Rotten Corpse"
- `DeadSkeleton3` (FormID `032660`) — "Skeleton"
- `DeadSkeletonSpecialOOODreadSetHelmet` (FormID `04D52F`) — "Skeleton"

**Changed:**

- `CreatureWraith1Weapon` (FormID `098304`) — "LOC_FN_CreatureWraith1" — `full`: `'LOC_FN_CreatureWraith1Weapon'` → `'LOC_FN_CreatureWraith1'`
- `CreatureAtronachFrost4` (FormID `00309D`) — "LOC_FN_CreatureAtronachFrost" — `full`: `'Frost Atronach'` → `'LOC_FN_CreatureAtronachFrost'`
- `CreatureXivilaiWeaponAyleidNOSUMMON` (FormID `004E38`) — "LOC_FN_CreatureXivilaiWeapon" — `full`: `'Xivilai'` → `'LOC_FN_CreatureXivilaiWeapon'`
- `CreatureWolf1` (FormID `007FB9`) — "LOC_FN_CreatureWolf" — `full`: `'Wolf'` → `'LOC_FN_CreatureWolf'`
- `CreatureWolf2` (FormID `007FBA`) — "LOC_FN_CreatureWolf" — `full`: `'Wolf'` → `'LOC_FN_CreatureWolf'`
- `CreatureWolf3` (FormID `007FBB`) — "LOC_FN_CreatureWolf" — `full`: `'Wolf'` → `'LOC_FN_CreatureWolf'`
- `CreatureWolfTimber1` (FormID `007FCB`) — "LOC_FN_CreatureWolfTimber" — `full`: `'Timber Wolf'` → `'LOC_FN_CreatureWolfTimber'`
- `CreatureWolfTimber2` (FormID `007FCC`) — "LOC_FN_CreatureWolfTimber" — `full`: `'Timber Wolf'` → `'LOC_FN_CreatureWolfTimber'`
- `CreatureWolfTimber3` (FormID `007FCD`) — "LOC_FN_CreatureWolfTimber" — `full`: `'Timber Wolf'` → `'LOC_FN_CreatureWolfTimber'`
- `CreatureRat1` (FormID `007FD0`) — "LOC_FN_CreatureRat" — `full`: `'Rat'` → `'LOC_FN_CreatureRat'`
- `CreatureRat2` (FormID `007FD2`) — "LOC_FN_CreatureRat" — `full`: `'Rat'` → `'LOC_FN_CreatureRat'`
- `CreatureRat3` (FormID `007FD3`) — "LOC_FN_CreatureRat" — `full`: `'Rat'` → `'LOC_FN_CreatureRat'`
- `CreatureRat4` (FormID `007FD4`) — "LOC_FN_CreatureRat" — `full`: `'Rat'` → `'LOC_FN_CreatureRat'`
- `CreatureBearBlack1` (FormID `007FD9`) — "LOC_FN_CreatureBearBlack" — `full`: `'Black Bear'` → `'LOC_FN_CreatureBearBlack'`
- `CreatureBearBlack2` (FormID `007FDA`) — "LOC_FN_CreatureBearBlack" — `full`: `'Black Bear'` → `'LOC_FN_CreatureBearBlack'`
- `CreatureBearBlack3` (FormID `007FDB`) — "LOC_FN_CreatureBearBlack" — `full`: `'Black Bear'` → `'LOC_FN_CreatureBearBlack'`
- `CreatureBearBrown1` (FormID `007FDF`) — "LOC_FN_CreatureBearBrown" — `full`: `'Brown Bear'` → `'LOC_FN_CreatureBearBrown'`
- `CreatureBearBrown2` (FormID `007FE0`) — "LOC_FN_CreatureBearBrown" — `full`: `'Brown Bear'` → `'LOC_FN_CreatureBearBrown'`
- `CreatureBearBrown3` (FormID `007FE1`) — "LOC_FN_CreatureBearBrown" — `full`: `'Brown Bear'` → `'LOC_FN_CreatureBearBrown'`
- `CreatureBoar1` (FormID `007FE7`) — "LOC_FN_CreatureBoar" — `full`: `'Boar'` → `'LOC_FN_CreatureBoar'`

_…195 more changed omitted (see JSON for full list)_

### Misc Item (MISC) — +0 -0 ~1

**Changed:**

- `LionHide01Snow` (FormID `00329C`) — "Snow Lion Pelt" — `full`: `''` → `'Snow Lion Pelt'`; `modl`: `'clutter\\LionPeltFix\\snowlionhide.nif'` → `'Clutter\\LionHide.NIF'`

### NPC (NPC_) — +17 -0 ~0

**Added:**

- `AdventurerImperialWarrior01` (FormID `004776`) — "Adventurer"
- `AdventureDeadSpecial02` (FormID `0136F8`) — "Order of the Dragonborne's Knight"
- `AdventurerImperialWarrior01Dead` (FormID `01C2DF`) — "Rinfal Vrethu"
- `ACommoner02DeadAmazonLoveStruck` (FormID `021DE0`) — "Amel Lentus"
- `AdventurerImperialWarrior02` (FormID `021FD9`) — "Adventurer cape green"
- `AdventurerImperialWarrior03` (FormID `0224CA`) — "Adventurer cape red"
- `AdventurerImperialWarrior01Test` (FormID `025166`) — "Test AI Adv Package"
- `AdventurerImperialWarrior01Dead2` (FormID `027DEA`) — "Adventurer"
- `AdventurerOrcSpellsword01Dead` (FormID `028D43`) — "Adventurer"
- `ACommoner01Dead` (FormID `02926B`) — "Commoner"
- `ACommoner02Dead` (FormID `02982A`) — "Commoner"
- `AdventureDeadSpecial03` (FormID `02A6FF`) — "Order of the Dragonborne's Knight"
- `AdventureDeadSpecial04` (FormID `02A700`) — "Order of the Dragonborne's Knight"
- `AdventureDeadSpecial05` (FormID `02A701`) — "Order of the Dragonborne's Elite Knight"
- `AdventureDeadSpecial01` (FormID `03A252`) — "Gherst Baerne"
- `AdventurerImperialWarrior01Dead3` (FormID `03CFE8`) — "Adventurer"
- `AdventureDeadSpecialTorne` (FormID `05130C`) — "Orio Torne"

### AI Package (PACK) — +9 -0 ~0

**Added:**

- `OOOZZZCreatureFollowPlayer` (FormID `00DCDB`)
- `OOOGraveMinoTravelCasa` (FormID `01647B`)
- `OOOGraveMinoTravelRaid` (FormID `01647D`)
- `OOOGraveMinoTravelHalfWayRaid` (FormID `019BCD`)
- `OOOGraveMinoTravelHalfWayCasa` (FormID `019BCE`)
- `OOOZZZCreatureFollowPlayerSummon` (FormID `025164`)
- `OOOHorunnMinoTravelRaid` (FormID `0399D3`)
- `OOONonungaloMinoTravelHome` (FormID `03A262`)
- `OOONonungaloMinoTravelRaid` (FormID `03A263`)

### Spell (SPEL) — +3 -0 ~0

**Added:**

- `PwSprigganSummonKodiak` (FormID `017CBA`) — "Summon Kodiak"
- `PwSprigganSummonGW` (FormID `017CBE`) — "Summon Kodiak"
- `SprigganSummonKodiak` (FormID `01CFF4`) — "Jephre's Spirit"

## ESP changes — `Oscuro's_Oblivion_Overhaul137.esp`

_Initial inventory (no prior version to compare against)._

- **Activator (ACTI):** 1 records
- **Potion / Ingestible (ALCH):** 239 records
- **Ammunition (AMMO):** 60 records
- **Armor (ARMO):** 520 records
- **Book (BOOK):** 5 records
- **Birthsign (BSGN):** 13 records
- **Cell (CELL):** 954 records
- **Class (CLAS):** 5 records
- **Clothing (CLOT):** 250 records
- **Container (CONT):** 672 records
- **Creature (CREA):** 219 records
- **Combat Style (CSTY):** 61 records
- **Dialogue Topic (DIAL):** 25 records
- **Enchantment (ENCH):** 448 records
- **Faction (FACT):** 56 records
- **Game Setting (GMST):** 191 records
- **Ingredient (INGR):** 77 records
- **Key (KEYM):** 11 records
- **Light (LIGH):** 2 records
- **Loading Screen (LSCR):** 16 records
- **Leveled Creature List (LVLC):** 294 records
- **Leveled Item List (LVLI):** 547 records
- **Leveled Spell List (LVSP):** 2 records
- **Magic Effect (MGEF):** 94 records
- **Misc Item (MISC):** 190 records
- **NPC (NPC_):** 1357 records
- **AI Package (PACK):** 297 records
- **Quest (QUST):** 35 records
- **Region (REGN):** 1 records
- **Script (SCPT):** 99 records
- **Sigil Stone (SGST):** 15 records
- **Skill (SKIL):** 21 records
- **Soul Gem (SLGM):** 27 records
- **Spell (SPEL):** 284 records
- **Weapon (WEAP):** 872 records
- **Worldspace (WRLD):** 29 records

## ESP changes — `Oscuro's_Oblivion_Overhaul137ESM.esp`

_Initial inventory (no prior version to compare against)._

- **Activator (ACTI):** 21 records
- **Potion / Ingestible (ALCH):** 42 records
- **Ammunition (AMMO):** 91 records
- **Armor (ARMO):** 1234 records
- **Book (BOOK):** 199 records
- **Cell (CELL):** 54 records
- **Class (CLAS):** 19 records
- **Clothing (CLOT):** 252 records
- **Container (CONT):** 1110 records
- **Creature (CREA):** 848 records
- **Combat Style (CSTY):** 121 records
- **Dialogue Topic (DIAL):** 16 records
- **Door (DOOR):** 5 records
- **Effect Shader (EFSH):** 9 records
- **Enchantment (ENCH):** 225 records
- **Faction (FACT):** 61 records
- **Global Variable (GLOB):** 43 records
- **Grass (GRAS):** 1 records
- **Idle Animation (IDLE):** 15 records
- **Ingredient (INGR):** 45 records
- **Key (KEYM):** 78 records
- **Light (LIGH):** 30 records
- **Leveled Creature List (LVLC):** 837 records
- **Leveled Item List (LVLI):** 2715 records
- **Leveled Spell List (LVSP):** 9 records
- **Misc Item (MISC):** 184 records
- **NPC (NPC_):** 2491 records
- **AI Package (PACK):** 641 records
- **Quest (QUST):** 34 records
- **Race (RACE):** 1 records
- **Script (SCPT):** 714 records
- **Sigil Stone (SGST):** 9 records
- **Soul Gem (SLGM):** 3 records
- **Sound (SOUN):** 25 records
- **Spell (SPEL):** 685 records
- **Static Object (STAT):** 1 records
- **Weapon (WEAP):** 1245 records

## ESP changes — `OOO_GameSettings.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewChests03.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewChests2.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewCreatures03.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewNPCs03.esp`

_No record-level changes detected._

## ESP changes — `Oscuro's_Oblivion_Overhaul.esp`

_No record-level changes detected._

