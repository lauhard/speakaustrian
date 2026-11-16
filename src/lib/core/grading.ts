import type { Item } from './content/schema';
import { collapse, GRAMMAR, isCorrect, type Tolerance } from './tolerance';

// 'near' = right, but only through a tolerance (case, ae/oe/ue/ss, typo, stray punctuation).
export type Verdict = 'correct' | 'near' | 'wrong';

export type Response =
	| { type: 'choice'; selected: number }
	| { type: 'cloze'; gaps: Record<string, string> }
	| { type: 'short'; text: string };

export type Grade = {
	verdict: Verdict;
	// Per-gap verdicts for cloze items.
	parts: Record<string, Verdict>;
	// First accepted answer per part, shown in feedback.
	expected: Record<string, string>;
};

// Exact answer -> 'correct'. Accepted only through a tolerance of 02g §3.1 -> 'near':
// it counts as right and the feedback points at the spelling.
export const gradeText = (input: string, accept: readonly string[], tolerance: Tolerance = GRAMMAR): Verdict => {
	const strict = collapse(input);
	if (strict === '') return 'wrong';
	if (accept.some((a) => collapse(a) === strict)) return 'correct';
	return isCorrect(tolerance, accept, input) ? 'near' : 'wrong';
};

const worst = (verdicts: readonly Verdict[]): Verdict =>
	verdicts.includes('wrong') ? 'wrong' : verdicts.includes('near') ? 'near' : 'correct';

export const gradeItem = (item: Item, response: Response): Grade => {
	if (item.type === 'choice' && response.type === 'choice') {
		const verdict: Verdict = response.selected === item.answer ? 'correct' : 'wrong';
		return { verdict, parts: { answer: verdict }, expected: { answer: item.options[item.answer] } };
	}
	if (item.type === 'short' && response.type === 'short') {
		const verdict = gradeText(response.text, item.accept);
		return { verdict, parts: { answer: verdict }, expected: { answer: item.accept[0] } };
	}
	if (item.type === 'cloze' && response.type === 'cloze') {
		const ids = Object.keys(item.gaps);
		const parts = Object.fromEntries(
			ids.map((id) => [id, gradeText(response.gaps[id] ?? '', item.gaps[id].accept)])
		);
		const expected = Object.fromEntries(ids.map((id) => [id, item.gaps[id].accept[0]]));
		return { verdict: worst(Object.values(parts)), parts, expected };
	}
	throw new Error(`response type ${response.type} does not match item type ${item.type}`);
};

// 02g: an answer accepted through a tolerance counts as right.
export const passes = (verdict: Verdict): boolean => verdict !== 'wrong';

export type ClozeSegment = { kind: 'text'; value: string } | { kind: 'gap'; id: string };

export const parseCloze = (text: string): ClozeSegment[] =>
	text
		.split(/(\{\{\w+\}\})/g)
		.filter((part) => part !== '')
		.map((part) => {
			const gap = /^\{\{(\w+)\}\}$/.exec(part);
			return gap ? { kind: 'gap' as const, id: gap[1] } : { kind: 'text' as const, value: part };
		});
