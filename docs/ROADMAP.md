# Roadmap – order of implementation (D23)

Each step is one small PR that is live after merge. Tick when merged. Spec refs by ID.

## Done
- [x] 000 Prototype: content schema, grading (cloze per gap), device TTS, local profile, CI, Cloudflare deploy
- [x] 001 Course overview (39 chapters), chapter A1-01 with micro lessons 1–4, free practice (D22), listening tasks with transcript fallback
- [x] 002 Core state: `GameState` schema, events `PROFILE_CREATED`/`PENSUM_CHANGED`/`LESSON_COMPLETED`/`OVERRIDE_GRANTED`, `makeReducer(policy)`, `defaultPolicy` (R-F1, R-F3, R-L1/3, R-G2, R-PL2), storage v2 + migration, daily workload at sign-up, plan day
- [x] 003 Vocabulary cards + Leitner review (R-W2, R-W5, R-W6, R-W7), answer tolerances of `02g` §3.1, free practice „Wörter“, picture tasks in A1-01, content rule D24 as a test
- [x] 004a UI/UX: design system (bundled font, tokens, component classes), home with smart continue, sticky action bar, result ring; free practice covers all chapters (D25); richer pictures for A1-01

## Next (in this order)
- [x] 004b A1-01 micro lessons 5–7: all 44 active A1-01 words now have a lesson and a card
- [ ] 004 A1-01 complete, split into three steps (not the finished UI/lesson steps 004a/004b above):
  - [x] 004a QA script for content pools: `pnpm qa` (`docs/QA.md`), pools file `<chapter>-pools.json` merged by `content/index.ts`, ≥ 2 twins for real chapters as content test, runs in CI; gaps G-009–G-011
  - [ ] 004b A1-01 pools in batches (Sonnet): remaining micro lessons (WOW topics A1-WOW-18/-01 with sourced facts, speaking pre-stages, form filling), practice pool, test pool with twins into `a1-01-pools.json`; done = `pnpm qa A1-01 --require-pools` without errors, warnings looked at (needs `02g`, `03` Q1–Q11, `02a` Can-Do, WOW facts with sources; G-009 decided first)
  - [ ] 004c Sample review of the A1-01 pools by a strong model in a fresh chat (≥ 20 % of the items), then Andi's approval
- [x] 005a Chapter attempt automaton in the core (04a §4.2): events `PRACTICE_ANSWERED`, `GATE_ANSWERED`, `TARGETED_PRACTICE_DONE`, `TEST_STARTED`, `TEST_ANSWERED`, `CORRECTION_ANSWERED`, `ERROR_REVIEW_ANSWERED`; policy points `outcomeAfterTest`, `outcomeAfterCorrection`, `recoveryAfterFail`, `bonusForNext`; error cards (R-W3); `ContentInfo` seam (not wired into the app yet)
- [x] 005b Draws as pure functions with seed (`core/draw.ts`): `testComposition` + `drawTest` (R-T1, R-T2, R-T4), `drawGate` (R-G1); card promotion by the test (R-W4), answer streak (R-E1), override effects `SET_RECOVERY`/`GRANT_ATTEMPT` (T-PL04)
- [x] 005c-1 DEMO sandbox + wiring: `ContentInfo` wired into the stores, `pools` (practice/test, `family`/`goals`/`refs`) in the content schema, DEMO pool (9 practice, 12 test items with twins), `demoConfig` (3 items per test/gate, 2 lives), own `demo` store (`storeFor(id)`), pure helpers in `core/flow.ts` (gate/test draws, targeted practice), loop test on the real pool
- [x] 005c-2 Chapter flow UI on DEMO: `ChapterFlow` (practice → readiness round → targeted practice → test with lives → correction round → error review → passed/restart), exam-mode instructions (German, translation on demand, V5), R-K6 hint from the 2nd failed attempt (names goals with most error cards; the question chat is only mentioned, it does not exist yet), review page shows error cards as tasks (`/review?store=demo` for the sandbox), e2e of all paths. Real chapters join as soon as 004 delivers their pools (then `storeFor` runs them in the course state).
- [ ] 006 Day view: plan day, streak, freeze, daily goal (R-E, R-S, R-D)
- [ ] 007 Export/import incl. old prototype format (`prototyp-erkenntnisse.md` §0)
- [ ] 008 Settings: daily workload, speech rate, voice, TTS diagnostics; device checklist Android/iOS
- [ ] 009 Further task types: matching, form filling, guided writing with lead points, speaking with recording (`02g`)
- [ ] 010 Chapters A1-02 … (two per batch), then milestone MS-A1 (R-M)

## Notes for the next steps
- Policy decision points not yet in `RulePolicy`: `examPassed`, `retakeUnlock`, `isExamReady` (step 010). Add each with its tests from `04b`.
- Not yet in the mechanics: mandatory speaking recording in the test (R-T7, with step 009), weekly-review guard on `TEST_STARTED` (R-W8, with the weekly review).
- Ship with `scripts/ship.sh "title" "body"` (push → PR → checks → merge → deploy).
