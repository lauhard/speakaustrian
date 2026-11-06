# CLAUDE.md – speakaustrian („Weg zur A2“)

Learning game for the Austrian ÖIF integration exam A2 (A1 → A2). Spec is ~80 % done and lives in `docs/spec/`. Svelte/SvelteKit tooling notes: `AGENTS.md`.

## Language
- Talk to Andi in **German** (du, direct, technical terms in English). Code, comments, commit messages: **English**.
- Functional patterns. Game logic = pure functions (`makeReducer(policy)` → `reducer(state, event)`), time only from events.

## Token efficiency (mandatory)
1. **Never scan the repo or read whole spec docs.** Start at `docs/INDEX.md`, then read only the section you need (`Read` with offset/limit).
2. **Find spec items by ID with Grep:** rules `R-…` / `RF-…` (`04a`), tests `T-…` / `P-…` (`04b`), decisions `D…`, sources `Q…`. Example: `Grep "R-L[0-9]" docs/spec/04a-zustandsautomat.md`.
3. **Never read large data files whole** (`*.tsv`, `content/**/*.json`): grep by ID or use `head`/`cut`.
4. Don't re-read a file you already have in context. Don't re-read after Edit/Write.
5. Svelte MCP (`AGENTS.md`): only when actually writing Svelte code, and fetch **only** the sections needed – not "list everything first".
6. Outputs short: result, open points, next step. No recaps, no restating the spec.
7. One ticket per session/branch. Ticket file = single source of context for that work.

## Spec authority
- Precedence: `docs/spec/00-masterprompt.md` > `00-kurzfassung.md` > phase docs. Rules: `04a`. Tests: `04b`.
- **Agents never invent rules, numbers or exam facts.** If the spec is silent, ambiguous or contradicts the repo: append an entry to `docs/spec-gaps.md` (format inside) and **stop** that part. Gaps are resolved in the Claude project chat (architecture/design/spec only), then synced back into `docs/spec/`.
- Exam facts only from `00-quellen.md`. Austrian German (D10) is the main form; German-German forms always marked.

## Workflow (D17)
`docs/tickets/README.md` – backlog → plan one ticket → branch `t/NNN-slug` → tests from acceptance criteria → Andi implements manually → tests green → push.
Commands: `/backlog`, `/ticket-plan NNN`, `/ticket-test NNN`, `/ticket-done NNN`. Agents: `planner`, `tester` (`.claude/agents/`).
**Do not write production code in `src/` unless Andi explicitly asks** – he implements. Tests, ticket docs, configs on request are fine.

## Commands
`pnpm install` · `pnpm dev` · `pnpm check` · `pnpm test` · `pnpm test:e2e` (vitest not yet installed → see ticket backlog / `docs/spec-gaps.md`).
