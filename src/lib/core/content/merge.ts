// Pools of a real chapter live in their own file `<chapter>-pools.json` (step 004a), so pool batches
// do not touch the lesson file. Shape: { chapterId, goals, pools: { practice, test } }.
type Raw = { chapterId?: unknown };
type PoolsRaw = Raw & { goals?: unknown; pools?: unknown };

// Returns the chapter with `goals` and `pools` of its pools file; without a file the chapter is unchanged.
export const withPools = <T extends Raw>(chapter: T, poolFiles: readonly unknown[]): T => {
	const file = (poolFiles as PoolsRaw[]).find((f) => f?.chapterId === chapter.chapterId);
	return file ? { ...chapter, goals: file.goals, pools: file.pools } : chapter;
};
