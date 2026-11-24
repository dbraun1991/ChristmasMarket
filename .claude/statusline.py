#!/usr/bin/env python3
"""Statuszeile für dieses Projekt (devland-Vorlage, ursprünglich ideastorm Idee 0067).

Claude Code übergibt nach jeder Antwort ein JSON auf stdin. Darin steht unter `rate_limits` die
Auslastung des Plans (5-Stunden-Fenster und Woche, in Prozent). Dieses Skript zeigt sie an und
schreibt sie nach `.runner/limits.json`, damit der Runner vor jeder neuen Idee prüfen kann, ob er
anfangen darf (docs/ideas/RUNNER.md, Schritt 1).
"""
import json
import sys
import time
from pathlib import Path

ZIEL = Path(__file__).resolve().parent.parent / ".runner" / "limits.json"

try:
    daten = json.load(sys.stdin)
except Exception:
    daten = {}

rl = daten.get("rate_limits") or {}


def fenster(name):
    f = rl.get(name) or {}
    p = f.get("used_percentage")
    return {"used_percentage": p, "resets_at": f.get("resets_at")} if p is not None else None


stand = {"zeit": int(time.time()), "five_hour": fenster("five_hour"), "seven_day": fenster("seven_day")}
try:
    ZIEL.parent.mkdir(parents=True, exist_ok=True)
    tmp = ZIEL.with_suffix(".tmp")
    tmp.write_text(json.dumps(stand))
    tmp.replace(ZIEL)
except Exception:
    pass


def pct(f):
    return "?" if f is None else f"{f['used_percentage']:.0f} %"


print(f"5 h: {pct(stand['five_hour'])} · Woche: {pct(stand['seven_day'])}")
