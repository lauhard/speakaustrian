import { describe, expect, it } from 'vitest';
import { accuracyPct, chapterStars } from './rating';

describe('chapter rating (K6, G-019 A)', () => {
	it('1 star for passing, 2 from 70 %, 3 from 90 % of all chapter answers', () => {
		expect(chapterStars({ correct: 69, total: 100 })).toBe(1);
		expect(chapterStars({ correct: 70, total: 100 })).toBe(2);
		expect(chapterStars({ correct: 89, total: 100 })).toBe(2);
		expect(chapterStars({ correct: 90, total: 100 })).toBe(3);
	});
	it('rounds like the screen and treats an empty tally as perfect', () => {
		expect(accuracyPct({ correct: 179, total: 200 })).toBe(90);
		expect(chapterStars({ correct: 0, total: 0 })).toBe(3);
	});
});
