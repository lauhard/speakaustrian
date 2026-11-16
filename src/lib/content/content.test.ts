import { describe, expect, it } from 'vitest';
import { allItems, availableFilters, course, pickPractice } from './index';

describe('course', () => {
	it('lists all 39 chapters in order', () => {
		expect(course.chapters).toHaveLength(39);
		expect(course.chapters[0].id).toBe('A1-01');
		expect(course.chapters.at(-1)?.id).toBe('A2-19');
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
