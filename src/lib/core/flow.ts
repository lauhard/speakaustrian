import { drawGate, drawTest, mixSkills, type PoolItem } from './draw';
import { seeded, shuffle } from './random';
import type { RulePolicy } from './policy';
import type { ChapterRun, GameState } from './state';

// What the chapter UI needs to know about the next step. Pure: seeds come from the run, never from a clock.

// R-G1: the items of readiness block `block`, in a fixed order per attempt (reload-safe).
export const gateDraw = (policy: RulePolicy, s: GameState, run: ChapterRun, practicePool: readonly PoolItem[], block: number): string[] =>
	mixSkills(drawGate(practicePool, policy.testComposition(s, run.id), block, `${run.id}:${run.attemptNo}:gate`), practicePool);

// The next unanswered item of the running readiness block, or undefined when the draw is used up.
// K3: each attempt practises the next round of the practice part, so a repeated chapter does not ask the same items again.
export const practiceItemAt = (part: readonly PoolItem[], attemptNo: number, roundSize: number, answered: number): PoolItem | undefined =>
	part.length === 0 ? undefined : part[((attemptNo - 1) * roundSize + answered) % part.length];

export const nextGateItem = (draw: readonly string[], answered: readonly string[]): string | undefined => draw.find((id) => !answered.includes(id));

// R-T2, R-T4: the test list for TEST_STARTED; the caller puts it into the event together with the attempt id.
export const testDraw = (policy: RulePolicy, s: GameState, run: ChapterRun, testPool: readonly PoolItem[], attemptId: string): string[] =>
	drawTest(testPool, policy.testComposition(s, run.id), run.seenTestItemIds, attemptId);

// K4: the target stack for TARGET_STARTED – up to TARGET_PER_GOAL items per weak goal (weakest first), at most TARGET_MAX,
// drawn from the practice pool in a fixed order per attempt and block (reload-safe), no item twice.
export const targetDraw = (policy: RulePolicy, run: ChapterRun, practicePool: readonly PoolItem[], goalIds: readonly string[], block: number): string[] => {
	const pool = shuffle(practicePool, seeded(`${run.id}:${run.attemptNo}:target:${block}`));
	return goalIds
		.reduce<string[]>((stack, goal) => {
			const fresh = pool.filter((p) => p.goals.includes(goal) && !stack.includes(p.id)).slice(0, policy.config.TARGET_PER_GOAL);
			return [...stack, ...fresh.map((p) => p.id)];
		}, [])
		.slice(0, policy.config.TARGET_MAX);
};

// R-G2: practice items that train one of the goals the readiness block missed.
export const targetedItems = (practicePool: readonly PoolItem[], goalIds: readonly string[]): string[] =>
	practicePool.filter((p) => p.goals.some((g) => goalIds.includes(g))).map((p) => p.id);
