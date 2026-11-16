// Answer comparison as specified in docs/spec/02g §3.1–3.2 (tolerance levels T0–T4).
export type Tolerance = {
	umlaut: boolean; // T1: ae/oe/ue/ss accepted for ä/ö/ü/ß
	caseInsensitive: boolean; // T2
	typo: boolean; // T3: distance depends on the word length
};

export const collapse = (s: string): string => s.normalize('NFC').trim().replace(/\s+/g, ' ');

const foldUmlauts = (s: string): string =>
	s
		.replace(/ä/g, 'ae')
		.replace(/ö/g, 'oe')
		.replace(/ü/g, 'ue')
		.replace(/Ä/g, 'Ae')
		.replace(/Ö/g, 'Oe')
		.replace(/Ü/g, 'Ue')
		.replace(/ß/g, 'ss');

export const normalize =
	(t: Tolerance) =>
	(s: string): string => {
		const collapsed = collapse(s).replace(/[.!?,;:]+$/g, '');
		const folded = t.umlaut ? foldUmlauts(collapsed) : collapsed;
		return t.caseInsensitive ? folded.toLowerCase() : folded;
	};

// T3: no tolerance below 5 characters, 1 for 5–8, 2 from 9.
export const allowedTypos = (length: number): 0 | 1 | 2 => (length < 5 ? 0 : length <= 8 ? 1 : 2);

// Damerau-Levenshtein (optimal string alignment): insert, delete, replace, swap neighbours.
export const damerauLevenshtein = (a: string, b: string): number => {
	const rows = a.length + 1;
	const cols = b.length + 1;
	const d = Array.from({ length: rows }, (_, i) => Array.from({ length: cols }, (_, j) => (i === 0 ? j : j === 0 ? i : 0)));
	for (let i = 1; i < rows; i++) {
		for (let j = 1; j < cols; j++) {
			const cost = a[i - 1] === b[j - 1] ? 0 : 1;
			d[i][j] = Math.min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + cost);
			if (i > 1 && j > 1 && a[i - 1] === b[j - 2] && a[i - 2] === b[j - 1]) d[i][j] = Math.min(d[i][j], d[i - 2][j - 2] + 1);
		}
	}
	return d[a.length][b.length];
};

export const isCorrect = (t: Tolerance, accepted: readonly string[], input: string): boolean => {
	const n = normalize(t);
	const given = n(input);
	if (given === '') return false;
	return accepted.some((a) => {
		const target = n(a);
		return given === target || (t.typo && damerauLevenshtein(given, target) <= allowedTypos(target.length));
	});
};

// Grammar gaps: the form is the learning goal, so no typo tolerance ("Zielform schlägt Toleranz").
export const GRAMMAR: Tolerance = { umlaut: true, caseInsensitive: true, typo: false };
// Vocabulary input: T1, T3 (02g UE-VOKABEL).
export const VOCAB: Tolerance = { umlaut: true, caseInsensitive: true, typo: true };
