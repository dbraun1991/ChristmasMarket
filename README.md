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

Öffnungszeiten und Preise laut eifel.info, Stand 17.10.2026. Für Reifferscheid gibt es
abweichende Angaben aus Vorjahren. Vor der Fahrt beim Veranstalter prüfen.

## Lizenz

Code: MIT, siehe [LICENSE](LICENSE). Kartendaten: © OpenStreetMap-Mitwirkende, ODbL.
