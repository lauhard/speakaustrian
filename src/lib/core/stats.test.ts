import { describe, expect, it } from 'vitest';
import { makeDefaultPolicy } from './policy';
import { newGame } from './reducer';
import { deriveStats } from './stats';
import type { GameState } from './state';

const base = newGame(makeDefaultPolicy(['A1-01']));
const withAttempt = (attempt: unknown): GameState =>
	({ ...base, course: { ...base.course, chapter: { id: 'A1-01', attempt } } }) as unknown as GameState;

describe('deriveStats', () => {
	it('reads streak numbers and hides lives and points outside a test', () => {
		const s = deriveStats({ ...base, streak: { ...base.streak, current: 4, best: 9, freezes: 1 } });
		expect(s).toEqual({ streak: 4, best: 9, freezes: 1, lives: null, points: null });
	});
	it('shows lives of a running test and of the correction round', () => {
		expect(deriveStats(withAttempt({ kind: 'TEST', lives: 2 })).lives).toBe(2);
		expect(deriveStats(withAttempt({ kind: 'CORRECTION', livesLeft: 1 })).lives).toBe(1);
		expect(deriveStats(withAttempt({ kind: 'PRACTICE' })).lives).toBeNull();
	});
});
