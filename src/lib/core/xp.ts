// XP and level (K9, docs/concepts/xp-flammen-kapitelfluss.md §3). Pure reward rules, device-local, never a pass rule (D8).
// Start values; the pilot (phase 7) calibrates them.
export const XP_ANSWER = { lesson: 5, practice: 5, gate: 8, target: 8, test: 10, review: 3 } as const;
export type XpKind = keyof typeof XP_ANSWER;
export const XP_LESSON_PASS = 20;
export const XP_LESSON_STARS3 = 10;
export const XP_GATE_PASS = 30;
export const XP_TEST_PASS = 100;
export const XP_TEST_PERFECT = 50;
export const XP_DAY_GOAL = 25;
// An already passed lesson again, and free mode / free practice: half the XP (no farming, concept §4).
export const XP_REDUCED = 0.5;
export const LEVEL_STEP = 100;

/** `chapterId`: the running course chapter, whose XP feed the flame bonus; null elsewhere. */
export type XpContext = { chapterId: string | null; reduced: boolean };
export type Xp = {
	total: number;
	// XP earned in the running course chapter, the base of the flame bonus
	chapter: Record<string, number>;
	// lessons whose first pass was paid (a repeated chapter attempt pays it once only)
	lessons: string[];
	// days whose day goal was paid
	days: string[];
	// passed chapters: chapter XP and flame bonus (trophy step)
	closed: Record<string, { xp: number; bonus: number }>;
};
export const emptyXp: Xp = { total: 0, chapter: {}, lessons: [], days: [], closed: {} };

export const scaled = (amount: number, ctx: XpContext): number => (ctx.reduced ? Math.round(amount * XP_REDUCED) : amount);

export const award = (x: Xp, amount: number, ctx: XpContext): Xp => {
	const xp = scaled(amount, ctx);
	if (xp <= 0) return x;
	const chapter = ctx.chapterId ? { ...x.chapter, [ctx.chapterId]: (x.chapter[ctx.chapterId] ?? 0) + xp } : x.chapter;
	return { ...x, total: x.total + xp, chapter };
};

/** First pass of a lesson: +20, +10 more with 3 stars (≥ 90 %); once per lesson. */
export const lessonPassed = (x: Xp, lessonId: string, percent: number, ctx: XpContext): Xp =>
	x.lessons.includes(lessonId) ? x : { ...award(x, XP_LESSON_PASS + (percent >= 90 ? XP_LESSON_STARS3 : 0), ctx), lessons: [...x.lessons, lessonId] };

export const dayGoal = (x: Xp, day: string): Xp => (x.days.includes(day) ? x : { ...award(x, XP_DAY_GOAL, { chapterId: null, reduced: false }), days: [...x.days.slice(-30), day] });

/** Chapter passed: test XP (+100, perfect +50), then the flame bonus = chapter XP × (multiplier − 1); once per chapter. */
export const chapterPassed = (x: Xp, chapterId: string, perfectTest: boolean, mult: number, ctx: XpContext): Xp => {
	if (x.closed[chapterId]) return x;
	const withTest = award(x, XP_TEST_PASS + (perfectTest ? XP_TEST_PERFECT : 0), ctx);
	const xp = withTest.chapter[chapterId] ?? 0;
	const bonus = ctx.chapterId === chapterId ? Math.round(xp * (mult - 1)) : 0;
	const { [chapterId]: _done, ...chapter } = withTest.chapter;
	return { ...withTest, total: withTest.total + bonus, chapter, closed: { ...x.closed, [chapterId]: { xp: ctx.chapterId === chapterId ? xp : scaled(XP_TEST_PASS + (perfectTest ? XP_TEST_PERFECT : 0), ctx), bonus } } };
};

/** Level n → n+1 costs 100 × n XP. */
export const levelOf = (total: number): { level: number; into: number; need: number } => {
	let level = 1;
	let rest = total;
	while (rest >= LEVEL_STEP * level) rest -= LEVEL_STEP * level++;
	return { level, into: rest, need: LEVEL_STEP * level };
};
