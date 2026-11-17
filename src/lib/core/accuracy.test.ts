import { describe, expect, it } from 'vitest';
import { answer, bank, emptyScore, fxOf, type Score } from './accuracy';

const play = (answers: boolean[], from: Score = emptyScore) => answers.reduce(answer, from);
const T = true, F = false;

describe('flame score', () => {
	it('earns one flame per 3 correct answers in a row', () => {
		expect(play([T, T]).pot).toBe(0);
		expect(play([T, T, T]).pot).toBe(1);
		expect(play([T, T, T, T, T, T, T]).pot).toBe(2);
	});
	it('a mistake loses the flames of the round, the score stays', () => {
		const s = play([T, T, T, T, T, T, F], { ...emptyScore, score: 5, best: 5 });
		expect(s).toMatchObject({ pot: 0, hits: 0, score: 5, armed: true });
	});
	it('a second mistake before the next flame wipes the score, the best stays', () => {
		expect(play([F, T, T, F], { ...emptyScore, score: 5, best: 5 })).toMatchObject({ score: 0, best: 5 });
	});
	it('a new flame disarms: the next mistake only costs the pot again', () => {
		expect(play([F, T, T, T, F], { ...emptyScore, score: 5, best: 5 })).toMatchObject({ score: 5, pot: 0, armed: true });
	});
	it('banking moves the pot into the score and updates the best', () => {
		expect(bank(play([T, T, T, T, T, T]))).toMatchObject({ score: 2, best: 2, pot: 0 });
	});
	it('names the animation of a change', () => {
		const s = play([T, T]);
		expect(fxOf(s, answer(s, T))).toBe('flame');
		expect(fxOf(play([T, T, T]), answer(play([T, T, T]), F))).toBe('lostPot');
		const armed = { ...emptyScore, score: 3, armed: true };
		expect(fxOf(armed, answer(armed, F))).toBe('lostScore');
		expect(fxOf(play([T, T, T]), bank(play([T, T, T])))).toBe('bank');
	});
});
