import { describe, expect, it } from 'vitest';
import { drawGate, drawTest, type PoolItem } from './draw';
import { makeDefaultPolicy } from './policy';
import { newGame } from './reducer';
import { Discipline } from './content/schema';

// Draws for chapter test and readiness round (docs/spec/04a R-T1, R-T2, R-T4, R-G1; 04b T-T01–T-T08, T-G01, T-G04).
const disciplines = Discipline.options;
// 10 base items per discipline over 5 goals, each with two twins: 180 items.
const pool: PoolItem[] = disciplines.flatMap((skill) =>
	Array.from({ length: 10 }, (_, i) => `${skill}-${i}`).flatMap((family, i) =>
		['', 'a', 'b'].map((suffix) => ({ id: family + suffix, skill, family, goals: [`${skill}-goal-${i % 5}`] }))
	)
);
const byId = new Map(pool.map((p) => [p.id, p]));
const count = (ids: string[], skill: string) => ids.filter((id) => byId.get(id)!.skill === skill).length;
const focus = (c: string) => (c === 'A1-02' ? 'hoeren' : c === 'A2-19' ? 'pruefung' : 'sprechen') as 'hoeren' | 'pruefung' | 'sprechen';
const policy = makeDefaultPolicy(['A1-01', 'A1-02', 'A2-19'], undefined, focus);
const spec = policy.testComposition(newGame(policy), 'A1-02');

describe('test composition (R-T1)', () => {
	it('T-T01: 20 items, 5 for the focus discipline and 3 for each other', () => {
		const ids = drawTest(pool, spec, [], 's');
		expect(ids).toHaveLength(20);
		expect(disciplines.map((d) => count(ids, d))).toEqual(disciplines.map((d) => (d === 'hoeren' ? 5 : 3)));
	});
	it('T-T02: exam training chapters take 4 reading and 4 listening items', () => {
		const quota = policy.testComposition(newGame(policy), 'A2-19').quota;
		expect(quota).toEqual({ lesen: 4, hoeren: 4, schreiben: 3, sprechen: 3, grammatikWortschatz: 3, werte: 3 });
	});
	it('T-PL07: the test length comes from the policy config', () => {
		const longer = makeDefaultPolicy(['A1-02'], { ...policy.config, TEST_PER_DISCIPLINE: 4, TEST_FOCUS_EXTRA: 1 }, focus);
		expect(drawTest(pool, longer.testComposition(newGame(longer), 'A1-02'), [], 's')).toHaveLength(25);
	});
});

describe('test draw (R-T2, R-T4)', () => {
	it('T-T03: never two items of one twin family in a test', () => {
		for (let seed = 0; seed < 200; seed++) {
			const families = drawTest(pool, spec, [], `${seed}`).map((id) => byId.get(id)!.family);
			expect(new Set(families).size).toBe(families.length);
		}
	});
	it('T-T04: same seed, same list; another seed, another list', () => {
		expect(drawTest(pool, spec, [], 'x')).toEqual(drawTest(pool, spec, [], 'x'));
		expect(drawTest(pool, spec, [], 'x')).not.toEqual(drawTest(pool, spec, [], 'y'));
	});
	it('T-T05: a discipline covers different goals before one repeats', () => {
		const ids = drawTest(pool, spec, [], 's');
		for (const d of disciplines) {
			const goals = ids.filter((id) => byId.get(id)!.skill === d).flatMap((id) => byId.get(id)!.goals);
			expect(new Set(goals).size).toBe(goals.length);
		}
	});
	it('T-T07: a second attempt avoids the items of the first', () => {
		const first = drawTest(pool, spec, [], 'a');
		const second = drawTest(pool, spec, first, 'b');
		expect(second.filter((id) => first.includes(id))).toEqual([]);
	});
	it('T-T08: when everything was seen, the items used longest ago return first', () => {
		const five: PoolItem[] = [1, 2, 3, 4, 5].map((i) => ({ id: `l${i}`, skill: 'lesen', family: `l${i}`, goals: ['g'] }));
		const drawn = drawTest(five, { quota: { lesen: 3 } }, ['l3', 'l1', 'l5', 'l2', 'l4'], 's');
		expect([...drawn].sort()).toEqual(['l1', 'l3', 'l5']);
	});
});

describe('readiness round blocks (R-G1)', () => {
	it('T-G01/T-G04: 20 items in the test mix, the next block shares none with the one before', () => {
		const b1 = drawGate(pool, spec, 1, 's');
		const b2 = drawGate(pool, spec, 2, 's');
		expect(b1).toHaveLength(20);
		expect(count(b1, 'hoeren')).toBe(5);
		expect(b2.filter((id) => b1.includes(id))).toEqual([]);
		expect(drawGate(pool, spec, 1, 's')).toEqual(b1);
	});
});
