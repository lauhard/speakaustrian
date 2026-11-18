import type { RulePolicy } from './policy';
import { trackDay } from './day';
import { seeded, shuffle } from './random';
import { addCards, addDays, addErrorCard, answerCard, errorCardId, type Direction, type Introduced } from './review';
import { initialState, type AttemptState, type ChapterId, type ChapterRun, type CoursePhase, type GameState, type LocalDate, type OverrideEffect, type OverrideGrant, type PensumMin, type RecoveryPlan } from './state';

// Pure core (docs/spec/04a §1): no I/O, no Date.now(). Time comes only from the event.
type EventBase = { id: string; at: string; tzOffsetMin: number };

export type GameEvent = EventBase &
	(
		| { type: 'PROFILE_CREATED'; name: string; pensumMin: PensumMin }
		| { type: 'PENSUM_CHANGED'; pensumMin: PensumMin }
		| { type: 'APP_OPENED' }
		| { type: 'ACTIVITY'; sec: number }
		// correct/total since K1; events without a score (older logs, migration) stay valid as passed.
		| { type: 'LESSON_COMPLETED'; chapterId: string; lessonId: string; introduced?: Introduced[]; correct?: number; total?: number }
		| { type: 'PRACTICE_ANSWERED'; itemId: string; correct: boolean }
		| { type: 'PRACTICE_SKIPPED' }
		| { type: 'GATE_ANSWERED'; itemId: string; correct: boolean }
		| { type: 'TARGETED_PRACTICE_DONE'; goalIds: string[] }
		| { type: 'TARGET_STARTED'; itemIds: string[] }
		| { type: 'TARGET_ANSWERED'; itemId: string; correct: boolean }
		| { type: 'TEST_STARTED'; attemptId: string; itemIds: string[] }
		| { type: 'TEST_ANSWERED'; attemptId: string; itemId: string; correct: boolean }
		| { type: 'CORRECTION_ANSWERED'; attemptId: string; twinId: string; correct: boolean }
		| { type: 'ERROR_REVIEW_ANSWERED'; cardId: string; correct: boolean }
		| { type: 'REVIEW_ANSWERED'; cardId: string; direction: Direction; correct: boolean }
		| { type: 'OVERRIDE_GRANTED'; grant: OverrideGrant }
	);

// What the mechanics need to know about the content. The core never imports content itself.
export type ContentInfo = {
	// undefined = the chapter has no practice/test pools yet; its attempt then stays in the lessons.
	chapter(c: ChapterId): { lessonIds: readonly string[]; practiceTotal: number } | undefined;
	baseOf(itemId: string): string;
	// All other items of the same twin family.
	twinsOf(itemId: string): readonly string[];
	goalsOf(itemId: string): readonly string[];
	// Review card refs (vocabulary ids) an item tests (R-W4).
	refsOf(itemId: string): readonly string[];
};
export const noContent: ContentInfo = { chapter: () => undefined, baseOf: (id) => id, twinsOf: () => [], goalsOf: () => [], refsOf: () => [] };

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
	minutesSpent: 0,
	tally: { correct: 0, total: 0 },
	practiceStreak: 0,
	heartEarned: false
});

const enterPhase = (policy: RulePolicy, s: GameState, phase: CoursePhase): GameState => ({
	...s,
	course: { ...s.course, phase, chapter: phase.kind === 'CHAPTER' ? newRun(policy, s, phase.id) : null }
});

// R-K1, R-K3: one twin per wrong item, preferably one not used in this test, else the least recently seen.
const pickTwins = (content: ContentInfo, run: ChapterRun, wrong: readonly string[], inTest: readonly string[], seed: string): string[] => {
	const lastSeen = (id: string) => run.seenTestItemIds.lastIndexOf(id);
	const twins = wrong.flatMap((item) => {
		const family = content.twinsOf(item);
		const unused = family.filter((t) => !inTest.includes(t));
		const pool = unused.length > 0 ? unused : family;
		return [...pool].sort((a, b) => lastSeen(a) - lastSeen(b)).slice(0, 1);
	});
	return shuffle(twins, seeded(seed));
};

