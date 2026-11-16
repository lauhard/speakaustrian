import { describe, expect, it } from 'vitest';
import { withPools } from '../content/merge.ts';
import { ChapterContent, type Discipline } from '../content/schema.ts';
import { checkChapter, checkUniqueIds, failed, germanGermanForms, isKnownWord, makeLexicon, parseInventory, type Finding, type QaContext } from './checks.ts';
import broken from './fixtures/broken.json';

const L = (s: string) => ({ de: s, en: `${s} (en)`, tl: `${s} (tl)` });
// R-T1 for a chapter with focus speaking: 5 + 5 × 3 = 20.
const quota: Record<Discipline, number> = { lesen: 3, hoeren: 3, schreiben: 3, sprechen: 5, grammatikWortschatz: 3, werte: 3 };
const inventory = parseInventory(
	['id\tlemma\tpos\thf\tlevel\tuse\tat\tset\tkind\tchapter', ...['wie', 'heißen', 'Sie', 'ich', 'wer', 'kommen', 'Frau', 'ja', 'nein', 'gut', 'danke', 'grüß Gott', 'servus', 'hallo', 'was', 'sagen', 'hier', 'und', 'die'].map((w, i) => `W-A1-${String(i + 1).padStart(4, '0')}\t${w}\tx\tGW\tA1\ta\t0\t\tv1\tA1-01`)].join('\n')
);
const ctx: QaContext = { quota, real: true, position: 1, knownChapters: [], earlierChapterIds: ['A1-01'], inventory, allowlist: ['Anna', 'Huber'], fileExists: () => false };

const item = (id: string, skill: Discipline, n: number, extra: object = {}) => ({
	id, skill, type: 'choice', instruction: L('Wählen Sie.'), explanation: L('Warum.'), prompt: `Wie heißen Sie? ${n}`, options: ['Ich heiße Anna.', 'Danke.'], answer: 0, goals: ['G1'], ...extra
});
// A chapter that meets every rule: 20 twin families of 3 (= 60 test items), 80 practice items, 20 % recycling.
const good = () => {
	const skills = (Object.keys(quota) as Discipline[]).flatMap((d) => Array.from({ length: quota[d] }, () => d));
	const test = skills.flatMap((d, f) => [0, 1, 2].map((t) => item(`OK-T${f}-${t}`, d, f * 3 + t, t ? { family: `OK-T${f}-0` } : {})));
	const practice = Array.from({ length: 4 }, (_, r) => skills.map((d, f) => item(`OK-P${r}-${f}`, d, 100 + r * 20 + f, r === 0 ? { refs: ['W-A1-0001'] } : {}))).flat();
	return { schemaVersion: 1, chapterId: 'A1-02', tlReviewStatus: 'machine', lessons: [{ id: 'OK-L1', title: L('Lektion'), items: [item('OK-L1-I1', 'lesen', 999)] }], goals: { G1: L('Grüßen') }, pools: { practice, test } };
};
const has = (findings: Finding[], check: string, level: string, itemId?: string) =>
	findings.some((x) => x.check === check && x.level === level && (itemId === undefined || x.itemId === itemId));

describe('qa on a chapter that meets the rules', () => {
	it('reports no errors and no warnings', () => {
		const findings = checkChapter(good(), ctx);
		expect(findings.filter((x) => x.level !== 'info')).toEqual([]);
		expect(failed(findings, true)).toBe(false);
	});
	it('sandbox chapters get the quantity rules as info only', () => {
		const findings = checkChapter({ ...good(), chapterId: 'DEMO', pools: { practice: good().pools.practice.slice(0, 20), test: good().pools.test.slice(0, 6) } }, { ...ctx, real: false, position: -1, quota: { lesen: 1, hoeren: 1 } });
		expect(has(findings, 'pool.size', 'info')).toBe(true);
		expect(failed(findings)).toBe(false);
	});
});

