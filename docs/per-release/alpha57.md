# alpha57 — release notes

_Compared against `alpha54`._

## File-level changes

- Added: 1
- Removed: 1
- Changed: 9

### Added

- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_SGST.json`

### Removed

- `OblivionRemastered/Content/Dev/ObvData/Data/OOO_ThePunishedRestored.esp`

### Changed

- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_ARMO.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_BOOK.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_CELL.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_CREA.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_ENCH.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_SCPT.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_SPELL.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/Oscuro's_Oblivion_Overhaul.esp`
- `OblivionRemastered/Content/Dev/ObvData/Data/SyncMap/Oscuro's_Oblivion_Overhaul.ini`

## ESP changes — `Oscuro's_Oblivion_Overhaul.esp`

### Armor (ARMO) — +12 -0 ~0

**Added:**

- `IronBootsDurable` (FormID `00DE28`) — "LOC_FN_IronBootsDurable"
- `IronCuirassDurable` (FormID `00DE29`) — "LOC_FN_IronCuirassDurable"
- `IronGauntletsDurable` (FormID `00DE2A`) — "LOC_FN_IronGauntletsDurable"
- `IronGreavesDurable` (FormID `00DE2B`) — "LOC_FN_IronGreavesDurable"
- `IronHelmetDurable` (FormID `00DE2C`) — "LOC_FN_IronHelmetDurable"
- `IronShieldDurable` (FormID `00DE2D`) — "LOC_FN_IronShieldDurable"
- `SteelBootsDurable` (FormID `00DE2E`) — "LOC_FN_SteelBootsDurable"
- `SteelCuirassDurable` (FormID `00DE2F`) — "LOC_FN_SteelCuirassDurable"
- `SteelGauntletsDurable` (FormID `00DE30`) — "LOC_FN_SteelGauntletsDurable"
- `SteelGreavesDurable` (FormID `00DE31`) — "LOC_FN_SteelGreavesDurable"
- `SteelHelmetDurable` (FormID `00DE32`) — "LOC_FN_SteelHelmetDurable"
- `SteelShieldDurable` (FormID `00DE33`) — "LOC_FN_SteelShieldDurable"

### Book (BOOK) — +0 -0 ~1

**Changed:**

- `ZAyleidBook1` (FormID `003916`) — "LOC_FN_ZAyleidBook1" — `modl`: `'clutter\\Books\\Gristle\\mintingatmiscarcand.nif'` → `'Clutter\\Books\\Folio01.NIF'`

### Cell (CELL) — +1 -1 ~10

**Added:**

- `Telepe` (FormID `016637`) — "LOC_FN_Telepe"

**Removed:**

- `Kemen` (FormID `016626`) — "LOC_FN_Kemen"

**Changed:**

