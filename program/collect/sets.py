"""Which armor/weapon sets exist in ItemClone."""
from pathlib import Path

from . import envelope

SETS_DIR = Path(r"X:\dev\OblivionRemastered_ItemClone\sets")


def shipped_sets() -> list[str]:
    if not SETS_DIR.is_dir():
        return []
    return sorted(p.name for p in SETS_DIR.iterdir()
                  if p.is_dir() and not p.name.startswith("_"))


def collect() -> dict:
    return envelope(shipped_sets(), source="sets.collect")
