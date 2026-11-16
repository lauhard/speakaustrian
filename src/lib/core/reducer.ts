import type { RulePolicy } from './policy';
import { initialState, type ChapterId, type ChapterRun, type CoursePhase, type GameState, type LocalDate, type OverrideEffect, type OverrideGrant, type PensumMin } from './state';

// Pure core (docs/spec/04a §1): no I/O, no Date.now(). Time comes only from the event.
type EventBase = { id: string; at: string; tzOffsetMin: number };

export type GameEvent = EventBase &
	(
		| { type: 'PROFILE_CREATED'; name: string; pensumMin: PensumMin }
		| { type: 'PENSUM_CHANGED'; pensumMin: PensumMin }
		| { type: 'APP_OPENED' }
		| { type: 'LESSON_COMPLETED'; chapterId: string; lessonId: string }
		| { type: 'OVERRIDE_GRANTED'; grant: OverrideGrant }
	);

export type Reducer = (state: GameState, event: GameEvent) => GameState;

// R-D1: local date of an event = UTC time shifted by the device offset at that moment.
export const localDate = (at: string, tzOffsetMin: number): LocalDate =>
	new Date(Date.parse(at) + tzOffsetMin * 60_000).toISOString().slice(0, 10);

// Plan day (derived, never stored): calendar days since the start date + 1.
export const planDay = (startDate: LocalDate, today: LocalDate): number =>
	Math.round((Date.parse(`${today}T00:00:00Z`) - Date.parse(`${startDate}T00:00:00Z`)) / 86_400_000) + 1;

// Course automaton (04a §4.1): what follows a completed chapter.
const phaseAfter = (order: readonly ChapterId[], completed: ChapterId): CoursePhase => {
	if (completed === 'A1-20') return { kind: 'MILESTONE_A1' };
	if (completed === 'A2-10') return { kind: 'SIM_DIAGNOSIS' };
	if (completed === 'A2-19') return { kind: 'EXIT_CHAIN' };
	const next = order[order.indexOf(completed) + 1];
	return next ? { kind: 'CHAPTER', id: next } : { kind: 'EXIT_CHAIN' };
};

const newRun = (policy: RulePolicy, s: GameState, id: ChapterId): ChapterRun => ({
	id,
	attemptNo: 1,
	startLives: policy.startLives(s, id),
	attempt: { kind: 'LESSONS', repeatMode: false, done: [] },
	seenTestItemIds: [],
	minutesSpent: 0
});

const enterPhase = (policy: RulePolicy, s: GameState, phase: CoursePhase): GameState => ({
	...s,
	course: { ...s.course, phase, chapter: phase.kind === 'CHAPTER' ? newRun(policy, s, phase.id) : null }
});

// R-PL3: effects of an accepted override run through the normal mechanics.
const applyEffect = (policy: RulePolicy, order: readonly ChapterId[], s: GameState, effect: OverrideEffect): GameState => {
	if (effect.kind !== 'COMPLETE_CHAPTER') return s; // recovery effects follow with the chapter test step
	const withCompletion: GameState = {
		...s,
		course: { ...s.course, completed: { ...s.course.completed, [effect.chapterId]: effect.completion } }
	};
	const isCurrent = s.course.phase.kind === 'CHAPTER' && s.course.phase.id === effect.chapterId;
	return isCurrent ? enterPhase(policy, withCompletion, phaseAfter(order, effect.chapterId)) : withCompletion;
};

export const makeReducer = (policy: RulePolicy, chapterOrder: readonly ChapterId[]): Reducer => (state, event) => {
	const s: GameState = {
		...state,
		clock: { ...state.clock, lastEventAt: event.at, lastLocalDate: localDate(event.at, event.tzOffsetMin) }
	};
	switch (event.type) {
		case 'PROFILE_CREATED': {
			if (s.profile || event.name.trim() === '' || chapterOrder.length === 0) return s;
			const withProfile: GameState = {
				...s,
				profile: { name: event.name.trim(), startDate: localDate(event.at, event.tzOffsetMin), pensumMin: event.pensumMin }
			};
			return enterPhase(policy, withProfile, { kind: 'CHAPTER', id: chapterOrder[0] });
		}
		case 'PENSUM_CHANGED':
			return s.profile ? { ...s, profile: { ...s.profile, pensumMin: event.pensumMin } } : s;
		case 'LESSON_COMPLETED': {
			const run = s.course.chapter;
			// Only lessons of the chapter in work count; re-reading passed chapters changes nothing (R-F1).
			if (!run || run.id !== event.chapterId || run.attempt.kind !== 'LESSONS') return s;
			if (run.attempt.done.includes(event.lessonId)) return s;
			const attempt = { ...run.attempt, done: [...run.attempt.done, event.lessonId] };
			return { ...s, course: { ...s.course, chapter: { ...run, attempt } } };
		}
		case 'OVERRIDE_GRANTED': {
			if (s.overrides.some((o) => o.grant.grantId === event.grant.grantId)) return s;
			const decision = policy.acceptOverride(s, event.grant);
			const recorded: GameState = { ...s, overrides: [...s.overrides, { grant: event.grant, at: event.at, decision }] };
			return decision.accepted
				? decision.effects.reduce((acc, effect) => applyEffect(policy, chapterOrder, acc, effect), recorded)
				: recorded;
		}
		case 'APP_OPENED':
			return s;
	}
};

export const newGame = (policy: RulePolicy): GameState => initialState({ id: policy.id, version: policy.version });
