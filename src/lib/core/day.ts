import { addDays, dueQueue } from './review';
import type { GameState, LocalDate } from './state';

// 04a §5.2–5.3. Session anchor R-D2 is not modelled yet: every event counts for its own local date.
export const DAY_GOAL_SEC = 20 * 60; // R-S1 / decision 4
export const ACTIVITY_TICK_SEC = 15; // R-D3
const MAX_FREEZES = 2; // R-S4
const BADGES = [7, 30, 60, 90]; // R-S5

const emptyDay = (dueAtStart: number) => ({ activeSec: 0, dueAtStart, answeredDue: 0, goalMet: false, frozen: false, simDeferred: false });

/** R-S2/R-S3: on the first event of a new date, protect missed days with freezes or break the streak. */
const evaluatePast = (s: GameState, today: LocalDate): GameState => {
	const last = s.streak.lastEvaluated;
	if (last === null || last >= today) return { ...s, streak: { ...s.streak, lastEvaluated: last ?? today } };
	const covered = Object.entries(s.days)
		.filter(([d, r]) => d < today && (r.goalMet || r.frozen))
		.map(([d]) => d)
		.sort();
	const lastMet = covered.at(-1);
	const streak = { ...s.streak, lastEvaluated: today };
	if (s.streak.current === 0 || lastMet === undefined) return { ...s, streak };
	const missed: LocalDate[] = [];
	for (let d = addDays(lastMet, 1); d < today; d = addDays(d, 1)) missed.push(d);
	if (missed.length === 0) return { ...s, streak };
	if (missed.length > s.streak.freezes) return { ...s, streak: { ...streak, current: 0 } }; // freezes stay (I-4)
	const days = { ...s.days };
	for (const d of missed) days[d] = { ...(days[d] ?? emptyDay(0)), frozen: true };
	return { ...s, days, streak: { ...streak, freezes: (s.streak.freezes - missed.length) as 0 | 1 | 2 } };
};

/** R-S1, R-S4, R-S5: book active time, then mark the day as met as soon as time and due queue allow. */
export const trackDay = (s: GameState, today: LocalDate, activeSec: number): GameState => {
	if (!s.profile) return s;
	const evaluated = evaluatePast(s, today);
	const due = dueQueue(evaluated, today).length;
	const day = evaluated.days[today] ?? emptyDay(due);
	const booked = { ...day, activeSec: day.activeSec + activeSec };
	const met = !booked.goalMet && booked.activeSec >= DAY_GOAL_SEC && due === 0;
	if (!met) return { ...evaluated, days: { ...evaluated.days, [today]: booked } };
	const current = evaluated.streak.current + 1;
	const freezes = current % 7 === 0 ? Math.min(MAX_FREEZES, evaluated.streak.freezes + 1) : evaluated.streak.freezes;
	return {
		...evaluated,
		days: { ...evaluated.days, [today]: { ...booked, goalMet: true } },
		streak: {
			...evaluated.streak,
			current,
			best: Math.max(evaluated.streak.best, current),
			freezes: freezes as 0 | 1 | 2,
			badges: [...new Set([...evaluated.streak.badges, ...BADGES.filter((b) => current >= b)])]
		}
	};
};
