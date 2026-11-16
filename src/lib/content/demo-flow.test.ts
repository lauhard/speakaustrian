import { describe, expect, it } from 'vitest';
import { contentInfo, findItem, poolItems, chapterContent } from './index';
import { gradeItem, passes, type Response } from '../core/grading';
import { gateDraw, nextGateItem, targetedItems, testDraw } from '../core/flow';
import { demoConfig, makeDefaultPolicy } from '../core/policy';
import { makeReducer, newGame, type GameEvent } from '../core/reducer';
import type { GameState } from '../core/state';
import type { Item } from '../core/content/schema';

// DEMO sandbox (005c): the whole chapter loop on the real demo pool with the small rule config.
const policy = { ...makeDefaultPolicy(['DEMO'], demoConfig), id: 'demo' };
const reduce = makeReducer(policy, ['DEMO'], contentInfo);
const practice = poolItems('DEMO', 'practice');
const test = poolItems('DEMO', 'test');

let n = 0;
const ev = <T extends object>(e: T) => ({ id: `e${n++}`, at: '2026-11-16T10:00:00Z', tzOffsetMin: 60, ...e }) as unknown as GameEvent;
const send = (s: GameState, ...events: object[]) => events.reduce<GameState>((acc, e) => reduce(acc, ev(e)), s);
const attempt = (s: GameState) => s.course.chapter!.attempt;

const right = (i: Item): Response =>
	i.type === 'choice' ? { type: 'choice', selected: i.answer } : i.type === 'short' ? { type: 'short', text: i.accept[0] } : { type: 'cloze', gaps: Object.fromEntries(Object.entries(i.gaps).map(([k, g]) => [k, g.accept[0]])) };
const wrong = (i: Item): Response =>
	i.type === 'choice' ? { type: 'choice', selected: (i.answer + 1) % i.options.length } : i.type === 'short' ? { type: 'short', text: 'xyz' } : { type: 'cloze', gaps: Object.fromEntries(Object.keys(i.gaps).map((k) => [k, 'xyz'])) };
const answer = (id: string, ok: boolean) => {
	const item = findItem(id)!;
	return passes(gradeItem(item, ok ? right(item) : wrong(item)).verdict);
};

const start = () => send(newGame(policy), { type: 'PROFILE_CREATED', name: 'Maria', pensumMin: 90 });
const toPractice = (s: GameState) => send(s, ...chapterContent('DEMO')!.lessons.map((l) => ({ type: 'LESSON_COMPLETED', chapterId: 'DEMO', lessonId: l.id })));
const doPractice = (s: GameState) => send(s, ...practice.map((p) => ({ type: 'PRACTICE_ANSWERED', itemId: p.id, correct: true })));
// Plays the readiness block with the given number of wrong answers.
const doGate = (s: GameState, wrongCount: number) => {
	const run = s.course.chapter!;
	if (run.attempt.kind !== 'GATE') throw new Error(`expected GATE, got ${run.attempt.kind}`);
	const draw = gateDraw(policy, s, run, practice, run.attempt.block);
	return send(s, ...draw.map((itemId, i) => ({ type: 'GATE_ANSWERED', itemId, correct: i >= wrongCount })));
};
const toTestReady = (s: GameState) => doGate(doPractice(toPractice(s)), 0);
const startTest = (s: GameState, attemptId: string) => send(s, { type: 'TEST_STARTED', attemptId, itemIds: testDraw(policy, s, s.course.chapter!, test, attemptId) });
const testItems = (s: GameState) => (attempt(s) as { items: string[] }).items;

describe('DEMO pool', () => {
	it('has a twin for every test item and every item grades right with its own answer', () => {
		for (const p of test) expect(test.filter((t) => t.family === p.family).length).toBeGreaterThanOrEqual(2);
		for (const id of [...practice, ...test].map((p) => p.id)) expect(answer(id, true), id).toBe(true);
		for (const id of [...practice, ...test].map((p) => p.id)) expect(answer(id, false), id).toBe(false);
	});
	it('draws one item per discipline for the test and the readiness block', () => {
		const s = toTestReady(start());
		const items = testDraw(policy, s, s.course.chapter!, test, 'a1');
		expect(items).toHaveLength(3);
		expect(new Set(items.map((id) => test.find((t) => t.id === id)!.skill)).size).toBe(3);
		expect(gateDraw(policy, s, s.course.chapter!, practice, 1)).toHaveLength(demoConfig.GATE_ITEMS);
	});
	it('serves the next unanswered item of a block', () => {
		expect(nextGateItem(['a', 'b', 'c'], ['a'])).toBe('b');
		expect(nextGateItem(['a'], ['a'])).toBeUndefined();
	});
});

