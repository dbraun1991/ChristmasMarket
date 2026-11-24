# AGENTS.md

Guidance for AI coding agents (and humans) working in this folder. For humans there is
[README.md](README.md); the reasons behind decisions are in [docs/adrs](docs/adrs/README.md).

## What this is

See [README.md](README.md). This file was created on 2026-11-24 together with the idea backlog; it
only holds the rules every devland project shares. Add project specifics (structure, stack,
conventions) as they come up.

## Conventions to preserve

- **Ideas vs. decisions.** Ideas live in `docs/ideas/` and may be rewritten freely. As soon as
  something is *decided*, record it as an ADR in `docs/adrs/` and link it from the idea.
- **ADRs are immutable once Accepted.** To change a decision, write a new ADR that supersedes the
  old one, set the old one's status to "Superseded by NNNN", and update `docs/adrs/README.md`.
- **Numbering**: ADRs and ideas are `NNNN-kebab-case.md`, four digits, separate ranges, next free
  number, never renumbered.
- **Code ↔ ADR coupling:** where code implements a decision, its comment says `ADR NNNN: <why>`.
- **Don't invent the idea.** Fill gaps with explicit open questions, mark own additions as
  **[Vorschlag]**.
- Idea files are German; this file and ADRs are English.

## Idea backlog and the runner agent

Ideas in `docs/ideas/` form a backlog that a separate **runner** session (second terminal,
`/runner`) implements ([ADR 0001](docs/adrs/0001-idea-backlog-with-runner-agent.md)). Full protocol: [docs/ideas/RUNNER.md](docs/ideas/RUNNER.md) — identical in every
project, master copy in `~/code/devland/_vorlage/`. In short:

- Each idea file has a header: `Status`, `Value` (0–10), `Quelle`, `Berührt`, `Konflikte`,
  `Hängt ab von`, and sections Idee / Akzeptanzkriterien / Offene Fragen / Umsetzung (German).
- `Value` and `Agent Ready` are set by the user or by the main session ([ADR 0002](docs/adrs/0002-main-session-directs-the-backlog.md): once criteria are
  complete and no question is open; otherwise it asks). The runner never sets them.
- The runner takes `Agent Ready` ideas by highest Value (tie: lower number), strictly one after
  another, only while usage is below 80 % (5 h) and 60 % (week). It sets `Klärung nötig` instead
  of deciding, never writes ADRs, and rolls back + aborts the run when the self-test is red.
- **Main session** (conversation) is the **director, not a coder** ([ADR 0002](docs/adrs/0002-main-session-directs-the-backlog.md)): file and split ideas,
  write acceptance criteria, set Value / Agent Ready, ask when unclear, write ADRs on the user's
  decision. It never changes code or tests — only the runner implements. Do not edit files listed in
  `Berührt` of an idea that is `In Arbeit`.

### Runner settings

Read by `docs/ideas/RUNNER.md`. Keep them current.

| Setting | Value |
|---|---|
| ADR folder | `docs/adrs/` |
| Backlog ADRs | runner: [ADR 0001](docs/adrs/0001-idea-backlog-with-runner-agent.md), director: [ADR 0002](docs/adrs/0002-main-session-directs-the-backlog.md) |
| Safety net | git, branch `main`: the runner commits each finished idea (`Idee NNNN: …`), never pushes |
| Self-test | none (static page). `python3 -m py_compile scripts/mkmap.py` if the script changes; check `index.html` in a browser and say so if you could not. |

Files: `.claude/commands/runner.md` (`/runner`), `.claude/statusline.py` + `.claude/settings.json`
(status line, writes `.runner/limits.json`), `.runner/` (gitignored; usage + per-idea backup),
`CLAUDE.md` (imports this file).
