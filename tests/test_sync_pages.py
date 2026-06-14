import importlib.util
from pathlib import Path

_MODULE_PATH = Path(__file__).resolve().parent.parent / "scripts" / "sync_pages.py"
_spec = importlib.util.spec_from_file_location("sync_pages", _MODULE_PATH)
sync_pages = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(sync_pages)


def test_module_imports():
    assert hasattr(sync_pages, "md_to_simple_html")


def test_fenced_code_block_becomes_pre_code():
    md = "```bash\ngit diff a..b\necho hi\n```"
    out = sync_pages.md_to_simple_html(md)
    assert "<pre><code>" in out
    assert "git diff a..b\necho hi" in out
    assert "</code></pre>" in out
    assert "<p>```bash</p>" not in out


def test_pipe_table_becomes_html_table():
    md = "| Name | Size |\n| --- | --- |\n| alpha91 | 215.9 MiB |"
    out = sync_pages.md_to_simple_html(md)
    assert "<table>" in out
    assert "<th>Name</th>" in out
    assert "<td>alpha91</td>" in out
    assert "<p>| Name | Size |</p>" not in out


def test_external_links_get_target_blank():
    md = "See [the repo](https://github.com/devakm/OblivionRemastered_OOO)."
    out = sync_pages.md_to_simple_html(md)
    assert 'target="_blank"' in out
    assert 'rel="noopener"' in out


def test_internal_links_stay_plain():
    md = "See [install](install.html)."
    out = sync_pages.md_to_simple_html(md)
    assert '<a href="install.html">install</a>' in out
    assert 'target="_blank"' not in out


def test_fence_with_nonword_language_tag():
    md = "```c++\nint x = 0;\n```\nnormal text"
    out = sync_pages.md_to_simple_html(md)
    assert "<pre><code>int x = 0;</code></pre>" in out
    assert "<p>normal text</p>" in out
    assert "```c++" not in out


def test_code_block_escapes_html():
    md = "```\n<b> & </b>\n```"
    out = sync_pages.md_to_simple_html(md)
    assert "&lt;b&gt; &amp; &lt;/b&gt;" in out


def test_nav_has_overview_and_new_items_in_order():
    shell = sync_pages.page_shell("T", "<p>body</p>", active_nav="Home")
    # New Items must be present and appear after Overview, before Changelog.
    assert ">New Items</a>" in shell
    i_over = shell.index(">Overview</a>")
    i_new = shell.index(">New Items</a>")
    i_chg = shell.index(">Changelog</a>")
    assert i_over < i_new < i_chg


def test_branding_mentions_ooorf():
    shell = sync_pages.page_shell("T", "<p>body</p>")
    assert "OOORF" in shell


def test_should_skip_true_when_marker_present(tmp_path):
    f = tmp_path / "overview.html"
    f.write_text("<!DOCTYPE html>\n<!-- DO-NOT-REGENERATE: x -->\n<html></html>", encoding="utf-8")
    assert sync_pages.should_skip(f) is True


def test_should_skip_false_when_marker_absent(tmp_path):
    f = tmp_path / "overview.html"
    f.write_text("<!DOCTYPE html>\n<html></html>", encoding="utf-8")
    assert sync_pages.should_skip(f) is False


def test_should_skip_false_when_file_missing(tmp_path):
    assert sync_pages.should_skip(tmp_path / "nope.html") is False
