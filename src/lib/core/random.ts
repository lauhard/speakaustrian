// Deterministic randomness from a string seed: draws are reproducible from the events (04a R-T2).
export const seeded = (seed: string): (() => number) => {
	let h = [...seed].reduce((acc, ch) => Math.imul(acc ^ ch.charCodeAt(0), 16777619), 2166136261) >>> 0;
	return () => {
		h = (h + 0x6d2b79f5) >>> 0;
		const t = Math.imul(h ^ (h >>> 15), 1 | h);
		const u = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
		return ((u ^ (u >>> 14)) >>> 0) / 4294967296;
	};
};

export const shuffle = <T>(list: readonly T[], random: () => number): T[] =>
	list
		.map((value) => ({ value, key: random() }))
		.sort((a, b) => a.key - b.key)
		.map((x) => x.value);
