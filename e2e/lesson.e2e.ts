import { expect, test } from '@playwright/test';

test('name entry, cloze grading and picture question', async ({ page }) => {
	await page.goto('/');
	await page.getByTestId('name-input').fill('Maria');
	await page.getByTestId('start').click();
	await page.getByTestId('start-lesson').click();

	// Task 1: multiple choice
	await page.getByRole('radio', { name: 'Grüß Gott!' }).check();
	await page.getByTestId('check').click();
	await expect(page.getByTestId('feedback')).toHaveAttribute('data-verdict', 'correct');
	await page.getByTestId('next').click();

	// Task 2: cloze with a wrong second gap
	await page.getByTestId('gap-1').fill('heiße');
	await page.getByTestId('gap-2').fill('von');
	await page.getByTestId('check').click();
	await expect(page.getByTestId('feedback')).toHaveAttribute('data-verdict', 'wrong');
	await page.getByTestId('next').click();

	// Task 3: cloze, spelling detail only
	await page.getByTestId('gap-1').fill('heissen');
	await page.getByTestId('check').click();
	await expect(page.getByTestId('feedback')).toHaveAttribute('data-verdict', 'near');
	await page.getByTestId('next').click();

	// Task 4: picture question
	await expect(page.getByTestId('item-image')).toBeVisible();
	await page.getByTestId('short-input').fill('Sommer');
	await page.getByTestId('check').click();
	await expect(page.getByTestId('feedback')).toHaveAttribute('data-verdict', 'correct');

	// Progress survives a reload (stored on the device)
	await page.goto('/');
	await expect(page.getByTestId('start-lesson')).toBeVisible();
});