- `Nornal` (FormID `01664D`) — "LOC_FN_Nornal" — `full`: `'Nornal'` → `'LOC_FN_Nornal'`
- `ICElvenGardensDovynArensHouse` (FormID `02C1BD`) — "LOC_FN_ICElvenGardensDovynArensHouse" — `full`: `"Dovyn Aren's House"` → `'LOC_FN_ICElvenGardensDovynArensHouse'`
- `Arpenia` (FormID `02C56F`) — "LOC_FN_Arpenia" — `full`: `'Arpenia'` → `'LOC_FN_Arpenia'`
- `Crowhaven02` (FormID `02C6F5`) — "LOC_FN_Crowhaven02" — `full`: `'Crowhaven Burial Halls'` → `'LOC_FN_Crowhaven02'`
- `ICTalosPlazaTheFoamingFlaskBasement` (FormID `03CEE6`) — "LOC_FN_ICTalosPlazaTheFoamingFlaskBasement" — `full`: `'The Foaming Flask Basement'` → `'LOC_FN_ICTalosPlazaTheFoamingFlaskBasement'`
- `ICElvenGardensTheKingandQueenTavernRooms` (FormID `047C97`) — "LOC_FN_ICElvenGardensTheKingandQueenTavernRooms" — `full`: `'The King and Queen Tavern Rooms'` → `'LOC_FN_ICElvenGardensTheKingandQueenTavernRooms'`
- `ICElvenGardensCyroninSintavsHouseBasement` (FormID `047CA8`) — "LOC_FN_ICElvenGardensCyroninSintavsHouseBasement" — `full`: `"Cyronin Sintav's Basement"` → `'LOC_FN_ICElvenGardensCyroninSintavsHouseBasement'`
- `OblivionRD004CitadelRightLord` (FormID `04D5FD`) — "LOC_FN_OblivionRD004CitadelRightLord" — `full`: `'The Anguish Shrine'` → `'LOC_FN_OblivionRD004CitadelRightLord'`
- `ICTempleDistrictTheAllSaintsInnUpstairs` (FormID `04EDA8`) — "LOC_FN_ICTempleDistrictTheAllSaintsInnUpstairs" — `full`: `"Willet's Private Quarters"` → `'LOC_FN_ICTempleDistrictTheAllSaintsInnUpstairs'`
- `KingscrestCavern04` (FormID `08371A`) — "LOC_FN_KingscrestCavern04" — `full`: `'Kingscrest Withered Forest'` → `'LOC_FN_KingscrestCavern04'`

### Creature (CREA) — +5 -0 ~0

**Added:**

- `CreatureOOOGargoyleAncient` (FormID `00DE15`) — "LOC_FN_CreatureOOOGargoyleAncient"
- `CreatureOOOGargoyleAncient02` (FormID `00DE16`) — "LOC_FN_CreatureOOOGargoyleAncient02"
- `CreatureOOOGargoyleAncient03` (FormID `00DE17`) — "LOC_FN_CreatureOOOGargoyleAncient03"
- `CreatureOOOGargoyleAncient04` (FormID `00DE18`) — "LOC_FN_CreatureOOOGargoyleAncient04"
- `CreatureOOOGargoyleAncient05` (FormID `00DE19`) — "LOC_FN_CreatureOOOGargoyleAncient05"

### Enchantment (ENCH) — +6 -0 ~0

**Added:**

- `MS13EnWeapThornblade01` (FormID `06B65B`)
- `MS13EnWeapThornblade02` (FormID `06B65C`)
- `MS13EnWeapThornblade03` (FormID `06B65D`)
- `MS13EnWeapThornblade04` (FormID `06B65E`)
- `MS13EnWeapThornblade05` (FormID `06B65F`)
- `MS13EnWeapThornblade06` (FormID `06B660`)

### Leveled Creature List (LVLC) — +2 -0 ~10

**Added:**

- `LL0Gargoyle100Ancient` (FormID `00DE1C`)
- `LL0Gargoyle100PackAncient` (FormID `00DE1D`)

**Changed:**

