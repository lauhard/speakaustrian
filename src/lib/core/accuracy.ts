// Flame score (Andi, 17.11.2026; G-018 decided). Pure rules, no clock:
// - every 3rd correct answer in a row earns a flame point for the running round (`pot`)
// - a mistake loses the pot; a second mistake before the next flame also wipes the banked score
// - when a round/chapter ends, the pot is banked into `score` (header)
export const HITS_PER_FLAME = 3;
export type Score = { score: number; best: number; pot: number; hits: number; armed: boolean };
export type ScoreFx = 'none' | 'hit' | 'flame' | 'lostPot' | 'lostScore' | 'bank';
export const emptyScore: Score = { score: 0, best: 0, pot: 0, hits: 0, armed: false };

export const answer = (s: Score, correct: boolean): Score => {
	if (correct) {
		const hits = s.hits + 1;
		return hits < HITS_PER_FLAME ? { ...s, hits } : { ...s, hits: 0, pot: s.pot + 1, armed: false };
	}
	return s.armed ? { ...s, score: 0, pot: 0, hits: 0 } : { ...s, pot: 0, hits: 0, armed: true };
};

export const bank = (s: Score): Score => {
	const score = s.score + s.pot;
	return { ...s, score, pot: 0, best: Math.max(s.best, score) };
};

/** Which animation a change deserves (view hint only). */
export const fxOf = (before: Score, after: Score): ScoreFx =>
	after.score < before.score ? 'lostScore'
	: after.pot < before.pot && after.score > before.score ? 'bank'
	: after.pot < before.pot ? 'lostPot'
	: after.pot > before.pot ? 'flame'
	: after.hits > before.hits ? 'hit'
	: 'none';
