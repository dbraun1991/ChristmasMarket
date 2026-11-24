# ADR 0001: Idea backlog with a runner agent, adopted from the devland template

Status: Accepted · Date: 2026-11-24

## Context
The user works on several projects in `~/code/devland`. `ideastorm` and `ultimate-quiz` already use
a numbered idea backlog plus a separate "runner" Claude Code session that implements ideas marked
`Agent Ready`. On 2026-11-24 the user asked to transfer that structure, ADRs included, to every
project folder and to note it in `AGENTS.md` and `README.md` ("bitte übertrage die struktur inkl.
adrs auf alle ordner. vermerke dies immer in der agents.md und readme.md").

## Decision
- Ideas live in `docs/ideas/NNNN-kebab-case.md` with the header and sections from
  `docs/ideas/README.md`. Decisions stay in `docs/adrs/`.
- The runner protocol is `docs/ideas/RUNNER.md`. It is identical in every project; the master copy
  lives in `~/code/devland/_vorlage/`. Project specifics (ADR folder, self-test, git or not) are
  listed in `AGENTS.md` → "Runner settings".
- `/runner` (`.claude/commands/runner.md`) starts a run. The status line
  (`.claude/statusline.py`) writes `.runner/limits.json`; the runner only starts a new idea at
  5 h usage below 80 % and weekly usage below 60 %.
- git is the safety net: the runner only touches files without uncommitted changes, commits each
  finished idea on its own (`Idee NNNN: …`) and never pushes. On a red test it rolls back with
  `git restore`. `.runner/` is gitignored.

## Consequences
- The runner never decides anything and never writes ADRs; open questions become `Klärung nötig`.
- Protocol changes are not picked up automatically: change the template and copy it to the
  projects by hand.
- `.claude/settings.json` uses an absolute path. Moving the folder requires updating it.
