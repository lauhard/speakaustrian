import type { GameState } from './state.ts';

/** Game numbers shown in the header/sidebar. Pure view model, no rules of its own. */
export type Stats = {
	streak: number;
	best: number;
	freezes: number;
	/** Lives of the running chapter test or correction round; null outside a test. */
	lives: number | null;
	/** Points/highscore are not specified yet (spec gap G-018); null hides the slot. */
	points: number | null;
};

export const deriveStats = (state: GameState): Stats => {
	const attempt = state.course.chapter?.attempt;
	const lives = attempt?.kind === 'TEST' ? attempt.lives : attempt?.kind === 'CORRECTION' ? attempt.livesLeft : null;
	return { streak: state.streak.current, best: state.streak.best, freezes: state.streak.freezes, lives, points: null };
};
