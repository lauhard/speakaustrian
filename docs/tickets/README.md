# Ticket workflow (D17d)

Goal: small, testable steps; each session loads only one ticket's context.

## Files
- `BACKLOG.md` – one line per ticket: ID, title, size (S/M/L), depends-on, status. **Titles only, no plans.** Written/updated by `/backlog`.
- `TEMPLATE.md` – ticket template. Written by Claude Code on the first `/backlog` run (sections: see below), then reused.
- `NNN-slug.md` – one file per ticket, created by `/ticket-plan NNN`. Self-contained: everything an implementer needs, with spec references by ID (R-…, T-…, D…) instead of copied text.

## Required ticket sections (TEMPLATE.md must contain them)
Goal (1–2 sentences) · Spec refs (IDs + doc§) · Scope / out of scope · Files to touch · Design (types, function signatures, data flow – no full implementation) · Acceptance criteria (numbered, testable, each mapped to `04b` T-IDs where they exist) · Test plan (Vitest / Playwright / manual device checklist) · Open questions → `docs/spec-gaps.md` · Definition of done.

## Flow
1. `/backlog` – create or update `BACKLOG.md` from the spec (dependency order; first: tooling + spec gaps G-001–G-004).
2. `/ticket-plan NNN` – planner agent writes `NNN-slug.md`, creates branch `t/NNN-slug`. Status → `planned`.
3. `/ticket-test NNN` – tester agent writes failing tests from the acceptance criteria. Status → `tests`.
4. Andi implements manually. Status → `impl`.
5. `/ticket-done NNN` – run checks + tests, tick DoD, status → `done`, commit; Andi pushes.

## Status values
`todo` · `blocked (G-NNN)` · `planned` · `tests` · `impl` · `done`

## CI
Minimal CI (typecheck + vitest) is its own early ticket. Merge-request/deploy CI later, as its own ticket.