- `LL2VampireLair100` (FormID `0340E3`) — + entry: level 1 × 2 → `0340E4`; + entry: level 1 × 3 → `0340E4`
- `LL1WildernessHighlands` (FormID `0343DB`) — + entry: level 12 × 1 → `0417EE`; + entry: level 18 × 1 → `00DE1C`
- `LL1WildernessPlains` (FormID `0343DC`) — + entry: level 12 × 1 → `0417EE`; + entry: level 13 × 1 → `02F502`; + entry: level 18 × 1 → `00DE1C`
- `LL1WildernessMountains` (FormID `0343DF`) — + entry: level 12 × 1 → `0417EE`; + entry: level 13 × 1 → `02F502`; + entry: level 18 × 1 → `00DE1C`
- `LL1WildernessHills` (FormID `0343E0`) — + entry: level 13 × 1 → `02F502`; + entry: level 18 × 1 → `00DE1C`
- `LL1WildernessForestMountain` (FormID `0343E2`) — + entry: level 13 × 1 → `02F502`; + entry: level 18 × 1 → `00DE1C`
- `LL1WildernessMountainsSnow` (FormID `064F66`) — + entry: level 13 × 1 → `02F502`; + entry: level 18 × 1 → `00DE1C`
- `LL0Imp100SpecialPackMystical` (FormID `008A63`) — + entry: level 15 × 1 → `0084F8`; + entry: level 15 × 1 → `0084F9`; + entry: level 15 × 1 → `00DE1D`; + entry: level 15 × 1 → `0263D0`; + entry: level 15 × 1 → `0263D1`; + entry: level 15 × 1 → `027881`; + entry: level 15 × 1 → `02F501`; + entry: level 15 × 1 → `0417ED`
- `LL1VampireZBoss100` (FormID `017E40`) — + entry: level 28 × 1 → `000D0D`; + entry: level 28 × 1 → `000D0E`; + entry: level 28 × 1 → `000D0F`; + entry: level 28 × 1 → `000D10`; + entry: level 28 × 1 → `000D11`; + entry: level 28 × 1 → `000D12`; - entry: level 30 × 1 → `000D0D`; - entry: level 30 × 1 → `000D0E`; - entry: level 30 × 1 → `000D0F`; - entry: level 30 × 1 → `000D10`; - entry: level 30 × 1 → `000D11`; - entry: level 30 × 1 → `000D12`
- `LL0Imp100Special` (FormID `02F502`) — + entry: level 15 × 1 → `0A9F5B`; + entry: level 15 × 1 → `008A62`; + entry: level 15 × 1 → `008A63`; + entry: level 15 × 1 → `00DE1D`; + entry: level 15 × 1 → `0417ED`

### Leveled Item List (LVLI) — +3 -1 ~76

**Added:**

- `bgLL1GargoyleDeathListAncient` (FormID `00DE14`)
- `bgLL0GargoyleAncientSurpriseShardsMulti` (FormID `00DE1B`)
- `bgLL0GargoyleAncientSurpriseStones` (FormID `00DE27`)

**Removed:**

- `LL1LootGold100` (FormID `014931`)

**Changed:**

