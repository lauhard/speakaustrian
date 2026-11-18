import { describe, expect, it } from 'vitest';
import { award, chapterPassed, dayGoal, emptyXp, lessonPassed, levelOf, XP_ANSWER } from './xp';

const course = { chapterId: 'A1-01', reduced: false };
const free = { chapterId: null, reduced: true };

describe('XP and level (K9)', () => {
	it('answers pay by task kind; reduced contexts pay half', () => {
		const x = [XP_ANSWER.lesson, XP_ANSWER.gate, XP_ANSWER.test].reduce((acc, a) => award(acc, a, course), emptyXp);
		expect(x).toMatchObject({ total: 23, chapter: { 'A1-01': 23 } });
		expect(award(emptyXp, XP_ANSWER.lesson, free)).toMatchObject({ total: 3, chapter: {} });
		expect(award(emptyXp, XP_ANSWER.review, { chapterId: null, reduced: false }).total).toBe(3);
	});
	it('a lesson pays +20 on its first pass, +10 with 3 stars, and only once', () => {
		const x = lessonPassed(emptyXp, 'L1', 90, course);
		expect(x.total).toBe(30);
		expect(lessonPassed(x, 'L1', 100, course)).toBe(x);
		expect(lessonPassed(emptyXp, 'L2', 60, course).total).toBe(20);
	});
	it('the day goal pays +25 once per day', () => {
		const x = dayGoal(emptyXp, '2026-11-18');
		expect(x.total).toBe(25);
		expect(dayGoal(x, '2026-11-18')).toBe(x);
	});
	it('passing: test +100 (+50 perfect), then the flame bonus on the chapter XP (concept example ×1.36)', () => {
		const before = award(emptyXp, 811, course);
		const x = chapterPassed(before, 'A1-01', false, 1.36, course);
		expect(x.closed['A1-01']).toEqual({ xp: 911, bonus: 328 });
		expect(x.total).toBe(911 + 328);
		expect(x.chapter['A1-01']).toBeUndefined();
		expect(chapterPassed(x, 'A1-01', true, 2, course)).toBe(x);
		expect(chapterPassed(emptyXp, 'A1-02', true, 1.5, free).closed['A1-02']).toEqual({ xp: 75, bonus: 0 });
	});
	it('level n → n+1 costs 100 × n XP', () => {
		expect([0, 99, 100, 299, 300, 1239, 4500].map((t) => levelOf(t).level)).toEqual([1, 1, 2, 2, 3, 5, 10]);
		expect(levelOf(350)).toEqual({ level: 3, into: 50, need: 300 });
	});
});
