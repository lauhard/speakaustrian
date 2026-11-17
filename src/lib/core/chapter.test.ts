import { describe, expect, it } from 'vitest';
import { makeDefaultPolicy, type RulePolicy } from './policy';
import { makeReducer, newGame, settleChapter, type ContentInfo, type GameEvent } from './reducer';
import { GameState } from './state';
import { practiceItemAt } from './flow';

// Chapter attempt automaton (docs/spec/04a §4.2), test cases of docs/spec/04b §1–5 and §13a.
const order = ['A1-01', 'A1-02', 'A1-03', 'A1-04'];
const policy = makeDefaultPolicy(order);
// Item families: "t3" is a base item, "t3a"/"t3b" are its twins.
const base = (id: string) => id.replace(/[ab]$/, '');
const content: ContentInfo = {
	chapter: () => ({ lessonIds: ['L1', 'L2'], practiceTotal: 2 }),
	baseOf: base,
	twinsOf: (id) => [base(id), `${base(id)}a`, `${base(id)}b`].filter((t) => t !== id),
	goalsOf: (id) => [`goal-${base(id)}`],
	refsOf: (id) => (id === 't1' ? ['W-A1-0001'] : [])
};
let n = 0;
const ev = <T extends object>(e: T, at = '2026-11-16T10:00:00Z') => ({ id: `e${n++}`, at, tzOffsetMin: 60, ...e }) as unknown as GameEvent;
const run = (p: RulePolicy, s: GameState, events: GameEvent[]) => events.reduce(makeReducer(p, order, content), s);
const play = (events: GameEvent[], p: RulePolicy = policy) => run(p, newGame(p), events);

const items = Array.from({ length: 20 }, (_, i) => `t${i + 1}`);
const profile = ev({ type: 'PROFILE_CREATED', name: 'Maria', pensumMin: 90 });
const lessons = (c: string) => ['L1', 'L2'].map((lessonId) => ev({ type: 'LESSON_COMPLETED', chapterId: c, lessonId }));
const practice = [ev({ type: 'PRACTICE_ANSWERED', itemId: 'p1', correct: true }), ev({ type: 'PRACTICE_ANSWERED', itemId: 'p2', correct: true })];
const gate = (wrong: number, block = 1) =>
	Array.from({ length: 20 }, (_, i) => ev({ type: 'GATE_ANSWERED', itemId: `g${block}-${i + 1}`, correct: i >= wrong }));
const start = (attemptId: string, itemIds = items) => ev({ type: 'TEST_STARTED', attemptId, itemIds });
// Answers the test in order; `wrong` lists the positions (0-based) answered wrong.
const answers = (attemptId: string, wrong: number[], count = 20) =>
	items.slice(0, count).map((itemId, i) => ev({ type: 'TEST_ANSWERED', attemptId, itemId, correct: !wrong.includes(i) }));
const toTestReady = (c: string) => [...lessons(c), ...practice, ...gate(0)];
const perfect = (c: string, attemptId: string) => [...toTestReady(c), start(attemptId), ...answers(attemptId, [])];
const attempt = (s: GameState) => s.course.chapter!.attempt;
const twinsOf = (s: GameState) => {
	const a = attempt(s);
	if (a.kind !== 'CORRECTION') throw new Error(`expected CORRECTION, got ${a.kind}`);
	return a.twins;
};
const correction = (attemptId: string, s: GameState, wrongAt = -1) =>
	twinsOf(s).map((twinId, i) => ev({ type: 'CORRECTION_ANSWERED', attemptId, twinId, correct: i !== wrongAt }));
const review = (s: GameState) => {
	const a = attempt(s);
	if (a.kind !== 'ERROR_REVIEW') throw new Error(`expected ERROR_REVIEW, got ${a.kind}`);
	return a.cardIds.map((cardId) => ev({ type: 'ERROR_REVIEW_ANSWERED', cardId, correct: true }));
};

