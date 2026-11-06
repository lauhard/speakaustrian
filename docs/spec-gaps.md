# Spec gaps & repo deviations

Agents append here instead of inventing. Andi takes open entries to the Claude project chat; the answer is written back (decision ID) and the spec doc updated.

Format:
```
## G-NNN – short title            (status: open | decided D.. | obsolete)
- Found in: ticket / file
- Spec says: … (doc + section/ID)
- Problem: …
- Options: A … / B …
- Blocks: ticket(s)
```

---

## G-001 – Adapter: `adapter-cloudflare` vs. static build   (status: open)
- Found in: repo setup (`package.json`, `wrangler.jsonc`)
- Spec says: Masterprompt 6.1/6.2 – stage 1 = Claude Artifact (static, single page), stage 2 optional Cloudflare; stack `adapter-static`.
- Problem: repo uses `@sveltejs/adapter-cloudflare` + wrangler. An Artifact needs a static bundle without server routes.
- Options: A switch to `adapter-static` now, Cloudflare Pages serves static later · B keep cloudflare, add a separate static build target for the Artifact · C drop Artifact stage, go straight to own web app.
- Blocks: build/CI ticket, any server route.

## G-002 – Storage: drizzle/D1 vs. local-only progress   (status: open)
- Found in: `drizzle.config.ts`, `src/lib/server/db`
- Spec says: progress **only local** + JSON export/import, no login (Kurzfassung §1, Masterprompt 6.4, `StoragePort`).
- Problem: DB scaffolding implies server-side persistence.
- Options: A remove drizzle/db · B keep unused for possible stage 2 (content hosting, feedback endpoint) but no progress data server-side.
- Blocks: storage ticket.

## G-003 – i18n: paraglide vs. `{de,en,tl}` content fields   (status: open)
- Found in: `project.inlang`, `messages/`
- Spec says: every instruction/vocab/explanation/feedback carries `{de,en,tl}` in content JSON; exam mode German only (Masterprompt 5.x, Kurzfassung §1).
- Problem: paraglide is fine for **UI strings**; content translations must stay in content JSON. Needs an explicit split, plus `tl` locale in paraglide.
- Options: A paraglide for UI only (de/en/tl), content via JSON fields · B no paraglide, UI strings also in JSON.
- Blocks: UI shell ticket.

## G-004 – Test & validation tooling missing   (status: open, low risk)
- Found in: `package.json`
- Spec says: Vitest (logic, `04b`), Playwright (flows), `zod` schemas (Masterprompt 6.2).
- Problem: vitest and zod not installed; Playwright present.
- Options: add in the first ticket (tooling) – no decision needed unless Andi prefers other libs.
- Blocks: all test tickets.

## G-005 – Audio: device TTS only vs. exam listening texts   (status: open, accepted risk R6)
- Found in: D17b vs. D13, `prototyp-erkenntnisse.md` E-P1/E-P3
- Spec says: D17b device TTS only (hardened); E-P3 recommends pre-produced audio for listening.
- Problem: exam-format listening (multi-speaker, tempo) with device TTS is unproven.
- Options: re-evaluate after device check (`geraetecheck.md`) and before the first listening content batch.
- Blocks: listening content batch (not app tickets).
