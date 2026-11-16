import { describe, expect, it } from 'vitest';
import { makeDefaultPolicy } from './policy';
import { makeReducer, newGame, type ContentInfo, type GameEvent } from './reducer';
import { chapterStatus } from './status';

const order = ['A1-01', 'A1-02'];
const policy = makeDefaultPolicy(order);
const content: ContentInfo = { chapter: () => ({ lessonIds: ['L1', 'L2'], practiceTotal: 1 }), baseOf: (i) => i, twinsOf: () => [], goalsOf: () => [], refsOf: () => [] };
let n = 0;
const ev = (e: object) => ({ id: `e${n++}`, at: '2026-11-16T10:00:00Z', tzOffsetMin: 60, ...e }) as unknown as GameEvent;
const play = (events: object[]) => events.map(ev).reduce(makeReducer(policy, order, content), newGame(policy));
const profile = { type: 'PROFILE_CREATED', name: 'Maria', pensumMin: 90 };
const lesson = (lessonId: string) => ({ type: 'LESSON_COMPLETED', chapterId: 'A1-01', lessonId });

describe('chapterStatus', () => {
	it('counts done lessons while in the lessons', () => {
		expect(chapterStatus(play([profile, lesson('L1')]), 'A1-01', ['L1', 'L2'])).toEqual({ phase: 'lessons', lessonsDone: 1, lessonsTotal: 2 });
	});
	it('shows all lessons done once the attempt moved on to practice', () => {
		expect(chapterStatus(play([profile, lesson('L1'), lesson('L2')]), 'A1-01', ['L1', 'L2'])).toEqual({ phase: 'practice', lessonsDone: 2, lessonsTotal: 2 });
	});
	it('is new for a chapter that is not in work', () => {
		expect(chapterStatus(play([profile]), 'A1-02', ['L1']).phase).toBe('new');
	});
});