describe('lessons → practice → readiness round (R-G)', () => {
	it('moves to practice after the last lesson and to the gate after the last practice item', () => {
		const s1 = play([profile, ...lessons('A1-01')]);
		expect(attempt(s1)).toEqual({ kind: 'PRACTICE', answered: 0, total: 2 });
		const s2 = run(policy, s1, practice);
		expect(attempt(s2)).toEqual({ kind: 'GATE', block: 1, items: [], wrong: [], correct: 0, answered: 0 });
	});
	it('K3: practice can be skipped straight to the readiness round; skipping elsewhere changes nothing', () => {
		const skipPractice = ev({ type: 'PRACTICE_SKIPPED' });
		const s1 = play([profile, ...lessons('A1-01'), skipPractice]);
		expect(attempt(s1)).toEqual({ kind: 'GATE', block: 1, items: [], wrong: [], correct: 0, answered: 0 });
		expect(run(policy, s1, [skipPractice])).toEqual(s1);
		const inLessons = play([profile]);
		expect(run(policy, inLessons, [skipPractice])).toEqual(inLessons);
	});
	it('K3: each attempt practises the next round of the practice part', () => {
		const part = Array.from({ length: 40 }, (_, i) => ({ id: `p${i}`, skill: 'lesen' as const, family: `p${i}`, goals: [] }));
		expect(practiceItemAt(part, 1, 20, 0)?.id).toBe('p0');
		expect(practiceItemAt(part, 1, 20, 19)?.id).toBe('p19');
		expect(practiceItemAt(part, 2, 20, 0)?.id).toBe('p20');
		expect(practiceItemAt(part, 3, 20, 5)?.id).toBe('p5');
		expect(practiceItemAt(part.slice(0, 15), 2, 20, 0)?.id).toBe('p5');
		expect(practiceItemAt([], 1, 20, 0)).toBeUndefined();
	});
	it('K1: a lesson below 51 % stays open, from 51 % it counts (rounded like the result screen)', () => {
		const lesson = (lessonId: string, correct: number, total: number) => ev({ type: 'LESSON_COMPLETED', chapterId: 'A1-01', lessonId, correct, total });
		const s = play([profile, lesson('L1', 2, 3), lesson('L2', 3, 7)]);
		expect(attempt(s)).toEqual({ kind: 'LESSONS', repeatMode: false, done: ['L1'] });
		expect(policy.isLessonPassed({ correct: 1, total: 2 })).toBe(false);
		expect(policy.isLessonPassed({ correct: 50, total: 99 })).toBe(true);
		expect(policy.isLessonPassed({ correct: 0, total: 0 })).toBe(false);
	});
	it('K2: practice stays locked until every lesson is passed; a later pass unlocks it', () => {
		const lesson = (lessonId: string, correct: number) => ev({ type: 'LESSON_COMPLETED', chapterId: 'A1-01', lessonId, correct, total: 4 });
		const s1 = play([profile, lesson('L1', 4), lesson('L2', 2)]);
		expect(attempt(s1).kind).toBe('LESSONS');
		expect(run(policy, s1, practice)).toEqual(s1);
		const s2 = run(policy, s1, [lesson('L2', 3)]);
		expect(attempt(s2)).toEqual({ kind: 'PRACTICE', answered: 0, total: 2 });
	});
	it('K2: lesson events without a score (older logs) stay valid as passed', () => {
		expect(attempt(play([profile, ...lessons('A1-01')])).kind).toBe('PRACTICE');
	});
	it('stays in the lessons while the chapter content has no pools yet', () => {
		const s = newGame(policy);
		const bare = [profile, ...lessons('A1-01')].reduce(makeReducer(policy, order), s);
		expect(attempt(bare).kind).toBe('LESSONS');
	});
	it('T-G02: 18 of 20 opens the test', () => {
		expect(attempt(play([profile, ...lessons('A1-01'), ...practice, ...gate(2)]))).toEqual({ kind: 'TEST_READY' });
	});
	it('T-G03: 17 of 20 leads to targeted practice for the goals of the wrong items', () => {
		const s = play([profile, ...lessons('A1-01'), ...practice, ...gate(3)]);
		expect(attempt(s)).toEqual({ kind: 'TARGETED_PRACTICE', block: 1, goalIds: ['goal-g1-1', 'goal-g1-2', 'goal-g1-3'], done: false });
	});
	it('T-G04: targeted practice is followed by a new gate block', () => {
		const s = play([profile, ...lessons('A1-01'), ...practice, ...gate(3), ev({ type: 'TARGETED_PRACTICE_DONE', goalIds: [] })]);
		expect(attempt(s)).toMatchObject({ kind: 'GATE', block: 2, answered: 0 });
	});
	it('counts a gate item only once (double tap)', () => {
		const twice = ev({ type: 'GATE_ANSWERED', itemId: 'g1-1', correct: true });
		expect(attempt(play([profile, ...lessons('A1-01'), ...practice, twice, twice]))).toMatchObject({ answered: 1, correct: 1 });
	});
	it('T-G05/T-G06: a wrong gate item creates an error card in box 1, due tomorrow; right answers move no card', () => {
		const s = play([profile, ...lessons('A1-01'), ...practice, ...gate(1)]);
		expect(Object.values(s.review.cards)).toEqual([expect.objectContaining({ id: 'err-g1-1', kind: 'error', refId: 'g1-1', box: 1, due: '2026-11-17' })]);
	});
});

