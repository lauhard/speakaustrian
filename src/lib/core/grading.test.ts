import { describe, expect, it } from 'vitest';
import { allItems, chapters } from '../content/index';
import { ChapterContent, type Item } from './content/schema';
import { gradeItem, gradeText, parseCloze, passes } from './grading';
import { damerauLevenshtein, isCorrect, VOCAB } from './tolerance';

const cloze: Item = {
	id: 'T-1',
	skill: 'grammatikWortschatz',
	type: 'cloze',
	instruction: { de: 'a', en: 'a', tl: 'a' },
	explanation: { de: 'a', en: 'a', tl: 'a' },
	text: 'Ich {{1}} Maria. Ich komme {{2}} Österreich.',
	gaps: { '1': { accept: ['heiße', 'bin'] }, '2': { accept: ['aus'] } }
};

describe('gradeText', () => {
	it('accepts exact answers and alternatives', () => {
		expect(gradeText('heiße', ['heiße', 'bin'])).toBe('correct');
		expect(gradeText('  bin ', ['heiße', 'bin'])).toBe('correct');
	});
	it('flags case, umlaut transliteration and punctuation as near', () => {
		expect(gradeText('Heisse', ['heiße'])).toBe('near');
		expect(gradeText('sommer.', ['Sommer'])).toBe('near');
		expect(gradeText('Oesterreich', ['Österreich'])).toBe('near');
	});
	it('rejects wrong and empty answers', () => {
		expect(gradeText('heißt', ['heiße'])).toBe('wrong');
		expect(gradeText('   ', ['heiße'])).toBe('wrong');
	});
	it('02g T3: typo tolerance by word length, only where allowed', () => {
		expect(damerauLevenshtein('Familienname', 'Familiennmae')).toBe(1);
		expect(isCorrect(VOCAB, ['Entschuldigung'], 'Entschuldigugn')).toBe(true);
		expect(isCorrect(VOCAB, ['danke'], 'dnake')).toBe(true);
		expect(isCorrect(VOCAB, ['gut'], 'gat')).toBe(false);
		expect(gradeText('kommts', ['kommst'])).toBe('wrong');
	});
});

describe('gradeItem', () => {
	it('grades every gap of a cloze and takes the worst verdict', () => {
		const grade = gradeItem(cloze, { type: 'cloze', gaps: { '1': 'bin', '2': 'von' } });
		expect(grade.parts).toEqual({ '1': 'correct', '2': 'wrong' });
		expect(grade.verdict).toBe('wrong');
		expect(grade.expected).toEqual({ '1': 'heiße', '2': 'aus' });
	});
	it('treats a missing gap as wrong', () => {
		expect(gradeItem(cloze, { type: 'cloze', gaps: { '1': 'heiße' } }).verdict).toBe('wrong');
	});
	it('reports near when only spelling details differ', () => {
		expect(gradeItem(cloze, { type: 'cloze', gaps: { '1': 'Heiße', '2': 'aus' } }).verdict).toBe('near');
	});
	it('rejects a response of the wrong type', () => {
		expect(() => gradeItem(cloze, { type: 'short', text: 'x' })).toThrow();
	});
});

describe('passes', () => {
	it('counts answers accepted through a tolerance', () => {
		expect(passes('near')).toBe(true);
		expect(passes('wrong')).toBe(false);
	});
});

describe('parseCloze', () => {
	it('splits text and gaps in order', () => {
		expect(parseCloze('Ich {{1}} Maria.')).toEqual([
			{ kind: 'text', value: 'Ich ' },
			{ kind: 'gap', id: '1' },
			{ kind: 'text', value: ' Maria.' }
		]);
	});
});

describe('content schema', () => {
	it('every item of every chapter is solvable with its first accepted answer', () => {
		expect(chapters.length).toBeGreaterThan(0);
		for (const item of allItems()) {
			const response =
				item.type === 'choice'
					? { type: 'choice' as const, selected: item.answer }
					: item.type === 'short'
						? { type: 'short' as const, text: item.accept[0] }
						: {
								type: 'cloze' as const,
								gaps: Object.fromEntries(Object.entries(item.gaps).map(([k, g]) => [k, g.accept[0]]))
							};
			expect(gradeItem(item, response).verdict).toBe('correct');
		}
	});
	it('rejects a cloze whose gaps do not match the text', () => {
		const lesson = { id: 'x', title: cloze.instruction, items: [{ ...cloze, gaps: { '1': { accept: ['a'] } } }] };
		const broken = { schemaVersion: 1, chapterId: 'X', tlReviewStatus: 'machine', lessons: [lesson] };
		expect(ChapterContent.safeParse(broken).success).toBe(false);
	});
});
