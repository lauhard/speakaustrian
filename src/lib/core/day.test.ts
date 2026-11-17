import { describe, expect, it } from 'vitest';
import { DAY_GOAL_SEC, trackDay } from './day';
import { makeDefaultPolicy } from './policy';
import { newGame } from './reducer';
import type { Card, GameState } from './state';

const base: GameState = { ...newGame(makeDefaultPolicy(['A1-01'])), profile: { name: 'Maria', startDate: '2026-11-02', pensumMin: 90 } };
const card = (id: string, due: string) =>
	({ id, kind: 'vocab', refId: id, box: 2, due, mastered: false, archived: false, directions: ['recognize'], nextDirection: 'recognize', lastWrongDirection: null }) as unknown as Card;
const withCards = (s: GameState, cards: Card[]): GameState => ({ ...s, review: { ...s.review, cards: Object.fromEntries(cards.map((c) => [c.id, c])) } });
const met = (s: GameState, day: string) => trackDay(s, day, DAY_GOAL_SEC);
const streakOn = (current: number, freezes: 0 | 1 | 2, lastMet: string): GameState => ({
	...base,
	days: { [lastMet]: { activeSec: DAY_GOAL_SEC, dueAtStart: 0, answeredDue: 0, goalMet: true, frozen: false, simDeferred: false } },
	streak: { ...base.streak, current, best: current, freezes, lastEvaluated: lastMet }
});

describe('day goal and streak (R-S1–R-S5)', () => {
	it('T-S01/T-S02: 20 min alone are not enough while cards are due; the last due card meets the goal at once', () => {
		const due = withCards(base, [card('c1', '2026-11-16')]);
		const s = met(due, '2026-11-16');
		expect(s.days['2026-11-16'].goalMet).toBe(false);
		const answered = trackDay(withCards(s, [card('c1', '2026-11-20')]), '2026-11-16', 0);
		expect(answered.days['2026-11-16'].goalMet).toBe(true);
		expect(answered.streak.current).toBe(1);
	});
	it('T-S03: 19 min are not met, 20 min are', () => {
		const s = trackDay(base, '2026-11-16', DAY_GOAL_SEC - 60);
		expect(s.streak.current).toBe(0);
		expect(trackDay(s, '2026-11-16', 60).streak.current).toBe(1);
	});
	it('T-S04: a met day stays met and counts once', () => {
		const s = trackDay(met(base, '2026-11-16'), '2026-11-16', 600);
		expect(s.streak.current).toBe(1);
	});
	it('T-S05: one missed day with one freeze is protected', () => {
		const s = trackDay(streakOn(10, 1, '2026-11-16'), '2026-11-18', 0);
		expect(s.streak).toMatchObject({ current: 10, freezes: 0 });
		expect(s.days['2026-11-17'].frozen).toBe(true);
	});
	it('T-S06: more missed days than freezes break the streak, freezes stay', () => {
		const s = trackDay(streakOn(10, 2, '2026-11-16'), '2026-11-20', 0);
		expect(s.streak).toMatchObject({ current: 0, freezes: 2, best: 10 });
	});
	it('T-S07: two missed days use both freezes', () => {
		expect(trackDay(streakOn(10, 2, '2026-11-16'), '2026-11-19', 0).streak).toMatchObject({ current: 10, freezes: 0 });
	});
	it('T-S08/T-S09: every 7th day earns a freeze, capped at 2', () => {
		expect(met(streakOn(6, 2, '2026-11-15'), '2026-11-16').streak).toMatchObject({ current: 7, freezes: 2 });
		expect(met(streakOn(13, 0, '2026-11-15'), '2026-11-16').streak).toMatchObject({ current: 14, freezes: 1 });
	});
	it('T-S10: a frozen day does not count but keeps the chain', () => {
		const frozen = trackDay(streakOn(6, 1, '2026-11-14'), '2026-11-16', 0);
		expect(met(frozen, '2026-11-16').streak).toMatchObject({ current: 7, freezes: 1 });
	});
	it('T-S11: badges stay after a break', () => {
		const s = met(streakOn(29, 0, '2026-11-15'), '2026-11-16');
		expect(s.streak.badges).toContain(30);
		expect(trackDay(s, '2026-11-20', 0).streak.badges).toContain(30);
	});
});
