import { describe, expect, it } from 'vitest';
import { answer, bank, close, emptyFlames, enter, fxOf, multiplier, tierOf, type Flames } from './flames';

const play = (f: Flames, answers: boolean[]) => answers.reduce(answer, f);
const start = enter(emptyFlames, 'A1-01');

describe('flames v2 (K8)', () => {
	it('3 right in a row = 1 round flame; the round end banks it into the chapter flames', () => {
		const f = play(start, [true, true, true, true]);
		expect(f).toMatchObject({ pot: 1, hits: 1, chapterFlames: 0 });
		expect(bank(f, false)).toMatchObject({ pot: 0, chapterFlames: 1, best: 1 });
	});
	it('1st mistake loses the pot, a 2nd before the next flame wipes the chapter flames', () => {
		const banked = bank(play(start, [true, true, true, true, true, true]), false);
		const once = play(banked, [true, true, true, false]);
		expect(once).toMatchObject({ pot: 0, armed: true, chapterFlames: 2 });
		expect(answer(once, false)).toMatchObject({ chapterFlames: 0 });
		// a new flame disarms again
		expect(play(once, [true, true, true, false])).toMatchObject({ armed: true, chapterFlames: 2 });
	});
	it('a shield takes the 2nd mistake: chapter flames stay, one shield gone, still armed', () => {
		const f = { ...bank(play(start, [true, true, true]), false), shields: 2 };
		const hit = play(f, [false, false]);
		expect(hit).toMatchObject({ chapterFlames: 1, shields: 1, armed: true });
		expect(fxOf(answer(f, false), hit)).toBe('shieldBroken');
		expect(play(hit, [false, false])).toMatchObject({ chapterFlames: 0, shields: 0 });
	});
	it('a perfect lesson or practice round earns a shield, max. 2; other rounds do not', () => {
		const perfect = play(start, [true, true]);
		expect(bank(perfect, true).shields).toBe(1);
		expect(bank(perfect, false).shields).toBe(0);
		expect(bank(play(start, [true, false]), true).shields).toBe(0);
		expect(bank(start, true).shields).toBe(0);
		expect(bank({ ...perfect, shields: 2 }, true).shields).toBe(2);
	});
	it('flames belong to one chapter; passing closes it and keeps the result', () => {
		const f = { ...play(start, [true, true, true]), shields: 1 };
		expect(enter(f, 'A1-01')).toBe(f);
		const closed = close(f, 'A1-01');
		expect(closed).toMatchObject({ chapterId: null, chapterFlames: 0, shields: 0, pot: 0, closed: { 'A1-01': 1 }, best: 1 });
		expect(close(f, 'A1-02')).toBe(f);
		expect(enter(closed, 'A1-02')).toMatchObject({ chapterId: 'A1-02', chapterFlames: 0 });
	});
	it('multiplier 1 + 0.02 per flame, capped at ×2; colour tiers', () => {
		expect([0, 9, 20, 50, 80].map(multiplier)).toEqual([1, 1.18, 1.4, 2, 2]);
		expect([0, 1, 9, 10, 19, 20, 34, 35].map(tierOf)).toEqual(['grey', 'orange', 'orange', 'red', 'red', 'violet', 'violet', 'blue']);
	});
});
