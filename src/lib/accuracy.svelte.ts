// Device-local flame score (like settings, not course progress). Rules: core/accuracy.ts.
import { answer, bank, emptyScore, fxOf, type Score, type ScoreFx } from './core/accuracy.ts';

const KEY = 'speakaustrian.score.v1';
const load = (): Score => {
	try {
		return { ...emptyScore, ...JSON.parse(localStorage.getItem(KEY) ?? '{}') };
	} catch {
		return emptyScore;
	}
};

let s = $state<Score>(typeof window === 'undefined' ? emptyScore : load());
let fx = $state<{ kind: ScoreFx; seq: number }>({ kind: 'none', seq: 0 });

const commit = (next: Score) => {
	fx = { kind: fxOf(s, next), seq: fx.seq + 1 };
	s = next;
	try {
		localStorage.setItem(KEY, JSON.stringify(s));
	} catch {
		/* private mode: keep it in memory */
	}
};

export const accuracy = {
	get score() { return s.score; },
	get best() { return s.best; },
	get pot() { return s.pot; },
	get hits() { return s.hits; },
	get fx() { return fx; },
	record: (correct: boolean) => commit(answer(s, correct)),
	bank: () => s.pot > 0 && commit(bank(s))
};
