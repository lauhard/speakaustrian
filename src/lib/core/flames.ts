// Flames v2 (K8, docs/concepts/xp-flammen-kapitelfluss.md §2). Pure reward rules, device-local, never a pass rule (D8).
// - 3 correct answers in a row earn a round flame (`pot`); the pot flies into the chapter flames when a round ends
// - 1st mistake: pot gone, `armed`; 2nd mistake before the next flame: chapter flames to 0, unless a shield takes the hit
// - a perfect lesson or practice round earns a shield (max. 2), valid until the chapter ends
// - flames exist only in the running course chapter; passing it closes the chapter (flames → multiplier, then 0)
export const HITS_PER_FLAME = 3;
export const MAX_SHIELDS = 2;
export const FLAME_MULT_STEP = 0.02;
export const FLAME_MULT_MAX = 2;
export const FLAME_TIERS = [
	{ min: 35, tier: 'blue' },
	{ min: 20, tier: 'violet' },
	{ min: 10, tier: 'red' },
	{ min: 1, tier: 'orange' },
	{ min: 0, tier: 'grey' }
] as const;
export type FlameTier = (typeof FLAME_TIERS)[number]['tier'];

export type Flames = {
	chapterId: string | null;
	chapterFlames: number;
	best: number;
	pot: number;
	hits: number;
	armed: boolean;
	shields: number;
	// answers of the running round, to see whether it was perfect (shield)
	round: { correct: number; total: number };
	// flames a passed chapter ended with (trophy step, XP multiplier in 030)
	closed: Record<string, number>;
};
export type FlameFx = 'none' | 'hit' | 'flame' | 'lostPot' | 'lostScore' | 'shieldBroken' | 'shieldEarned' | 'bank';

export const emptyFlames: Flames = { chapterId: null, chapterFlames: 0, best: 0, pot: 0, hits: 0, armed: false, shields: 0, round: { correct: 0, total: 0 }, closed: {} };

const fresh = (f: Flames, chapterId: string | null): Flames => ({ ...f, chapterId, chapterFlames: 0, pot: 0, hits: 0, armed: false, shields: 0, round: { correct: 0, total: 0 } });

/** Flames belong to one chapter; answering in another one starts it from zero. A repeated attempt keeps them. */
export const enter = (f: Flames, chapterId: string): Flames => (f.chapterId === chapterId ? f : fresh(f, chapterId));

export const answer = (f: Flames, correct: boolean): Flames => {
	const round = { correct: f.round.correct + Number(correct), total: f.round.total + 1 };
	if (correct) {
		const hits = f.hits + 1;
		return hits < HITS_PER_FLAME ? { ...f, round, hits } : { ...f, round, hits: 0, pot: f.pot + 1, armed: false };
	}
	if (!f.armed) return { ...f, round, pot: 0, hits: 0, armed: true };
	// 2nd mistake: a shield takes the hit and stays armed, otherwise the chapter flames are gone.
	return f.shields > 0 ? { ...f, round, pot: 0, hits: 0, shields: f.shields - 1 } : { ...f, round, pot: 0, hits: 0, chapterFlames: 0 };
};

/** End of a round: the pot goes into the chapter flames; `shieldRound` = lesson or practice round, which can earn a shield. */
export const bank = (f: Flames, shieldRound: boolean): Flames => {
	const chapterFlames = f.chapterFlames + f.pot;
	const perfect = shieldRound && f.round.total > 0 && f.round.correct === f.round.total;
	return {
		...f,
		chapterFlames,
		pot: 0,
		best: Math.max(f.best, chapterFlames),
		shields: Math.min(MAX_SHIELDS, f.shields + Number(perfect)),
		round: { correct: 0, total: 0 }
	};
};

/** Chapter passed: bank what is left, keep the result for the trophy/XP, start the next chapter at zero. */
export const close = (f: Flames, chapterId: string): Flames => {
	if (f.chapterId !== chapterId) return f;
	const banked = bank(f, false);
	return { ...fresh(banked, null), closed: { ...f.closed, [chapterId]: banked.chapterFlames } };
};

export const multiplier = (chapterFlames: number): number => Math.min(FLAME_MULT_MAX, Math.round((1 + FLAME_MULT_STEP * chapterFlames) * 100) / 100);
export const tierOf = (chapterFlames: number): FlameTier => FLAME_TIERS.find((t) => chapterFlames >= t.min)!.tier;

/** Which animation a change deserves (view hint only). */
export const fxOf = (before: Flames, after: Flames): FlameFx =>
	after.shields < before.shields ? 'shieldBroken'
	: after.shields > before.shields ? 'shieldEarned'
	: after.chapterFlames < before.chapterFlames ? 'lostScore'
	: after.chapterFlames > before.chapterFlames ? 'bank'
	: after.pot < before.pot ? 'lostPot'
	: after.pot > before.pot ? 'flame'
	: after.hits > before.hits ? 'hit'
	: 'none';