describe('chapter test, lives, correction (R-T, R-L, R-K, R-F2)', () => {
	it('starts the test with the start lives and remembers the drawn items', () => {
		const s = play([profile, ...toTestReady('A1-01'), start('a1')]);
		expect(attempt(s)).toMatchObject({ kind: 'TEST', attemptId: 'a1', items, idx: 0, lives: 3, wrong: [] });
		expect(s.course.chapter!.seenTestItemIds).toEqual(items);
		expect(GameState.safeParse(s).success).toBe(true);
	});
	it('ignores answers that are not for the current item (double tap, stale attempt)', () => {
		const first = ev({ type: 'TEST_ANSWERED', attemptId: 'a1', itemId: 't1', correct: false });
		const stale = ev({ type: 'TEST_ANSWERED', attemptId: 'old', itemId: 't2', correct: false });
		expect(attempt(play([profile, ...toTestReady('A1-01'), start('a1'), first, first, stale]))).toMatchObject({ idx: 1, lives: 2 });
	});
	it('T-L01: the third error ends the attempt at once', () => {
		const s = play([profile, ...toTestReady('A1-01'), start('a1'), ...answers('a1', [0, 1, 2], 3)]);
		expect(attempt(s)).toEqual({ kind: 'ERROR_REVIEW', cardIds: ['err-t1', 'err-t2', 'err-t3'], done: [] });
	});
	it('T-F03/T-K01/T-K02: errors with lives left lead straight to the correction round with unused twins', () => {
		const s = play([profile, ...toTestReady('A1-01'), start('a1'), ...answers('a1', [4, 9])]);
		const twins = twinsOf(s);
		expect(twins.map(base).sort()).toEqual(['t10', 't5']);
		expect(twins.every((t) => !items.includes(t))).toBe(true);
		expect(attempt(s)).toMatchObject({ kind: 'CORRECTION', attemptId: 'a1', idx: 0, livesLeft: 1 });
	});
	it('T-K05: a twin that was already in the test is used when no unused one exists', () => {
		const withTwins = ['t1', 't1a', 't1b', ...items.slice(3)];
		const all = withTwins.map((itemId, i) => ev({ type: 'TEST_ANSWERED', attemptId: 'a1', itemId, correct: i !== 0 }));
		const s = play([profile, ...toTestReady('A1-01'), start('a1', withTwins), ...all]);
		expect(twinsOf(s)).toHaveLength(1);
		expect(base(twinsOf(s)[0])).toBe('t1');
	});
	it('T-F04/T-K04/T-L08: all twins right passes the chapter without a bonus', () => {
		const s1 = play([profile, ...toTestReady('A1-01'), start('a1'), ...answers('a1', [4, 9])]);
		const s2 = run(policy, s1, correction('a1', s1));
		expect(s2.course.completed['A1-01'].reason).toBe('passed');
		expect(s2.course.phase).toEqual({ kind: 'CHAPTER', id: 'A1-02' });
		expect(s2.course.chapter).toMatchObject({ id: 'A1-02', attemptNo: 1, startLives: 3 });
		expect(s2.course.perfectStreak).toEqual({ current: 0, best: 0 });
	});
	it('T-K03/T-L04: a wrong twin ends the round at once', () => {
		const s1 = play([profile, ...toTestReady('A1-01'), start('a1'), ...answers('a1', [4, 9])]);
		const s2 = run(policy, s1, correction('a1', s1, 0).slice(0, 1));
		expect(attempt(s2)).toMatchObject({ kind: 'ERROR_REVIEW', done: [] });
		expect((attempt(s2) as { cardIds: string[] }).cardIds.sort()).toEqual(['err-t10', 'err-t5']);
	});
	it('T-K06/T-K07: after the error review a new attempt repeats the lessons with full lives', () => {
		const s1 = play([profile, ...toTestReady('A1-01'), start('a1'), ...answers('a1', [0, 1, 2], 3)]);
		const [c1, c2, c3] = review(s1);
		const wrong = ev({ type: 'ERROR_REVIEW_ANSWERED', cardId: 'err-t3', correct: false });
		const s2 = run(policy, s1, [c1, c2, wrong]);
		expect(attempt(s2)).toMatchObject({ kind: 'ERROR_REVIEW', done: ['err-t1', 'err-t2'] });
		const s3 = run(policy, s2, [c3]);
		expect(s3.course.chapter).toMatchObject({ attemptNo: 2, startLives: 3, attempt: { kind: 'LESSONS', repeatMode: true, done: [] } });
	});
});

