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

## G-006 – Near misses in typed answers (case, ae/oe/ue/ss, trailing punctuation)   (status: decided – Andi, 16.11.2026: “near” also counts as right in the chapter test, `02g` §3.1; tolerances T0–T4 in `core/tolerance.ts`, with spelling hint)
- Found in: prototype `src/lib/core/grading.ts` (`Verdict = correct | near | wrong`, `passes(verdict, {nearCounts})`)
- Spec says: `04a` defines errors per task (I-1) but not how typed answers are compared.
- Problem: does "sommer" for "Sommer" or "heisse" for "heiße" cost a life in the chapter test?
- Options: A near counts everywhere, with a spelling hint (prototype default in practice) · B near counts in practice, is an error in chapter test/simulation · C noun capitalisation is always an error (it is graded in the exam's writing part), umlaut transliteration is tolerated.
- Blocks: chapter-test ticket (R-T), content authoring of `accept` lists.
- Note 16.11.: masterprompt Phase 2 says `02g` defines tolerances per task type (case per learning goal, ae/oe/ue/ss, typo distance). `02g` is not in the repo yet → sync it, then close this gap from `02g`.

## G-007 – AI help and writing feedback without the Artifact viewer   (status: open)
- Found in: D18 (no Artifact delivery)
- Spec says: decision 5 and masterprompt 6.3 – stage 1 used "Claude in the viewer"; stage 2 an own endpoint.
- Problem: with Cloudflare hosting the viewer route is gone. Remaining: copy-prompt + offline help (free), or an own endpoint (Workers AI or an API key → cost, abuse limits).
- Options: A copy-prompt + offline help only for now · B add a rate-limited Worker endpoint later.
- Blocks: TutorPort/FeedbackPort tickets.

## G-008 – Picture tasks: scope and image production   (status: decided D21 + D24 + D25 – free picture description is not needed)
- Decided: any item type may carry an optional picture; pictures are static, reviewed assets made at authoring time (no runtime generation).
- Note 16.11.: `03a` names picture topics (Q05) for A2 speaking: bank, mobile shop, market, parents' evening, German course (A2-10, A2-11, A2-13, A2-14).
- Open: which exam parts picture tasks train (check `00-quellen.md` A/B for picture-based speaking/writing parts), how many per chapter, style guide for the pictures, free-text picture description (needs G-007).
- Blocks: content schema ticket, first content batch.

## G-008 – Small additions to the 04a type sketch for the chapter attempt   (status: decided 16.11.2026 – Andi: keep as implemented; error review does not move the error card)
- Found in: step 005a (`core/state.ts`, `core/policy.ts`)
- Spec says: `04a` §1a `outcomeAfterTest(run): 'PASSED' | 'CORRECTION' | 'FAILED'`, `outcomeAfterCorrection(run)`, `bonusForNext(s, run)`; §2 `GATE { block, items, correct, answered }`, `TARGETED_PRACTICE { goalIds, done }`.
- Problem: (1) R-PL1 forbids `if (lives === 0)` in the core, but the sketch has no result for "test goes on". (2) The goals for targeted practice (R-G2) need the wrong gate items, which the sketch does not keep. (3) The next gate block number is lost in `TARGETED_PRACTICE`. (4) The policy cannot see from the run whether the last twin was right or whether the pass was a perfect first attempt.
- Implemented: (1) extra result `'CONTINUE'`, policy asked after every test answer · (2) `GATE.wrong: string[]` · (3) `TARGETED_PRACTICE.block` · (4) extra parameters `outcomeAfterCorrection(run, allCorrect)`, `bonusForNext(s, run, perfectFirst)`. No rule changed; both new fields have schema defaults.
- Also open: does a right answer in the error review (R-K4) move the Leitner box of the error card? Implemented: no (card stays in box 1, due tomorrow).
- Blocks: nothing.

## G-009 – Does “test pool ≥ 60” count twins?   (status: open)
- Found in: 004a QA script (`src/lib/core/qa/checks.ts`, `pool.size`, `pool.twins`, `pool.quota`)
- Spec says: `03` Q6 / `04a` POOL_MIN: pool ≥ 60 items and ≥ 2.5 × test; R-K3: test items ≥ 2 twins; R-T2: never two twins in one test; R-T4: a new attempt prefers unseen items.
- Problem: 60 items with 2 twins each are only 20 families = exactly one test of 20. A second attempt can only show twins of the same 20 tasks, and a correction round uses them up as well.
- Options: A 60 counts items incl. twins (QA today: ≥ 60 items, family ≥ 3, quota reachable with families) · B 60 counts families (≥ 180 items) · C in between; recommendation for A1-01: about 30 families / ≈ 90 items.
- Blocks: 004b (size of the A1-01 test pool). Decision in the project chat.

## G-010 – Size of the practice part   (status: open)
- Found in: 004a QA script (`practice.size`, `practice.gate`)
- Spec says: masterprompt Phase 5 no. 2: practice pool for the practice part (“≈ 40”) and several readiness blocks of 20; no. 11: practice part + ≥ 2 readiness blocks without overlap with the test pool. R-G1: readiness round = last block of the practice part, drawn from the practice pool.
- Problem: “≈ 40” is no hard number, and the spec does not say whether the practice part and the readiness blocks may share items. The app walks the whole practice pool as practice part and then draws the blocks from the same pool.
- Implemented: error if a discipline has fewer than 2 × quota practice items (2 blocks without repeats, R-G1); only a warning below 40 + 2 × 20 = 80 items.
- Options: A 80 is a hard minimum, practice part = 40 fixed items, blocks from the rest · B as implemented (blocks may reuse practice-part items) · C other number.
- Blocks: nothing (004b can aim at ≥ 80).

## G-011 – Measuring “≥ 20 % recycling”   (status: open)
- Found in: 004a QA script (`recycling`)
- Spec says: `03` Q8: ≥ 20 % of the practice items recycle earlier chapters, “QA über `learningGoalIds` und Wortschatz-Index”.
- Problem: A1-01 has no earlier chapter, and the spec does not say whether earlier lessons of the same chapter count. Item goals are chapter-local ids so far.
- Implemented: a practice item counts as recycled if a `refs` id belongs to an earlier chapter in `03c` or a goal id is a goal of an earlier chapter; first chapter: not measured (info).
- Options: A as implemented, A1-01 exempt · B in A1-01 earlier lessons count (needs lesson ids on pool items) · C measure by the words in the text instead of `refs`.
- Blocks: nothing for A1-01; settle before 010 (A1-02).
