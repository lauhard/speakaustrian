---
description: Create or update docs/tickets/BACKLOG.md (titles + dependencies only) and TEMPLATE.md if missing
---

Use the `planner` agent.

1. If `docs/tickets/TEMPLATE.md` is missing: write it with the sections listed in `docs/tickets/README.md`.
2. Create/update `docs/tickets/BACKLOG.md` as a table: `ID | Title | Size | Depends on | Status`. IDs `001`, `002`, … stable forever (never renumber; append new ones).
3. Source: `docs/INDEX.md` → Masterprompt 6.2–6.8 and Phase 5 headings, `04a` §1–§7 headings, `docs/spec-gaps.md`. Read headings/sections only, not whole docs.
4. Order by dependency. Start with: tooling (vitest, zod, CI minimal), resolving G-001–G-004, core types (`GameState`, events), `makeReducer(policy)` skeleton + `defaultPolicy`, then rule families (R-F, R-T, R-G, R-L, R-K, …), ports/adapters, storage + export/import, TTS (`SpeechOutPort`, D17b), content schema, UI shell.
5. Mark tickets that depend on an open gap as `blocked (G-NNN)`.
6. No plans in the backlog. Report to Andi in German: number of tickets, first 5, blocked ones.

Arguments (optional): $ARGUMENTS – e.g. "add: …" to append tickets.