describe('bonus lives (R-L3)', () => {
	it('T-L05–T-L07: perfect first attempts stack the bonus up to 5 lives', () => {
		const s1 = play([profile, ...perfect('A1-01', 'a1')]);
		expect(s1.course.chapter).toMatchObject({ id: 'A1-02', startLives: 4 });
		expect(s1.course.perfectStreak).toEqual({ current: 1, best: 1 });
		const s2 = run(policy, s1, perfect('A1-02', 'a2'));
		expect(s2.course.chapter).toMatchObject({ id: 'A1-03', startLives: 5 });
		const s3 = run(policy, s2, perfect('A1-03', 'a3'));
		expect(s3.course.chapter).toMatchObject({ id: 'A1-04', startLives: 5 });
		expect(s3.course.perfectStreak).toEqual({ current: 3, best: 3 });
	});
	it('T-L02: with 5 lives, 4 errors still reach the correction round', () => {
		const s2 = play([profile, ...perfect('A1-01', 'a1'), ...perfect('A1-02', 'a2'), ...toTestReady('A1-03'), start('a3'), ...answers('a3', [0, 1, 2, 3])]);
		expect(twinsOf(s2)).toHaveLength(4);
	});
	it('T-L09/T-L10: the bonus holds for every attempt; a perfect second attempt earns none', () => {
		const s1 = play([profile, ...perfect('A1-01', 'a1'), ...toTestReady('A1-02'), start('a2'), ...answers('a2', [0, 1, 2, 3], 4)]);
		const s2 = run(policy, s1, review(s1));
		expect(s2.course.chapter).toMatchObject({ id: 'A1-02', attemptNo: 2, startLives: 4 });
		const s3 = run(policy, s2, perfect('A1-02', 'a2b'));
		expect(s3.course.chapter).toMatchObject({ id: 'A1-03', startLives: 3 });
		expect(s3.course.perfectStreak).toEqual({ current: 0, best: 1 });
	});
});

describe('policy seam (R-PL1, R-PL3)', () => {
	it('T-PL03: a stub recovery plan re-enters at TEST_READY instead of the lessons', () => {
		const stub: RulePolicy = {
			...policy,
			recoveryAfterFail: () => ({ errorReview: true, entry: 'TEST_READY', repeatMode: false, resetLives: true, newSelection: true })
		};
		const s1 = play([profile, ...toTestReady('A1-01'), start('a1'), ...answers('a1', [0, 1, 2], 3)], stub);
		const s2 = run(stub, s1, review(s1));
		expect(s2.course.chapter).toMatchObject({ attemptNo: 2, startLives: 3, attempt: { kind: 'TEST_READY' } });
	});
	it('T-PL07: lives and the end of the test are decided by the policy, not the core', () => {
		const stub: RulePolicy = { ...policy, startLives: () => 1, outcomeAfterTest: () => 'CONTINUE' };
		const s = play([profile, ...toTestReady('A1-01'), start('a1'), ...answers('a1', [0, 1], 2)], stub);
		expect(attempt(s)).toMatchObject({ kind: 'TEST', idx: 2, lives: -1 });
	});
});

