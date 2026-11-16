import { ChapterContent, type Discipline, type Item, type Localized } from '../content/schema.ts';
import { DE_FORMS } from './de-forms.ts';

// Content QA for chapter pools (step 004a). Pure functions: files, policy and inventory come in through `QaContext`.
// Spec: masterprompt Phase 5 no. 11 · 03 Q6/Q8/Q10 · 04a R-T1–R-T3, R-G1, R-K3, POOL_MIN, TWINS_MIN_TESTPOOL.
//
// Vocabulary check – why this design (masterprompt: "Lemmatisierung bzw. Formenliste; Ausnahmeliste"):
// the inventory (03c) only has base forms, the texts have inflected forms and compounds. A real German
// lemmatizer would be a heavy dependency and still guess. Instead a token counts as known if it is
//   1. a form that already occurs in the lessons of this or an earlier chapter (the lessons are the reviewed
//      teaching text, so every form there has been introduced), or an inventory lemma up to this chapter, or
//   2. an inventory lemma plus a regular ending (heiß-e, komm-st, Name-n), or
//   3. on the allowlist (proper names, places; `src/lib/content/qa-allowlist.json`).
// Everything else is reported as a WARNING per item, not as an error: step 2 is deliberately loose (few false
// alarms), irregular forms and compounds cannot be decided by a script. A person or the reviewer agent then
// either rewrites the item or puts the word on the allowlist. `pnpm qa --strict` turns warnings into failures.

export type Level = 'error' | 'warning' | 'info';
export type Finding = { level: Level; check: string; chapterId: string; itemId?: string; message: string };
export type InventoryEntry = { id: string; lemma: string; chapter: string };

export const QA_CONFIG = {
	POOL_MIN: 60, // 04a constants, 03 Q6
	TWINS_MIN_TESTPOOL: 2, // R-K3
	GATE_BLOCKS_MIN: 2, // masterprompt Phase 5 no. 11
	PRACTICE_PART_ITEMS: 40, // masterprompt Phase 5 no. 2 ("≈ 40"), fixed minimum by G-010 (decided A)
	TEST_PARTS_MAX: 3, // R-T3
	RECYCLING_MIN: 0.2 // 03 Q8
} as const;

export type QaContext = {
	// Result of `policy.testComposition` for this chapter (R-T1); the readiness round uses the same mix (R-G1).
	quota: Partial<Record<Discipline, number>>;
	// Real course chapter (`A1-01` …): quantity rules are errors. Sandbox chapters (DEMO) only get them as info.
	real: boolean;
	// Index of the chapter in the course order, -1 for chapters outside the course.
	position: number;
	// Parsed chapters whose lessons count as introduced (earlier chapters; for DEMO the chapter it borrows from).
	knownChapters: readonly ChapterContent[];
	// Ids of the chapters before this one (recycling, Q8) and inventory entries up to and including this chapter.
	earlierChapterIds: readonly string[];
	inventory: readonly InventoryEntry[];
	allowlist: readonly string[];
	fileExists: (src: string) => boolean;
	requirePools?: boolean;
};

// `docs/spec/03c-kapitel-wortschatz.tsv`: id, lemma, …, chapter (last column).
export const parseInventory = (tsv: string): InventoryEntry[] =>
	tsv
		.split('\n')
		.slice(1)
		.map((line) => line.split('\t'))
		.filter((c) => c.length >= 10)
		.map((c) => ({ id: c[0], lemma: c[1], chapter: c[9].trim() }));