- `LL1LootWeapon0Magic75` (FormID `03E501`) — + entry: level 15 × 1 → `03C7F5`; + entry: level 25 × 1 → `03C7F1`; + entry: level 25 × 1 → `03C7F3`; + entry: level 25 × 1 → `03C7F5`; + entry: level 28 × 1 → `03C7F3`; + entry: level 30 × 1 → `03C7F1`
- `LL1LootWeapon0Magic25` (FormID `03E503`) — + entry: level 15 × 1 → `03C7F5`; + entry: level 25 × 1 → `03C7F1`; + entry: level 25 × 1 → `03C7F3`; + entry: level 25 × 1 → `03C7F5`; + entry: level 30 × 1 → `03C7F1`; - entry: level 18 × 1 → `03C7F5`; - entry: level 23 × 1 → `03C7F1`; - entry: level 26 × 1 → `03C7F5`; - entry: level 31 × 1 → `03C7F1`
- `LL0NPCArmorHeavyCuirass100iron` (FormID `001F14`) — + entry: level 1 × 1 → `00DE29`
- `LL0NPCArmorHeavyCuirass100steel` (FormID `001F15`) — + entry: level 1 × 1 → `00DE2F`
- `LL0NPCArmorHeavyShield100at35` (FormID `003270`) — + entry: level 1 × 1 → `023923`; + entry: level 1 × 1 → `0352C1`; + entry: level 1 × 1 → `03634A`; + entry: level 1 × 1 → `036350`; + entry: level 1 × 1 → `036356`; + entry: level 1 × 1 → `03635C`; + entry: level 1 × 1 → `001213`; + entry: level 1 × 1 → `001C53`; + entry: level 1 × 1 → `002AF1`; + entry: level 1 × 1 → `00CFD3`; + entry: level 1 × 1 → `00DE2D`; + entry: level 1 × 1 → `00DE33`; + entry: level 1 × 1 → `021BC6`; - entry: level 35 × 1 → `023923`; - entry: level 35 × 1 → `0352C1`; - entry: level 35 × 1 → `03634A`; - entry: level 35 × 1 → `036350`; - entry: level 35 × 1 → `036356`; - entry: level 35 × 1 → `03635C`
- `LL0NPCArmorHeavyShield100at29` (FormID `003271`) — + entry: level 1 × 1 → `001213`; + entry: level 1 × 1 → `001C53`; + entry: level 1 × 1 → `002AF1`; + entry: level 1 × 1 → `00CFD3`; + entry: level 1 × 1 → `00DE2D`; + entry: level 1 × 1 → `00DE33`; + entry: level 1 × 1 → `021BC6`
- `LL0NPCArmorHeavyShield100at24` (FormID `003272`) — + entry: level 1 × 1 → `001213`; + entry: level 1 × 1 → `001C53`; + entry: level 1 × 1 → `002AF1`; + entry: level 1 × 1 → `00CFD3`; + entry: level 1 × 1 → `00DE2D`; + entry: level 1 × 1 → `00DE33`; + entry: level 1 × 1 → `021BC6`
- `LL0NPCArmorHeavyShield100at22` (FormID `003273`) — + entry: level 1 × 1 → `001213`; + entry: level 1 × 1 → `001C53`; + entry: level 1 × 1 → `002AF1`; + entry: level 1 × 1 → `00DE2D`; + entry: level 1 × 1 → `00DE33`; + entry: level 1 × 1 → `021BC6`
- `LL0NPCArmorHeavyShield100at18` (FormID `003274`) — + entry: level 1 × 1 → `001213`; + entry: level 1 × 1 → `001C53`; + entry: level 1 × 1 → `002AF1`; + entry: level 1 × 1 → `00DE2D`; + entry: level 1 × 1 → `00DE33`; + entry: level 1 × 1 → `021BC6`
- `LL0NPCArmorHeavyShield100at16` (FormID `003275`) — + entry: level 1 × 1 → `001C53`; + entry: level 1 × 1 → `00DE2D`; + entry: level 1 × 1 → `00DE33`; + entry: level 1 × 1 → `021BC6`
- `LL0NPCArmorHeavyShield100at12` (FormID `003276`) — + entry: level 1 × 1 → `001213`; + entry: level 1 × 1 → `001C53`; + entry: level 1 × 1 → `00DE2D`; + entry: level 1 × 1 → `00DE33`; + entry: level 1 × 1 → `021BC6`
- `LL0NPCArmorHeavyShield100at10` (FormID `003277`) — + entry: level 1 × 1 → `001C53`; + entry: level 1 × 1 → `00DE2D`; + entry: level 1 × 1 → `00DE33`; + entry: level 1 × 1 → `021BC6`
- `LL0NPCArmorHeavyHelmet100at35` (FormID `00327A`) — + entry: level 1 × 1 → `001C54`; + entry: level 1 × 1 → `00DE2C`; + entry: level 1 × 1 → `00DE32`
- `LL0NPCArmorHeavyHelmet100at29` (FormID `00327B`) — + entry: level 1 × 1 → `001C54`; + entry: level 1 × 1 → `00DE2C`; + entry: level 1 × 1 → `00DE32`
- `LL0NPCArmorHeavyHelmet100at24` (FormID `00327C`) — + entry: level 1 × 1 → `001C54`; + entry: level 1 × 1 → `00DE2C`; + entry: level 1 × 1 → `00DE32`
- `LL0NPCArmorHeavyHelmet100at18` (FormID `00327D`) — + entry: level 1 × 1 → `001C54`; + entry: level 1 × 1 → `00DE2C`; + entry: level 1 × 1 → `00DE32`
- `LL0NPCArmorHeavyHelmet100at16` (FormID `00327E`) — + entry: level 1 × 1 → `001C54`; + entry: level 1 × 1 → `00DE2C`; + entry: level 1 × 1 → `00DE32`
- `LL0NPCArmorHeavyHelmet100at12` (FormID `00327F`) — + entry: level 1 × 1 → `001C54`; + entry: level 1 × 1 → `00DE2C`; + entry: level 1 × 1 → `00DE32`
- `LL0NPCArmorHeavyHelmet100at10` (FormID `003280`) — + entry: level 1 × 1 → `001C54`; + entry: level 1 × 1 → `00DE2C`; + entry: level 1 × 1 → `00DE32`
- `LL0NPCArmorHeavyGreaves100at35` (FormID `003282`) — + entry: level 1 × 1 → `001C52`; + entry: level 1 × 1 → `00DE2B`; + entry: level 1 × 1 → `00DE31`

