# Docs index – read only what the task needs

| File | What | Read when | Key sections |
|---|---|---|---|
| `spec/00-kurzfassung.md` | Working state, all decisions D1–D17 in one table | Orientation, "is X decided?" | §2 rules 1–7, §3 D-table, §9 phase 5–7 key points |
| `spec/00-masterprompt.md` | Full spec, highest authority | Only for a spec question the summary doesn't answer | §3–3c decisions, Phase 5 (content), 6.2 stack, 6.3 ports, 6.4 storage/export, 6.7 UX, 6.8 repo tree |
| `spec/04a-zustandsautomat.md` | **Normative game rules**: architecture, policy layer, state model (TS), events, automata, rules R-…, edge cases RF-…, constants | Any core/logic ticket | §1 arch · §1a policy (D16) · §2 `GameState` · §3 events · §4 automata · §5 rules · §6 RF · §7 constants |
| `spec/04b-testfaelle.md` | 174 test cases + invariants = Vitest spec | Writing tests for a rule | §1–12 by rule family · §13 invariants P-… · §13a policy seam · §14 coverage matrix |
| `spec/04-spielregeln.md` | Rationale, pass simulation, risks | Only if the *why* of a rule matters | §1 overview · §2 simulation · §6 risks |
| `spec/04c-simulationsskript.md` | Docs for `scripts/plan/sim04.py`, `plan04.py` | Forecast/calibration tickets | – |
| `spec/00-quellen.md` | Verified exam facts with sources | Exam format/WOW facts | A A2 · B A1 · D WOW · G open gaps |
| `spec/prototyp-erkenntnisse.md` | TTS findings (Android), genus, prototype export format | TTS/`SpeechOutPort`, import of prototype progress | E-P1, E-P3 (v4 TTS pattern), §0 export format |
| `spec-gaps.md` | Open spec questions / repo-vs-spec deviations | Before starting a ticket that touches them | – |
| `DEPLOY.md` | Cloudflare hosting, one-time setup | Deploy/CI tickets | – |
| `tickets/README.md` | Ticket workflow | Once per session | – |
| `tickets/BACKLOG.md` | Ticket list + dependencies (written by `/backlog`) | Picking next ticket | – |

## Also in `spec/` (synced 16.11.2026)
`02a` Can-Do matrix · `02c-wortschatz-inventar.md` · `02d` grammar progression · `02f` WOW topics · `02g` task types + correction rules · `03-curriculum.md` (Q1–Q11, D10) · `03a` chapter spec · `03b` coverage · `03c-kapitel-wortschatz.tsv` (grep by chapter, never read whole) · `03d` · `03e` · `03f` · `03g` AT/DE varieties

## Not in the repo
`02b` Handlungsfelder · `02e` Redemittel/Textsorten · `02c` inventory `.tsv` · `01-ressourcen.md` · `geraetecheck.md` (not written yet)
