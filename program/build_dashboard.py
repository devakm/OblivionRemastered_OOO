"""Generate program/dashboard.html -- the OOO program view.

Static, self-contained, opened via file://. Never runs a generator or a
build: it prints the command instead, so opening the page is side-effect free.

Run: py -3 program/build_dashboard.py
"""
import html as _html
from datetime import datetime
from pathlib import Path

from .collect import (maps, milestones, pages, plots, releases, repos, runs, sessions)
from .tab_id import tab_head

HERE = Path(__file__).resolve().parent
CSS = """:root{color-scheme:light dark;--bg:#faf9f7;--fg:#222;--panel:#fff;--line:#ddd;--rule:#eee;
--muted:#777;--soft:#555;--link:#1a4d8f;--ok:#176d2c;--ok-bg:#eef7ef;--bad:#b3261e;--bad-bg:#fff5f5;
--warn:#8a6d00;--warn-bg:#fff8e1;--warn-line:#e8d9a0;--code:#f2f0ec;--grp:#f4f2ee;--track:#eee}
@media (prefers-color-scheme:dark){:root{--bg:#16171a;--fg:#e4e2de;--panel:#1f2024;--line:#3a3b40;
--rule:#2c2d31;--muted:#9a9890;--soft:#b5b2ab;--link:#8ab4f8;--ok:#6fcf87;--ok-bg:#1d3324;--bad:#f28b82;
--bad-bg:#3a1f1e;--warn:#e6c35c;--warn-bg:#352d14;--warn-line:#5c4d1e;--code:#2c2d31;--grp:#26272b;
--track:#2c2d31}}
body{font:14px/1.5 system-ui,sans-serif;margin:24px;background:var(--bg);color:var(--fg)}
.panel{border:1px solid var(--line);border-radius:8px;padding:14px 18px;margin:0 0 18px;background:var(--panel)}
.panel-error{border-color:var(--bad);background:var(--bad-bg)}
h1{font-size:20px}h2{font-size:15px;margin:0 0 10px}
table{border-collapse:collapse;width:100%}td,th{text-align:left;padding:4px 8px;border-bottom:1px solid var(--rule)}
.FRESH,.running,.MET{color:var(--ok);font-weight:600}
.STALE,.orphaned,.CONTRADICTED{color:var(--bad);font-weight:600}
.UNKNOWN,.UNVERIFIED{color:var(--warn);font-weight:600}
.done{color:var(--muted)}.PENDING{color:var(--soft);font-weight:600}
.pipeline{margin:0 0 12px}.ms{display:inline-block;padding:3px 10px;border:1px solid var(--line);
border-radius:14px;margin-right:6px;font-size:12px}.ms.in_progress{border-color:var(--warn);
background:var(--warn-bg);font-weight:600}.ms.done{border-color:var(--ok);background:var(--ok-bg);color:var(--ok)}
.next{background:var(--warn-bg);border:1px solid var(--warn-line);border-radius:6px;padding:8px 12px;margin:12px 0 0}
code{background:var(--code);padding:1px 5px;border-radius:4px;font-size:12px}
.stamp{color:var(--muted);font-size:12px}
.cols{display:flex;gap:26px;flex-wrap:wrap}.cols>div{flex:1 1 320px;min-width:0}
h3{font-size:13px;color:var(--soft);margin:0 0 6px}a{color:var(--link)}
.vers{font-size:16px;margin:0 0 18px;padding:10px 14px;background:var(--panel);
border:1px solid var(--line);border-radius:8px}.vers b{font-size:17px}.verr{color:var(--bad)}
.bar{height:8px;background:var(--track);border-radius:5px;overflow:hidden;margin:6px 0 14px}
.bar i{display:block;height:100%;background:var(--ok)}
.age{margin:0 0 12px;font-size:13px;color:var(--muted)}.age #age{font-weight:600}
.badge{display:inline-block;min-width:30px;text-align:center;color:#fff;font:700 11px/18px system-ui;
border-radius:5px;padding:0 4px}
.find{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin:0 0 10px}
.find input{flex:1 1 260px;font:14px system-ui;padding:6px 10px;border:1px solid var(--line);border-radius:6px;
background:var(--panel);color:var(--fg)}
.chip{border:1px solid var(--line);background:var(--panel);color:var(--fg);border-radius:14px;
padding:2px 10px 2px 3px;font:12px system-ui;cursor:pointer}.chip.off{opacity:.35}
tr.grp td{background:var(--grp);padding-top:8px}
td.tab{font-family:ui-monospace,monospace;font-size:12px;color:var(--soft)}
details{margin-top:14px}summary{cursor:pointer;color:var(--soft)}"""