// K6: a valid chapter answer adds to the tally of the run; invalid events (wrong state, double taps) do not.
const tallied = (run: ChapterRun | null, e: GameEvent): ChapterRun | null => {
	if (!run) return run;
	const a = run.attempt;
	const add = (correct: number, total: number): ChapterRun => ({ ...run, tally: { correct: run.tally.correct + correct, total: run.tally.total + total } });
	switch (e.type) {
		case 'LESSON_COMPLETED':
			return run.id === e.chapterId && a.kind === 'LESSONS' && e.total !== undefined ? add(e.correct ?? 0, e.total) : run;
		case 'PRACTICE_ANSWERED':
			return a.kind === 'PRACTICE' ? add(Number(e.correct), 1) : run;
		case 'GATE_ANSWERED':
			return a.kind === 'GATE' && !a.items.includes(e.itemId) ? add(Number(e.correct), 1) : run;
		case 'TEST_ANSWERED':
			return a.kind === 'TEST' && a.attemptId === e.attemptId && a.items[a.idx] === e.itemId ? add(Number(e.correct), 1) : run;
		case 'TARGET_ANSWERED':
			return a.kind === 'TARGETED_PRACTICE' && a.items[a.answered] === e.itemId ? add(Number(e.correct), 1) : run;
		case 'CORRECTION_ANSWERED':
			return a.kind === 'CORRECTION' && a.attemptId === e.attemptId && a.twins[a.idx] === e.twinId ? add(Number(e.correct), 1) : run;
		default:
			return run;
	}
};

const gateBlock = (block: number): AttemptState => ({ kind: 'GATE', block, items: [], wrong: [], correct: 0, answered: 0 });

const entryState = (content: ContentInfo, id: ChapterId, plan: Pick<RecoveryPlan, 'entry' | 'repeatMode'>): AttemptState => {
	switch (plan.entry) {
		case 'LESSONS':
			return { kind: 'LESSONS', repeatMode: plan.repeatMode, done: [] };
		case 'PRACTICE':
			return { kind: 'PRACTICE', answered: 0, total: content.chapter(id)?.practiceTotal ?? 0 };
		case 'GATE':
			return gateBlock(1);
		case 'TEST_READY':
			return { kind: 'TEST_READY' };
	}
};

// R-PL3: effects of an accepted override run through the normal mechanics.
const applyEffect = (policy: RulePolicy, order: readonly ChapterId[], s: GameState, effect: OverrideEffect): GameState => {
	if (effect.kind !== 'COMPLETE_CHAPTER') {
		// SET_RECOVERY / GRANT_ATTEMPT: the plan waits in the run and replaces the policy's plan once (T-PL04).
		const run = s.course.chapter;
		return run && run.id === effect.chapterId ? { ...s, course: { ...s.course, chapter: { ...run, recovery: effect.plan } } } : s;
	}
	const withCompletion: GameState = {
		...s,
		course: { ...s.course, completed: { ...s.course.completed, [effect.chapterId]: effect.completion } }
	};
	const isCurrent = s.course.phase.kind === 'CHAPTER' && s.course.phase.id === effect.chapterId;
	return isCurrent ? enterPhase(policy, withCompletion, phaseAfter(order, effect.chapterId)) : withCompletion;
};

// Content can arrive after the learner finished the lessons (e.g. pools are added to a chapter): the attempt then still says
// LESSONS with every lesson done and no event would move it on. Settling is pure and runs after loading a saved state.
export const settleChapter = (content: ContentInfo) => (state: GameState): GameState => {
	const run = state.course.chapter;
	const info = run ? content.chapter(run.id) : undefined;
	if (!run || !info) return state;
	const to = (attempt: AttemptState): GameState => ({ ...state, course: { ...state.course, chapter: { ...run, attempt } } });
	// The size of the practice part can change with the content (G-010): keep the count, move on if it is already reached.
	if (run.attempt.kind === 'PRACTICE' && run.attempt.total !== info.practiceTotal)
		return to(run.attempt.answered >= info.practiceTotal ? gateBlock(1) : { ...run.attempt, total: info.practiceTotal });
	if (run.attempt.kind !== 'LESSONS') return state;
	const done = run.attempt.done;
	if (!info.lessonIds.every((l) => done.includes(l))) return state;
	return to(entryState(content, run.id, { entry: 'PRACTICE', repeatMode: run.attempt.repeatMode }));
};

