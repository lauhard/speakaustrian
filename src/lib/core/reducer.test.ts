import { describe, expect, it } from 'vitest';
import { makeDefaultPolicy, type RulePolicy } from './policy';
import { localDate, makeReducer, newGame, planDay, type GameEvent } from './reducer';
import { GameState } from './state';

const order = ['A1-01', 'A1-02', 'A1-03'];
const policy = makeDefaultPolicy(order);
const base = { tzOffsetMin: 60 };
let n = 0;
const ev = <T extends object>(e: T, at = '2026-11-16T10:00:00Z') => ({ id: `e${n++}`, at, ...base, ...e }) as unknown as GameEvent;
const play = (p: RulePolicy, events: GameEvent[]) => events.reduce(makeReducer(p, order), newGame(p));
const started = ev({ type: 'PROFILE_CREATED', name: ' Maria ', pensumMin: 90 });
const skip = ev({ type: 'OVERRIDE_GRANTED', grant: { grantId: 'g1', kind: 'CHAPTER_SKIP', target: 'A1-01', source: 'debug' } });

describe('time', () => {
	it('R-D1: local date follows the device offset, also across midnight', () => {
		expect(localDate('2026-11-16T23:30:00Z', 60)).toBe('2026-11-17');
		expect(localDate('2026-11-16T00:30:00Z', -120)).toBe('2026-11-15');
	});
	it('plan day counts from 1', () => {
		expect(planDay('2026-11-16', '2026-11-16')).toBe(1);
		expect(planDay('2026-11-16', '2026-12-01')).toBe(16);
	});
});

describe('profile and lessons', () => {
	it('creates the profile and opens the first chapter with base lives', () => {
		const s = play(policy, [started]);
		expect(s.profile).toEqual({ name: 'Maria', startDate: '2026-11-16', pensumMin: 90 });
		expect(s.course.phase).toEqual({ kind: 'CHAPTER', id: 'A1-01' });
		expect(s.course.chapter?.startLives).toBe(3);
		expect(s.ruleset).toEqual({ id: 'default', version: 1 });
		expect(GameState.safeParse(s).success).toBe(true);
	});
	it('books a finished lesson once and ignores other chapters', () => {
		const done = ev({ type: 'LESSON_COMPLETED', chapterId: 'A1-01', lessonId: 'A1-01-L01' });
		const other = ev({ type: 'LESSON_COMPLETED', chapterId: 'DEMO', lessonId: 'DEMO-01' });
		const s = play(policy, [started, done, done, other]);
		expect(s.course.chapter?.attempt).toEqual({ kind: 'LESSONS', repeatMode: false, done: ['A1-01-L01'] });
	});
});

describe('access (R-F1)', () => {
	it('opens only the chapter in work', () => {
		const s = play(policy, [started]);
		expect(policy.canAccessChapter(s, 'A1-01').allowed).toBe(true);
		expect(policy.canAccessChapter(s, 'A1-02')).toEqual({ allowed: false, reason: 'previous-chapter' });
	});
});

describe('policy seam (D16)', () => {
	it('T-PL01: default policy records and rejects an override, nothing else changes', () => {
		const before = play(policy, [started]);
		const after = play(policy, [started, skip]);
		expect(after.overrides).toHaveLength(1);
		expect(after.overrides[0].decision.accepted).toBe(false);
		expect(after.course).toEqual(before.course);
	});
	it('T-PL02: a stub policy can complete a chapter as skipped and the course moves on', () => {
		const stub: RulePolicy = {
			...policy,
			id: 'stub',
			acceptOverride: (_s, o) => ({
				accepted: true,
				effects: [{ kind: 'COMPLETE_CHAPTER', chapterId: o.target, completion: { reason: 'skipped', at: 'x', grantId: o.grantId } }]
			})
		};
		const s = play(stub, [started, skip, skip]);
		expect(s.course.completed['A1-01'].reason).toBe('skipped');
		expect(s.course.phase).toEqual({ kind: 'CHAPTER', id: 'A1-02' });
		expect(s.overrides).toHaveLength(1);
		expect(stub.canAccessChapter(s, 'A1-02').allowed).toBe(true);
	});
	it('R-PL4: unknown override kinds do not pass the schema', () => {
		const s = play(policy, [started, skip]);
		const tampered = structuredClone(s) as unknown as { overrides: { grant: { kind: string } }[] };
		tampered.overrides[0].grant.kind = 'TELEPORT';
		expect(GameState.safeParse(tampered).success).toBe(false);
	});
	it('R-L1/R-L3: start lives come from the policy config and are capped', () => {
		const s = { ...play(policy, [started]), course: { ...play(policy, [started]).course, nextChapterBonus: 2 as const } };
		expect(policy.startLives(s, 'A1-02')).toBe(5);
		expect(makeDefaultPolicy(order, { ...policy.config, LIVES_BASE: 4 }).startLives(s, 'A1-02')).toBe(5);
	});
});

describe('migration from storage v1', () => {
	it('replays the old profile and its finished lessons', async () => {
		const { legacyEvents } = await import('./migrate');
		const events = legacyEvents({ name: 'Maria', createdAt: '2026-11-10T08:00:00Z', lessonsDone: ['A1-01-L02', 'DEMO-01'] }, 60);
		const s = play(policy, events);
		expect(s.profile?.startDate).toBe('2026-11-10');
		expect(s.course.chapter?.attempt).toMatchObject({ kind: 'LESSONS', done: ['A1-01-L02'] });
	});
});
