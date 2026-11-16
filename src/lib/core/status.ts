import type { GameState } from './state';

// Where a chapter stands, for overview screens. Pure: derived from the state, never stored.
export type ChapterPhase = 'new' | 'lessons' | 'practice' | 'gate' | 'test' | 'review' | 'passed';
export type ChapterStatus = { phase: ChapterPhase; lessonsDone: number; lessonsTotal: number };

const PHASE: Record<string, ChapterPhase> = {
	LESSONS: 'lessons',
	PRACTICE: 'practice',
	GATE: 'gate',
	TARGETED_PRACTICE: 'gate',
	TEST_READY: 'test',
	TEST: 'test',
	CORRECTION: 'test',
	ERROR_REVIEW: 'review'
};

export const chapterStatus = (s: GameState, chapterId: string, lessonIds: readonly string[]): ChapterStatus => {
	const total = lessonIds.length;
	if (chapterId in s.course.completed) return { phase: 'passed', lessonsDone: total, lessonsTotal: total };
	const run = s.course.chapter?.id === chapterId ? s.course.chapter : null;
	if (!run) return { phase: 'new', lessonsDone: 0, lessonsTotal: total };
	const a = run.attempt;
	// After the lessons every lesson is done, even though the attempt no longer lists them (bug: home showed 0/7).
	const done = a.kind === 'LESSONS' ? lessonIds.filter((l) => a.done.includes(l)).length : total;
	return { phase: PHASE[a.kind] ?? 'lessons', lessonsDone: done, lessonsTotal: total };
};
