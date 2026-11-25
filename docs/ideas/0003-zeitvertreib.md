# 0003: Zeitvertreib — Gitarre, Joggen, Harry Potter

Status: Agent Ready · Value: 5 · Stand: 2026-11-25
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
- Packliste: **keine** Gitarre (wird nur auf der Seite erwähnt), keine weiteren neuen Einträge.
  Laufschuhe und Laufsachen stehen schon drauf und bleiben, wie sie sind.
- Der Zähler „x von y eingepackt“ bleibt dadurch bei derselben Gesamtzahl.

## Offene Fragen

Keine. Geklärt am 2026-11-25:
1. Platz: eigene Sektion nach Verpflegung.
2. Packliste: Gitarre nur auf der Seite erwähnen („die nehme ich mit“), Buch explizit als Harry
   Potter.

## Umsetzung

–
