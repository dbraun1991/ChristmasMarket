# 0001: Verpflegung — eigenes Essen neben den Buden

Status: Rohidee · Value: 6 · Stand: 2026-11-25
Quelle: Diktat 2026-11-25
Berührt: index.html
Konflikte: –
Hängt ab von: –

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

(Entwurf, wird nach Klärung der offenen Fragen vervollständigt)

- Die Seite zeigt einen Bereich „Verpflegung“ mit den Gruppen Morgens, Mittags und Getränke und
  genau den oben genannten Gerichten und Getränken. Bei den Overnight Oats stehen die Zutaten dabei.
- Die Packliste enthält „Overnight-Schale“ und „Protein-Shaker“.
- **[Vorschlag]** Bereits gesetzte Haken der Packliste bleiben nach dem Update auf den richtigen
  Einträgen. Die Haken werden heute nach Position gespeichert (`eifel-packliste` in localStorage),
  neue Einträge dürfen sie also nicht verschieben.
- Stil und Aufbau passen zum Rest der Seite (kein Build-Schritt, alles inline in `index.html`),
  auch auf dem Handy.

## Offene Fragen

1. Wo steht der Bereich „Verpflegung“ auf der Seite: als eigene Sektion (z. B. nach „Freitag bis
   Sonntag“) oder eingebaut in die Tageskarten des Ablaufs?
2. Packliste: eigene Kategorie (z. B. „Küche & Verpflegung“) oder in eine bestehende (Specials /
   Unterwegs)?
3. Sollen auch die Zutaten (Hafer, Haferdrink, TK-Beeren, Proteinpulver, Linsen, Kokosmilch, Tofu,
   Eier, Gemüse, SnackMeals …) als Einkaufs-/Packliste auf die Seite?
4. **[Vorschlag]** Weitere Utensilien auf die Packliste: Kühltasche/Kühlakkus für TK-Beeren,
   Wasserkocher für die SnackMeals und den Tee, Besteck. Gibt es in der Unterkunft eine Küche mit
   Herd und Pfanne (für Omelett, Dal und Curry)?

## Umsetzung

(trägt der Runner ein)
