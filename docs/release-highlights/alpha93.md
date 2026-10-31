### Fixed: same-model creatures showing the wrong creature

In OOO, many creatures share one 3D model (all imps and gargoyles use the imp
model). In the remaster, every creature in such a group showed whichever one the
game looked up last: its name, stats and loot. A gargoyle group could show up as
five Ancient Gargoyles, and an imp spawn as a gargoyle. The game placed the right
creatures; it only displayed the wrong one.

**RAX now gives each creature its own copy of the shared form**, so each one shows
its own name, stats and loot. In testing, 20–28% of these creatures showed the
wrong creature before the fix and 0 of 181 after it. The fix is on by default; to
turn it off, create
`OblivionRemastered\Binaries\Win64\ue4ss\Mods\RAX\formsplit.json` (next to RAX's
`enabled.txt`) containing `{ "enabled": false }`.

alpha93 still needs **"UE4SS new" (v3.0.1-1164)**, as alpha92 did.

### Ayleid weapons

The new Ayleid set gives the Ayleid weapons (daggers, swords, claymores, maces, axes,
war hammers and bows, 122 items) their own meshes and materials. In alpha92 they
borrowed the Elven weapons.

### Ancient Harbinger gear without Deluxe

Without the Deluxe Edition patch, the Ancient Harbinger armor and weapons now use
the Obsidian set instead of Glass armor and Iron weapons. With Deluxe they keep the
Deluxe Edition models, as before. The Harbinger greaves also use the greaves mesh
now; they showed the boots mesh before.

### Wilderness spawns rebalanced

- The six general wilderness lists (Highlands, Plains, Mountains, Hills, Forest
  Mountain and Snowy Mountains) now add creatures in steps at levels 14, 18 and 24.
- Shivering Isles water, shoreline and wilderness lists move their level steps up
  (19 to 20 or 22, 27 to 30), so the danger rises a little later.

### West Kvatch Sylvan Ranger Camp moved onto the terrain

OOO placed this camp on a flat terrain pad that the remaster's terrain does not
have, so its tents, bedrolls and clutter floated above the slope. The whole camp
(32 objects) now sits 225 units west, on the remaster's ground, with its tents and
bedrolls resting on the terrain. A large vanilla rock that sat under the camp is
moved out of it.

**Known gap for existing saves:** a save records the Tamriel worldspace the moment
the character first enters Tamriel, so any save that has left the starter dungeon
with an earlier OOORF alpha installed keeps the old camp positions, and parts of the
camp (barrels, bedrolls and other items) may still float. It does not matter
whether that save has visited the camp. Only these show all the corrections:

- a new game that has not yet left the starter dungeon, or
- a save that has never had an OOORF alpha installed. OOOR Slim makes no world
  changes, so saves that only ran Slim count as clean.

### Other changes

- **Item textures:** every item set's mips and inventory icons are regenerated from
  the edited art. This includes the alpha92.1 Draconis shield and Ancestral icon
  fixes, so alpha93 installs over alpha92 or alpha92.1.