_…56 more changed omitted (see JSON for full list)_

### Script (SCPT) — +0 -0 ~1

**Changed:**

- `StoneEffectScriptGargoyle` (FormID `015557`) — `edid`: `'GhostEffectScriptSpriggan'` → `'StoneEffectScriptGargoyle'`

### Sigil Stone (SGST) — +9 -0 ~9

**Added:**

- `bgSDStoneFireAncientOOO` (FormID `00DE1E`) — "LOC_FN_bgSDStoneFireAncientOOO"
- `bgSDStoneFrostAncientOOO` (FormID `00DE1F`) — "LOC_FN_bgSDStoneFrostAncientOOO"
- `bgSDStoneMagickaAncientOOO` (FormID `00DE20`) — "LOC_FN_bgSDStoneMagickaAncientOOO"
- `bgSDStoneRainbowAncientOOO` (FormID `00DE21`) — "LOC_FN_bgSDStoneRainbowAncientOOO"
- `bgSDStoneResfireAncientOOO` (FormID `00DE22`) — "LOC_FN_bgSDStoneResfireAncientOOO"
- `bgSDStoneResfrostAncientOOO` (FormID `00DE23`) — "LOC_FN_bgSDStoneResfrostAncientOOO"
- `bgSDStoneResistAncientOOO` (FormID `00DE24`) — "LOC_FN_bgSDStoneResistAncientOOO"
- `bgSDStoneResshockAncientOOO` (FormID `00DE25`) — "LOC_FN_bgSDStoneResshockAncientOOO"
- `bgSDStoneShockAncientOOO` (FormID `00DE26`) — "LOC_FN_bgSDStoneShockAncientOOO"

**Changed:**

- `bgSDStoneFireOOO` (FormID `000800`) — "LOC_FN_bgSDStoneFireOOO" — `full`: `'Fire Stone'` → `'LOC_FN_bgSDStoneFireOOO'`
- `bgSDStoneFrostOOO` (FormID `000801`) — "LOC_FN_bgSDStoneFrostOOO" — `full`: `'Frost Stone'` → `'LOC_FN_bgSDStoneFrostOOO'`
- `bgSDStoneShockOOO` (FormID `000802`) — "LOC_FN_bgSDStoneShockOOO" — `full`: `'Shock Stone'` → `'LOC_FN_bgSDStoneShockOOO'`
- `bgSDStoneMagickaOOO` (FormID `000803`) — "LOC_FN_bgSDStoneMagickaOOO" — `full`: `'Arcane Stone'` → `'LOC_FN_bgSDStoneMagickaOOO'`
- `bgSDStoneResistOOO` (FormID `000804`) — "LOC_FN_bgSDStoneResistOOO" — `full`: `'Negation Stone'` → `'LOC_FN_bgSDStoneResistOOO'`
- `bgSDStoneResfireOOO` (FormID `000805`) — "LOC_FN_bgSDStoneResfireOOO" — `full`: `'Flameguard Stone'` → `'LOC_FN_bgSDStoneResfireOOO'`
- `bgSDStoneResfrostOOO` (FormID `000806`) — "LOC_FN_bgSDStoneResfrostOOO" — `full`: `'Frostguard Stone'` → `'LOC_FN_bgSDStoneResfrostOOO'`
- `bgSDStoneResshockOOO` (FormID `000807`) — "LOC_FN_bgSDStoneResshockOOO" — `full`: `'Shockguard Stone'` → `'LOC_FN_bgSDStoneResshockOOO'`
- `bgSDStoneRainbowOOO` (FormID `000808`) — "LOC_FN_bgSDStoneRainbowOOO" — `full`: `'Elemental Stone'` → `'LOC_FN_bgSDStoneRainbowOOO'`

