# 037 – Proofread all texts (A1-01 … A1-03; A1-04/05 after batch 2)

Andi, 18.11.2026: „Die Beschreibungen und Erklärungen müssen fehlerfrei sein. Englische Beschreibung ergibt wenig Sinn.“
Example he marked wrong (A1-02 card „E = e, I = i“, en): “German E sounds like ‘e’ in ‘sehr’ – not like English ‘ee’. German I sounds like ‘i’ in ‘Sie’ – not like English ‘eye’.” – mixes letter names and sounds; the reader cannot follow it.

## Scope per chapter (one agent per chapter)
Every learner-facing text, **all of them, not a sample**: lesson `title`, `intro.situation`/`goal`, card `phrase`/`note`/`examples`, item `instruction`, `prompt`/`text`/options, `explanation`, image `alt`, chapter title. Languages de, en, tl.

## Rules
- **German:** correct spelling, grammar, punctuation (Austrian standard, D10: AT form first, German-German form marked „in Deutschland: …“). Simple, but never wrong. Learner-level vocabulary rule stays (only words of this and earlier chapters in task texts).
- **English:** natural, correct, and it must make sense to an English speaker who is learning German. Do not translate word by word; say the same thing clearly. Pronunciation: describe the **sound** with a clear English comparison (“like ‘eh’ in ‘bed’”, “like ‘ee’ in ‘see’”), and keep **letter names** apart from sounds („The letter E is called ‘eh’ – the English letter E is called ‘ee’“). Every claim must be true.
- **Tagalog:** simple, correct, Taglish allowed; same meaning as en.
- **Consistency:** the same thing is said the same way across de/en/tl (no extra or missing facts in one language); the solution matches the actual correct option; quoted words match the item.
- Do not change answers, ids, options' correctness, vocabulary, pictures or structure – only wording (fix a factual error if you find one and report it).

## Method (token-efficient)
1. Dump the chapter's texts with a small `python3 -c` script (one line per text: id, field, de | en | tl) – don't open the whole JSON in the editor.
2. Fix in the generator (`scripts/content/a1-02/gen_a102_lessons.py`, `scripts/content/a1-03/gen_a103_lessons.py`); A1-01 has no generator → patch `src/lib/content/a1-01.json` with a small Python script (keep formatting: `json.dump(..., ensure_ascii=False, indent='\t')` as the file uses – check first).
3. Regenerate, `pnpm qa` (0 errors), `pnpm test`.
4. Report: number of texts checked, number changed, the 10 most important fixes (before → after), anything unclear. Don't commit.
