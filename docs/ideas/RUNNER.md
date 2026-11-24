# Runner protocol

How the **runner agent** works. The runner is a separate Claude Code session in a
second terminal. It implements ideas from `docs/ideas/` that are marked **Agent Ready**,
one after another, without touching the main (conversation) session.

This file is **the same in every project** (master copy: `~/code/devland/_vorlage/`, derived
from `ideastorm` and `ultimate-quiz`). Everything project-specific — ADR folder, the numbers of
the backlog ADRs, git or not, the self-test — is listed in `AGENTS.md` → **"Runner settings"**.
Read that block first; where this file says "the runner ADR", "the director ADR", "the ADR
folder" or "the self-test", it means the values listed there.

Start it like this:

```sh
cd ~/code/devland/<project>
claude
> /runner
```

`/runner` is defined in `.claude/commands/runner.md` and only points here. Without the
command, "Lies docs/ideas/RUNNER.md und starte einen Lauf." works the same.

Read `AGENTS.md` first. Every convention there applies to the runner too. Never run
`git init`, never push, never change branches.

---

## Roles

| Who | May | May not |
|---|---|---|
| **User** | set `Agent Ready`, set `Value`, write acceptance criteria, resolve conflicts, decide. The user may also tell the main session to write `Agent Ready` / `Value` into a file ("0003 Agent Ready, Value 5"); that counts as the user setting it. | — |
| **Main session** (conversation, the director — director ADR) | file ideas, split them, write criteria, mark conflicts, set `Value` and `Agent Ready` once no question is open, ask the user otherwise, write ADRs on the user's decision | change code or tests; decide open product questions on its own; edit files listed in `Berührt` of an idea that is `In Arbeit` |
| **Runner** | implement `Agent Ready` ideas, set `In Arbeit` / `Umgesetzt` / `Klärung nötig`, file new `Rohidee`s, commit its own work (git projects) | write or change ADRs (not even Proposed), set `Agent Ready` or `Value`, invent requirements, decide anything, push |

## Idea file header

Every idea is `docs/ideas/NNNN-kebab-case.md` (four digits, never renumbered, next free
number for new ideas). The header is read by the runner:

```
Status: Agent Ready · Value: 4 · Stand: YYYY-MM-DD
Quelle: …
Berührt: index.html, docs/…
Konflikte: – | ADR 0002 (…) | ADR 0002 (…) — gelöst: <how, by the user>
Hängt ab von: – | Idee 0006
```

Sections: `## Idee`, `## Akzeptanzkriterien`, `## Offene Fragen`, `## Umsetzung`.
Ideas taken over from an older notes folder may still have free-form sections; they are
`Rohidee` until the main session brings them into this form.

**Status values:** `Rohidee` → `Agent Ready` → `In Arbeit` → `Umgesetzt`, plus
`Klärung nötig` and `Verworfen`.

**Value:** 0–10, 10 = most valuable, set by the user or the main session (director ADR), never
by the runner. `–` = not rated.

## Safety net: git or backup

`AGENTS.md` → "Runner settings" says which one applies.

- **git project:** git is the backup. Before claiming an idea, every file the runner will change
  must have **no uncommitted changes** (`git status --porcelain -- <files>` is empty), except the
  idea file itself and `docs/ideas/README.md`. If a file is dirty, the user or the main session is
  working on it: set `Klärung nötig` ("Datei X hat nicht committete Änderungen") and go on with
  the next idea. Rollback = `git restore -- <files>` plus deleting the files listed in `NEU.txt`.
  The runner commits each finished idea (step 6). It never pushes, never rewrites history, never
  uses `git add -A` / `git add .` / `git commit -a`, and never commits files it did not change.
- **No git:** copy every file before changing it to `.runner/backup/NNNN/<same relative path>`.
  Rollback = copy them back plus deleting the files listed in `NEU.txt`.

In both cases `.runner/backup/NNNN/` exists while idea NNNN is `In Arbeit`. It holds
`DATEIEN.txt` (every file the runner changed so far, one path per line), `NEU.txt` (files it
created), and — without git — the copies.

## A run

A run works through ideas **strictly one at a time**. Each idea is finished completely
(code, check, docs, report, commit) before the next one is picked. The run ends when no
pickable idea is left, or when it is aborted (see step 6).

### 0. Before the first idea

1. Read `AGENTS.md` (incl. "Runner settings"), this file and the ADR folder's README.
2. Look for ideas with `Status: In Arbeit`. They come from an interrupted run. For each one:
   roll back using `.runner/backup/NNNN/` (see "Safety net"), set the status to
   `Klärung nötig` with the question "Lauf wurde unterbrochen — Änderungen zurückgesetzt,
   neu starten?", and remove the backup folder.
3. Run the **self-test** from "Runner settings". If it is **not green**, change nothing and stop
   the run with the output. Broken code must not become the base for new work. If the project
   has no automated self-test, note "kein Selbsttest vorhanden" and continue.

### 1. Check the usage limit, then pick the next idea

**Usage limit first.** The runner and the user's main session share one Claude plan. The
user's requirements work must never run short because the runner used the budget.
Before **every** new idea (also the first one):

1. Read `.runner/limits.json`. The status line (`.claude/statusline.py`) writes it after every
   answer, with `five_hour.used_percentage` and `seven_day.used_percentage`.
2. Start a new idea only if **both** hold:
   - 5-hour window: used **below 80 %**
   - week: used **below 60 %** (keeps about 40 % of the week for the main session)
