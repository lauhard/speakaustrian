import { ChapterContent, Course, type Discipline, type Item, type Lesson } from '../core/content/schema';
import a101 from './a1-01.json';
import courseRaw from './course.json';
import demo from './demo.json';

// Parsing at import time makes invalid content fail the build and the unit tests.
export const course: Course = Course.parse(courseRaw);
export const chapters: ChapterContent[] = [a101, demo].map((raw) => ChapterContent.parse(raw));

export const PREVIEW_CHAPTER = 'DEMO';

export const chapterContent = (chapterId: string): ChapterContent | undefined =>
	chapters.find((c) => c.chapterId === chapterId);

export const findLesson = (chapterId: string, lessonId: string): Lesson | undefined =>
	chapterContent(chapterId)?.lessons.find((l) => l.id === lessonId);

export const allItems = (): Item[] => chapters.flatMap((c) => c.lessons.flatMap((l) => l.items));

export type PracticeFilter = Discipline | 'bild';

export const matchesFilter = (item: Item, filter: PracticeFilter): boolean =>
	filter === 'bild' ? item.image !== undefined : item.skill === filter;

export const availableFilters = (items: readonly Item[]): PracticeFilter[] =>
	(['lesen', 'hoeren', 'schreiben', 'sprechen', 'grammatikWortschatz', 'werte', 'bild'] as const).filter((f) =>
		items.some((i) => matchesFilter(i, f))
	);

// Free practice (D22): a random selection, no lives, no effect on chapter progress.
export const pickPractice = (
	items: readonly Item[],
	filter: PracticeFilter,
	count: number,
	random: () => number
): Item[] => {
	const pool = items.filter((i) => matchesFilter(i, filter));
	// Fisher-Yates on a copy with an injectable random source (testable).
	const shuffled = pool.reduce<Item[]>((acc, item, i) => {
		const j = Math.floor(random() * (i + 1));
		const next = [...acc, item];
		[next[i], next[j]] = [next[j], next[i]];
		return next;
	}, []);
	return shuffled.slice(0, count);
};
