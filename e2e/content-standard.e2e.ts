import { expect, test } from '@playwright/test';

// Content standard v2 pilot (A1-03-L01): intro, rule/culture cards, word bank fills gaps in order and can be taken back.
test('content standard v2: lesson intro, rule cards and a word bank cloze', async ({ page }) => {
	await page.goto('/');
	await page.getByTestId('name-input').fill('Maria');
	await page.getByTestId('start').click();
	await page.getByTestId('settings-link').click();
	await page.getByTestId('setting-unlock').check();
	await page.goto('/chapter/A1-03/A1-03-L01');
	await expect(page.getByTestId('lesson-intro')).toBeVisible();
	await expect(page.getByTestId('card-rule')).toHaveCount(2);
	await expect(page.getByTestId('card-culture')).toHaveCount(1);
	await page.screenshot({ path: 'test-results/cs-learn.png', fullPage: true });
	await page.getByTestId('to-tasks').click();
	// Items 1–3 are choice tasks; item 4 is the dialogue cloze with a word bank.
	for (let i = 0; i < 3; i++) {
		await page.getByRole('radio').first().check();
		await page.getByTestId('check').click();
		await page.getByTestId('next').click();
	}
	const bank = page.getByTestId('bank-word');
	await bank.filter({ hasText: /^kommen$/ }).click();
	await bank.filter({ hasText: /^kommt$/ }).click();
	await expect(page.getByTestId('gap-1')).toHaveValue('kommen');
	await expect(page.getByTestId('gap-2')).toHaveValue('kommt');
	await bank.filter({ hasText: /^kommt$/ }).click();
	await expect(page.getByTestId('gap-2')).toHaveValue('');
	await bank.filter({ hasText: /^komme$/ }).click();
	await page.screenshot({ path: 'test-results/cs-bank.png' });
	await page.getByTestId('check').click();
	await expect(page.getByTestId('feedback')).toHaveAttribute('data-verdict', 'correct');
});
