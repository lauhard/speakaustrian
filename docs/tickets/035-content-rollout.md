# 035 – Content standard v2 rollout: lessons (batch 1: A1-02, A1-03 ✅ · batch 2: A1-04, A1-05)

**Context = this file + `docs/content-standard.md` (read it whole, it is short) + the pilot.** Do not read other spec docs, do not read whole `src/lib/content/*.json` (grep / `python3 -c` with filters only).

## Template (approved by Andi, 18.11.2026)
- Pilot lesson: `# L01` block in `scripts/content/a1-03/gen_a103_lessons.py` (batch 1 result for more examples: `scripts/content/a1-02/gen_a102_lessons.py`, incl. its standard asserts in `lesson()`) – copy its shape exactly:
  `intro=INTRO(L(situation…), L(goal…))`, cards with `PHRASE` / `RULE(…, examples=[…])` / `CULTURE`, 6–8 items, each with a situation instruction (`L(de short, en/tl full)`), cloze with `bank=[correct…, 1–2 distractors]` (or `hints=[…]`), explanations = rule + why the typical wrong option is wrong.
- Reference pictures: `static/img/a1-03-karte.svg`, `a1-03-oesterreich.svg`, `a1-05-sachen.svg`, `a1-05-tische.svg` (code in `gen_a103_pics.py`, `a1-05.py` – `geo_map`, `halo`, `BOOK`, `HEFT`). New or redrawn pictures match this level of detail.

## Task per chapter (one agent per chapter)
1. Rewrite **every lesson** of the chapter in its lessons generator to the standard (A1-03: L02–L13, L01 is done).
   - Keep: lesson ids and order, titles, `introduces`, goal ids (`G1`…), vocab, pools (`*_pools.py` untouched), picture file names already used by pools (redraw in place, keep facts the pools rely on).
   - German text (prompts, options, cloze text, bank, audio, card phrases/examples, `intro.situation.de`) uses **only vocabulary of this and earlier chapters** + proper names (Anna, Jose, Tom, Lukas, Maria, Wien, Graz, Billa …). Check with `grep -P "\tA1-0N$" docs/spec/03c-kapitel-wortschatz.tsv` and the `vocab` lemmas of earlier chapters. `note` texts may use simple metalanguage (Artikel, Verb, Plural).
   - Austrian German first (Jänner, Paradeiser, Grüß Gott …); a German-German form is always marked („in Deutschland: …“).
   - en: natural; tl: simple, Taglish allowed.
2. Pictures: for every picture a lesson uses, ask: unambiguous? needed for the answer? details readable at 360 px? If not → redraw (same file name) to reference level. Render all pictures of the chapter (`rsvg-convert -w 400 static/img/a1-0N-*.svg`) into one contact sheet in `/tmp` and look at it before finishing.
3. Run the generator(s), then `pnpm qa` (0 errors; no new warnings) and `pnpm test`.
4. Report (short): lessons rewritten, items per lesson, pictures redrawn + why, vocabulary doubts, anything you could not solve. **Do not commit, do not touch app code, schema, other chapters or `docs/`.**

## Done when
- [ ] every lesson: intro, 3–6 cards (rule card for every checked rule), 6–8 items, ≥ 1 picture, ≥ 1 cloze with bank/hint, all instructions with situation, all explanations with rule + wrong-option reason
- [ ] pictures of the chapter checked on a contact sheet; ambiguous ones redrawn
- [ ] `pnpm qa` 0 errors, `pnpm test` green
- [ ] Opus spot check (≥ 20 % of items, fresh eyes) → fixes → ship (one PR per batch)