describe('qa on the broken fixture: one finding per check', () => {
	const findings = checkChapter(broken, ctx);
	it.each([
		['pool.size', 'error', undefined],
		['pool.twins', 'error', 'FX-T1'],
		['pool.quota', 'error', undefined],
		['pool.family-skill', 'warning', 'FX-T2'],
		['practice.gate', 'error', undefined],
		['practice.size', 'warning', undefined],
		['pool.duplicate', 'error', 'FX-T3'],
		['choice.options', 'error', 'FX-T1'],
		['goals.uncovered', 'error', undefined],
		['test.parts', 'error', 'FX-T2'],
		['i18n.blank', 'error', 'FX-T3B'],
		['image.missing', 'error', 'FX-T1B'],
		['vocab.unknown', 'warning', 'FX-T3B'],
		['variety.de', 'warning', 'FX-T3B'],
		['recycling', 'error', undefined]
	] as const)('%s (%s)', (check, level, itemId) => expect(has(findings, check, level, itemId)).toBe(true));
	it('fails', () => expect(failed(findings)).toBe(true));
	it('names only the unknown words', () => {
		expect(findings.find((x) => x.check === 'vocab.unknown' && x.itemId === 'FX-T3B')?.message).toMatch(/: Tomate, Quantenphysik$/);
	});
});

describe('schema errors and missing pools', () => {
	it('reports duplicate ids and a family that is no base item of the pool', () => {
		const c = good();
		c.pools.test[1] = { ...c.pools.test[1], id: 'OK-T0-0' };
		c.pools.test[5] = { ...c.pools.test[5], family: 'OK-P0-0' } as (typeof c.pools.test)[number];
		const findings = checkChapter(c, ctx);
		expect(findings.every((x) => x.check === 'schema' && x.level === 'error')).toBe(true);
		expect(findings.some((x) => /unique/.test(x.message))).toBe(true);
		expect(has(findings, 'schema', 'error', 'OK-T1-2')).toBe(true);
	});
	it('a chapter without pools is info, or an error when pools are required', () => {
		const { pools: _pools, goals: _goals, ...lessonsOnly } = good();
		expect(has(checkChapter(lessonsOnly, ctx), 'pools.missing', 'info')).toBe(true);
		expect(has(checkChapter(lessonsOnly, { ...ctx, requirePools: true }), 'pools.missing', 'error')).toBe(true);
	});
	it('finds item ids used in two chapters', () => {
		const a = ChapterContent.parse(good());
		expect(checkUniqueIds([a, { ...a, chapterId: 'A1-03' }])[0]).toMatchObject({ check: 'ids.duplicate', level: 'error' });
		expect(checkUniqueIds([a])).toEqual([]);
	});
});

describe('pools file merge', () => {
	const { pools, goals, ...lessonsOnly } = good();
	it('adds goals and pools of the matching file', () => {
		const merged = withPools(lessonsOnly, [{ chapterId: 'A1-09', pools: {} }, { chapterId: 'A1-02', goals, pools }]);
		expect(ChapterContent.parse(merged).pools?.test).toHaveLength(60);
	});
	it('leaves a chapter without a file unchanged', () => expect(withPools(lessonsOnly, [{ chapterId: 'A1-09' }])).toBe(lessonsOnly));
});

describe('vocabulary and variety helpers', () => {
	const lex = makeLexicon(['heißen', 'Name', 'sein (Verb)', "Wie geht's?", 'kommen'], ['Ich bin Anna.'], ['Wien']);
	it.each(['heiße', 'heißt', 'Namen', 'kommst', 'bin', "geht's", 'Wien', 'WIE'])('knows %s', (w) => expect(isKnownWord(w, lex)).toBe(true));
	it.each(['Wohnort', 'arbeiten', 'Verb'])('does not know %s', (w) => expect(isKnownWord(w, lex)).toBe(false));
	it('finds German-German forms incl. plural, not Austrian ones', () => {
		expect(germanGermanForms('Zwei Tomaten und ein Brötchen, bitte.')).toEqual(['Tomaten', 'Brötchen']);
		expect(germanGermanForms('Ein Paradeiser und eine Semmel im Jänner.')).toEqual([]);
	});
});
