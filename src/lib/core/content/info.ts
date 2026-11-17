import type { ContentInfo } from '../reducer';
import { splitPractice, type PoolItem } from '../draw';
import { defaultConfig } from '../policy';
import type { ChapterContent, Item } from './schema';

export type PoolKind = 'practice' | 'test';

// The pool of a chapter as the draw functions need it (R-G1, R-T2). Items without `family` are their own family.
export const poolOf = (chapter: ChapterContent | undefined, kind: PoolKind): PoolItem[] =>
	(chapter?.pools?.[kind] ?? []).map((i) => ({ id: i.id, skill: i.skill, family: i.family ?? i.id, goals: i.goals ?? [] }));

// Practice part and the pool for the readiness blocks (≥ 2 blocks, masterprompt phase 5 no. 11).
export const practiceSplit = (chapter: ChapterContent | undefined) =>
	splitPractice(poolOf(chapter, 'practice'), defaultConfig.PRACTICE_PART_ITEMS, 2 * defaultConfig.GATE_ITEMS);

const itemsOf = (c: ChapterContent): Item[] => [...c.lessons.flatMap((l) => l.items), ...(c.pools?.practice ?? []), ...(c.pools?.test ?? [])];

// The seam between content and mechanics: the reducer only sees ids, twin families, goals and card refs.
export const makeContentInfo = (chapters: readonly ChapterContent[]): ContentInfo => {
	const byId = new Map(chapters.flatMap((c) => itemsOf(c).map((i) => [i.id, i] as const)));
	const familyOf = (id: string) => byId.get(id)?.family ?? id;
	return {
		// A chapter without pools has no practice/test yet, so its attempt stays in the lessons.
		chapter: (id) => {
			const c = chapters.find((ch) => ch.chapterId === id);
			// K3: a practice round asks at most PRACTICE_ROUND_ITEMS of the practice part.
			const practiceTotal = Math.min(defaultConfig.PRACTICE_ROUND_ITEMS, practiceSplit(c).part.length);
			return c?.pools ? { lessonIds: c.lessons.map((l) => l.id), practiceTotal } : undefined;
		},
		baseOf: familyOf,
		twinsOf: (id) => {
			const family = familyOf(id);
			return [...byId.values()].filter((i) => i.id !== id && familyOf(i.id) === family).map((i) => i.id);
		},
		goalsOf: (id) => byId.get(id)?.goals ?? [],
		refsOf: (id) => byId.get(id)?.refs ?? []
	};
};
