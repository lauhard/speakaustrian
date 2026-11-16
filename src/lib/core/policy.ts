import type { ChapterId, ChapterRun, Completion, GameState, OverrideDecision, OverrideGrant } from './state';

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
	// R-PL2: the default rules reject every override (D11: no skipping).
	acceptOverride: () => ({ accepted: false, reason: 'default policy accepts no overrides' })
});
