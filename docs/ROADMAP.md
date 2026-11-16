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
- [ ] 004 A1-01 complete: remaining micro lessons (WOW topics A1-WOW-18/-01 with sourced facts, speaking pre-stages, form filling), error cards (R-W3), practice pool, test pool ≥ 60 with twins (needs `02g`, `03` Q1–Q11, `02a` Can-Do, WOW facts with sources)
- [x] 005a Chapter attempt automaton in the core (04a §4.2): events `PRACTICE_ANSWERED`, `GATE_ANSWERED`, `TARGETED_PRACTICE_DONE`, `TEST_STARTED`, `TEST_ANSWERED`, `CORRECTION_ANSWERED`, `ERROR_REVIEW_ANSWERED`; policy points `outcomeAfterTest`, `outcomeAfterCorrection`, `recoveryAfterFail`, `bonusForNext`; error cards (R-W3); `ContentInfo` seam (not wired into the app yet)
- [x] 005b Draws as pure functions with seed (`core/draw.ts`): `testComposition` + `drawTest` (R-T1, R-T2, R-T4), `drawGate` (R-G1); card promotion by the test (R-W4), answer streak (R-E1), override effects `SET_RECOVERY`/`GRANT_ATTEMPT` (T-PL04)
- [ ] 005c Chapter flow UI: practice → readiness round → test with lives → correction round → error review → next chapter; wire `ContentInfo` in `game.svelte.ts`; review page must show error cards; needs pools (004), until then on `DEMO` with a small config
- [ ] 006 Day view: plan day, streak, freeze, daily goal (R-E, R-S, R-D)
- [ ] 007 Export/import incl. old prototype format (`prototyp-erkenntnisse.md` §0)
- [ ] 008 Settings: daily workload, speech rate, voice, TTS diagnostics; device checklist Android/iOS
- [ ] 009 Further task types: matching, form filling, guided writing with lead points, speaking with recording (`02g`)
- [ ] 010 Chapters A1-02 … (two per batch), then milestone MS-A1 (R-M)

## Notes for the next steps
- Policy decision points not yet in `RulePolicy`: `examPassed`, `retakeUnlock`, `isExamReady` (step 010). Add each with its tests from `04b`.
- Not yet in the mechanics: mandatory speaking recording in the test (R-T7, with step 009), weekly-review guard on `TEST_STARTED` (R-W8, with the weekly review), R-K6 hint (UI, 005c).
- Ship with `scripts/ship.sh "title" "body"` (push → PR → checks → merge → deploy).
