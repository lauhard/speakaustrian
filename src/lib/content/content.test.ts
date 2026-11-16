import { describe, expect, it } from 'vitest';
import { allItems, availableFilters, chapters, course, pickPractice } from './index';

describe('course', () => {
	it('lists all 39 chapters in order', () => {
		expect(course.chapters).toHaveLength(39);
		expect(course.chapters[0].id).toBe('A1-01');
		expect(course.chapters.at(-1)?.id).toBe('A2-19');
	});
});

describe('free practice items', () => {
	it('include practice pool items of every chapter but never test pool items', () => {
		const ids = new Set(allItems().map((i) => i.id));
		for (const c of chapters) {
			for (const i of c.pools?.practice ?? []) expect(ids.has(i.id), i.id).toBe(true);
			for (const i of c.pools?.test ?? []) expect(ids.has(i.id), i.id).toBe(false);
		}
		expect(ids.has('A1-01-P-SP1-1')).toBe(true);
	});
});

describe('pickPractice', () => {
	const items = allItems();
	it('returns only items of the chosen filter, without duplicates', () => {
		const picked = pickPractice(items, 'hoeren', 5, () => 0.42);
		expect(picked.length).toBeGreaterThan(0);
		expect(picked.every((i) => i.skill === 'hoeren')).toBe(true);
		expect(new Set(picked.map((i) => i.id)).size).toBe(picked.length);
	});
	it('offers picture practice only for items with a picture', () => {
		expect(availableFilters(items)).toContain('bild');
		expect(pickPractice(items, 'bild', 10, Math.random).every((i) => i.image)).toBe(true);
	});
	it('is deterministic for a fixed random source', () => {
		const a = pickPractice(items, 'grammatikWortschatz', 6, () => 0.3).map((i) => i.id);
		const b = pickPractice(items, 'grammatikWortschatz', 6, () => 0.3).map((i) => i.id);
		expect(a).toEqual(b);
	});
});

// D24: every course chapter needs gap-fill and picture tasks.
describe('content rules per chapter', () => {
	const real = chapters.filter((c) => /^A[12]-\d{2}$/.test(c.chapterId));
	it.each(real.map((c) => [c.chapterId, c] as const))('%s has cloze and picture tasks', (_id, chapter) => {
		const items = chapter.lessons.flatMap((l) => l.items);
		expect(items.some((i) => i.type === 'cloze')).toBe(true);
		expect(items.filter((i) => i.image).length).toBeGreaterThanOrEqual(2);
	});
	// R-K3: real chapters need ≥ 2 twins per test item (the schema only asks for 1, the DEMO sandbox uses that).
	it.each(real.map((c) => [c.chapterId, c] as const))('%s: every test item has at least 2 twins', (_id, chapter) => {
		const test = chapter.pools?.test ?? [];
		for (const i of test) expect(test.filter((t) => (t.family ?? t.id) === (i.family ?? i.id)).length, i.id).toBeGreaterThanOrEqual(3);
	});
	it('every picture file exists', async () => {
		const { existsSync } = await import('node:fs');
		for (const item of allItems()) if (item.image) expect(existsSync(`static${item.image.src}`), item.image.src).toBe(true);
	});
});
