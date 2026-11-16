import { makeContentInfo, poolOf, practiceSplit, type PoolKind } from '../core/content/info';
import { withPools } from '../core/content/merge';
import { ChapterContent, Course, type Discipline, type Item, type Lesson, type Vocab } from '../core/content/schema';
import a101 from './a1-01.json';
import courseRaw from './course.json';
import demo from './demo.json';

// Parsing at import time makes invalid content fail the build and the unit tests.
export const course: Course = Course.parse(courseRaw);
// Pools of real chapters come from `<chapter>-pools.json`, if the file exists (see core/content/merge.ts).
const poolFiles = Object.values(import.meta.glob('./*-pools.json', { eager: true, import: 'default' }));
export const chapters: ChapterContent[] = [a101, demo].map((raw) => ChapterContent.parse(withPools(raw, poolFiles)));

export const PREVIEW_CHAPTER = 'DEMO';

export const contentInfo = makeContentInfo(chapters);
export const practiceParts = (chapterId: string) => practiceSplit(chapterContent(chapterId));
export const poolItems = (chapterId: string, kind: PoolKind) => poolOf(chapterContent(chapterId), kind);

// Any item by id: lessons and pools (error cards and test lists only keep ids).
export const findItem = (itemId: string): Item | undefined =>
	chapters.flatMap((c) => [...c.lessons.flatMap((l) => l.items), ...(c.pools?.practice ?? []), ...(c.pools?.test ?? [])]).find((i) => i.id === itemId);

export const chapterContent = (chapterId: string): ChapterContent | undefined =>
	chapters.find((c) => c.chapterId === chapterId);

export const findLesson = (chapterId: string, lessonId: string): Lesson | undefined =>
	chapterContent(chapterId)?.lessons.find((l) => l.id === lessonId);

export const allVocab = (): Vocab[] => chapters.flatMap((c) => c.vocab ?? []);

export const vocabByRef = (refId: string): Vocab | undefined => allVocab().find((v) => v.id === refId);

// What a lesson introduces, in the shape the LESSON_COMPLETED event needs (R-W2, R-W7).
export const introducedBy = (lesson: Lesson) =>
	(lesson.introduces ?? []).map((refId) => ({ refId, isNoun: vocabByRef(refId)?.article !== undefined }));

// Free practice (D22): lesson tasks plus the practice pool. The test pool stays out, so chapter tests keep fresh tasks.
export const allItems = (): Item[] => chapters.flatMap((c) => [...c.lessons.flatMap((l) => l.items), ...(c.pools?.practice ?? [])]);

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
