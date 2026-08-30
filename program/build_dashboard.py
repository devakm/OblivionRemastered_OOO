"""Generate program/dashboard.html -- the OOO program view.

Static, self-contained, opened via file://. Never runs a generator or a
build: it prints the command instead, so opening the page is side-effect free.

Run: py -3 program/build_dashboard.py
"""
import html as _html
from pathlib import Path

from .collect import maps, milestones, releases, repos, runs, sessions, views

HERE = Path(__file__).resolve().parent
CSS = """body{font:14px/1.5 system-ui,sans-serif;margin:24px;background:#faf9f7;color:#222}
.panel{border:1px solid #ddd;border-radius:8px;padding:14px 18px;margin:0 0 18px;background:#fff}
.panel-error{border-color:#c33;background:#fff5f5}
h1{font-size:20px}h2{font-size:15px;margin:0 0 10px}
table{border-collapse:collapse;width:100%}td,th{text-align:left;padding:4px 8px;border-bottom:1px solid #eee}
.FRESH{color:#176d2c;font-weight:600}.STALE{color:#b3261e;font-weight:600}
.UNKNOWN{color:#8a6d00;font-weight:600}
.orphaned{color:#b3261e;font-weight:600}.running{color:#176d2c;font-weight:600}
.done{color:#777}
.MET{color:#176d2c;font-weight:600}.CONTRADICTED{color:#b3261e;font-weight:600}
.UNVERIFIED{color:#8a6d00;font-weight:600}.PENDING{color:#555;font-weight:600}
.pipeline{margin:0 0 12px}.ms{display:inline-block;padding:3px 10px;border:1px solid #ccc;
border-radius:14px;margin-right:6px;font-size:12px}.ms.in_progress{border-color:#8a6d00;
background:#fff8e1;font-weight:600}.ms.done{border-color:#176d2c;background:#eef7ef;color:#176d2c}
.next{background:#fff8e1;border:1px solid #e8d9a0;border-radius:6px;padding:8px 12px;margin:12px 0 0}
code{background:#f2f0ec;padding:1px 5px;border-radius:4px;font-size:12px}
.stamp{color:#777;font-size:12px}
.cols{display:flex;gap:26px;flex-wrap:wrap}.cols>div{flex:1 1 320px;min-width:0}
h3{font-size:13px;color:#555;margin:0 0 6px}a{color:#1a4d8f}
.vers{font-size:16px;margin:0 0 18px;padding:10px 14px;background:#fff;
border:1px solid #ddd;border-radius:8px}.vers b{font-size:17px}.verr{color:#b3261e}
.bar{height:8px;background:#eee;border-radius:5px;overflow:hidden;margin:6px 0 14px}
.bar i{display:block;height:100%;background:#176d2c}"""


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
        cmd = (f'<code>{_html.escape(v["generator"])}</code>' if v["generator"]
               else '<span class=stamp>hand-maintained — no generator</span>')
        age = f'{v["age_days"]}d' if v["age_days"] is not None else "missing"
        # A bare UNKNOWN reads as "we did not look". Say which it is.
        why = {"UNKNOWN": " <span class=stamp>(no declared inputs — cannot "
                          "prove freshness, so never green)</span>",
               "STALE": " <span class=stamp>(older than its inputs)</span>"}.get(v["state"], "")
        rows.append(f'<tr><td>{_html.escape(v["name"])}</td>'
                    f'<td class="{v["state"]}">{v["state"]}</td><td>{age}</td>'
                    f'<td>{cmd}{why}</td></tr>')
    body = ('<table><tr><th>View</th><th>State</th><th>Age</th>'
            '<th>Rebuild with</th></tr>' + "".join(rows) + '</table>')
    return panel("Views", env, body)


