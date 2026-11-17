// "No mistakes" run: counts correct answers in a row, resets on a mistake. No game rule yet (device-local, like settings).
import { step, type Run } from './core/accuracy.ts';
const KEY = 'speakaustrian.accuracy.v1';

const load = (): Run => {
	try {
		return { current: 0, best: 0, ...JSON.parse(localStorage.getItem(KEY) ?? '{}') };
	} catch {
		return { current: 0, best: 0 };
	}
};

let run = $state<Run>(typeof window === 'undefined' ? { current: 0, best: 0 } : load());

export const accuracy = {
	get current() {
		return run.current;
	},
	get best() {
		return run.best;
	},
	record(correct: boolean) {
		run = step(run, correct);
		try {
			localStorage.setItem(KEY, JSON.stringify(run));
		} catch {
			/* private mode: the run just stays in memory */
		}
	}
};
