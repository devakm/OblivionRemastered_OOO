import importlib.util
from pathlib import Path

_MODULE_PATH = Path(__file__).resolve().parent.parent / "scripts" / "sync_pages.py"
_spec = importlib.util.spec_from_file_location("sync_pages", _MODULE_PATH)
sync_pages = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(sync_pages)


def test_module_imports():
    assert hasattr(sync_pages, "md_to_simple_html")