3. If one is at or above its limit, **do not start a new idea.** End the run normally with
   "Grenze erreicht: 5 h NN % / Woche NN %, Reset <resets_at as local time>".
4. If the file is missing, older than 15 minutes, or a value is `null`: send one short message
   (this refreshes the status line), then read it again. Still unknown → end the run with
   "Auslastung unbekannt, nichts begonnen". Never guess.

An idea that is already running is finished, even if it crosses the limit. The check only
happens between ideas.

Candidates: every `docs/ideas/NNNN-*.md` with `Status: Agent Ready`. Skip a candidate
(and note why for the final report) when:

- `Hängt ab von` names an idea that is not `Umgesetzt` ("0007 blockiert durch 0003"), or
  a condition that is not met yet.

Of the rest, take the **highest Value**. On a tie, the **lower number** (older idea).
Value `–` (not rated) counts as lower than 0, so unrated ideas come last.
No candidate left → go to "End of the run".

### 2. Check before touching anything

Set the idea to `Klärung nötig`, write the question under `## Offene Fragen` (dated,
marked `Runner, YYYY-MM-DD`) and go back to step 1 if any of these holds:

- `## Akzeptanzkriterien` is missing or still says "(fehlt …)", or contains a `⟨offen …⟩`
  placeholder. Criteria marked `[Vorschlag]` count as confirmed once the idea is `Agent Ready`.
- `Konflikte` names a conflict that is not marked `— gelöst: …`.
- The idea contradicts an **Accepted** ADR or an `Umgesetzt` idea, even if nobody
  wrote it down yet. Add the conflict to the header as well.
- The criteria leave a choice open that changes behaviour, content, texts users see, or
  anything an ADR would record. **Ask, don't pick.**
- `Berührt` is empty and the affected files cannot be named with certainty from the
  criteria.
- git project: a file in `Berührt` has uncommitted changes (see "Safety net").

### 3. Claim and secure

1. Set `Status: In Arbeit (Runner, YYYY-MM-DD HH:MM)`.
2. Create `.runner/backup/NNNN/`, list every file in `Berührt` (plus any further file you will
   change) in `DATEIEN.txt`. Without git, copy each of them to
   `.runner/backup/NNNN/<same relative path>`. If you later need to touch another file, add it
   (and, without git, back it up) first. For a file that does not exist yet, note it in
   `NEU.txt`, so a rollback deletes it.

### 4. Implement

- **ADR check first:** in every file you are about to change, look up the `ADR NNNN`
  comments in and around the affected code and read those ADRs. If the change would break an
  Accepted ADR → roll back (step 6, red path) and set `Klärung nötig` with the conflict, but do
  not abort the run for this. Keep the references correct, and add `ADR NNNN: <why>` comments
  to code you write for a decision.
- Follow `AGENTS.md` (structure, language, conventions).
- Do exactly what the criteria say. Nothing extra. If something else looks worth doing,
  file it as a new idea (step 7) instead of doing it.
- Keep `README.md` / `AGENTS.md` in sync only where the idea's criteria say so; otherwise
  note the needed change in the report.

### 5. Verify

1. Run the self-test from "Runner settings" (if one exists). It must be green.
2. Check every acceptance criterion and note how it was checked.
3. If something can only be checked in a real browser (or on real hardware) and you could not,
   say so in the report ("im Browser nicht geprüft").

### 6. Finish or roll back

**Green and all criteria met:**

- `Status: Umgesetzt · …`, `Stand:` today.
- Fill `## Umsetzung`: date, what changed (file + short description), test result, how each
  criterion was checked, anything not checked.
- Update the idea's row in `docs/ideas/README.md` (move it to "Umgesetzt").
- git project: commit exactly the files in `DATEIEN.txt`, `NEU.txt`, the idea file and
  `docs/ideas/README.md` (`git add -- <those files>`), message `Idee NNNN: <Titel>`.
- Delete `.runner/backup/NNNN/`.
- Continue with step 1.

**Test red or a criterion cannot be met:**

- Roll back (see "Safety net") and delete the backup folder.
- `Status: Klärung nötig`, and under `## Offene Fragen` the error output / what failed.
- Update the row in `docs/ideas/README.md`.
- **Abort the run.** Do not pick another idea.

### 7. New thoughts during the run

When something comes up that is not part of the current idea (a bug, a missing rule,
an idea): file it as a new `docs/ideas/NNNN-kebab.md` with `Status: Rohidee · Value: –`,
`Quelle: Runner, YYYY-MM-DD, bei Idee NNNN`, and add it to the "Rohideen" table in
`docs/ideas/README.md`. Never set Value or Agent Ready on it.

### Overnight

In the runner terminal, `/loop 2h /runner` starts a run every two hours. Each run checks the
limit first (step 1), so a run after a reset of the 5-hour window picks up where the last one
stopped. The terminal must stay open and the computer must stay awake. Without `/loop`, a single
`/runner` works as before.

### End of the run

Print a short German summary in the terminal:

- umgesetzt: NNNN title (one line each, git: with commit hash)
- Klärung nötig: NNNN, plus the question
- übersprungen: NNNN, plus the reason (blocked by NNNN, …)
- neue Rohideen: NNNN
- abgebrochen: yes/no, why
- Auslastung am Ende: 5 h NN % · Woche NN %

Do not edit `README.md` (beyond what an idea's criteria require) or the memory. The user and
the main session take the results from there.
