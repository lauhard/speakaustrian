# Roadmap – order of implementation (D23)

Each step is one small PR that is live after merge. Tick when merged. Spec refs by ID.

## Done
- [x] 000 Prototype: content schema, grading (cloze per gap), device TTS, local profile, CI, Cloudflare deploy
- [x] 001 Course overview (39 chapters), chapter A1-01 with micro lessons 1–4, free practice (D22), listening tasks with transcript fallback
- [x] 002 Core state: `GameState` schema, events `PROFILE_CREATED`/`PENSUM_CHANGED`/`LESSON_COMPLETED`/`OVERRIDE_GRANTED`, `makeReducer(policy)`, `defaultPolicy` (R-F1, R-F3, R-L1/3, R-G2, R-PL2), storage v2 + migration, daily workload at sign-up, plan day
- [x] 003 Vocabulary cards + Leitner review (R-W2, R-W5, R-W6, R-W7), answer tolerances of `02g` §3.1, free practice „Wörter“, picture tasks in A1-01, content rule D24 as a test

## Next (in this order)
- [ ] 004 A1-01 complete: micro lessons 5–14 (remaining A1-01 words: er, sie, es, wir, ihr, mir, was, ja, nein, auch, vorstellen), error cards (R-W3), practice pool, test pool ≥ 60 with twins (needs `02g`, `03` Q1–Q11, `02a` Can-Do, WOW facts with sources)
- [ ] 005 Chapter flow: practice → readiness round 18/20 (R-G) → chapter test with lives (R-T, R-L) → correction round (R-K) → unlock next chapter (R-F)
- [ ] 006 Day view: plan day, streak, freeze, daily goal (R-E, R-S, R-D)
- [ ] 007 Export/import incl. old prototype format (`prototyp-erkenntnisse.md` §0)
- [ ] 008 Settings: daily workload, speech rate, voice, TTS diagnostics; device checklist Android/iOS
- [ ] 009 Further task types: matching, form filling, guided writing with lead points, speaking with recording (`02g`)
- [ ] 010 Chapters A1-02 … (two per batch), then milestone MS-A1 (R-M)

## Notes for the next steps
- Policy decision points not yet in `RulePolicy`: `testComposition`, `outcomeAfterTest`, `outcomeAfterCorrection`, `recoveryAfterFail`, `bonusForNext` (step 005), `examPassed`, `retakeUnlock`, `isExamReady` (step 010). Add each with its tests from `04b`.
- Ship with `scripts/ship.sh "title" "body"` (push → PR → checks → merge → deploy).
