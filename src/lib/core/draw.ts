import type { Discipline } from './content/schema';
import type { TestSpec } from './policy';
import { seeded, shuffle } from './random';

// Draws for the chapter test and the readiness round (docs/spec/04a R-T2, R-T4, R-G1).
// Pure: the caller passes the seed and puts the result into the event (TEST_STARTED).
export type PoolItem = { id: string; skill: Discipline; family: string; goals: readonly string[] };

const quotas = (spec: TestSpec) => Object.entries(spec.quota) as [Discipline, number][];

// R-T2: per discipline quota, goals not yet in the test first, never two items of one twin family.
// R-T4: unseen items first, then the ones seen longest ago.
export const drawTest = (pool: readonly PoolItem[], spec: TestSpec, seen: readonly string[], seed: string): string[] => {
	const random = seeded(seed);
	const lastSeen = (id: string) => seen.lastIndexOf(id);
	const pickFor = (picked: PoolItem[], [skill, quota]: [Discipline, number]): PoolItem[] => {
		const candidates = shuffle(
			pool.filter((p) => p.skill === skill),
			random
		);
		const step = (acc: PoolItem[], left: number): PoolItem[] => {
			if (left === 0) return acc;
			const families = new Set(acc.map((p) => p.family));
			const goals = new Set(acc.flatMap((p) => p.goals));
			const repeatsGoal = (p: PoolItem) => Number(p.goals.every((g) => goals.has(g)));
			const [next] = candidates
				.filter((p) => !families.has(p.family))
				.sort((a, b) => lastSeen(a.id) - lastSeen(b.id) || repeatsGoal(a) - repeatsGoal(b));
			return next ? step([...acc, next], left - 1) : acc;
		};
		return step(picked, quota);
	};
	return quotas(spec)
		.reduce(pickFor, [] as PoolItem[])
		.map((p) => p.id);
};

// R-G1/R-G2: block n is the n-th slice of one seeded order per discipline, so blocks do not overlap
// while the pool lasts; after that the order starts again.
export const drawGate = (pool: readonly PoolItem[], spec: TestSpec, block: number, seed: string): string[] => {
	const random = seeded(seed);
	return quotas(spec).flatMap(([skill, quota]) => {
		const ordered = shuffle(
			pool.filter((p) => p.skill === skill),
			random
		);
		if (ordered.length === 0) return [];
		return Array.from({ length: Math.min(quota, ordered.length) }, (_, i) => ordered[((block - 1) * quota + i) % ordered.length].id);
	});
};
