import { describe, expect, it } from 'vitest';
import { defaultConfig, makeDefaultPolicy } from './policy';
import { makeReducer, newGame, type GameEvent } from './reducer';
import { addDays, answerCard, buildQuestion, dueQueue, gradeProduce, newVocabCard } from './review';

const order = ['A1-01', 'A1-02'];
const policy = makeDefaultPolicy(order);
const reduce = makeReducer(policy, order);
let n = 0;
const ev = (e: object, at: string) => ({ id: `r${n++}`, at, tzOffsetMin: 60, ...e }) as unknown as GameEvent;
const name = { id: 'W-A1-0324', lemma: 'Name', article: 'der' as const, en: 'name', tl: 'pangalan' };
const danke = { id: 'W-A1-0092', lemma: 'danke', en: 'thank you', tl: 'salamat' };
const bitte = { id: 'W-A1-0091', lemma: 'bitte', en: 'please', tl: 'pakiusap' };
const gut = { id: 'W-A1-0173', lemma: 'gut', en: 'good', tl: 'mabuti' };

const afterLesson = [
	ev({ type: 'PROFILE_CREATED', name: 'Maria', pensumMin: 90 }, '2026-11-16T10:00:00Z'),
	ev({ type: 'LESSON_COMPLETED', chapterId: 'A1-01', lessonId: 'L1', introduced: [{ refId: name.id, isNoun: true }, { refId: danke.id, isNoun: false }] }, '2026-11-16T10:30:00Z')
].reduce(reduce, newGame(policy));

describe('cards', () => {
	it('R-W2: a finished lesson creates cards in box 1, due the next day', () => {
		const card = afterLesson.review.cards['card-W-A1-0324'];
		expect(card).toMatchObject({ box: 1, due: '2026-11-17', directions: ['recognize', 'produce', 'genus'] });
		expect(afterLesson.review.cards['card-W-A1-0092'].directions).toEqual(['recognize', 'produce']);
		expect(dueQueue(afterLesson, '2026-11-16')).toHaveLength(0);
		expect(dueQueue(afterLesson, '2026-11-17')).toHaveLength(2);
	});
	it('R-W5: right moves up with intervals 1/3/7/14/30, right in box 5 masters the card', () => {
		const days = ['2026-11-17', '2026-11-20', '2026-11-27', '2026-12-11'];
		const walked = days.reduce((card, day) => answerCard(card, true, day, defaultConfig), newVocabCard({ refId: 'x', isNoun: false }, '2026-11-16'));
		expect(walked).toMatchObject({ box: 5, due: addDays('2026-12-11', 30), mastered: false });
		expect(answerCard(walked, true, walked.due, defaultConfig).mastered).toBe(true);
	});
	it('R-W5: wrong falls back to box 1, due tomorrow', () => {
		const card = { ...newVocabCard({ refId: 'x', isNoun: false }, '2026-11-16'), box: 4 as const };
		expect(answerCard(card, false, '2026-11-20', defaultConfig)).toMatchObject({ box: 1, due: '2026-11-21', lastWrongDirection: 'recognize' });
	});
	it('R-W7: direction rotates, stays after a mistake, box 5 nouns are always produced with article', () => {
		const start = newVocabCard({ refId: name.id, isNoun: true }, '2026-11-16');
		const once = answerCard(start, true, '2026-11-17', defaultConfig);
		expect(once.nextDirection).toBe('produce');
		expect(answerCard(once, false, '2026-11-20', defaultConfig).nextDirection).toBe('produce');
		const box4 = { ...start, box: 4 as const, nextDirection: 'genus' as const };
		expect(answerCard(box4, true, '2026-12-01', defaultConfig).nextDirection).toBe('produce');
	});
	it('books a review answer once: only a due card in its current direction', () => {
		const answer = ev({ type: 'REVIEW_ANSWERED', cardId: 'card-W-A1-0092', direction: 'recognize', correct: true }, '2026-11-17T09:00:00Z');
		const once = reduce(afterLesson, answer);
		expect(once.review.cards['card-W-A1-0092']).toMatchObject({ box: 2, due: '2026-11-20', nextDirection: 'produce' });
		expect(reduce(once, { ...answer, id: 'again' })).toEqual(once);
	});
});

describe('questions and grading', () => {
	it('recognize: three options, the right one among them', () => {
		const q = buildQuestion('recognize', danke, [name, danke, bitte, gut], () => 0.4);
		expect(q.direction).toBe('recognize');
		if (q.direction !== 'recognize') return;
		expect(q.options).toHaveLength(3);
		expect(q.options[q.answer]).toBe(danke);
	});
	it('genus falls back to recognize for words without article', () => {
		expect(buildQuestion('genus', danke, [name, bitte, gut], () => 0.4).direction).toBe('recognize');
	});
	it('02g: article is strict, the noun tolerates case and typos', () => {
		expect(gradeProduce('der Name', name)).toBe('correct');
		expect(gradeProduce('der name', name)).toBe('near');
		expect(gradeProduce('die Name', name)).toBe('wrong');
		expect(gradeProduce('Name', name)).toBe('wrong');
		expect(gradeProduce('dnake', danke)).toBe('near');
	});
});
