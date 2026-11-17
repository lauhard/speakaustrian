import type { Score } from './state';

// K6, G-019 (decided A, Andi 18.11.2026): chapter rating from the accuracy of all graded chapter answers.
// 1 star for passing, 2 from 70 %, 3 from 90 % – the same steps as the lesson stars. A reward, never a pass rule (D8).
export const CHAPTER_STAR_PCT = [70, 90] as const;

export const accuracyPct = (s: Score): number => (s.total === 0 ? 100 : Math.round((s.correct / s.total) * 100));

export const chapterStars = (chapter: Score): 1 | 2 | 3 => {
	const pct = accuracyPct(chapter);
	return (1 + CHAPTER_STAR_PCT.filter((min) => pct >= min).length) as 1 | 2 | 3;
};
