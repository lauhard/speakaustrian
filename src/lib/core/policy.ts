import type { ChapterId, ChapterRun, Completion, GameState, OverrideDecision, OverrideGrant, RecoveryPlan } from './state';

// Rule policy (D16, docs/spec/04a §1a): the reducer does the mechanics, every rule decision is
// asked here. Decision points are added to this interface in the step that first needs them
// (see docs/ROADMAP.md); nothing in the core may hard-code a rule (R-PL1).

export type Access = { allowed: true } | { allowed: false; reason: 'previous-chapter' | 'milestone' | 'unknown-chapter' };

// Constants of 04a §7. Only values used by implemented rules are listed; the rest follows per step.
export type RuleConfig = {
	LIVES_BASE: number;
	LIVES_MAX: number;
	BONUS_MAX: number;
	GATE_ITEMS: number;
	GATE_MIN_CORRECT: number;
	LEITNER_INTERVALS_DAYS: readonly number[];
};

export interface RulePolicy {
	id: string;
	version: number;
	config: RuleConfig;
	canAccessChapter(s: GameState, c: ChapterId): Access;
	completionOnPass(s: GameState, c: ChapterId, run: ChapterRun, at: string): Completion;
	startLives(s: GameState, c: ChapterId): number;
	isTestReady(gate: { correct: number; answered: number }): boolean;
	// Asked after every test answer; 'CONTINUE' (not in the 04a sketch, G-008) keeps the lives rule out of the core.
	outcomeAfterTest(run: ChapterRun): 'CONTINUE' | 'PASSED' | 'CORRECTION' | 'FAILED';
	// Asked after a wrong twin or after the last twin.
	outcomeAfterCorrection(run: ChapterRun, allCorrect: boolean): 'PASSED' | 'FAILED';
	recoveryAfterFail(s: GameState, run: ChapterRun): RecoveryPlan;
	bonusForNext(s: GameState, run: ChapterRun, perfectFirst: boolean): 0 | 1 | 2;
	acceptOverride(s: GameState, o: OverrideGrant): OverrideDecision;
}

export const defaultConfig: RuleConfig = {
	LIVES_BASE: 3,
	LIVES_MAX: 5,
	BONUS_MAX: 2,
	GATE_ITEMS: 20,
	GATE_MIN_CORRECT: 18,
	LEITNER_INTERVALS_DAYS: [1, 3, 7, 14, 30]
};

const examDone = (s: GameState, kind: string, mustPass: boolean): boolean =>
	s.course.examHistory.some((e) => e.kind === kind && (!mustPass || e.passed));

// The chapter order comes from the course content, so the policy stays free of content knowledge.
export const makeDefaultPolicy = (chapterOrder: readonly ChapterId[], config: RuleConfig = defaultConfig): RulePolicy => ({
	id: 'default',
	version: 1,
	config,
	// R-F1 linear unlock, R-F3 locks at milestones.
	canAccessChapter: (s, c) => {
		const index = chapterOrder.indexOf(c);
		if (index < 0) return { allowed: false, reason: 'unknown-chapter' };
		if (c in s.course.completed) return { allowed: true };
		if (index > 0 && !(chapterOrder[index - 1] in s.course.completed)) return { allowed: false, reason: 'previous-chapter' };
		if (c === 'A2-01' && !examDone(s, 'MS-A1', true)) return { allowed: false, reason: 'milestone' };
		if (c === 'A2-11' && !examDone(s, 'SIM-A2-1', false)) return { allowed: false, reason: 'milestone' };
		return { allowed: true };
	},
	completionOnPass: (_s, _c, _run, at) => ({ reason: 'passed', at }),
	// R-L1, R-L3: base lives plus the bonus earned in the previous chapter, capped.
	startLives: (s) => Math.min(config.LIVES_MAX, config.LIVES_BASE + s.course.nextChapterBonus),
	// R-G2
	isTestReady: (gate) => gate.answered >= config.GATE_ITEMS && gate.correct >= config.GATE_MIN_CORRECT,
	// R-L1: no lives left ends the attempt at once. R-F2: passed only without errors, otherwise correction.
	outcomeAfterTest: (run) => {
		const t = run.attempt;
		if (t.kind !== 'TEST') return 'CONTINUE';
		if (t.lives <= 0) return 'FAILED';
		if (t.idx < t.items.length) return 'CONTINUE';
		return t.wrong.length === 0 ? 'PASSED' : 'CORRECTION';
	},
	// R-K2: one wrong twin fails the attempt.
	outcomeAfterCorrection: (_run, allCorrect) => (allCorrect ? 'PASSED' : 'FAILED'),
	// R-K4, R-K5: error review, then the whole chapter again in repeat mode with a new selection.
	recoveryAfterFail: () => ({ errorReview: true, entry: 'LESSONS', repeatMode: true, resetLives: true, newSelection: true }),
	// R-L3 (I-2): only a perfect first attempt adds to the bonus this chapter started with.
	bonusForNext: (s, _run, perfectFirst) => (perfectFirst ? (Math.min(config.BONUS_MAX, s.course.nextChapterBonus + 1) as 0 | 1 | 2) : 0),
	// R-PL2: the default rules reject every override (D11: no skipping).
	acceptOverride: () => ({ accepted: false, reason: 'default policy accepts no overrides' })
});