### Spell (SPEL) — +1 -0 ~1

**Added:**

- `AbGargoyleAncient` (FormID `00DE1A`) — "LOC_FN_AbGargoyleAncient"

**Changed:**

- `AbStoneGargoyle` (FormID `015558`) — "LOC_FN_AbStoneGargoyle" — `edid`: `'AbGhostSpriggan'` → `'AbStoneGargoyle'`; `full`: `'LOC_FN_AbGhostSpriggan'` → `'LOC_FN_AbStoneGargoyle'`

### Weapon (WEAP) — +0 -0 ~10

**Changed:**

- `WeapLightOfDawnNoFlame` (FormID `004E56`) — "LOC_FN_WeapLightOfDawnNoFlame" — `modl`: `'Weapons\\Akaviri weapon\\Claymore.NIF'` → `'Weapons\\Silver\\RugDumphsSword.NIF'`
- `WeapLightOfDawnNoFlameA` (FormID `004E57`) — "LOC_FN_WeapLightOfDawnNoFlameA" — `modl`: `'Weapons\\Akaviri weapon\\Claymore.NIF'` → `'Weapons\\Silver\\RugDumphsSword.NIF'`
- `WeapLightOfDawnNoFlameB` (FormID `004E58`) — "LOC_FN_WeapLightOfDawnNoFlameB" — `modl`: `'Weapons\\Akaviri weapon\\Claymore.NIF'` → `'Weapons\\Silver\\RugDumphsSword.NIF'`
- `WeapLightOfDawnNoFlameC` (FormID `004E59`) — "LOC_FN_WeapLightOfDawnNoFlameC" — `modl`: `'Weapons\\Akaviri weapon\\Claymore.NIF'` → `'Weapons\\Silver\\RugDumphsSword.NIF'`
- `WeapLightOfDawnFlameA` (FormID `006C93`) — "LOC_FN_WeapLightOfDawnFlameA" — `modl`: `'Weapons\\Akaviri weapon\\Claymore.NIF'` → `'Weapons\\Silver\\RugDumphsSword.NIF'`
- `WeapLightOfDawnFlameB` (FormID `006C94`) — "LOC_FN_WeapLightOfDawnFlameB" — `modl`: `'Weapons\\Akaviri weapon\\Claymore.NIF'` → `'Weapons\\Silver\\RugDumphsSword.NIF'`
- `WeapLightOfDawnFlameC` (FormID `006C95`) — "LOC_FN_WeapLightOfDawnFlameC" — `modl`: `'Weapons\\Akaviri weapon\\Claymore.NIF'` → `'Weapons\\Silver\\RugDumphsSword.NIF'`
- `WeapHeavenFuryLongsword01` (FormID `007AE7`) — "LOC_FN_WeapHeavenFuryLongsword01" — `modl`: `'Weapons\\Silver\\LongSword.NIF'` → `'Weapons\\Silver\\ms13thornblade.NIF'`
- `WeapLightOfDawnFlame` (FormID `013400`) — "LOC_FN_WeapLightOfDawnFlame" — `modl`: `'Weapons\\Akaviri weapon\\Claymore.NIF'` → `'Weapons\\Silver\\RugDumphsSword.NIF'`
- `WeapIronZDagger` (FormID `01F944`) — "LOC_FN_WeapIronZDagger" — `modl`: `'Weapons\\Iron\\Dagger.NIF'` → `'Weapons\\Silver\\RugDumphsSword.NIF'`

