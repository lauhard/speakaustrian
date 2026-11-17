import { describe, expect, it } from 'vitest';
import { step, type Run } from './accuracy';

describe('accuracy run', () => {
	it('counts up, keeps the best and resets on a mistake', () => {
		const at = (answers: boolean[]): Run => answers.reduce(step, { current: 0, best: 0 });
		expect(at([true, true, true])).toEqual({ current: 3, best: 3 });
		expect(at([true, true, true, false])).toEqual({ current: 0, best: 3 });
		expect(at([true, true, true, false, true])).toEqual({ current: 1, best: 3 });
	});
});