describe('cards and answer streak (R-W4, R-E1)', () => {
	const intro = ev({ type: 'LESSON_COMPLETED', chapterId: 'A1-01', lessonId: 'L0', introduced: [{ refId: 'W-A1-0001', isNoun: false }] });
	it('R-W4: content answered right in the test moves its box-1 cards to box 2, due in 3 days', () => {
		const s = play([profile, intro, ...toTestReady('A1-01'), start('a1'), ...answers('a1', [], 1)]);
		expect(s.review.cards['card-W-A1-0001']).toMatchObject({ box: 2, due: '2026-11-19' });
	});
	it('R-W4: a wrong test answer leaves the cards where they are', () => {
		const s = play([profile, intro, ...toTestReady('A1-01'), start('a1'), ...answers('a1', [0], 1)]);
		expect(s.review.cards['card-W-A1-0001']).toMatchObject({ box: 1 });
	});
	it('T-E01/T-E02: right answers count up, a wrong one resets, the record stays', () => {
		const s1 = play([profile, ...lessons('A1-01'), ...practice, ...gate(0)]);
		expect(s1.answerStreak).toEqual({ current: 22, best: 22 });
		const s2 = run(policy, s1, [start('a1'), ...answers('a1', [1], 3)]);
		expect(s2.answerStreak).toEqual({ current: 1, best: 23 });
	});
});

describe('override effects (T-PL04)', () => {
	it('a granted attempt replaces the default recovery plan once', () => {
		const plan = { errorReview: true, entry: 'TEST_READY' as const, repeatMode: false, resetLives: true, newSelection: true };
		const stub: RulePolicy = { ...policy, acceptOverride: (_s, o) => ({ accepted: true, effects: [{ kind: 'GRANT_ATTEMPT', chapterId: o.target, plan }] }) };
		const grant = ev({ type: 'OVERRIDE_GRANTED', grant: { grantId: 'g9', kind: 'EXTRA_RETRY', target: 'A1-01', source: 'teacher' } });
		const s1 = play([profile, ...toTestReady('A1-01'), start('a1'), ...answers('a1', [0, 1, 2], 3), grant], stub);
		expect(s1.overrides).toHaveLength(1);
		const s2 = run(stub, s1, review(s1));
		expect(s2.course.chapter).toMatchObject({ attemptNo: 2, attempt: { kind: 'TEST_READY' } });
		expect(s2.course.chapter!.recovery).toBeUndefined();
	});
});

describe('settleChapter (content arrives after the lessons were finished)', () => {
	const noPools: ContentInfo = { ...content, chapter: () => undefined };
	const stale = () => [...lessons('A1-01')].reduce(makeReducer(policy, order, noPools), [profile].reduce(makeReducer(policy, order, noPools), newGame(policy)));
	it('moves a finished LESSONS attempt to PRACTICE once the chapter has pools', () => {
		const s = stale();
		expect(attempt(s).kind).toBe('LESSONS');
		expect(attempt(settleChapter(content)(s)).kind).toBe('PRACTICE');
	});
	it('leaves unfinished lessons and chapters without pools untouched', () => {
		const half = [profile, ...lessons('A1-01').slice(0, 1)].reduce(makeReducer(policy, order, noPools), newGame(policy));
		expect(settleChapter(content)(half)).toBe(half);
		expect(settleChapter(noPools)(stale())).toEqual(stale());
	});
	it('adapts a running practice part to a new size', () => {
		const big: ContentInfo = { ...content, chapter: () => ({ lessonIds: ['L1', 'L2'], practiceTotal: 90 }) };
		const s = [profile, ...lessons('A1-01'), ...practice].reduce(makeReducer(policy, order, big), newGame(policy));
		expect(attempt(s)).toMatchObject({ kind: 'PRACTICE', answered: 2, total: 90 });
		expect(attempt(settleChapter({ ...content, chapter: () => ({ lessonIds: ['L1', 'L2'], practiceTotal: 40 }) })(s))).toMatchObject({ kind: 'PRACTICE', answered: 2, total: 40 });
		expect(attempt(settleChapter(content)(s)).kind).toBe('GATE');
	});
});
