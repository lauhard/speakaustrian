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

// Round-robin over groups: a1, b1, c1, a2, b2 …
const interleave = <T>(groups: readonly (readonly T[])[]): T[] =>
	Array.from({ length: Math.max(0, ...groups.map((g) => g.length)) }, (_, i) => groups.flatMap((g) => (i < g.length ? [g[i]] : []))).flat();

const groupBy = <T>(list: readonly T[], key: (t: T) => string): T[][] =>
	[...list.reduce((acc, t) => acc.set(key(t), [...(acc.get(key(t)) ?? []), t]), new Map<string, T[]>()).values()];

// Interleaving (04 §didactics): neighbours differ in discipline, and a twin family only comes again after all other families.
export const practiceOrder = (pool: readonly PoolItem[]): PoolItem[] => {
	const families = interleave(groupBy(groupBy(pool, (p) => p.family), (family) => family[0].skill));
	return interleave(families.map((family) => family.map((p) => [p]))).flat();
};

// G-010 (decision A): the practice part is a fixed set of `partSize` items, the readiness blocks draw from the rest.
// A pool that is too small for that (sandbox chapter) is walked whole and shared.
export const splitPractice = (pool: readonly PoolItem[], partSize: number, gateNeed: number): { part: readonly PoolItem[]; rest: readonly PoolItem[] } => {
	if (pool.length < partSize + gateNeed) return { part: pool, rest: pool };
	const ordered = practiceOrder(pool);
	return { part: ordered.slice(0, partSize), rest: ordered.slice(partSize) };
};

// Same idea for a drawn block: mix the disciplines instead of asking them one after the other.
export const mixSkills = (ids: readonly string[], pool: readonly PoolItem[]): string[] =>
	interleave(groupBy(ids, (id) => pool.find((p) => p.id === id)?.skill ?? '')).flat();
