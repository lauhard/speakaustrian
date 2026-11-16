import { z } from 'zod';

// Every learner-facing help text exists in simple German, English and Tagalog.
export const Localized = z.object({
	de: z.string().min(1),
	en: z.string().min(1),
	tl: z.string().min(1)
});
export type Localized = z.infer<typeof Localized>;

// Disciplines as in docs/spec/04a §2.
export const Discipline = z.enum(['lesen', 'hoeren', 'schreiben', 'sprechen', 'grammatikWortschatz', 'werte']);
export type Discipline = z.infer<typeof Discipline>;

const ItemBase = z.object({
	id: z.string().regex(/^[A-Z0-9-]+$/),
	skill: Discipline,
	instruction: Localized,
	explanation: Localized,
	// Optional picture stimulus. `alt` must not give the answer away.
	image: z.object({ src: z.string().min(1), alt: Localized }).optional(),
	// German text read aloud by the speech port (never the answer of the item).
	audioText: z.string().min(1).optional(),
	// Listening task: the text is only heard, not shown (transcript appears in the feedback).
	audioOnly: z.boolean().optional(),
	// Twin family (R-K1): id of the base item this item is a twin of. Items without it are their own family.
	family: z.string().regex(/^[A-Z0-9-]+$/).optional(),
	// Learning goals the item trains (R-G2 targeted practice, R-T2 draw) and vocabulary ids it tests (R-W4).
	goals: z.array(z.string().min(1)).optional(),
	refs: z.array(z.string().regex(/^W-A[12]-\d{4}$/)).optional()
});

export const ChoiceItem = ItemBase.extend({
	type: z.literal('choice'),
	prompt: z.string().min(1).optional(),
	options: z.array(z.string().min(1)).min(2),
	answer: z.number().int().nonnegative()
}).refine((i) => i.answer < i.options.length, { message: 'answer index out of range' });

// Gap markers in `text` look like {{1}}, {{2}} … and must match the keys of `gaps`.
export const ClozeItem = ItemBase.extend({
	type: z.literal('cloze'),
	text: z.string().min(1),
	gaps: z.record(z.string(), z.object({ accept: z.array(z.string().min(1)).min(1) }))
}).refine(
	(i) => {
		const inText = [...i.text.matchAll(/\{\{(\w+)\}\}/g)].map((m) => m[1]).sort();
		const declared = Object.keys(i.gaps).sort();
		return inText.length > 0 && JSON.stringify(inText) === JSON.stringify(declared);
	},
	{ message: 'gap markers in text and keys of gaps must match' }
);

export const ShortItem = ItemBase.extend({
	type: z.literal('short'),
	prompt: z.string().min(1),
	accept: z.array(z.string().min(1)).min(1)
});

export const Item = z.union([ChoiceItem, ClozeItem, ShortItem]);
export type Item = z.infer<typeof Item>;
export type ChoiceItem = z.infer<typeof ChoiceItem>;
export type ClozeItem = z.infer<typeof ClozeItem>;
export type ShortItem = z.infer<typeof ShortItem>;

// One teaching card of a micro lesson: a German phrase to hear and a short note on its use.
export const Card = z.object({ phrase: z.string().min(1), note: Localized });
export type Card = z.infer<typeof Card>;

// Vocabulary entry; `id` is the stable inventory id (02c/03c). Nouns with one article get a genus card.
export const Vocab = z.object({
	id: z.string().regex(/^W-A[12]-\d{4}$/),
	lemma: z.string().min(1),
	article: z.enum(['der', 'die', 'das']).optional(),
	en: z.string().min(1),
	tl: z.string().min(1)
});
export type Vocab = z.infer<typeof Vocab>;

export const Lesson = z.object({
	id: z.string().min(1),
	title: Localized,
	// Vocabulary ids introduced by this lesson (review cards are created when it is finished, R-W2).
	introduces: z.array(z.string()).optional(),
	cards: z.array(Card).optional(),
	items: z.array(Item).min(1)
});
export type Lesson = z.infer<typeof Lesson>;

export const ChapterContent = z
	.object({
		schemaVersion: z.literal(1),
		chapterId: z.string().min(1),
		// Tagalog texts are machine-made until a native speaker reviewed them (E2).
		tlReviewStatus: z.enum(['machine', 'reviewed']),
		vocab: z.array(Vocab).optional(),
		lessons: z.array(Lesson).min(1),
		// Practice pool (incl. the readiness round, R-G1) and test pool (R-T2). Without pools the chapter stays in its lessons.
		pools: z.object({ practice: z.array(Item).min(1), test: z.array(Item).min(1) }).optional()
	})
	.superRefine((c, ctx) => {
		const items = [...c.lessons.flatMap((l) => l.items), ...(c.pools?.practice ?? []), ...(c.pools?.test ?? [])];
		if (new Set(items.map((i) => i.id)).size !== items.length) ctx.addIssue({ code: 'custom', message: 'item ids must be unique' });
		if (new Set(c.lessons.map((l) => l.id)).size !== c.lessons.length) ctx.addIssue({ code: 'custom', message: 'lesson ids must be unique' });
		const vocabIds = new Set((c.vocab ?? []).map((v) => v.id));
		for (const l of c.lessons) {
			for (const ref of l.introduces ?? []) {
				if (!vocabIds.has(ref)) ctx.addIssue({ code: 'custom', message: `${l.id}: unknown vocabulary id ${ref}` });
			}
		}
		for (const kind of ['practice', 'test'] as const) {
			const pool = c.pools?.[kind] ?? [];
			const ids = new Set(pool.map((i) => i.id));
			for (const i of pool) {
				if (!i.goals?.length) ctx.addIssue({ code: 'custom', message: `${i.id}: pool items need goals` });
				if (i.family && (!ids.has(i.family) || pool.find((p) => p.id === i.family)?.family)) {
					ctx.addIssue({ code: 'custom', message: `${i.id}: family must be the id of a base item of the same pool` });
				}
			}
		}
		// Masterprompt: every test item has at least one twin (the QA target for real chapters is 2, R-K3).
		const test = c.pools?.test ?? [];
		for (const i of test) {
			if (test.filter((t) => (t.family ?? t.id) === (i.family ?? i.id)).length < 2) ctx.addIssue({ code: 'custom', message: `${i.id}: test item without a twin` });
		}
		for (const i of items) {
			if (i.audioOnly && !i.audioText) ctx.addIssue({ code: 'custom', message: `${i.id}: audioOnly needs audioText` });
		}
	});
export type ChapterContent = z.infer<typeof ChapterContent>;

export const Course = z.object({
	schemaVersion: z.literal(1),
	tlReviewStatus: z.enum(['machine', 'reviewed']),
	chapters: z
		.array(
			z.object({
				id: z.string().regex(/^A[12]-\d{2}$/),
				title: Localized,
				// Focus of the chapter test (03a); 'pruefung' = exam training chapter.
				focus: z.union([Discipline, z.literal('pruefung')])
			})
		)
		.min(1)
});
export type Course = z.infer<typeof Course>;