const makeCoreReducer = (policy: RulePolicy, chapterOrder: readonly ChapterId[], content: ContentInfo = noContent): Reducer => (state, event) => {
	const s: GameState = {
		...state,
		clock: { ...state.clock, lastEventAt: event.at, lastLocalDate: localDate(event.at, event.tzOffsetMin) }
	};
	const today = localDate(event.at, event.tzOffsetMin);
	const run = tallied(s.course.chapter, event);
	const withRun = (base: GameState, next: ChapterRun): GameState => ({ ...base, course: { ...base.course, chapter: next } });
	const withAttempt = (base: GameState, attempt: AttemptState): GameState => (run ? withRun(base, { ...run, attempt }) : base);
	const withError = (base: GameState, itemId: string): GameState => ({
		...base,
		review: { ...base.review, cards: addErrorCard(base.review.cards, content.baseOf(itemId), today) }
	});
	// R-E1: consecutive right, automatically graded answers; a wrong one resets, the record stays.
	const counted = (base: GameState, correct: boolean): GameState => {
		const current = correct ? base.answerStreak.current + 1 : 0;
		return { ...base, answerStreak: { current, best: Math.max(base.answerStreak.best, current) } };
	};
	const graded = (base: GameState, itemId: string, correct: boolean): GameState => counted(correct ? base : withError(base, itemId), correct);
	// R-W4: content answered right in the chapter test lifts its cards from box 1 to box 2.
	const promote = (base: GameState, itemId: string): GameState => {
		const refs = content.refsOf(itemId);
		const cards = Object.fromEntries(
			Object.entries(base.review.cards).map(([id, c]) => [
				id,
				c.box === 1 && c.kind !== 'error' && refs.includes(c.refId) ? { ...c, box: 2 as const, due: addDays(today, policy.config.LEITNER_INTERVALS_DAYS[1]) } : c
			])
		);
		return { ...base, review: { ...base.review, cards } };
	};
	// R-F2: book the completion, the bonus and the perfect streak, then let the course automaton move on.
	const pass = (base: GameState, current: ChapterRun, perfectFirst: boolean): GameState => {
		const streak = perfectFirst ? base.course.perfectStreak.current + 1 : 0;
		const booked: GameState = {
			...base,
			course: {
				...base.course,
				completed: { ...base.course.completed, [current.id]: policy.completionOnPass(base, current.id, current, event.at) },
				results: {
					...base.course.results,
					[current.id]: { test: current.lastTest ?? { correct: 0, total: 0 }, chapter: current.tally, attemptNo: current.attemptNo, at: event.at }
				},
				nextChapterBonus: policy.bonusForNext(base, current, perfectFirst),
				perfectStreak: { current: streak, best: Math.max(base.course.perfectStreak.best, streak) }
			}
		};
		return enterPhase(policy, booked, phaseAfter(chapterOrder, current.id));
	};
	// R-K4/R-K5 as data: the plan of the policy says where the next attempt starts.
	const nextAttempt = (base: GameState, current: ChapterRun, plan: RecoveryPlan): GameState =>
		withRun(base, {
			...current,
			recovery: undefined,
			attemptNo: current.attemptNo + 1,
			startLives: plan.resetLives ? policy.startLives(base, current.id) : current.startLives,
			attempt: entryState(content, current.id, plan)
		});
	const fail = (base: GameState, current: ChapterRun, wrong: readonly string[]): GameState => {
		const plan = current.recovery ?? policy.recoveryAfterFail(base, current);
		if (!plan.errorReview) return nextAttempt(base, current, plan);
		const cardIds = [...new Set(wrong.map((item) => errorCardId(content.baseOf(item))))];
		return withRun(base, { ...current, attempt: { kind: 'ERROR_REVIEW', cardIds, done: [] } });
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
			// Only lessons of the chapter in work count; re-reading passed chapters changes nothing (R-F1).
			if (!run || run.id !== event.chapterId || run.attempt.kind !== 'LESSONS') return s;
			// The tally (K6) counts repeated and failed lessons too.
			if (run.attempt.done.includes(event.lessonId)) return withRun(s, run);
			// K1, K2: a failed lesson stays open, so practice and readiness stay locked until every lesson is passed.
			if (event.total !== undefined && !policy.isLessonPassed({ correct: event.correct ?? 0, total: event.total })) return withRun(s, run);
			const done = [...run.attempt.done, event.lessonId];
			const info = content.chapter(run.id);
			const attempt: AttemptState =
				info && info.lessonIds.every((l) => done.includes(l)) ? entryState(content, run.id, { entry: 'PRACTICE', repeatMode: false }) : { ...run.attempt, done };
			// R-W2: review cards for what the lesson introduced.
			const cards = addCards(s.review.cards, event.introduced ?? [], today);
			return { ...s, course: { ...s.course, chapter: { ...run, attempt } }, review: { ...s.review, cards } };
		}
		case 'PRACTICE_ANSWERED': {
			if (!run || run.attempt.kind !== 'PRACTICE') return s;
			const answered = run.attempt.answered + 1;
			const booked = graded(s, event.itemId, event.correct);
			const streaked: ChapterRun = { ...run, practiceStreak: event.correct ? run.practiceStreak + 1 : 0 };
			const current: ChapterRun = policy.practiceHeart(streaked)
				? { ...streaked, heartEarned: true, startLives: Math.min(policy.config.LIVES_MAX, streaked.startLives + 1) }
				: streaked;
			return withRun(booked, { ...current, attempt: answered >= run.attempt.total ? gateBlock(1) : { ...run.attempt, answered } });
		}
		case 'PRACTICE_SKIPPED':
			// K3: practice is optional, skipping leads straight to the readiness round.
			return run?.attempt.kind === 'PRACTICE' ? withAttempt(s, gateBlock(1)) : s;
		case 'GATE_ANSWERED': {
			const g = run?.attempt;
			if (!g || g.kind !== 'GATE' || g.items.includes(event.itemId)) return s;
			const gate = {
				...g,
				items: [...g.items, event.itemId],
				wrong: event.correct ? g.wrong : [...g.wrong, event.itemId],
				correct: g.correct + Number(event.correct),
				answered: g.answered + 1
			};
			// R-G3: only errors touch the cards.
			const booked = graded(s, event.itemId, event.correct);
			if (gate.answered < policy.config.GATE_ITEMS) return withAttempt(booked, gate);
			if (policy.isTestReady(gate)) return withAttempt(booked, { kind: 'TEST_READY' });
			// K4: weakest goals first (most wrong items), so the capped stack trains them; the full list stays visible.
			const misses = gate.wrong.flatMap((item) => content.goalsOf(item));
			const count = (g: string) => misses.filter((m) => m === g).length;
			const goalIds = [...new Set(misses)].sort((a, b) => count(b) - count(a));
			return withAttempt(booked, { kind: 'TARGETED_PRACTICE', block: gate.block, goalIds, done: false, items: [], answered: 0 });
		}
		case 'TARGETED_PRACTICE_DONE': {
			// K4: a started stack is mandatory; DONE only moves on while no stack was started (older states, empty pools).
			if (!run || run.attempt.kind !== 'TARGETED_PRACTICE' || run.attempt.items.length > 0) return s;
			return withAttempt(s, gateBlock(run.attempt.block + 1));
		}
		case 'TARGET_STARTED': {
			const t = run?.attempt;
			if (!t || t.kind !== 'TARGETED_PRACTICE' || t.items.length > 0) return s;
			const items = event.itemIds.slice(0, policy.config.TARGET_MAX);
			return withAttempt(s, items.length === 0 ? gateBlock(t.block + 1) : { ...t, items, answered: 0 });
		}
		case 'TARGET_ANSWERED': {
			const t = run?.attempt;
			if (!t || t.kind !== 'TARGETED_PRACTICE' || t.items[t.answered] !== event.itemId) return s;
			const booked = graded(s, event.itemId, event.correct);
			const answered = t.answered + 1;
			// K4: after the last item a new readiness block follows (V2).
			return withAttempt(booked, answered >= t.items.length ? gateBlock(t.block + 1) : { ...t, answered });
		}
		case 'TEST_STARTED': {
			if (!run || run.attempt.kind !== 'TEST_READY' || event.itemIds.length === 0) return s;
			return withRun(s, {
				...run,
				seenTestItemIds: [...run.seenTestItemIds.filter((id) => !event.itemIds.includes(id)), ...event.itemIds],
				attempt: { kind: 'TEST', attemptId: event.attemptId, items: event.itemIds, idx: 0, lives: run.startLives, wrong: [], audioPlays: {} }
			});
		}
		case 'TEST_ANSWERED': {
			const t = run?.attempt;
			if (!run || !t || t.kind !== 'TEST' || t.attemptId !== event.attemptId || t.items[t.idx] !== event.itemId) return s;
			const test = {
				...t,
				idx: t.idx + 1,
				lives: t.lives - Number(!event.correct),
				wrong: event.correct ? t.wrong : [...t.wrong, event.itemId]
			};
			const booked = event.correct ? promote(counted(s, true), event.itemId) : graded(s, event.itemId, false);
			const finished = policy.outcomeAfterTest({ ...run, attempt: test }) !== 'CONTINUE';
			const current: ChapterRun = { ...run, attempt: test, ...(finished ? { lastTest: { correct: test.idx - test.wrong.length, total: test.items.length } } : {}) };
			switch (policy.outcomeAfterTest(current)) {
				case 'CONTINUE':
					return withRun(booked, current);
				case 'PASSED':
					return pass(booked, current, run.attemptNo === 1);
				case 'FAILED':
					return fail(booked, current, test.wrong);
				case 'CORRECTION': {
					// R-K2 (T-K02): the correction round follows at once, no state in between.
					const twins = pickTwins(content, run, test.wrong, test.items, test.attemptId);
					return withRun(booked, { ...current, attempt: { kind: 'CORRECTION', attemptId: test.attemptId, twins, idx: 0, livesLeft: test.lives } });
				}
			}
			return s;
		}
		case 'CORRECTION_ANSWERED': {
			const c = run?.attempt;
			if (!run || !c || c.kind !== 'CORRECTION' || c.attemptId !== event.attemptId || c.twins[c.idx] !== event.twinId) return s;
			const booked = graded(s, event.twinId, event.correct);
			const current: ChapterRun = { ...run, attempt: { ...c, idx: c.idx + 1 } };
			if (event.correct && c.idx + 1 < c.twins.length) return withRun(booked, current);
			return policy.outcomeAfterCorrection(current, event.correct) === 'PASSED' ? pass(booked, current, false) : fail(booked, current, c.twins);
		}
		case 'ERROR_REVIEW_ANSWERED': {
			const r = run?.attempt;
			// R-K4: every error card of the attempt once right; a wrong answer just comes again.
			if (!run || !r || r.kind !== 'ERROR_REVIEW' || !event.correct || !r.cardIds.includes(event.cardId) || r.done.includes(event.cardId)) return s;
			const done = [...r.done, event.cardId];
			if (done.length < r.cardIds.length) return withAttempt(s, { ...r, done });
			return nextAttempt(s, run, run.recovery ?? policy.recoveryAfterFail(s, run));
		}
		case 'REVIEW_ANSWERED': {
			const card = s.review.cards[event.cardId];
			// Only a due card in its current direction is booked (idempotent against double taps).
			if (!card || card.mastered || card.due > today || card.nextDirection !== event.direction) return s;
			const next = answerCard(card, event.correct, today, policy.config);
			return counted({ ...s, review: { ...s.review, cards: { ...s.review.cards, [card.id]: next } } }, event.correct);
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
		case 'ACTIVITY':
			return s;
	}
};

// Every event runs through the day bookkeeping (R-D1, R-S1–R-S5) after the core rules.
export const makeReducer = (policy: RulePolicy, chapterOrder: readonly ChapterId[], content: ContentInfo = noContent): Reducer => {
	const core = makeCoreReducer(policy, chapterOrder, content);
	return (state, event) => trackDay(core(state, event), localDate(event.at, event.tzOffsetMin), event.type === 'ACTIVITY' ? event.sec : 0);
};

export const newGame = (policy: RulePolicy): GameState => initialState({ id: policy.id, version: policy.version });
