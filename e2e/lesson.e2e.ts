import { expect, test } from '@playwright/test';

const signIn = async (page: import('@playwright/test').Page) => {
	await page.goto('/');
	await page.getByTestId('name-input').fill('Maria');
	await page.getByTestId('start').click();
};

test('chapter A1-01: learn cards, tasks, lesson marked as done', async ({ page }) => {
	await signIn(page);
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

	await expect(page.getByTestId('result')).toBeVisible();
	await page.getByTestId('back').click();
	await expect(page.getByTestId('lesson-A1-01-L02')).toContainText('✓');
});

test('free practice: picture tasks only', async ({ page }) => {
	await signIn(page);
	await page.getByTestId('free-practice').click();
	await page.getByTestId('practice-bild').click();
	await expect(page.getByTestId('item-image')).toBeVisible();
});
