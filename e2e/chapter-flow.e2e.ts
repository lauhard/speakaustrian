import { readFileSync } from 'node:fs';
import { expect, test, type Page } from '@playwright/test';

// Chapter flow on the DEMO sandbox (005c): lessons → practice → readiness round → test → correction / error review.
type Item = { id: string; type: 'choice' | 'cloze' | 'short'; answer?: number; options?: string[]; gaps?: Record<string, { accept: string[] }>; accept?: string[] };
const demo = JSON.parse(readFileSync('src/lib/content/demo.json', 'utf8'));
const items: Record<string, Item> = Object.fromEntries(
	[...demo.lessons.flatMap((l: { items: Item[] }) => l.items), ...demo.pools.practice, ...demo.pools.test].map((i: Item) => [i.id, i])
);

const signIn = async (page: Page) => {
	await page.goto('/');
	await page.getByTestId('name-input').fill('Maria');
	await page.getByTestId('start').click();
};

// Fills in the current task right or wrong and checks it; the caller taps "next".
const answer = async (page: Page, correct: boolean) => {
	const id = await page.locator('form[data-item]').getAttribute('data-item');
	const item = items[id ?? ''];
	if (item.type === 'choice') {
		const pick = correct ? item.answer! : ((item.answer ?? 0) + 1) % item.options!.length;
		await page.getByRole('radio').nth(pick).check();
	} else if (item.type === 'short') {
		await page.getByTestId('short-input').fill(correct ? item.accept![0] : 'xyz');
	} else {
		for (const [gap, g] of Object.entries(item.gaps!)) await page.getByTestId(`gap-${gap}`).fill(correct ? g.accept[0] : 'xyz');
	}
	await page.getByTestId('check').click();
};

const phase = (page: Page) =>
	page
		.getByTestId('flow-phase')
		.getAttribute('data-phase', { timeout: 1500 })
		.catch(() => null);

// Plays tasks of one phase until the phase changes; `correctAt(n)` decides each answer (n = 0-based count in this phase).
const play = async (page: Page, name: string, correctAt: (n: number) => boolean = () => true) => {
	for (let n = 0; (await phase(page)) === name; n++) {
		await answer(page, correctAt(n));
		await page.getByTestId('next').click();
	}
};

// From the chapter page: the lesson, then practice (and the readiness round when `gate` is true).
const lessonAndPractice = async (page: Page) => {
	await page.getByTestId('lesson-DEMO-01').click();
	for (let i = 0; i < 6; i++) {
		await answer(page, true);
		await page.getByTestId('next').click();
	}
	await page.getByTestId('back').click();
	await play(page, 'PRACTICE');
};

const toTestReady = async (page: Page) => {
	await signIn(page);
	await page.goto('/chapter/DEMO');
	await lessonAndPractice(page);
	await play(page, 'GATE');
	await expect(page.getByTestId('flow-start-test')).toBeVisible();
};

test('DEMO chapter: perfect run to the end (bonus life, restart)', async ({ page }) => {
	await toTestReady(page);
	await page.getByTestId('flow-start-test').click();
	await expect(page.getByTestId('lives')).toHaveAttribute('data-lives', '2');
	await play(page, 'TEST');
	await expect(page.getByTestId('flow-passed')).toBeVisible();
	await expect(page.getByTestId('flow-passed')).toContainText(/Bonus|bonus/);
	// Flame score: a perfect chapter banks its flames into the header score.
	await expect(page.getByTestId('bank-points')).toBeVisible();
	await expect.poll(async () => Number(await page.locator('header [data-testid="stat-score"] b').innerText())).toBeGreaterThan(0);
	await page.screenshot({ path: 'test-results/flame-bank.png' });
	await page.getByTestId('flow-restart').click();
	await expect(page.getByTestId('lesson-DEMO-01')).toBeVisible();
});

test('DEMO chapter: one mistake → correction round with a twin → passed without bonus', async ({ page }) => {
	await toTestReady(page);
	await page.getByTestId('flow-start-test').click();
	await answer(page, false);
	await expect(page.getByTestId('life-lost')).toBeVisible();
	await page.getByTestId('next').click();
	await expect(page.getByTestId('lives')).toHaveAttribute('data-lives', '1');
	await play(page, 'TEST');
	await expect(page.getByTestId('flow-phase')).toHaveAttribute('data-phase', 'CORRECTION');
	await play(page, 'CORRECTION');
	await expect(page.getByTestId('flow-passed')).toBeVisible();
	await expect(page.getByTestId('flow-passed')).not.toContainText(/Bonus|bonus/);
});

