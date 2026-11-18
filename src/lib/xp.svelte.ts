// Device-local XP and level (K9; like flames, not course progress). Rules: core/xp.ts.
import { award, chapterPassed, dayGoal, emptyXp, lessonPassed, levelOf, type Xp, type XpContext } from './core/xp.ts';

const KEY = 'speakaustrian.xp.v1';
const load = (): Xp => {
	try {
		return { ...emptyXp, ...JSON.parse(localStorage.getItem(KEY) ?? '{}') };
	} catch {
		return emptyXp;
	}
};

let s = $state<Xp>(typeof window === 'undefined' ? emptyXp : load());
// Last gain (for the "+N XP" pop) and level-ups.
let fx = $state<{ gain: number; levelUp: boolean; seq: number }>({ gain: 0, levelUp: false, seq: 0 });

const commit = (next: Xp) => {
	if (next === s) return;
	fx = { gain: next.total - s.total, levelUp: levelOf(next.total).level > levelOf(s.total).level, seq: fx.seq + 1 };
	s = next;
	try {
		localStorage.setItem(KEY, JSON.stringify(s));
	} catch {
		/* private mode: keep it in memory */
	}
};

export const xp = {
	get total() { return s.total; },
	get level() { return levelOf(s.total); },
	get fx() { return fx; },
	closedOf: (chapterId: string) => s.closed[chapterId],
	hasLesson: (lessonId: string) => s.lessons.includes(lessonId),
	award: (amount: number, ctx: XpContext | null) => ctx && commit(award(s, amount, ctx)),
	lessonPassed: (lessonId: string, percent: number, ctx: XpContext | null) => ctx && commit(lessonPassed(s, lessonId, percent, ctx)),
	chapterPassed: (chapterId: string, perfectTest: boolean, mult: number, ctx: XpContext | null) => ctx && commit(chapterPassed(s, chapterId, perfectTest, mult, ctx)),
	dayGoal: (day: string) => commit(dayGoal(s, day))
};
