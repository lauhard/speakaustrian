// Device-local flames (K8; like settings, not course progress). Rules: core/flames.ts.
import { answer, bank, close, emptyFlames, enter, fxOf, multiplier, tierOf, type FlameFx, type Flames } from './core/flames.ts';

const KEY = 'speakaustrian.flames.v2';
const load = (): Flames => {
	try {
		const v2 = localStorage.getItem(KEY);
		if (v2) return { ...emptyFlames, ...JSON.parse(v2) };
		// v1 (one global score): keep only the record.
		const v1 = JSON.parse(localStorage.getItem('speakaustrian.score.v1') ?? '{}') as { best?: number };
		return { ...emptyFlames, best: v1.best ?? 0 };
	} catch {
		return emptyFlames;
	}
};

let s = $state<Flames>(typeof window === 'undefined' ? emptyFlames : load());
let fx = $state<{ kind: FlameFx; seq: number }>({ kind: 'none', seq: 0 });

const commit = (next: Flames) => {
	if (next === s) return;
	fx = { kind: fxOf(s, next), seq: fx.seq + 1 };
	s = next;
	try {
		localStorage.setItem(KEY, JSON.stringify(s));
	} catch {
		/* private mode: keep it in memory */
	}
};

export const flames = {
	get chapterFlames() { return s.chapterFlames; },
	get best() { return s.best; },
	get pot() { return s.pot; },
	get hits() { return s.hits; },
	get shields() { return s.shields; },
	get multiplier() { return multiplier(s.chapterFlames); },
	get tier() { return tierOf(s.chapterFlames); },
	get fx() { return fx; },
	closedOf: (chapterId: string): number | undefined => s.closed[chapterId],
	/** `chapterId` = the running course chapter, or null where no flames count (review, free practice, demo, free mode). */
	record: (chapterId: string | null, correct: boolean) => chapterId && commit(answer(enter(s, chapterId), correct)),
	bank: (shieldRound: boolean) => s.chapterId && commit(bank(s, shieldRound)),
	close: (chapterId: string) => commit(close(s, chapterId))
};

// Colour per tier (K8 table), for the flame icon.
export const TIER_CLASS = {
	grey: 'text-stone-400',
	orange: 'fill-orange-400 text-orange-500',
	red: 'fill-red-500 text-red-600',
	violet: 'fill-violet-500 text-violet-600',
	blue: 'fill-blue-500 text-blue-600'
} as const;