test('DEMO chapter: no lives left → error review → chapter again in repeat mode', async ({ page }) => {
	await toTestReady(page);
	await page.getByTestId('flow-start-test').click();
	await play(page, 'TEST', () => false);
	await expect(page.getByTestId('flow-phase')).toHaveAttribute('data-phase', 'ERROR_REVIEW');
	await expect(page.getByTestId('flow-rk6')).toHaveCount(0);
	await play(page, 'ERROR_REVIEW');
	await expect(page.getByTestId('lesson-DEMO-01')).toBeVisible();

	// R-K6: the 2nd failed attempt names the goals with the most mistakes.
	await lessonAndPractice(page);
	await play(page, 'GATE');
	await page.getByTestId('flow-start-test').click();
	await play(page, 'TEST', () => false);
	await expect(page.getByTestId('flow-phase')).toHaveAttribute('data-phase', 'ERROR_REVIEW');
	await expect(page.getByTestId('flow-rk6')).toBeVisible();
});

test('DEMO chapter: a weak readiness block leads to targeted practice and a new block', async ({ page }) => {
	await signIn(page);
	await page.goto('/chapter/DEMO');
	await lessonAndPractice(page);
	await play(page, 'GATE', () => false);
	await expect(page.getByTestId('flow-phase')).toHaveAttribute('data-phase', 'TARGETED_PRACTICE');
	await play(page, 'TARGETED_PRACTICE');
	await expect(page.getByTestId('flow-phase')).toHaveAttribute('data-phase', 'GATE');
});

test('review page: error cards of the DEMO test come back the next day and are asked as tasks', async ({ page }) => {
	await page.clock.install({ time: new Date('2026-11-16T09:00:00') });
	await toTestReady(page);
	await page.getByTestId('flow-start-test').click();
	await play(page, 'TEST', () => false);
	await play(page, 'ERROR_REVIEW');

	// R-W3: the wrong tasks made error cards (box 1, due tomorrow); they are asked first, wrong ones again in the round.
	await page.clock.setFixedTime(new Date('2026-11-17T09:00:00'));
	await page.goto('/review?store=demo');
	await expect(page.getByTestId('review-errors')).toBeVisible();
	await answer(page, false);
	await page.getByTestId('next').click();
	await expect(page.getByTestId('review-errors')).toBeVisible();
	for (let i = 0; i < 4 && (await page.getByTestId('review-errors').isVisible()); i++) {
		await answer(page, true);
		await page.getByTestId('next').click();
	}
	await expect(page.getByTestId('review-none')).toBeVisible();
});

test('DEMO chapter: a lesson below 51 % stays open and keeps practice locked (K1, K2, K10)', async ({ page }) => {
	await signIn(page);
	await page.goto('/chapter/DEMO');
	await page.getByTestId('lesson-DEMO-01').click();
	for (let i = 0; i < 6; i++) {
		await answer(page, i < 3);
		await page.getByTestId('next').click();
	}
	// 3 of 6 = 50 %: not passed, no stars, solutions without a green tick.
	await expect(page.getByTestId('result')).toHaveAttribute('data-passed', 'false');
	await expect(page.getByTestId('result-heading')).toBeVisible();
	await expect(page.getByTestId('misses')).not.toContainText('✓');
	await page.getByTestId('back').click();
	await expect(page.getByTestId('lesson-DEMO-01')).toHaveAttribute('data-done', 'false');
	await expect(page.getByTestId('chapter-flow')).toHaveCount(0);

	// Second try with 4 of 6 (67 %) passes and opens practice.
	await page.getByTestId('lesson-DEMO-01').click();
	for (let i = 0; i < 6; i++) {
		await answer(page, i < 4);
		await page.getByTestId('next').click();
	}
	await expect(page.getByTestId('result')).toHaveAttribute('data-passed', 'true');
	await page.getByTestId('back').click();
	await expect(page.getByTestId('flow-phase')).toHaveAttribute('data-phase', 'PRACTICE');
});
