"""
Bootstrap Wrye Bash for use as a TES4-parsing library.

Wrye Bash is designed as a desktop application, not a library. To use its
record-parsing machinery from a CLI script we have to:

  1. Add `<wrye-bash>/Mopy` to sys.path so `bash.*` imports resolve.
  2. Install null translations so `_()` calls succeed.
  3. Manually register game modules (skipping the Steam/GOG path detection,
     which would otherwise need network/registry access we don't care about).
  4. Set the active game and call `init()` to load record-class definitions
     and Oblivion-specific RecordHeader struct sizes.

Runtime dependencies that wrye-bash pulls in via its import chain
(unavoidable even though we don't use the GUI):

  - chardet
  - wxPython
  - lz4
  - pyyaml

Install with:  py -3 -m pip install chardet wxPython lz4 pyyaml

Usage:
    from _wrye_bootstrap import bootstrap_wrye_bash
    bootstrap_wrye_bash()
    from bash.mod_files import LoadFactory, ModFile  # now importable
"""

from __future__ import annotations

import gettext
import os
import pkgutil
import sys
from pathlib import Path

# Default location of the wrye-bash checkout. Override with WRYE_BASH_MOPY env var
# if the checkout lives elsewhere.
DEFAULT_WRYE_MOPY = Path(r"X:/dev/wrye-bash/Mopy")

# Game we activate. "Oblivion Remastered (Steam)" is the right module for OBR
# alphas — wrye-bash's dev branch ships explicit OBR support.
ACTIVE_GAME_DISPLAY_NAME = "Oblivion Remastered (Steam)"

_bootstrapped = False


def bootstrap_wrye_bash(wrye_mopy: Path | str | None = None,
                        game_dn: str = ACTIVE_GAME_DISPLAY_NAME) -> None:
    """Idempotent — safe to call multiple times. Subsequent calls return immediately."""
    global _bootstrapped
    if _bootstrapped:
        return

    mopy = Path(wrye_mopy or os.environ.get("WRYE_BASH_MOPY") or DEFAULT_WRYE_MOPY)
    if not (mopy / "bash" / "__init__.py").is_file():
        raise SystemExit(
            f"Wrye Bash checkout not found at {mopy}. Set WRYE_BASH_MOPY or "
            f"adjust DEFAULT_WRYE_MOPY in {__file__}."
        )

    sys.path.insert(0, str(mopy))
    gettext.NullTranslations().install()

    # Step 3: register game modules without Steam/GOG path detection
    # (mirrors bush._supportedGames sans the get_*_game_paths calls).
    from bash import bush  # noqa
    from bash import game as game_init  # noqa

    for _importer, modname, ispkg in pkgutil.iter_modules(game_init.__path__):
        if not ispkg:
            continue
        try:
            module = __import__("bash.game", globals(), locals(), [modname], 0)
            module_container = getattr(module, modname)
            gtype = getattr(module_container, "GAME_TYPE", None)
            if gtype is None:
                continue
            game_types = (gtype if isinstance(gtype, dict)
                          else {gtype.unique_display_name: gtype})
            bush._allGames.update(game_types)
        except (ImportError, AttributeError):
            # Some game modules (e.g. those needing platform-specific deps we
            # don't have) may fail to import. That's fine — we only need the
            # one we'll activate below.
            continue

    if game_dn not in bush._allGames:
        available = sorted(n for n in bush._allGames if "Oblivion" in n)
        raise SystemExit(
            f"Game {game_dn!r} not found in registered modules.\n"
            f"Available Oblivion variants: {available}"
        )

    # Step 4: activate game
    bush.game = bush._allGames[game_dn]("")
    bush.game.init()
    _bootstrapped = True
