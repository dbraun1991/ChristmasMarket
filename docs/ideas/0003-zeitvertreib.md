# 0003: Zeitvertreib — Gitarre, Joggen, Harry Potter

Status: Umgesetzt · Value: 5 · Stand: 2026-11-25
Quelle: Diktat 2026-11-25
Berührt: index.html
Konflikte: –
Hängt ab von: –

## Idee

Neben den Weihnachtsmärkten und dem Kochen gibt es am Wochenende weiteren Zeitvertreib. Das soll
auf der Seite stehen:

- Gitarre spielen
- Laufen gehen (Joggen)
- Buch lesen (Harry Potter)

## Akzeptanzkriterien

- Neue eigene Sektion „Zeitvertreib“ direkt nach der Verpflegungs-Sektion („Was wir selbst
  essen“) und vor „Was uns erwartet“.
- Sie nennt genau die drei Zeitvertreibe: **Gitarre spielen**, **Joggen** (Laufen gehen) und
  **Lesen: Harry Potter**. Ein kurzer Satz macht klar: neben Märkten und Kochen.
- Stil und Aufbau passen zur Verpflegungs-Sektion (Eyebrow + Überschrift, kleine Karten), auch auf
  dem Handy ohne horizontales Scrollen. Kein Build-Schritt, alles inline in `index.html`.
- Packliste: Der bestehende Eintrag „Buch“ heißt künftig „Buch (Harry Potter)“; sein Schlüssel
  `data-id="buch"` bleibt unverändert (ADR 0003), ein gesetzter Haken bleibt also erhalten.
- Packliste: Der bestehende Eintrag „Laufsachen“ bekommt einen Hinweis im vorhandenen
  `hint`-Stil: „inkl. Laufhandschuhe“. Text, Schlüssel (`data-id="laufsachen"`) und Platz des
  Eintrags bleiben sonst unverändert.
- Packliste: **keine** Gitarre (wird nur auf der Seite erwähnt), keine neuen Einträge. Laufschuhe
  bleiben, wie sie sind.
- Der Zähler „x von y eingepackt“ bleibt dadurch bei derselben Gesamtzahl.

## Offene Fragen

Keine. Geklärt am 2026-11-25:
1. Platz: eigene Sektion nach Verpflegung.
2. Packliste: Gitarre nur auf der Seite erwähnen („die nehme ich mit“), Buch explizit als Harry
   Potter.
3. Laufen: Handschuhe als Hinweis bei „Laufsachen“ erwähnen, kein eigener Eintrag
   (Nachtrag 2026-11-25).

## Umsetzung

Runner, 2026-11-25.

**Geändert:** `index.html`
- Neue Sektion „Zeitvertreib“ (Eyebrow) / „Was wir sonst noch machen“ (h2) direkt nach
  „Was wir selbst essen“ und vor „Was uns erwartet“. Satz: „Neben den Märkten und dem Kochen bleibt
  Zeit für anderes.“ Drei Karten mit denselben Klassen wie die Verpflegung (`.meals`/`.meal`):
  „Gitarre spielen“, „Joggen“ (Hinweis „Laufen gehen“), „Lesen: Harry Potter“.
- Packliste: „Buch“ → „Buch (Harry Potter)“, `data-id="buch"` unverändert; „Laufsachen“ bekommt
  `<span class="hint">inkl. Laufhandschuhe</span>`, sonst unverändert.

**Selbsttest:** keiner vorhanden (statische Seite, `scripts/mkmap.py` nicht geändert).

**Kriterien geprüft** (Chrome, lokal über `python3 -m http.server`):
- Reihenfolge der Eyebrows per DOM: … Verpflegung, Zeitvertreib, Die drei Märkte … ✔
- Kartentitel genau die drei Zeitvertreibe, Satz „neben Märkten und Kochen“ vorhanden ✔
- Stil: gleiche Klassen wie Verpflegung, Screenshot Desktop geprüft; Handy: in 390-px-iframe
  einspaltig, `scrollWidth == clientWidth` (kein horizontales Scrollen) ✔
- „Buch (Harry Potter)“ / „Laufsachen inkl. Laufhandschuhe“ im DOM ✔; gespeicherte Haken
  `{buch, laufsachen}` unter `eifel-packliste-v2` nach Reload weiter gesetzt (ADR 0003) ✔
- Keine Gitarre in der Packliste, keine neuen Einträge: 24 Checkboxen vorher und nachher,
  Zähler „x von 24 eingepackt“ ✔

Nicht geprüft: echtes Handy (nur iframe-Simulation, Fenster ließ sich nicht verkleinern).