def panel(title: str, env: dict, body_html: str) -> str:
    cls = "panel" if env.get("ok") else "panel panel-error"
    if not env.get("ok"):
        body_html = f'<p><b>collector failed:</b> {_html.escape(str(env.get("error")))}</p>'
    return (f'<section class="{cls}"><h2>{_html.escape(title)}</h2>{body_html}'
            f'<p class=stamp>{_html.escape(env.get("source",""))} · '
            f'{_html.escape(env.get("collected_at",""))}</p></section>')


def _badge(code: str, projects: dict) -> str:
    c = projects.get(code, {}).get("color", "#777")
    return f'<span class=badge style="background:{c}">{_html.escape(code)}</span>'


def _age(d) -> str:
    if d is None:
        return "missing"
    return "today" if d < 1 else f"{d:g}d"


def pages_panel() -> str:
    """The directory: every page across the OOO projects, grouped by project,
    with the tab title it shows -- so the right tab can be found -- and every
    unregistered page on disk listed below, so none goes missing."""
    env = pages.collect()
    data = env["data"] if env["ok"] else {"projects": {}, "pages": [], "other": []}
    projects = data["projects"]
    legend = "".join(
        f'<button class=chip data-p="{k}">{_badge(k, projects)} {_html.escape(p["name"])}</button>'
        for k, p in projects.items())
    rows, last = [], None
    for r in data["pages"]:
        if r["project"] != last:
            last = r["project"]
            rows.append(f'<tr class=grp data-p="{last}"><td colspan=5>{_badge(last, projects)} '
                        f'<b>{_html.escape(projects[last]["name"])}</b></td></tr>')
        state = (f' <span class="{r["state"]}">{r["state"]}</span>' if r["state"] else "")
        cmd = (f'<br><span class=stamp>rebuild: <code>{_html.escape(r["generator"])}</code></span>'
               if r["generator"] and r["state"] == "STALE" else "")
        link = (f'<a href="{_html.escape(r["url"])}" target=_blank>{_html.escape(r["label"])}</a>'
                if r["exists"] else f'{_html.escape(r["label"])} <span class=STALE>missing</span>')
        rows.append(f'<tr class=pg data-p="{r["project"]}"><td>{link}<br>'
                    f'<span class=stamp>{_html.escape(r["about"])}</span></td>'
                    f'<td>{_html.escape(r["kind"])}</td><td class=tab>{_html.escape(r["tab"])}</td>'
                    f'<td>{_age(r["age_days"])}{state}{cmd}</td></tr>')
    other = "".join(
        f'<tr class=pg data-p="{o["project"]}"><td>{_badge(o["project"], projects)} '
        f'<a href="{_html.escape(o["url"])}" target=_blank>{_html.escape(o["title"] or Path(o["path"]).name)}</a>'
        f'<br><span class=stamp>{_html.escape(o["path"])}</span></td>'
        f'<td>{_html.escape(o["note"]) or "<i>unregistered — add to collect/pages.py or delete</i>"}</td>'
        f'<td>{_age(o["age_days"])}</td></tr>' for o in data["other"])
    body = (f'<div class=find><input id=q type=search placeholder="Filter pages… (/ to focus)" autofocus>'
            f'{legend}</div>'
            '<table id=pages><tr><th>Page</th><th>Kind</th><th>Browser tab shows</th><th>Updated</th></tr>'
            + "".join(rows) + '</table>'
            f'<details><summary>Other pages found on disk ({len(data["other"])}) — '
            'old copies, experiments, unregistered</summary>'
            '<table id=other><tr><th>Page</th><th>What it is</th><th>Updated</th></tr>'
            + other + '</table></details>')
    return panel("Pages", env, body)


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


