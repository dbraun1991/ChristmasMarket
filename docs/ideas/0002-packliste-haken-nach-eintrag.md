# 0002: Packlisten-Haken nach Eintrag statt nach Position speichern

Status: Umgesetzt · Value: 7 · Stand: 2026-11-25
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

Runner, 2026-11-25.

**Geändert:** `index.html`
- Alle 22 Checkboxen der Packliste haben ein festes `data-id` in kebab-case (z. B. `bademantel`,
  `schuhe-weihnachtsmarkt`, `satzvey-tickets`), auch die drei verschachtelten Schuh-Einträge.
- Das Skript speichert die Haken als Objekt `{ "<data-id>": true|false }` unter dem neuen
  localStorage-Schlüssel `eifel-packliste-v2`; der alte Schlüssel `eifel-packliste` (Array) wird
  nicht mehr gelesen. Ist unter dem neuen Schlüssel kein Objekt gespeichert (z. B. ein Array),
  wird es ignoriert. Kommentar `ADR 0003: …` steht beim Speichern.

**Selbsttest:** keiner vorhanden (statische Seite).

**Kriterien geprüft** (Headless-Chrome mit einer Testkopie der Seite im Scratchpad):
- Eindeutige Schlüssel: `grep` auf doppelte `data-id` → keine; 22 Checkboxen, 22 Schlüssel.
- Objekt statt Array / neuer Eintrag: In der Testkopie wurde ganz oben in „Specials“ ein neuer
  Eintrag eingefügt, vorab gespeichert waren `buch`, `schuhe-laufschuhe`, `thermosflasche`. Genau
  diese drei waren danach abgehakt, der neue Eintrag nicht. Nach Abhaken von `powerbank` stand im
  Speicher das Objekt mit `powerbank: true`.
- Alte Daten: ein Array `[true,true,true]` unter `eifel-packliste` hatte keine Wirkung und keinen Fehler.
- Zähler: „3 von 23 eingepackt“ → nach Abhaken „4 von 23“ (23 mit Testeintrag). Dialog öffnen
  und schließen per Button funktioniert. localStorage-Zugriffe stehen weiter in try/catch
  (Code gelesen; ein Browser ohne localStorage wurde nicht eigens simuliert).
- Optik im Browser nicht angesehen (nur Attribute ergänzt, kein Layout geändert).
