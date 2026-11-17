export type Run = { current: number; best: number };

/** "No mistakes" run: +1 per correct answer, back to 0 on a mistake; `best` keeps the record. */
export const step = (run: Run, correct: boolean): Run => {
	const current = correct ? run.current + 1 : 0;
	return { current, best: Math.max(run.best, current) };
};
