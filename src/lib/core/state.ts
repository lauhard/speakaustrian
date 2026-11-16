import { z } from 'zod';
import { Discipline } from './content/schema';

// Game state as specified in docs/spec/04a §2. One zod schema = one source of truth for
// types, persistence and import validation (R-PL4: unknown kinds are rejected, not ignored).

export const LocalDate = z.string().regex(/^\d{4}-\d{2}-\d{2}$/);
export type LocalDate = z.infer<typeof LocalDate>;
// 'DEMO' is the sandbox chapter of the preview (005c); the course itself only has A1-01 … A2-19.
export const ChapterId = z.string().regex(/^(A[12]-\d{2}|DEMO)$/);
export type ChapterId = z.infer<typeof ChapterId>;
export const PensumMin = z.union([z.literal(60), z.literal(90), z.literal(105), z.literal(120)]);
export type PensumMin = z.infer<typeof PensumMin>;

export const Completion = z.object({
	reason: z.enum(['passed', 'skipped', 'waived']),
	at: z.string(),
	grantId: z.string().optional()
});
export type Completion = z.infer<typeof Completion>;

export const RecoveryPlan = z.object({
	errorReview: z.boolean(),
	entry: z.enum(['LESSONS', 'PRACTICE', 'GATE', 'TEST_READY']),
	repeatMode: z.boolean(),
	resetLives: z.boolean(),
	newSelection: z.boolean()
});
export type RecoveryPlan = z.infer<typeof RecoveryPlan>;

export const OverrideGrant = z.object({
	grantId: z.string().min(1),
	kind: z.enum(['CHAPTER_SKIP', 'EXTRA_RETRY', 'RECOVERY_VARIANT']),
	target: z.string().min(1),
	source: z.enum(['placement', 'teacher', 'content-pack', 'debug']),
	reason: z.string().optional(),
	payload: z.record(z.string(), z.unknown()).optional()
});
export type OverrideGrant = z.infer<typeof OverrideGrant>;

export const OverrideEffect = z.discriminatedUnion('kind', [
	z.object({ kind: z.literal('COMPLETE_CHAPTER'), chapterId: ChapterId, completion: Completion }),
	z.object({ kind: z.literal('SET_RECOVERY'), chapterId: ChapterId, plan: RecoveryPlan }),
	z.object({ kind: z.literal('GRANT_ATTEMPT'), chapterId: ChapterId, plan: RecoveryPlan })
]);
export type OverrideEffect = z.infer<typeof OverrideEffect>;

export const OverrideDecision = z.union([
	z.object({ accepted: z.literal(false), reason: z.string() }),
	z.object({ accepted: z.literal(true), effects: z.array(OverrideEffect) })
]);
export type OverrideDecision = z.infer<typeof OverrideDecision>;

export const CoursePhase = z.discriminatedUnion('kind', [
	z.object({ kind: z.literal('NO_PROFILE') }),
	z.object({ kind: z.literal('CHAPTER'), id: ChapterId }),
	z.object({ kind: z.literal('MILESTONE_A1') }),
	z.object({ kind: z.literal('SIM_DIAGNOSIS') }),
	z.object({ kind: z.literal('EXIT_CHAIN') }),
	z.object({ kind: z.literal('MODEL_TEST') }),
	z.object({ kind: z.literal('READY_FOR_EXAM') })
]);
export type CoursePhase = z.infer<typeof CoursePhase>;

export const AttemptState = z.discriminatedUnion('kind', [
	z.object({ kind: z.literal('LESSONS'), repeatMode: z.boolean(), done: z.array(z.string()) }),
	z.object({ kind: z.literal('PRACTICE'), answered: z.number(), total: z.number() }),
	// `wrong` is not in the 04a sketch: the goals for targeted practice (R-G2) are derived from it (G-008).
	z.object({
		kind: z.literal('GATE'),
		block: z.number(),
		items: z.array(z.string()),
		wrong: z.array(z.string()).default([]),
		correct: z.number(),
		answered: z.number()
	}),
	z.object({ kind: z.literal('TARGETED_PRACTICE'), block: z.number().default(1), goalIds: z.array(z.string()), done: z.boolean() }),
	z.object({ kind: z.literal('TEST_READY') }),
	z.object({
		kind: z.literal('TEST'),
		attemptId: z.string(),
		items: z.array(z.string()),
		idx: z.number(),
		lives: z.number(),
		wrong: z.array(z.string()),
		audioPlays: z.record(z.string(), z.number())
	}),
	z.object({ kind: z.literal('CORRECTION'), attemptId: z.string(), twins: z.array(z.string()), idx: z.number(), livesLeft: z.number() }),
	z.object({ kind: z.literal('ERROR_REVIEW'), cardIds: z.array(z.string()), done: z.array(z.string()) }),
	z.object({ kind: z.literal('PASSED'), perfectFirst: z.boolean() })
]);
export type AttemptState = z.infer<typeof AttemptState>;

