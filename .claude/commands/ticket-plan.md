---
description: Plan one ticket (planner agent) and create its branch
argument-hint: <ticket-id e.g. 007>
---

Ticket: $ARGUMENTS

Use the `planner` agent:
1. Check `docs/tickets/BACKLOG.md`: dependencies `done`, not `blocked`. Otherwise report and stop.
2. `git switch main && git pull --ff-only`, then `git switch -c t/$ARGUMENTS-<slug>`.
3. Write `docs/tickets/$ARGUMENTS-<slug>.md` from `TEMPLATE.md`.
4. Set status `planned` in BACKLOG.md. Commit `docs(ticket): plan $ARGUMENTS <slug>`.
5. Report: path + short summary + open gaps.
