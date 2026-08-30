"""Read-only collectors for the OOO program dashboard.

Every collector returns the same envelope so a failing feed renders as a
failed panel naming the error -- never as an absent one, which would read
as "nothing to report".
"""
from datetime import datetime


def envelope(data, source: str, ok: bool = True, error: str | None = None) -> dict:
    return {"data": data, "collected_at": datetime.now().isoformat(timespec="seconds"),
            "source": source, "ok": ok, "error": error}
