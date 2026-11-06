---
description: Verify a ticket after manual implementation and close it
argument-hint: <ticket-id>
---

Ticket: $ARGUMENTS

1. Run `pnpm check` and `pnpm test` (plus `pnpm test:e2e` if the ticket has Playwright tests). Report only failures, compactly.
2. If anything fails: list failing test IDs + one-line cause each. Do **not** fix production code unless Andi asks. Stop.
3. If green: tick the ticket's DoD, set status `done` in BACKLOG.md, commit `chore(ticket): close $ARGUMENTS`.
4. Tell Andi it is ready to push (`git push -u origin HEAD`). Do not push yourself unless asked.