describe('chapter loop on DEMO', () => {
	it('walks lessons → practice → readiness → test → passed', () => {
		let s = start();
		expect(attempt(s).kind).toBe('LESSONS');
		s = toPractice(s);
		expect(attempt(s)).toMatchObject({ kind: 'PRACTICE', total: practice.length });
		s = doPractice(s);
		expect(attempt(s)).toMatchObject({ kind: 'GATE', block: 1 });
		s = doGate(s, 0);
		expect(attempt(s).kind).toBe('TEST_READY');
		s = startTest(s, 'a1');
		s = send(s, ...testItems(s).map((itemId) => ({ type: 'TEST_ANSWERED', attemptId: 'a1', itemId, correct: true })));
		expect(s.course.completed.DEMO).toBeDefined();
		expect(s.course.nextChapterBonus).toBe(1);
		expect(s.course.phase.kind).toBe('EXIT_CHAIN');
	});
	it('sends a gate below the threshold to targeted practice on the missed goals, then a new block', () => {
		let s = doGate(doPractice(toPractice(start())), 2);
		const a = attempt(s);
		expect(a.kind).toBe('TARGETED_PRACTICE');
		const goals = (a as { goalIds: string[] }).goalIds;
		expect(goals.length).toBeGreaterThan(0);
		expect(targetedItems(practice, goals).length).toBeGreaterThan(0);
		s = send(s, { type: 'TARGETED_PRACTICE_DONE' });
		expect(attempt(s)).toMatchObject({ kind: 'GATE', block: 2 });
	});
	it('one error → correction round with a twin that was not in the test → passed without bonus', () => {
		let s = startTest(toTestReady(start()), 'a1');
		const [first, ...rest] = testItems(s);
		s = send(s, { type: 'TEST_ANSWERED', attemptId: 'a1', itemId: first, correct: false }, ...rest.map((itemId) => ({ type: 'TEST_ANSWERED', attemptId: 'a1', itemId, correct: true })));
		const a = attempt(s);
		if (a.kind !== 'CORRECTION') throw new Error(`expected CORRECTION, got ${a.kind}`);
		expect(a.twins).toHaveLength(1);
		expect(contentInfo.baseOf(a.twins[0])).toBe(contentInfo.baseOf(first));
		expect(a.twins[0]).not.toBe(first);
		s = send(s, { type: 'CORRECTION_ANSWERED', attemptId: 'a1', twinId: a.twins[0], correct: true });
		expect(s.course.completed.DEMO).toBeDefined();
		expect(s.course.nextChapterBonus).toBe(0);
		expect(Object.values(s.review.cards).some((c) => c.kind === 'error')).toBe(true);
	});
	it('two errors cost both lives → error review → whole chapter again with a new test selection', () => {
		let s = startTest(toTestReady(start()), 'a1');
		const first = testItems(s);
		s = send(s, ...first.slice(0, 2).map((itemId) => ({ type: 'TEST_ANSWERED', attemptId: 'a1', itemId, correct: false })));
		const review = attempt(s);
		if (review.kind !== 'ERROR_REVIEW') throw new Error(`expected ERROR_REVIEW, got ${review.kind}`);
		s = send(s, ...review.cardIds.map((cardId) => ({ type: 'ERROR_REVIEW_ANSWERED', cardId, correct: true })));
		expect(s.course.chapter).toMatchObject({ attemptNo: 2, attempt: { kind: 'LESSONS', repeatMode: true } });
		s = toTestReady(s);
		s = startTest(s, 'a2');
		const second = testItems(s);
		// R-T4: the pool has two families per discipline, so attempt 2 uses the families attempt 1 did not.
		const fams = (ids: string[]) => ids.map((id) => contentInfo.baseOf(id));
		expect(fams(second).some((f) => !fams(first).includes(f))).toBe(true);
	});
});
