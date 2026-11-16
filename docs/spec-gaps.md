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

## G-001 – Adapter: `adapter-cloudflare` vs. static build   (status: decided D18 – Cloudflare Workers, no Artifact delivery)
- Found in: repo setup (`package.json`, `wrangler.jsonc`)
- Spec says: Masterprompt 6.1/6.2 – stage 1 = Claude Artifact (static, single page), stage 2 optional Cloudflare; stack `adapter-static`.
- Problem: repo uses `@sveltejs/adapter-cloudflare` + wrangler. An Artifact needs a static bundle without server routes.
- Options: A switch to `adapter-static` now, Cloudflare Pages serves static later · B keep cloudflare, add a separate static build target for the Artifact · C drop Artifact stage, go straight to own web app.
- Blocks: build/CI ticket, any server route.

## G-002 – Storage: drizzle/D1 vs. local-only progress   (status: decided D19 – drizzle removed, progress local only)
- Found in: `drizzle.config.ts`, `src/lib/server/db`
- Spec says: progress **only local** + JSON export/import, no login (Kurzfassung §1, Masterprompt 6.4, `StoragePort`).
- Problem: DB scaffolding implies server-side persistence.
- Options: A remove drizzle/db · B keep unused for possible stage 2 (content hosting, feedback endpoint) but no progress data server-side.
- Blocks: storage ticket.

## G-003 – i18n: paraglide vs. `{de,en,tl}` content fields   (status: decided D20 – option A)
- Found in: `project.inlang`, `messages/`
- Spec says: every instruction/vocab/explanation/feedback carries `{de,en,tl}` in content JSON; exam mode German only (Masterprompt 5.x, Kurzfassung §1).
- Problem: paraglide is fine for **UI strings**; content translations must stay in content JSON. Needs an explicit split, plus `tl` locale in paraglide.
- Options: A paraglide for UI only (de/en/tl), content via JSON fields · B no paraglide, UI strings also in JSON.
- Blocks: UI shell ticket.

## G-004 – Test & validation tooling missing   (status: done – vitest, zod, CI in place)
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

## G-006 – Near misses in typed answers (case, ae/oe/ue/ss, trailing punctuation)   (status: open)
- Found in: prototype `src/lib/core/grading.ts` (`Verdict = correct | near | wrong`, `passes(verdict, {nearCounts})`)
- Spec says: `04a` defines errors per task (I-1) but not how typed answers are compared.
- Problem: does "sommer" for "Sommer" or "heisse" for "heiße" cost a life in the chapter test?
- Options: A near counts everywhere, with a spelling hint (prototype default in practice) · B near counts in practice, is an error in chapter test/simulation · C noun capitalisation is always an error (it is graded in the exam's writing part), umlaut transliteration is tolerated.
- Blocks: chapter-test ticket (R-T), content authoring of `accept` lists.

## G-007 – AI help and writing feedback without the Artifact viewer   (status: open)
- Found in: D18 (no Artifact delivery)
- Spec says: decision 5 and masterprompt 6.3 – stage 1 used "Claude in the viewer"; stage 2 an own endpoint.
- Problem: with Cloudflare hosting the viewer route is gone. Remaining: copy-prompt + offline help (free), or an own endpoint (Workers AI or an API key → cost, abuse limits).
- Options: A copy-prompt + offline help only for now · B add a rate-limited Worker endpoint later.
- Blocks: TutorPort/FeedbackPort tickets.

## G-008 – Picture tasks: scope and image production   (status: partly decided D21)
- Decided: any item type may carry an optional picture; pictures are static, reviewed assets made at authoring time (no runtime generation).
- Open: which exam parts picture tasks train (check `00-quellen.md` A/B for picture-based speaking/writing parts), how many per chapter, style guide for the pictures, free-text picture description (needs G-007).
- Blocks: content schema ticket, first content batch.
