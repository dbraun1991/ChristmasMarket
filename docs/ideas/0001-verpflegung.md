# 0001: Verpflegung — eigenes Essen neben den Buden

Status: Umgesetzt · Value: 6 · Stand: 2026-11-25
Quelle: Diktat 2026-11-25
Berührt: index.html
Konflikte: –
Hängt ab von: Idee 0002 (Haken nach Eintrag speichern)

## Idee

Neben den Essensbuden auf den Märkten braucht es eigene Verpflegung. Die Seite bekommt dazu einen
Bereich „Verpflegung“, und die Packliste bekommt die nötigen Utensilien.

**Morgens**
- Müsli als Overnight Oats: Hafer, Haferdrink, TK-Beeren, Proteinpulver

**Mittags** (Auswahl)
- Linsendal mit Tomate und Kokosmilch
- HotWater-Outdoor-SnackMeals
- Omelett mit Gemüse
- Nudeln oder Reis mit Tofu und Gemüse (Curry)

**Getränke**
- Wasser / Tee
- Proteinshake

**Packliste, neu**
- Overnight-Schale
- Protein-Shaker

## Akzeptanzkriterien

- Neue eigene Sektion „Verpflegung“ direkt nach der Ablauf-Sektion „Freitag bis Sonntag“,
  gegliedert in **Morgens**, **Mittags** und **Getränke**, mit genau den oben genannten Gerichten
  und Getränken. Bei den Overnight Oats stehen die Zutaten dabei (Hafer, Haferdrink, TK-Beeren,
  Proteinpulver). Ein kurzer Satz macht klar: Ergänzung zu den Essensbuden auf den Märkten.
- Die Packliste bekommt eine neue Kategorie „Küche & Verpflegung“ mit genau zwei Einträgen:
  „Overnight-Schale“ und „Protein-Shaker“. Keine Zutaten und keine weiteren Utensilien.
- Der Zähler „x von y eingepackt“ zählt die neuen Einträge mit.
- Die beiden neuen Einträge bekommen eigene Schlüssel nach dem Schema aus Idee 0002. Die neue
  Kategorie steht dort in der Packliste, wo sie inhaltlich passt.
- Stil und Aufbau passen zum Rest der Seite (kein Build-Schritt, alles inline in `index.html`),
  auch auf dem Handy ohne horizontales Scrollen.

## Offene Fragen

Keine. Geklärt am 2026-11-25:
1. Platz: eigene Sektion nach dem Ablauf.
2. Packliste: neue Kategorie „Küche & Verpflegung“.
3. Zutaten: nicht auf die Packliste, nur im Bereich Verpflegung.
4. Weitere Utensilien: keine („ich denke daran“).

## Umsetzung

Runner, 2026-11-25.

**Geändert:** `index.html`
- Neue Sektion (Eyebrow „Verpflegung“, Überschrift „Was wir selbst essen“) direkt nach „Freitag
  bis Sonntag“, mit Satz „Als Ergänzung zu den Essensbuden auf den Märkten …“ und drei Karten
  **Morgens** (Overnight Oats mit Zutaten Hafer, Haferdrink, TK-Beeren, Proteinpulver),
  **Mittags** („zur Auswahl“, die vier Gerichte) und **Getränke** (Wasser / Tee, Proteinshake).
- CSS `.meals` / `.meal` im Stil der Markt-Karten, unter 820 px einspaltig.
- Packliste: neue Kategorie „Küche & Verpflegung“ als letzte, nach „Unterwegs“ (dort steht schon
  die Thermosflasche), mit „Overnight-Schale“ (`data-id="overnight-schale"`) und
  „Protein-Shaker“ (`data-id="protein-shaker"`).

**Selbsttest:** keiner vorhanden (statische Seite).

**Kriterien geprüft** (Headless-Chrome, Testkopie im Scratchpad):
- Reihenfolge der Überschriften: … › Freitag bis Sonntag › Was wir selbst essen › Was uns erwartet.
- Inhalte: Screenshots bei 1280 px und 500 px angesehen, genau die Gerichte/Getränke aus der Idee.
- Zähler: „0 von 24 eingepackt“ (vorher 22), nach Abhaken des Protein-Shakers „1 von 24“ und
  gespeichert als `{"protein-shaker":true}`.
- Schlüssel: keine doppelten `data-id`.
- Handy: bei 500 px Breite `scrollWidth` < Fensterbreite, also kein horizontales Scrollen. Schmaler
  als 500 px ließ Headless-Chrome nicht zu; 375 px im echten Handy nicht geprüft.
- Dunkelmodus nicht angesehen (nur bestehende Farbvariablen verwendet).
