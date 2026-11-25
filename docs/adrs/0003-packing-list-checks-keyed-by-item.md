# ADR 0003: Packing list checks are stored per item key, not by position

Status: Accepted · Date: 2026-11-25

## Context
The packing list in `index.html` stored its checkboxes in localStorage (`eifel-packliste`) as an
array in DOM order. Idea 0001 adds new entries; any insertion or reordering would move saved checks
onto the wrong items. On 2026-11-25 the user asked for a smarter storage "e.g. via JSON" and
decided: use the new structure, the checks have not been used yet, so no migration.

## Decision
- Every packing list checkbox gets a fixed, unique key (e.g. `data-id`).
- Checks are stored as a JSON object `{ "<key>": true|false }`.
- Old array data is not migrated; it is ignored without error.

## Consequences
- Entries can be added, removed or reordered without corrupting saved checks.
- New entries must get a key; renaming a key drops that item's saved check.
- Implemented by idea 0002 ([../ideas/0002-packliste-haken-nach-eintrag.md](../ideas/0002-packliste-haken-nach-eintrag.md)).