export const ChapterRun = z.object({
	id: ChapterId,
	attemptNo: z.number().int().positive(),
	startLives: z.number().int().positive(),
	attempt: AttemptState,
	seenTestItemIds: z.array(z.string()),
	// Plan of an accepted override (SET_RECOVERY/GRANT_ATTEMPT); used once instead of the policy's plan.
	recovery: RecoveryPlan.optional(),
	minutesSpent: z.number()
});
export type ChapterRun = z.infer<typeof ChapterRun>;

export const ExamKind = z.enum(['MS-A1', 'SIM-A2-1', 'SIM-A2-2', 'GP-A2']);
export const ExamResult = z.object({
	examId: z.string(),
	kind: ExamKind,
	at: z.string(),
	passed: z.boolean(),
	shares: z.record(z.string(), z.number())
});
export type ExamResult = z.infer<typeof ExamResult>;

export const Direction = z.enum(['recognize', 'produce', 'genus']);
export const Card = z.object({
	id: z.string(),
	kind: z.enum(['vocab', 'set', 'grammar', 'wow', 'error']),
	refId: z.string(),
	box: z.union([z.literal(1), z.literal(2), z.literal(3), z.literal(4), z.literal(5)]),
	due: LocalDate,
	mastered: z.boolean(),
	archived: z.boolean(),
	directions: z.array(Direction),
	nextDirection: Direction,
	lastWrongDirection: Direction.nullable(),
	isNoun: z.boolean()
});
export type Card = z.infer<typeof Card>;

export const DayRecord = z.object({
	activeSec: z.number(),
	dueAtStart: z.number(),
	answeredDue: z.number(),
	goalMet: z.boolean(),
	frozen: z.boolean(),
	simDeferred: z.boolean()
});

export const GameState = z.object({
	schemaVersion: z.literal(2),
	ruleset: z.object({ id: z.string(), version: z.number() }),
	overrides: z.array(z.object({ grant: OverrideGrant, at: z.string(), decision: OverrideDecision })),
	profile: z.object({ name: z.string().min(1), startDate: LocalDate, pensumMin: PensumMin }).nullable(),
	course: z.object({
		phase: CoursePhase,
		completed: z.record(ChapterId, Completion),
		chapter: ChapterRun.nullable(),
		perfectStreak: z.object({ current: z.number(), best: z.number() }),
		nextChapterBonus: z.union([z.literal(0), z.literal(1), z.literal(2)]),
		// Exam run details follow with the simulation step (04a §4.3).
		exam: z.record(z.string(), z.unknown()).nullable(),
		examHistory: z.array(ExamResult),
		exit: z.object({ chain: z.union([z.literal(0), z.literal(1)]), modelTestPassed: z.boolean(), readySince: LocalDate.nullable() }),
		usedTestSets: z.record(z.string(), z.number())
	}),
	review: z.object({ cards: z.record(z.string(), Card), weeklyLastDone: LocalDate.nullable(), deferredFrom: LocalDate.nullable() }),
	days: z.record(LocalDate, DayRecord),
	streak: z.object({
		current: z.number(),
		best: z.number(),
		freezes: z.union([z.literal(0), z.literal(1), z.literal(2)]),
		lastEvaluated: LocalDate.nullable(),
		badges: z.array(z.number())
	}),
	answerStreak: z.object({ current: z.number(), best: z.number() }),
	clock: z.object({ lastEventAt: z.string(), lastLocalDate: LocalDate.nullable(), skewNotice: z.boolean() }),
	session: z.object({ anchorDate: LocalDate.nullable(), anchorStartedAt: z.string().nullable(), lastActivityAt: z.string().nullable() })
});
export type GameState = z.infer<typeof GameState>;
export type { Discipline };

export const initialState = (ruleset: { id: string; version: number }): GameState => ({
	schemaVersion: 2,
	ruleset,
	overrides: [],
	profile: null,
	course: {
		phase: { kind: 'NO_PROFILE' },
		completed: {},
		chapter: null,
		perfectStreak: { current: 0, best: 0 },
		nextChapterBonus: 0,
		exam: null,
		examHistory: [],
		exit: { chain: 0, modelTestPassed: false, readySince: null },
		usedTestSets: {}
	},
	review: { cards: {}, weeklyLastDone: null, deferredFrom: null },
	days: {},
	streak: { current: 0, best: 0, freezes: 0, lastEvaluated: null, badges: [] },
	answerStreak: { current: 0, best: 0 },
	clock: { lastEventAt: '', lastLocalDate: null, skewNotice: false },
	session: { anchorDate: null, anchorStartedAt: null, lastActivityAt: null }
});
