import { drawGate, drawTest, type PoolItem } from './draw';
import type { RulePolicy } from './policy';
import type { ChapterRun, GameState } from './state';

// What the chapter UI needs to know about the next step. Pure: seeds come from the run, never from a clock.

// R-G1: the items of readiness block `block`, in a fixed order per attempt (reload-safe).
export const gateDraw = (policy: RulePolicy, s: GameState, run: ChapterRun, practicePool: readonly PoolItem[], block: number): string[] =>
	drawGate(practicePool, policy.testComposition(s, run.id), block, `${run.id}:${run.attemptNo}:gate`);

// The next unanswered item of the running readiness block, or undefined when the draw is used up.
export const nextGateItem = (draw: readonly string[], answered: readonly string[]): string | undefined => draw.find((id) => !answered.includes(id));

// R-T2, R-T4: the test list for TEST_STARTED; the caller puts it into the event together with the attempt id.
export const testDraw = (policy: RulePolicy, s: GameState, run: ChapterRun, testPool: readonly PoolItem[], attemptId: string): string[] =>
	drawTest(testPool, policy.testComposition(s, run.id), run.seenTestItemIds, attemptId);

// R-G2: practice items that train one of the goals the readiness block missed.
export const targetedItems = (practicePool: readonly PoolItem[], goalIds: readonly string[]): string[] =>
	practicePool.filter((p) => p.goals.some((g) => goalIds.includes(g))).map((p) => p.id);
