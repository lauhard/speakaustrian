import type { Vocab } from './content/schema';
import type { RuleConfig } from './policy';
import type { Card, GameState, LocalDate } from './state';
import { collapse, isCorrect, VOCAB } from './tolerance';
import type { Verdict } from './grading';

// Review cards (Leitner), docs/spec/04a §5.5. Fixed mechanics for every policy (R-PL6);
// only the intervals come from the policy config.
export type Direction = Card['nextDirection'];
export type Introduced = { refId: string; isNoun: boolean };

export const addDays = (date: LocalDate, days: number): LocalDate =>
	new Date(Date.parse(`${date}T00:00:00Z`) + days * 86_400_000).toISOString().slice(0, 10);

// R-W2: a new card starts in box 1 and is due the next day. R-W7: nouns also train the genus.
export const newVocabCard = (intro: Introduced, today: LocalDate): Card => ({
	id: `card-${intro.refId}`,
	kind: 'vocab',
	refId: intro.refId,
	box: 1,
	due: addDays(today, 1),
	mastered: false,
	archived: false,
	directions: intro.isNoun ? ['recognize', 'produce', 'genus'] : ['recognize', 'produce'],
	nextDirection: 'recognize',
	lastWrongDirection: null,
	isNoun: intro.isNoun
});

export const addCards = (cards: GameState['review']['cards'], introduced: readonly Introduced[], today: LocalDate) =>
	introduced.reduce((acc, intro) => {
		const card = newVocabCard(intro, today);
		return card.id in acc ? acc : { ...acc, [card.id]: card };
	}, cards);

// R-W3: a wrong task creates an error card for its base item (box 1, due tomorrow); an existing one falls back.
export const errorCardId = (baseItemId: string): string => `err-${baseItemId}`;
export const addErrorCard = (cards: GameState['review']['cards'], baseItemId: string, today: LocalDate): GameState['review']['cards'] => {
	const id = errorCardId(baseItemId);
	const fresh: Card = {
		id,
		kind: 'error',
		refId: baseItemId,
		box: 1,
		due: addDays(today, 1),
		mastered: false,
		archived: false,
		directions: ['recognize'],
		nextDirection: 'recognize',
		lastWrongDirection: null,
		isNoun: false
	};
	return { ...cards, [id]: id in cards ? { ...cards[id], box: 1, due: fresh.due, mastered: false } : fresh };
};

// R-W5 + R-W7: right -> next box, due after that box's interval, direction rotates (box 5 noun: produce);
// right in box 5 -> mastered; wrong -> box 1, due tomorrow, same direction first again.
export const answerCard = (card: Card, correct: boolean, today: LocalDate, config: RuleConfig): Card => {
	if (!correct) return { ...card, box: 1, due: addDays(today, 1), lastWrongDirection: card.nextDirection };
	if (card.box === 5) return { ...card, mastered: true, lastWrongDirection: null };
	const box = (card.box + 1) as Card['box'];
	const rotated = card.directions[(card.directions.indexOf(card.nextDirection) + 1) % card.directions.length];
	return {
		...card,
		box,
		due: addDays(today, config.LEITNER_INTERVALS_DAYS[box - 1]),
		nextDirection: box === 5 && card.isNoun ? 'produce' : rotated,
		lastWrongDirection: null
	};
};

// R-W5/R-W6: due = due date reached; error cards first, then by due date (stable by id).
export const dueQueue = (s: GameState, today: LocalDate): Card[] =>
	Object.values(s.review.cards)
		.filter((c) => !c.mastered && !c.archived && c.due <= today)
		.sort((a, b) => Number(b.kind === 'error') - Number(a.kind === 'error') || a.due.localeCompare(b.due) || a.id.localeCompare(b.id));

export type Question =
	| { direction: 'recognize'; vocab: Vocab; options: Vocab[]; answer: number }
	| { direction: 'produce'; vocab: Vocab }
	| { direction: 'genus'; vocab: Vocab };

// Builds the question for one card. `random` is injected so the choice of distractors is testable.
export const buildQuestion = (direction: Direction, vocab: Vocab, pool: readonly Vocab[], random: () => number): Question => {
	if (direction === 'genus' && vocab.article) return { direction, vocab };
	if (direction === 'produce') return { direction, vocab };
	const others = pool.filter((v) => v.id !== vocab.id && v.en !== vocab.en);
	const picked = [...others].sort(() => random() - 0.5).slice(0, 2);
	const answer = Math.floor(random() * (picked.length + 1));
	return { direction: 'recognize', vocab, options: [...picked.slice(0, answer), vocab, ...picked.slice(answer)], answer };
};

// The full form a learner should produce: nouns with their article (R-W7).
export const fullForm = (v: Vocab): string => (v.article ? `${v.article} ${v.lemma}` : v.lemma);

// 02g UE-VOKABEL: lemma with T1/T3 tolerance, the article is a strict token.
export const gradeProduce = (input: string, vocab: Vocab): Verdict => {
	const text = collapse(input);
	if (text === '') return 'wrong';
	if (!vocab.article) return text === vocab.lemma ? 'correct' : isCorrect(VOCAB, [vocab.lemma], text) ? 'near' : 'wrong';
	const [first, ...rest] = text.split(' ');
	if (first.toLowerCase() !== vocab.article) return 'wrong';
	const lemma = rest.join(' ');
	if (text === fullForm(vocab)) return 'correct';
	return isCorrect(VOCAB, [vocab.lemma], lemma) ? 'near' : 'wrong';
};
