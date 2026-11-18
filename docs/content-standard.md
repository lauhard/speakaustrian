# Content standard v2 („Speak Austrian“)

> Status: **draft for Andi's review** (18.11.2026) · pilot: `A1-03-L01` · applies to every chapter once approved.
> Why: Andi's review of A1-02 … A1-05 – pictures not unambiguous (Buch vs Heft), crude SVGs (country map),
> gap texts with too much room for interpretation, too little introduction, thin explanations.
> Precedence unchanged: `docs/spec/00-masterprompt.md` > `00-kurzfassung.md` > this file. Exam facts only from `00-quellen.md`.
> Vocabulary rule unchanged: only words of the chapter and earlier chapters (`03c`), Austrian German first (D10).

## 1. Lesson structure

Every lesson has four parts, in this order:

| Part | Field | Rule |
|---|---|---|
| **Intro** | `intro.situation` | 1–3 short sentences in plain German (+ en/tl): a real Austrian situation in which the topic is needed (Magistrat, Deutschkurs, Hausarzt, Billa …). Names and places stay the same across the chapter. |
| | `intro.goal` | One can-do sentence, „Am Ende kannst du …“ – concrete and checkable (not „Länder lernen“, but „sagen, woher du kommst, und andere danach fragen“). |
| **Learn cards** | `cards[]` | 3–6 cards. Each card teaches **one** thing. Kinds: `phrase` (a speakable model sentence), `rule` (headline = the rule in a few words, `note` = why, `examples` = 2–3 speakable sentences), `culture` (Austrian everyday knowledge, only with a source if it is a fact). Every rule that a task checks appears on a card first. |
| **Tasks** | `items[]` | **6–8 items**, progression from recognising to producing: picture/reading → listening → choice in context → gap text → speaking/writing. ≥ 1 picture task, ≥ 1 gap text, ≥ 2 skills. |
| **Solutions** | `explanation` | For every item: why the answer is right **and** why the typical wrong option is wrong (see §4). |

## 2. Task design

- **Situation in the instruction.** The instruction says *who, where, what* (translated): „Sie sind beim Magistrat. Die Beamtin fragt Sie.“ – not only „Wählen Sie die richtige Antwort.“ Exception: exam-format test items (only German, V5).
- **The German prompt carries the language.** Prompt = what is said or read in the situation. The translation never gives away the answer.
- **One correct answer, by construction.** Distractors are plausible learner errors (wrong preposition, wrong article, wrong person), not nonsense and not a second correct answer. Check each distractor: „Could a native speaker say this here?“ → if yes, replace it.
- **Context makes the answer unique.** Use names, pictures, previous sentence or a mini dialogue so that only one answer fits.
- **Listening:** the audio text is natural (Grüß Gott, Austrian names and places) and the transcript appears in the solution.
- **No trick questions,** no double negation, no answer that depends on a picture detail smaller than a name sign.

## 3. Gap texts (cloze) – no room for interpretation

A gap is acceptable only if **exactly one** word fits for a learner at this level. Use at least one of these tools:

| Tool | Field | When |
|---|---|---|
| **Word bank** | `bank` | Default for A1. Contains all correct words **plus 1–2 distractors** of the same word class. Tapping a word fills the next empty gap. |
| **Gap hint** | `gaps.N.hint` | For verb forms and articles: the base form or category in brackets, e.g. `(kommen)`, `(Artikel)`, `(Land)`. |
| **Mini dialogue** | text | The other line of the dialogue fixes the meaning: „– Woher kommen Sie? – Ich komme {{1}} Österreich.“ |

- `accept` lists **all** correct spellings (incl. Austrian/German variants if both are correct; capitalisation is graded by the grader).
- Never gap a word that the learner cannot derive from the cards or earlier lessons.
- Max. 3 gaps per item at A1, max. 1 gap per sentence.

## 4. Solutions (`explanation`)

Structure, 2–4 short sentences, plain German + en/tl:
1. **Answer + rule:** „Richtig: *aus den Philippinen*. Bei Ländern mit Artikel sagt man *aus der / aus den*.“
2. **Why the typical wrong option is wrong:** „*Ich wohne Philippinen* fehlt die Präposition – und *wohnen* sagt, wo du jetzt lebst, nicht woher du kommst.“
3. Optional **Austrian note** (D10) or a memory hook.

## 5. Pictures

Pictures are part of the task, so they follow the same rule as gap texts: **one unambiguous reading.**

- **Distinguish objects by shape, not by colour.** Buch = thick, hard cover, spine with title, standing or closed; Heft = thin, soft, lines on the cover page, spiral or staples. If two objects could still be confused, label them or don't ask for both.
- **Real shapes for real things.** Country outlines, flags, coins and traffic signs come from real data (country outlines: Natural Earth via `world-atlas`, projected with `d3-geo` – `scripts/content/geo.mjs`). Neighbouring countries in their true position; capitals at their true position.
- **Reference pictures (Andi, 18.11.2026: „level of detail und design passen“):** `a1-03-karte.svg`, `a1-03-oesterreich.svg` (real outlines, quiet neighbours, labels with a white halo) and `a1-05-sachen.svg`, `a1-05-tische.svg` (Buch with hard cover and page block vs. Heft with spiral binding). New pictures match their level of detail.
- **One flat style** (see `a1-01-amt.svg`): white background or a quiet floor colour, 2–3 accent colours, Archivo-like labels, no gradients, no clip art.
- **Every detail that a question asks for is visible at 360 px width** (phone): name signs ≥ 14 px, clocks with clear hands, numbers big.
- **`alt`** describes what is shown without giving away the answer.
- Render every new picture and look at it before shipping (contact sheet in `/tmp`).

## 6. Review checklist (per lesson, before `pnpm qa`)

- [ ] Intro: situation + can-do goal, en/tl present
- [ ] Every checked rule is on a card first
- [ ] 6–8 items, recognising → producing, ≥ 1 picture, ≥ 1 gap text
- [ ] Every instruction names the situation (except exam-format items)
- [ ] Each item: exactly one correct answer; distractors are plausible learner errors
- [ ] Each gap: word bank or hint or dialogue; `accept` complete
- [ ] Each solution: rule + why the wrong option is wrong
- [ ] Pictures: unambiguous, real shapes, readable at 360 px, rendered and looked at
- [ ] Vocabulary only from this and earlier chapters; AT form first, DE form marked
