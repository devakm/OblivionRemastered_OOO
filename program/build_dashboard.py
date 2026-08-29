"""Generate program/dashboard.html -- the OOO program view.

Static, self-contained, opened via file://. Never runs a generator or a
build: it prints the command instead, so opening the page is side-effect free.

Run: py -3 program/build_dashboard.py
"""
import html as _html
from pathlib import Path

from .collect import views

HERE = Path(__file__).resolve().parent
CSS = """body{font:14px/1.5 system-ui,sans-serif;margin:24px;background:#faf9f7;color:#222}
.panel{border:1px solid #ddd;border-radius:8px;padding:14px 18px;margin:0 0 18px;background:#fff}
.panel-error{border-color:#c33;background:#fff5f5}
h1{font-size:20px}h2{font-size:15px;margin:0 0 10px}
table{border-collapse:collapse;width:100%}td,th{text-align:left;padding:4px 8px;border-bottom:1px solid #eee}
.FRESH{color:#176d2c;font-weight:600}.STALE{color:#b3261e;font-weight:600}
.UNKNOWN{color:#8a6d00;font-weight:600}
code{background:#f2f0ec;padding:1px 5px;border-radius:4px;font-size:12px}
.stamp{color:#777;font-size:12px}"""


def panel(title: str, env: dict, body_html: str) -> str:
    cls = "panel" if env.get("ok") else "panel panel-error"
    if not env.get("ok"):
        body_html = f'<p><b>collector failed:</b> {_html.escape(str(env.get("error")))}</p>'
    return (f'<section class="{cls}"><h2>{_html.escape(title)}</h2>{body_html}'
            f'<p class=stamp>{_html.escape(env.get("source",""))} · '
            f'{_html.escape(env.get("collected_at",""))}</p></section>')


def views_panel() -> str:
    env = views.collect()
    rows = []
    for v in env["data"] if env["ok"] else []:
        cmd = f'<code>{_html.escape(v["generator"])}</code>' if v["generator"] else "—"
        age = f'{v["age_days"]}d' if v["age_days"] is not None else "missing"
        rows.append(f'<tr><td>{_html.escape(v["name"])}</td>'
                    f'<td class="{v["state"]}">{v["state"]}</td><td>{age}</td><td>{cmd}</td></tr>')
    body = ('<table><tr><th>View</th><th>State</th><th>Age</th><th>Rebuild with</th></tr>'
            + "".join(rows) + '</table>')
    return panel("Views", env, body)


def render(panels: list[str]) -> str:
    return (f'<!doctype html><meta charset=utf-8><title>OOO Program</title>'
            f'<style>{CSS}</style><h1>Oscuro’s Oblivion Overhaul Remastered — Program</h1>'
            + "".join(panels))


def main(out: Path | None = None) -> Path:
    out = Path(out) if out else HERE / "dashboard.html"
    out.write_text(render([views_panel()]), encoding="utf-8")
    return out


if __name__ == "__main__":
    print(main().as_uri())
