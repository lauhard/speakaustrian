import { expect, test } from '@playwright/test';

const signIn = async (page: import('@playwright/test').Page) => {
	await page.goto('/');
	await page.getByTestId('name-input').fill('Maria');
	await page.getByTestId('start').click();
};

test('chapter A1-01: learn cards, tasks, lesson marked as done', async ({ page }) => {
	await signIn(page);
	await expect(page.getByTestId('plan-day')).toContainText('1');
	await page.getByTestId('chapter-A1-01').click();
	await page.getByTestId('lesson-A1-01-L02').click();
	await page.getByTestId('to-tasks').click();

	// Cloze with an accepted alternative
	await page.getByTestId('gap-1').fill('bin');
	await page.getByTestId('check').click();
	await expect(page.getByTestId('feedback')).toHaveAttribute('data-verdict', 'correct');
	await page.getByTestId('next').click();

	// Reading task
	await page.getByRole('radio', { name: 'Santos' }).check();
	await page.getByTestId('check').click();
	await page.getByTestId('next').click();

	await page.getByRole('radio', { name: 'Grüß Gott, Herr Huber!' }).check();
	await page.getByTestId('check').click();
	await page.getByTestId('next').click();

	// Cloze: one gap wrong, one with a spelling detail
	await page.getByTestId('gap-1').fill('heißt');
	await page.getByTestId('gap-2').fill('heisse');
	await page.getByTestId('check').click();
	await expect(page.getByTestId('feedback')).toHaveAttribute('data-verdict', 'wrong');
	await page.getByTestId('next').click();

	// Listening task (no speech engine in the test browser: answer directly)
	await page.getByRole('radio', { name: 'Anna' }).check();
	await page.getByTestId('check').click();
	await expect(page.getByTestId('feedback')).toContainText('Ich heiße Anna Gruber.');
	await page.getByTestId('next').click();

	// Picture tasks: gap-fill and a short description
	await expect(page.getByTestId('item-image')).toBeVisible();
	await page.getByTestId('gap-1').fill('Anna');
	await page.getByTestId('gap-2').fill('Huber');
	await page.getByTestId('check').click();
	await page.getByTestId('next').click();
	await page.getByTestId('short-input').fill('er heisst Jonas Huber');
	await page.getByTestId('check').click();
	await expect(page.getByTestId('feedback')).toHaveAttribute('data-verdict', 'near');
	await page.getByTestId('next').click();
	await page.getByRole('radio', { name: 'Der Vorname von Herrn Huber ist Jonas.' }).check();
	await page.getByTestId('check').click();
	await page.getByTestId('next').click();

	await expect(page.getByTestId('result')).toBeVisible();
	await page.getByTestId('back').click();
	await expect(page.getByTestId('lesson-A1-01-L02')).toHaveAttribute('data-done', 'true');

	// Progress survives a reload (stored on the device)
	await page.reload();
	await expect(page.getByTestId('lesson-A1-01-L02')).toHaveAttribute('data-done', 'true');
});

test('free practice: picture tasks only', async ({ page }) => {
	await signIn(page);
	await page.getByTestId('free-practice').click();
	await page.getByTestId('practice-bild').click();
	await expect(page.getByTestId('item-image')).toBeVisible();
});

test('review: cards from a finished lesson are due the next day', async ({ page }) => {
	await page.clock.install({ time: new Date('2026-11-16T09:00:00') });
	await signIn(page);
	await page.getByTestId('chapter-A1-01').click();
	await page.getByTestId('lesson-A1-01-L04').click();
	await page.getByTestId('to-tasks').click();
	for (let i = 0; i < 5; i++) {
		const radio = page.getByRole('radio').first();
		if (await radio.isVisible()) await radio.check();
		else {
			await page.getByTestId('gap-1').fill('Danke');
			await page.getByTestId('gap-2').fill('dir');
		}
		await page.getByTestId('check').click();
		await page.getByTestId('next').click();
	}
	await page.getByTestId('back').click();
	await page.goto('/');
	await expect(page.getByTestId('review-due')).toHaveCount(0);

	// Next day: 8 cards are due; a right answer moves the card out of today's queue.
	await page.clock.setFixedTime(new Date('2026-11-17T09:00:00'));
	await page.reload();
	await expect(page.getByTestId('review-due')).toContainText('8');
	await page.getByTestId('review-due').click();
	await page.locator('input[data-correct="true"]').check();
	await page.getByTestId('card-check').click();
	await expect(page.getByTestId('card-feedback')).toHaveAttribute('data-verdict', 'correct');
	await page.goto('/');
	await expect(page.getByTestId('review-due')).toContainText('7');
});

test('free practice: words', async ({ page }) => {
	await signIn(page);
	await page.getByTestId('free-practice').click();
	await page.getByTestId('practice-woerter').click();
	await expect(page.getByTestId('card-check')).toBeVisible();
});
