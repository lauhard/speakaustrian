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

## Workflow (D23)
Claude implements. Small vertical steps from `docs/ROADMAP.md`: branch `t/NNN-slug` → code + tests → `pnpm check && pnpm test` (+ e2e for UI flows) → `scripts/ship.sh "title" "body"` (PR → CI green → squash-merge to `main`) → Cloudflare deploys to https://speakaustrian.lauhard.workers.dev. Update `docs/ROADMAP.md` in the same PR. Never push straight to `main`. Ticket files (`docs/tickets/`) only for steps that need a written plan.

## Commands
`pnpm install` · `pnpm dev` · `pnpm check` · `pnpm test` (Vitest, core) · `pnpm test:e2e` (Playwright; set `PW_CHROMIUM` to reuse an installed browser) · `pnpm build` · `pnpm deploy`.

## Architecture (as built)
`src/lib/core` pure logic (content schema, grading, `state.ts`, `policy.ts`, `reducer.ts`) · `src/lib/game.svelte.ts` composition root (clock, ids, storage → `dispatch`) · `src/lib/ports` interfaces · `src/lib/adapters/web` device TTS, localStorage · `src/lib/content` lesson JSON · `src/routes` UI · `messages/` UI strings (paraglide, de/en/tl). Hosting: Cloudflare Workers (D18), see `docs/DEPLOY.md`. Imports of own TS files use `#lib/….ts`.

## Content rules (D24, D25)
- Every chapter: gap-fill tasks and ≥ 2 picture tasks; **every lesson: ≥ 1 picture task** (Andi, 16.11.2026; A1-01 follows in content run 2). Tests in `src/lib/content/content.test.ts`.
- Pictures: SVG in `static/img/`, one flat style (see `a1-01-amt.svg`, `a1-01-nacht.svg`), an unambiguous scene that is needed for the answer and carries several details to ask about (people, name signs, clock, place). Render and look at every new picture before shipping. No decorative or ambiguous pictures.
- Only vocabulary of the chapter and earlier chapters (`grep -P "\tA1-01$" docs/spec/03c-kapitel-wortschatz.tsv`); situations go into the translated `instruction`.
- Content pipeline: one generator per chapter `scripts/content/a1-NN.py` on `scripts/content/lib.py` (lessons, pools, pictures; writes JSON + SVG, renders a contact sheet to `/tmp`). Chapter files are loaded by name, no code change. Batch = 2 chapters → `pnpm qa` → slim review agent (Sonnet, 20 %, blockers/should-fix, G-017) → ship. Local e2e only for UI changes.
- UI: use the component classes in `src/routes/layout.css` (`btn-primary`, `btn-secondary`, `card`, `card-link`, `option`, `field`, `feedback`, `chip`, `badge`, `bar`, `actionbar`) instead of long utility strings.
