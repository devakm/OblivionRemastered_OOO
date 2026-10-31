"""Browser-tab identity for generated pages: a project code in front of the title
plus a coloured letter favicon, so same-named pages from different OOO projects
(two "Review dashboard"s, two "SyncMap review"s) are told apart at a glance.

The code/colour table is shared by convention with ItemClone, MapRender and RAX
(tools/tab_id.py in each) and with collect/pages.py PROJECTS -- keep them in step.
"""
import html
from urllib.parse import quote

CODE, COLOR = "OOO", "#6b3fa0"


def tab_head(title: str, code: str = CODE, color: str = COLOR) -> str:
    """`<title>` + `<link rel=icon>` for a page; `title` is plain text."""
    svg = (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'>"
           f"<rect width='32' height='32' rx='7' fill='{color}'/>"
           f"<text x='16' y='22' font-family='Arial,sans-serif' font-weight='700' "
           f"font-size='{15 if len(code) < 3 else 11}' fill='#fff' text-anchor='middle'>"
           f"{code}</text></svg>")
    return (f"<title>{html.escape(code)} · {html.escape(title)}</title>"
            f'<link rel=icon href="data:image/svg+xml,{quote(svg)}">')
