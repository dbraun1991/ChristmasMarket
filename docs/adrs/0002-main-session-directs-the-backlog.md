# ADR 0002: The main session directs the backlog: it sets Value and criteria, never writes code

Status: Accepted · Date: 2026-11-24

## Context
In `ultimate-quiz` (its ADR 0004) it worked well that the main session only files ideas and the
runner implements them. The user's words there: "denk dran, du bist director, kein coder. lege nur
ideen ab" and "vergebe value und akzeptanz selbst .. bei fragen, frag". On 2026-11-24 the user decided
to adopt this rule, together with ADR 0001, in every project.

## Decision
- The **main session is the director**. It files ideas, writes acceptance criteria, sets `Value`
  (0–10) and sets `Agent Ready` once the criteria are complete and no question or conflict is open.
- If anything is unclear, it **asks the user** and leaves the idea as `Rohidee` until answered.
  It never decides open product questions on its own; own additions stay marked **[Vorschlag]**
  and need the user's yes (an explicit "alles nach deinen Vorschlägen" counts).
- The main session **never changes code or tests**. Only the runner implements. File chores the
  user asks for explicitly remain allowed.
- The user may still set or override `Value` and `Agent Ready` at any time.
- The runner never sets `Value` or `Agent Ready`.

## Consequences
- Ideas reach the runner faster; the user only answers questions.
- The main session states the Value it chose in its reply, so the user can correct it.
- Even small code changes go through an idea and the runner.
