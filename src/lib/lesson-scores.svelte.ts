import { defaultConfig } from '#lib/core/policy.ts';

// Best score per lesson in percent (device-local view data, like the flame score; cleared by resetAll).
const KEY = 'speakaustrian.lessonscores.v1';
const load = (): Record<string, number> => {
	try {
		return JSON.parse(localStorage.getItem(KEY) ?? '{}');
	} catch {
		return {};
	}
};
let best = $state<Record<string, number>>(typeof window === 'undefined' ? {} : load());

export const lessonScores = {
	of: (lessonId: string): number | undefined => best[lessonId],
	record(lessonId: string, percent: number) {
		if ((best[lessonId] ?? -1) >= percent) return;
		best = { ...best, [lessonId]: percent };
		try {
			localStorage.setItem(KEY, JSON.stringify(best));
		} catch {
			/* private mode */
		}
	}
};

// Star thresholds of a lesson result in percent: the first star means passed (K1), three stars from 90 % (concept §3).
export const STARS = [defaultConfig.LESSON_PASS_PCT, 70, 90] as const;
