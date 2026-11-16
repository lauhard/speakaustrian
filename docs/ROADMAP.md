# Roadmap – order of implementation (D23)

Each step is one small PR that is live after merge. Tick when merged. Spec refs by ID.

## Done
- [x] 000 Prototype: content schema, grading (cloze per gap), device TTS, local profile, CI, Cloudflare deploy
- [x] 001 Course overview (39 chapters), chapter A1-01 with micro lessons 1–4, free practice (D22), listening tasks with transcript fallback

## Next (in this order)
- [ ] 002 Core state: `GameState`, events, `makeReducer(policy)` + `defaultPolicy` skeleton (`04a` §1a–§3), storage v2 with migration from the current profile
- [ ] 003 Vocabulary cards + Leitner review queue (R-W, `04a` §5; genus rotation V4) for the A1-01 words – needs `03c` rows (ask Andi to sync `02c`/`03c` into `docs/spec/`)
- [ ] 004 A1-01 complete: micro lessons 5–14, practice pool, test pool ≥ 60 with twins (needs `02g`, `03` Q1–Q11, `02a` Can-Do, WOW facts with sources)
- [ ] 005 Chapter flow: practice → readiness round 18/20 (R-G) → chapter test with lives (R-T, R-L) → correction round (R-K) → unlock next chapter (R-F)
- [ ] 006 Day view: plan day, streak, freeze, daily goal (R-E, R-S, R-D)
- [ ] 007 Export/import incl. old prototype format (`prototyp-erkenntnisse.md` §0)
- [ ] 008 Settings: daily workload, speech rate, voice, TTS diagnostics; device checklist Android/iOS
- [ ] 009 Further task types: matching, form filling, guided writing with lead points, speaking with recording (`02g`)
- [ ] 010 Chapters A1-02 … (two per batch), then milestone MS-A1 (R-M)

## Blocked by missing docs in the repo
`02c`, `02g`, `03`, `03c`, `03g`, `02a`, `02f` live only in the Claude project. Reading them through the project tool costs many tokens per session; committing them once to `docs/spec/` makes steps 003, 004, 009, 010 cheap.