def milestones_panel(env: dict) -> str:
    """Where we are and what is next. Next steps are derived from the gap,
    never typed twice -- a hand-kept list is what drifts."""
    data = env["data"] if env["ok"] else {}
    pipe = "".join(
        f'<span class="ms {_html.escape(m["status"])}">{_html.escape(m["name"])}</span>'
        for m in data.get("milestones", []))
    rows = []
    for m in data.get("milestones", []):
        for c in m["criteria"]:
            rows.append(f'<tr><td>{_html.escape(m["name"])}</td>'
                        f'<td>{_html.escape(c.get("claim", ""))}</td>'
                        f'<td class="{c["state"]}">{c["state"]}</td></tr>')
    nxt = data.get("next", {})
    unmet = "".join(f'<li>{_html.escape(c.get("claim", ""))} '
                    f'<span class="{c["state"]}">({c["state"]})</span></li>'
                    for c in nxt.get("unmet", []))
    body = (f'<p><b>{_html.escape(data.get("goal", ""))}</b><br>'
            f'<span class=stamp>focus: {_html.escape(data.get("current_focus", ""))}</span></p>'
            f'<div class=pipeline>{pipe}</div>'
            '<table><tr><th>Milestone</th><th>Claim</th><th>State</th></tr>'
            + "".join(rows) + '</table>'
            + (f'<div class=next><b>Next steps toward '
               f'{_html.escape(str(nxt.get("name", "")))}:</b><ul>{unmet}</ul></div>'
               if unmet else
               f'<div class=next>Every criterion for '
               f'{_html.escape(str(nxt.get("name", "")))} is MET.</div>'))
    return panel("Program", env, body)


def maps_panel() -> str:
    """Human-gated zone validation: progress, what remains, and work in flight.

    No generator and no staleness verdict -- a row flips only when a person
    validates the zone in-game, so the tracker lags live work by design. The
    recent-activity list is what stops that lag reading as no progress.
    """
    env = maps.collect()
    data = env["data"] if env["ok"] else {}
    total, ok_n = data.get("total", 0), data.get("confirmed_count", 0)
    pct = round(100 * ok_n / total) if total else 0
    head = (f'<p>Zone validation <b>{ok_n}/{total}</b> confirmed in-game '
            f'({pct}%). <span class=stamp>Every row is validated by hand; '
            f'there is no generator and no freshness check.</span></p>'
            f'<div class=bar><i style="width:{pct}%"></i></div>')
    rows = "".join(
        f'<tr><td>{_html.escape(z["cell"])}</td><td>{_html.escape(z["donor"])}</td>'
        f'<td class=PENDING>awaiting in-game</td></tr>'
        for z in data.get("pending", []))
    if rows:
        caves = ", ".join(data.get("caves", []))
        body = (head + f'<h3>Outstanding — {_html.escape(caves)}</h3>'
                '<table><tr><th>Zone</th><th>Donor</th><th>State</th></tr>'
                + rows + '</table>')
        recent = data.get("recent") or []
        if recent:
            body += ('<h3>Recent work on these zones</h3><ul>'
                     + "".join(f'<li><code>{_html.escape(r)}</code></li>'
                               for r in recent) + '</ul>')
        else:
            body += ('<p class=stamp>No commits naming these zones since '
                     '2026-08-01.</p>')
    elif data.get("tracker_exists"):
        body = head + '<p class=MET>No zone is awaiting in-game validation.</p>'
    else:
        body = f'<p class=stamp>tracker not found: {_html.escape(str(data.get("tracker","")))}</p>'
    return panel("Map zone validation (MapClone phase 9)", env, body)


def runs_panel() -> str:
    """Orphans first -- an orphan's purpose text is the whole reason the ledger exists."""
    env = runs.collect()
    order = {"orphaned": 0, "running": 1, "done": 2}
    rows = []
    for r in sorted(env["data"] if env["ok"] else [],
                    key=lambda r: (order.get(r.get("status"), 3),
                                   r.get("started") or "")):
        rows.append(
            f'<tr><td>{_html.escape(str(r.get("repo","")))}</td>'
            f'<td>{_html.escape(str(r.get("kind","")))}</td>'
            f'<td class="{_html.escape(str(r.get("status","")))}">'
            f'{_html.escape(str(r.get("status","")))}</td>'
            f'<td>{_html.escape(str(r.get("started") or ""))}</td>'
            f'<td>{_html.escape(str(r.get("purpose") or ""))}</td></tr>')
    body = ('<table><tr><th>Repo</th><th>Kind</th><th>Status</th><th>Started</th>'
            '<th>Purpose</th></tr>' + "".join(rows) + '</table>'
            if rows else '<p class=stamp>no recorded runs</p>')
    return panel("In flight", env, body)


