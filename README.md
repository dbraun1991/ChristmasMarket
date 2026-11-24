# ChristmasMarket

Statische Seite zu einem Weihnachtsmarkt-Wochenende in der Eifel: Reifferscheid, Monschau und Burg Satzvey mit Öffnungszeiten, Ablauf und OpenStreetMap-Karte.

**Live**: https://dbraun1991.github.io/ChristmasMarket/

## Aufbau

- `index.html`: die ganze Seite (HTML, CSS, JS inline), kein Build-Schritt.
- `map.jpg`: statischer Kartenausschnitt aus OpenStreetMap-Kacheln (© OpenStreetMap-Mitwirkende).
- `scripts/mkmap.py`: erzeugt `map.jpg` neu und gibt die Marker-Positionen (in Prozent) für die `.pin`-Links in `index.html` aus.
  `python3 scripts/mkmap.py <tile-cache-dir> map.jpg` (braucht Pillow und curl).

Lokal ansehen: `index.html` im Browser öffnen, oder `python3 -m http.server` und http://localhost:8000.

## Deployment

GitHub Actions veröffentlicht bei jedem Push auf `main` (`.github/workflows/deploy-pages.yml`).
Einmalig im Repo: **Settings → Pages → Source: GitHub Actions**.

## Daten

Öffnungszeiten und Preise laut eifel.info, burgsatzvey.de und StädteRegion Aachen,
Stand 22.11.2026.

## Lizenz

Code: MIT, siehe [LICENSE](LICENSE). Kartendaten: © OpenStreetMap-Mitwirkende, ODbL.

## Ideen und Runner

Neue Ideen landen als nummerierte Dateien in [docs/ideas/](docs/ideas/README.md). Eine zweite
Claude-Code-Sitzung, der **Runner**, setzt Ideen mit Status `Agent Ready` nacheinander um, die mit dem
höchsten Value zuerst ([ADR 0001](docs/adrs/0001-idea-backlog-with-runner-agent.md)):

```sh
cd ~/code/devland/ChristmasMarket
claude
> /runner            # ein Lauf
> /loop 2h /runner   # über Nacht alle zwei Stunden
```

- Die Hauptsitzung (das normale Gespräch) legt Ideen ab, schreibt Akzeptanzkriterien, vergibt Value
  und `Agent Ready`, fragt bei Unklarem und schreibt selbst keinen Code ([ADR 0002](docs/adrs/0002-main-session-directs-the-backlog.md)).
- Der Runner entscheidet nichts und schreibt keine ADRs; bei offenen Fragen setzt er `Klärung nötig`.
  Er beginnt eine neue Idee nur, solange die Auslastung unter 80 % (5 h) und 60 % (Woche) liegt.
- Jede umgesetzte Idee wird ein eigener git-Commit; **pushen machst du.**
- Protokoll: [docs/ideas/RUNNER.md](docs/ideas/RUNNER.md) (in allen devland-Projekten gleich).
