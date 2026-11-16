import { z } from 'zod';

// Every learner-facing help text exists in simple German, English and Tagalog.
export const Localized = z.object({
	de: z.string().min(1),
	en: z.string().min(1),
	tl: z.string().min(1)
});
export type Localized = z.infer<typeof Localized>;

const ItemBase = z.object({
	id: z.string().regex(/^[A-Z0-9-]+$/),
	instruction: Localized,
	explanation: Localized,
	// Optional picture stimulus. `alt` must not give the answer away.
	image: z.object({ src: z.string().min(1), alt: Localized }).optional(),
	// German text read aloud by the speech port (never the answer of the item).
	audioText: z.string().min(1).optional()
});

export const ChoiceItem = ItemBase.extend({
	type: z.literal('choice'),
	prompt: z.string().min(1),
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

export const Lesson = z
	.object({
		schemaVersion: z.literal(1),
		id: z.string().min(1),
		title: Localized,
		// Tagalog texts are machine-made until a native speaker reviewed them (E2).
		tlReviewStatus: z.enum(['machine', 'reviewed']),
		items: z.array(Item).min(1)
	})
	.refine((l) => new Set(l.items.map((i) => i.id)).size === l.items.length, {
		message: 'item ids must be unique'
	});
export type Lesson = z.infer<typeof Lesson>;