def repos_panel(annotations: dict | None = None) -> str:
    env = repos.collect(annotations)
    rows = []
    for r in env["data"] if env["ok"] else []:
        warn = [] if r["has_remote"] else ["<b>no remote</b>"]
        if r["dirty"]:
            warn.append(f'{r["dirty"]} uncommitted')
        rows.append(f'<tr><td colspan=5><b>{_html.escape(r["repo"])}</b> '
                    f'<span class=stamp>on {_html.escape(r["head"])} '
                    f'{" · ".join(warn)}</span></td></tr>')
        for b in r["branches"]:
            rows.append(
                f'<tr><td>{_html.escape(b["name"])}</td><td>{b["bucket"]}</td>'
                f'<td>+{b["ahead"]} / -{b["behind"]}</td><td>{_html.escape(b["last"])}</td>'
                f'<td>{_html.escape(b["intent"])}</td></tr>')
    body = ('<table><tr><th>Branch</th><th>Bucket</th><th>Ahead/Behind</th>'
            '<th>Last</th><th>Intent</th></tr>' + "".join(rows) + '</table>')
    return panel("Branches", env, body)


def sessions_panel(limit: int = 10) -> str:
    env = sessions.collect(limit)
    data = env["data"] if env["ok"] else {"sessions": [], "handoffs": []}
    srows = "".join(
        f'<tr><td>{_html.escape(s["started"])}</td><td><code>{_html.escape(s["id"])}</code></td>'
        f'<td>{_html.escape(s["label"])}</td></tr>' for s in data["sessions"])
    hrows = "".join(
        f'<tr><td>{_html.escape(h["date"])}</td><td>{_html.escape(h["set_name"])}</td>'
        f'<td><a href="{Path(h["path"]).as_uri()}">{_html.escape(Path(h["path"]).name)}</a></td>'
        f'</tr>' for h in data["handoffs"])
    body = ('<div class=cols>'
            '<div><h3>Recent sessions</h3><table>'
            '<tr><th>Started</th><th>Id</th><th>Label</th></tr>' + srows + '</table></div>'
            '<div><h3>Recent handoffs</h3><table>'
            '<tr><th>Date</th><th>Set</th><th>Document</th></tr>' + hrows + '</table></div>'
            '</div>')
    return panel("Sessions and handoffs", env, body)


def version_header() -> str:
    """Lead with what shipped and what is next -- both derived, never declared."""
    env = releases.collect()
    if not env["ok"]:
        return ('<p class=vers><span class=verr>release state unavailable: '
                f'{_html.escape(str(env["error"]))}</span></p>')
    d = env["data"]
    return (f'<p class=vers>Current release <b>{_html.escape(d["latest"]["tag"])}</b>'
            f' &nbsp;→&nbsp; in progress <b>{_html.escape(d["next"])}</b>'
            f' <span class=stamp>({d["released_count"]} alpha tags; '
            f'{_html.escape(d["latest"]["tag"])} corroborated by manifest + archive)</span></p>')


def render(panels: list[str]) -> str:
    return (f'<!doctype html><meta charset=utf-8><title>OOO Release Tracker</title>'
            f'<style>{CSS}</style>'
            f'<h1>Oscuro’s Oblivion Overhaul Remastered — Release Tracker</h1>'
            + version_header() + "".join(panels))


def main(out: Path | None = None) -> Path:
    out = Path(out) if out else HERE / "dashboard.html"
    ms = milestones.collect()
    annotations = ms["data"]["branches"] if ms["ok"] else {}
    out.write_text(
        render([milestones_panel(ms), maps_panel(), repos_panel(annotations),
                runs_panel(), views_panel(), sessions_panel()]),
        encoding="utf-8")
    return out


if __name__ == "__main__":
    print(main().as_uri())
