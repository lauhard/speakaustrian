---
description: Write tests for a planned ticket (tester agent)
argument-hint: <ticket-id>
---

Ticket: $ARGUMENTS

Use the `tester` agent:
1. Ensure you are on branch `t/$ARGUMENTS-*`. Read `docs/tickets/$ARGUMENTS-*.md`.
2. Write tests per its test plan; run them; they must fail for the right reason.
3. Set status `tests` in BACKLOG.md. Commit `test: $ARGUMENTS <slug>`.
4. Report: files, test count, run summary.
