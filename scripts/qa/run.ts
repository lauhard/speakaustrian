// Content QA (masterprompt Phase 5 no. 11): `pnpm qa [chapterId …] [--file path.json] [--strict] [--require-pools]`.
// Thin shell around the pure checks in src/lib/core/qa/checks.ts (design notes, incl. the vocabulary check, are there).
//   no args          all chapters in src/lib/content (pools merged from `<chapter>-pools.json`)
//   --file           check one extra chapter file instead (e.g. the broken fixture)
//   --strict         warnings fail too (use before a batch goes to review)
//   --require-pools  a chapter without pools is an error (use for the chapter a batch is written for)
// Exit code 1 if a check fails. Expected output on today's content: docs/QA.md.
import { existsSync, readdirSync, readFileSync } from 'node:fs';
import { withPools } from '../../src/lib/core/content/merge.ts';
import { ChapterContent } from '../../src/lib/core/content/schema.ts';
import { demoConfig, makeDefaultPolicy } from '../../src/lib/core/policy.ts';
import { checkChapter, checkUniqueIds, failed, formatFindings, parseInventory } from '../../src/lib/core/qa/checks.ts';

const dir = 'src/lib/content';
const json = (path: string) => JSON.parse(readFileSync(path, 'utf8'));
const args = process.argv.slice(2);
const flag = (name: string) => args.includes(name);
const fileArg = args.includes('--file') ? args[args.indexOf('--file') + 1] : undefined;
const only = args.filter((a) => !a.startsWith('--') && a !== fileArg);

const course = json(`${dir}/course.json`);
const order: string[] = course.chapters.map((c: { id: string }) => c.id);
const focusOf = (id: string) => course.chapters.find((c: { id: string }) => c.id === id)?.focus;
const policy = makeDefaultPolicy(order, undefined, focusOf);
const demoPolicy = makeDefaultPolicy(order, demoConfig);

const files = readdirSync(dir).filter((n) => n.endsWith('.json') && !['course.json', 'qa-allowlist.json'].includes(n));
const poolFiles = files.filter((n) => n.endsWith('-pools.json')).map((n) => json(`${dir}/${n}`));
const repoChapters = files.filter((n) => !n.endsWith('-pools.json')).map((n) => withPools(json(`${dir}/${n}`), poolFiles));
const raws = fileArg ? [json(fileArg)] : repoChapters.filter((r) => only.length === 0 || only.includes(r.chapterId));

const parsedRepo = repoChapters.flatMap((r) => { const p = ChapterContent.safeParse(r); return p.success ? [p.data] : []; });
const inventory = parseInventory(readFileSync('docs/spec/03c-kapitel-wortschatz.tsv', 'utf8'));
const allowlist: string[] = json(`${dir}/qa-allowlist.json`).words;

const findings = raws.flatMap((raw) => {
	const id: string = raw.chapterId;
	const real = /^A[12]-\d{2}$/.test(id);
	const position = order.indexOf(id);
	// Chapters outside the course (DEMO) borrow from the first chapter.
	const scope = order.slice(0, Math.max(position, 0) + 1);
	return checkChapter(raw, {
		quota: (real ? policy : demoPolicy).testComposition(undefined as never, id).quota,
		real,
		position,
		knownChapters: parsedRepo.filter((c) => c.chapterId !== id && scope.includes(c.chapterId)),
		earlierChapterIds: scope.filter((s) => s !== id),
		inventory: inventory.filter((e) => scope.includes(e.chapter)),
		allowlist,
		fileExists: (src) => existsSync(`static${src}`),
		requirePools: flag('--require-pools')
	});
});
const all = [...findings, ...(fileArg ? [] : checkUniqueIds(parsedRepo))];
console.log(formatFindings(all));
process.exit(failed(all, flag('--strict')) ? 1 : 0);