export const tokenize = (text: string): string[] =>
	text
		.replace(/\{\{\w+\}\}/g, ' ')
		.replace(/[’`´]/g, "'")
		.match(/\p{L}+(?:'\p{L}+)*/gu) ?? [];

// German texts the learner reads or hears in a task (stimulus, options, accepted answers).
export const germanTexts = (item: Item): string[] => {
	const own =
		item.type === 'choice'
			? [item.prompt ?? '', ...item.options]
			: item.type === 'cloze'
				? [item.text, ...Object.values(item.gaps).flatMap((g) => g.accept)]
				: [item.prompt, ...item.accept];
	return [...own, item.audioText ?? ''].filter((t) => t !== '');
};

// German text of the lessons: vocabulary, cards (phrase + note), titles, instructions and explanations count as introduced.
const lessonTexts = (c: ChapterContent): string[] => [
	...(c.vocab ?? []).map((v) => v.lemma),
	...c.lessons.flatMap((l) => [
		l.title.de,
		...(l.cards ?? []).flatMap((card) => [card.phrase, card.note.de]),
		...l.items.flatMap((i) => [...germanTexts(i), i.instruction.de, i.explanation.de])
	])
];

export type Lexicon = { forms: ReadonlySet<string>; stems: ReadonlySet<string> };

export const makeLexicon = (lemmas: readonly string[], texts: readonly string[], allowlist: readonly string[]): Lexicon => {
	const lemmaTokens = lemmas.flatMap((l) => tokenize(l.replace(/\([^)]*\)/g, ' '))).map((t) => t.toLowerCase());
	const verbStem = (t: string) => (t.length > 4 && t.endsWith('en') ? [t.slice(0, -2)] : t.length > 3 && t.endsWith('n') ? [t.slice(0, -1)] : []);
	return {
		forms: new Set([...lemmaTokens, ...texts.flatMap(tokenize).map((t) => t.toLowerCase()), ...allowlist.map((a) => a.toLowerCase())]),
		stems: new Set(lemmaTokens.flatMap((t) => [t, ...verbStem(t)]))
	};
};

const ENDINGS = ['est', 'et', 'en', 'es', 'er', 'em', 'st', 'e', 't', 'n', 's'];

export const isKnownWord = (token: string, lex: Lexicon): boolean => {
	const t = token.toLowerCase();
	if (lex.forms.has(t) || lex.stems.has(t)) return true;
	if (t.includes("'") && t.split("'").every((part, i) => i > 0 || isKnownWord(part, lex))) return true;
	return ENDINGS.some((e) => t.endsWith(e) && lex.stems.has(t.slice(0, -e.length)));
};

const PLURAL = ['', 'n', 's', 'en', 'e', 'es'];
export const germanGermanForms = (text: string): string[] => {
	const phraseHits = DE_FORMS.filter((f) => f.includes(' ') && text.includes(f));
	const tokenHits = tokenize(text).filter((t) => PLURAL.some((p) => t.endsWith(p) && DE_FORMS.includes(t.slice(0, t.length - p.length))));
	return [...new Set([...phraseHits, ...tokenHits])];
};

const norm = (s: string) => s.trim().toLowerCase().replace(/\s+/g, ' ');
const familyOf = (i: Item) => i.family ?? i.id;
const fingerprint = (i: Item) => norm(JSON.stringify([i.type, germanTexts(i), i.image?.src ?? '']));
const groupBy = <T>(xs: readonly T[], key: (x: T) => string): Map<string, T[]> =>
	xs.reduce((m, x) => m.set(key(x), [...(m.get(key(x)) ?? []), x]), new Map<string, T[]>());

const localizedOf = (c: ChapterContent): [string | undefined, string, Localized][] => {
	const ofItem = (i: Item): [string | undefined, string, Localized][] => [
		[i.id, 'instruction', i.instruction],
		[i.id, 'explanation', i.explanation],
		...(i.image ? [[i.id, 'image.alt', i.image.alt] as [string, string, Localized]] : [])
	];
	return [
		...Object.entries(c.goals ?? {}).map(([g, t]) => [undefined, `goal ${g}`, t] as [undefined, string, Localized]),
		...c.lessons.flatMap((l) => [
			[undefined, `lesson ${l.id} title`, l.title] as [undefined, string, Localized],
			...(l.cards ?? []).map((card) => [undefined, `lesson ${l.id} card "${card.phrase}"`, card.note] as [undefined, string, Localized]),
			...l.items.flatMap(ofItem)
		]),
		...[...(c.pools?.practice ?? []), ...(c.pools?.test ?? [])].flatMap(ofItem)
	];
};

export const checkChapter = (raw: unknown, ctx: QaContext): Finding[] => {
	const rawId = String((raw as { chapterId?: unknown })?.chapterId ?? '?');
	const parsed = ChapterContent.safeParse(raw);
	// 1. Schema: also covers unique ids, `family` pointing to a base item of the same pool, goals with titles,
	//    answer index in range, ≥ 1 twin per test item, all three languages present.
	if (!parsed.success) {
		return parsed.error.issues.map((issue) => {
			const itemId = /^([A-Z0-9-]+):/.exec(issue.message)?.[1];
			return { level: 'error' as const, check: 'schema', chapterId: rawId, itemId, message: `${issue.path.join('.')} ${issue.message}`.trim() };
		});
	}
	const c = parsed.data;
	const C = QA_CONFIG;
	const sizeLevel: Level = ctx.real ? 'error' : 'info';
	const f = (level: Level, check: string, message: string, itemId?: string): Finding => ({ level, check, chapterId: c.chapterId, itemId, message });
	const lessonItems = c.lessons.flatMap((l) => l.items);
	const practice = c.pools?.practice ?? [];
	const test = c.pools?.test ?? [];
	const pool = [...practice, ...test];
	const quota = Object.entries(ctx.quota) as [Discipline, number][];
	// Sandbox chapters only test the disciplines they have items for (demoConfig).
	const applies = (items: readonly Item[], d: Discipline) => ctx.real || items.some((i) => i.skill === d);

	const general: Finding[] = [
		// 6. Translations (the schema guarantees the fields, here: blank or apparently untranslated texts).
		...localizedOf(c).flatMap(([itemId, where, t]) => [
			...(['de', 'en', 'tl'] as const).filter((lang) => t[lang].trim() === '').map((lang) => f('error', 'i18n.blank', `${where}.${lang} is blank`, itemId)),
			...(tokenize(t.de).length >= 3 && (norm(t.tl) === norm(t.de) || norm(t.en) === norm(t.de)) ? [f('warning', 'i18n.untranslated', `${where}: en/tl equals de`, itemId)] : [])
		]),
		// 7. Picture files.
		...[...lessonItems, ...pool].filter((i) => i.image && !ctx.fileExists(i.image.src)).map((i) => f('error', 'image.missing', `picture ${i.image?.src} not found`, i.id)),
		// 9. D10: German-German forms (03g) in learner texts. Marking cannot be expressed in the schema yet, so every hit is a warning.
		...[...lessonItems, ...pool].flatMap((i) => {
			const hits = [...new Set(germanTexts(i).flatMap(germanGermanForms))];
			return hits.length ? [f('warning', 'variety.de', `German-German form (D10): ${hits.join(', ')}`, i.id)] : [];
		})
	];
	if (!c.pools) return [...general, f(ctx.requirePools ? 'error' : 'info', 'pools.missing', 'no pools yet – pool checks skipped')];

	const families = [...groupBy(test, familyOf).entries()];
	const baseSkill = (id: string, members: Item[]) => (members.find((m) => m.id === id) ?? members[0]).skill;
	const usedGoals = new Set(pool.flatMap((i) => i.goals ?? []));
	const duplicates = [...groupBy(pool, fingerprint).values()].filter((g) => g.length > 1);

	const lex = makeLexicon(
		ctx.inventory.map((e) => e.lemma),
		[c, ...ctx.knownChapters].flatMap(lessonTexts),
		ctx.allowlist
	);
	const earlierVocab = new Set(ctx.inventory.filter((e) => ctx.earlierChapterIds.includes(e.chapter)).map((e) => e.id));
	const earlierGoals = new Set(ctx.knownChapters.filter((k) => ctx.earlierChapterIds.includes(k.chapterId)).flatMap((k) => Object.keys(k.goals ?? {})));
	const recycled = practice.filter((i) => (i.refs ?? []).some((r) => earlierVocab.has(r)) || (i.goals ?? []).some((g) => earlierGoals.has(g)));
	const practiceMin = C.PRACTICE_PART_ITEMS + C.GATE_BLOCKS_MIN * quota.reduce((sum, [, n]) => sum + n, 0);

	return [
		...general,
		// 2. Test pool: size, twins, quota per discipline reachable with families (R-T2: never two twins in one test).
		...(test.length < C.POOL_MIN ? [f(sizeLevel, 'pool.size', `test pool has ${test.length} items, needs ≥ ${C.POOL_MIN}`)] : []),
		...families
			.filter(([, members]) => members.length < C.TWINS_MIN_TESTPOOL + 1)
			.map(([id, members]) => f(sizeLevel, 'pool.twins', `test item has ${members.length - 1} twin(s), needs ≥ ${C.TWINS_MIN_TESTPOOL} (R-K3)`, id)),
		...families
			.filter(([, members]) => new Set(members.map((m) => m.skill)).size > 1)
			.map(([id]) => f('warning', 'pool.family-skill', 'twins of one family have different disciplines', id)),
		...quota
			.filter(([d]) => applies(test, d))
			.map(([d, n]) => [d, n, families.filter(([id, members]) => baseSkill(id, members) === d).length] as const)
			.filter(([, n, have]) => have < n)
			.map(([d, n, have]) => f('error', 'pool.quota', `test needs ${n} × ${d} from different twin families, pool has ${have} (R-T1, R-T2)`)),
		// 3. Practice pool: ≥ 2 readiness blocks without repeats (R-G1), plus the practice part.
		...quota
			.filter(([d]) => applies(practice, d))
			.map(([d, n]) => [d, n * C.GATE_BLOCKS_MIN, practice.filter((i) => i.skill === d).length] as const)
			.filter(([, need, have]) => have < need)
			.map(([d, need, have]) => f(sizeLevel, 'practice.gate', `${C.GATE_BLOCKS_MIN} readiness blocks need ${need} × ${d} in the practice pool, it has ${have} (R-G1)`)),
		...(practice.length < practiceMin ? [f(sizeLevel, 'practice.size', `practice pool has ${practice.length} items; practice part (${C.PRACTICE_PART_ITEMS}) + ${C.GATE_BLOCKS_MIN} readiness blocks need ${practiceMin} (G-010)`)] : []),
		// Masterprompt: every item has ≥ 1 twin. In the practice pool a twin is a family member; a warning, the draws do not depend on it.
		...(ctx.real ? [...groupBy(practice, familyOf).values()].filter((m) => m.length < 2).map(([i]) => f('warning', 'practice.twins', 'practice item without a twin', i.id)) : []),
		// 3./Q6: no task twice – neither across practice and test pool nor as a "twin" with the same surface.
		...duplicates.flatMap(([first, ...rest]) => rest.map((i) => f('error', 'pool.duplicate', `same task text as ${first.id}`, i.id))),
		// 4. Choice: the answer index is checked by the schema; equal options would make two answers right.
		...pool
			.filter((i) => i.type === 'choice' && new Set(i.options.map(norm)).size !== i.options.length)
			.map((i) => f('error', 'choice.options', 'choice has duplicate options', i.id)),
		// 5. Goals: every chapter goal is trained; test tasks have at most 3 parts (R-T3).
		...Object.keys(c.goals ?? {})
			.filter((g) => !usedGoals.has(g))
			.map((g) => f('error', 'goals.uncovered', `goal ${g} is not covered by any pool item`)),
		...test
			.filter((i) => i.type === 'cloze' && Object.keys(i.gaps).length > C.TEST_PARTS_MAX)
			.map((i) => f('error', 'test.parts', `test task has more than ${C.TEST_PARTS_MAX} parts (R-T3)`, i.id)),
		// 8. Vocabulary within the chapter scope (design note at the top of this file).
		...pool.flatMap((i) => {
			const unknown = [...new Set(germanTexts(i).flatMap(tokenize).filter((t) => !isKnownWord(t, lex)))];
			return unknown.length ? [f(ctx.real ? 'warning' : 'info', 'vocab.unknown', `not in the vocabulary up to this chapter: ${unknown.join(', ')}`, i.id)] : [];
		}),
		// 10. Recycling (Q8): practice items that use vocabulary (`refs`) or goals of earlier chapters. Not measurable in the first chapter (G-011).
		...(ctx.position <= 0
			? [f('info', 'recycling.na', 'recycling not measured: no earlier chapter (G-011)')]
			: recycled.length < C.RECYCLING_MIN * practice.length
				? [f(sizeLevel, 'recycling', `${recycled.length} of ${practice.length} practice items recycle earlier chapters, needs ≥ ${C.RECYCLING_MIN * 100} % (Q8)`)]
				: [])
	];
};

// Item ids must be unique across all chapters (error cards and test lists only keep ids).
export const checkUniqueIds = (chapters: readonly ChapterContent[]): Finding[] => {
	const all = chapters.flatMap((c) => [...c.lessons.flatMap((l) => l.items), ...(c.pools?.practice ?? []), ...(c.pools?.test ?? [])].map((i) => ({ id: i.id, chapterId: c.chapterId })));
	return [...groupBy(all, (x) => x.id).values()]
		.filter((g) => new Set(g.map((x) => x.chapterId)).size > 1)
		.map((g) => ({ level: 'error' as const, check: 'ids.duplicate', chapterId: g[1].chapterId, itemId: g[0].id, message: `item id also used in ${g[0].chapterId}` }));
};

export const failed = (findings: readonly Finding[], strict = false): boolean =>
	findings.some((x) => x.level === 'error' || (strict && x.level === 'warning'));

export const formatFindings = (findings: readonly Finding[]): string => {
	const order: Level[] = ['error', 'warning', 'info'];
	const lines = [...findings]
		.sort((a, b) => a.chapterId.localeCompare(b.chapterId) || order.indexOf(a.level) - order.indexOf(b.level))
		.map((x) => `${x.level.toUpperCase().padEnd(7)} ${x.chapterId.padEnd(6)} ${(x.itemId ?? '–').padEnd(16)} [${x.check}] ${x.message}`);
	const count = (l: Level) => findings.filter((x) => x.level === l).length;
	return [...lines, `QA: ${count('error')} error(s), ${count('warning')} warning(s), ${count('info')} info`].join('\n');
};
