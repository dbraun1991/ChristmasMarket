# 0002: Packlisten-Haken nach Eintrag statt nach Position speichern

Status: Agent Ready · Value: 7 · Stand: 2026-11-25
Quelle: Diktat 2026-11-25, bei Idee 0001
Berührt: index.html
Konflikte: –
Entscheidung: [ADR 0003](../adrs/0003-packing-list-checks-keyed-by-item.md)
Hängt ab von: –

## Idee

Die Packliste speichert ihre Haken heute als Array nach Position (`eifel-packliste` in
localStorage). Kommt ein Eintrag dazu oder wird umsortiert, landen Haken auf falschen Einträgen.
Stattdessen soll jeder Eintrag einen festen Schlüssel haben und die Haken als JSON-Objekt
`{ "<schlüssel>": true|false }` gespeichert werden.

## Akzeptanzkriterien

- Jede Checkbox der Packliste hat einen festen, eindeutigen Schlüssel (z. B. `data-id` in
  kebab-case, aus dem Eintragsnamen abgeleitet), auch die verschachtelten Schuh-Einträge.
- Gespeichert wird ein JSON-Objekt Schlüssel → abgehakt, kein Array nach Position.
- Ein neuer Eintrag an beliebiger Stelle oder eine geänderte Reihenfolge lässt alle gesetzten
  Haken auf ihren Einträgen.
- Keine Übernahme alter Haken: alte gespeicherte Daten im Array-Format werden ignoriert und
  führen zu keinem Fehler (z. B. neuer localStorage-Schlüssel).
- Zähler „x von y eingepackt“, Öffnen/Schließen des Dialogs und das Verhalten ohne localStorage
  (try/catch) funktionieren wie bisher.
- Ein Code-Kommentar beim Speichern sagt `ADR 0003: …` und erklärt kurz, warum nach Schlüssel statt Position gespeichert
  wird.

## Offene Fragen

Keine. Geklärt am 2026-11-25: Haken wurden noch nicht benutzt, keine Migration nötig.

## Umsetzung

(trägt der Runner ein)