def plots_panel() -> str:
    """Newest MapClone review artifacts, newest first.

    Not a view: every run writes a NEW timestamped png, so there is nothing to
    call stale -- the mtime IS the content. gate_only flags a plot that landed
    in the pre-build gate folder but not the review folder, which is the
    asymmetry that previously made new plots invisible to review.
    """
    env = plots.collect()
    data = env["data"] if env["ok"] else {}
    rows = data.get("plots") or []
    if not rows:
        body = (f'<p class=stamp>no plots found in '
                f'{_html.escape(str(data.get("review_dir","")))}</p>')
        return panel("Plots (MapClone)", env, body)

    newest = data.get("newest_age_hours")
    head = (f'<p>Newest plot <b>{newest}h</b> old. '
            f'<span class=stamp>Review copies in '
            f'{_html.escape(str(data.get("review_dir","")))}; click to open.'
            f'</span></p>')
    trs = []
    for r in rows:
        if r["unexpected"]:
            warn = (' <span class=CONTRADICTED>gate-only — never copied '
                    'for review</span>')
        elif r["gate_only"]:
            warn = ' <span class=stamp>gate-only (by design)</span>'
        else:
            warn = ""
        trs.append(f'<tr><td><a href="{_html.escape(r["url"])}">'
                   f'{_html.escape(r["name"])}</a>{warn}</td>'
                   f'<td>{r["age_hours"]}h</td><td>{r["kb"]} KB</td></tr>')
    body = (head + '<table><tr><th>Plot</th><th>Age</th><th>Size</th></tr>'
            + "".join(trs) + '</table>')
    n_bad = data.get("unexpected_count", 0)
    n_gate = data.get("gate_only_count", 0)
    if n_bad:
        body += (f'<p><b class=CONTRADICTED>{n_bad} plot(s) reached the build '
                 f'gate but were never copied for review</b> — the dual-save '
                 f'regression. Producer: <code>work/plot_water_xy_actual.py</code>.</p>')
    if n_gate - n_bad:
        body += (f'<p class=stamp>{n_gate - n_bad} further gate-only plot(s) are '
                 f'expected: plot_water_analysis.py (cumulative grid) and '
                 f'plot_water_z_analysis.py (YZ side view) single-save by design.</p>')
    return panel("Plots (MapClone)", env, body)


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


                                   # noqa: E501
SELF_AGE_JS = """<script>(function(){
var el=document.getElementById('age'),t=Date.parse(el.dataset.gen);
function tick(){var m=Math.round((Date.now()-t)/60000),s;
if(m<1)s='just now';else if(m<60)s=m+' min ago';
else if(m<1440)s=(m/60).toFixed(1)+' h ago';else s=(m/1440).toFixed(1)+' days ago';
el.textContent='generated '+s;
el.className=m>1440?'CONTRADICTED':m>30?'UNVERIFIED':'MET';}
tick();setInterval(tick,30000);})();</script>"""


FILTER_JS = """<script>(function(){
var q=document.getElementById('q'),off={};
function apply(){var t=q.value.toLowerCase();
document.querySelectorAll('tr.pg').forEach(function(r){
r.hidden=off[r.dataset.p]||(t&&r.textContent.toLowerCase().indexOf(t)<0);});
document.querySelectorAll('tr.grp').forEach(function(g){var n=g.nextElementSibling,any=false;
while(n&&!n.classList.contains('grp')){if(!n.hidden)any=true;n=n.nextElementSibling;}g.hidden=!any;});}
q.addEventListener('input',apply);
document.querySelectorAll('.chip').forEach(function(c){c.onclick=function(){
off[c.dataset.p]=!off[c.dataset.p];c.classList.toggle('off');apply();};});
document.addEventListener('keydown',function(e){if(e.key==='/'&&document.activeElement!==q){
e.preventDefault();q.focus();}});})();</script>"""


def self_age(now=None) -> str:
    """The page is a snapshot; say how old it is.

    Every other view here gets a staleness verdict. Without this the dashboard
    was the one artifact that could silently go stale while looking current --
    the exact drift it exists to catch. Client-side only: reading the clock is
    not a side effect, and the page still never runs a generator.
    """
    gen = (now or datetime.now()).isoformat(timespec="seconds")
    return (f'<p class=age><span id=age data-gen="{gen}">generated {gen}</span>'
            f' · snapshot taken {gen} — rerun '
            f'<code>py -3 -m program.build_dashboard</code> to refresh</p>')


def render(panels: list[str], now=None) -> str:
    return (f'<!doctype html><meta charset=utf-8>{tab_head("Hub")}'
            f'<style>{CSS}</style>'
            f'<h1>OOO Hub <span class=stamp>— every dashboard, tracker, guide and report, '
            f'plus Oscuro’s Oblivion Overhaul Remastered release status</span></h1>'
            + self_age(now) + version_header() + "".join(panels) + SELF_AGE_JS + FILTER_JS)


def main(out: Path | None = None) -> Path:
    out = Path(out) if out else HERE / "dashboard.html"
    ms = milestones.collect()
    annotations = ms["data"]["branches"] if ms["ok"] else {}
    out.write_text(
        render([pages_panel(), milestones_panel(ms), maps_panel(), plots_panel(),
                repos_panel(annotations), runs_panel(), sessions_panel()]),
        encoding="utf-8")
    return out


if __name__ == "__main__":
    print(main().as_uri())
