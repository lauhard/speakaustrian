import { expect, test } from '@playwright/test';

test('settings: unlock all chapters opens A1-02 in free mode', async ({ page }) => {
	await page.goto('/');
	await page.getByTestId('name-input').fill('Maria');
	await page.getByTestId('start').click();
	await expect(page.getByTestId('chapter-A1-02')).toHaveCount(0);
	await page.getByTestId('settings-link').click();
	await page.getByTestId('setting-unlock').check();
	await page.goto('/');
	await page.getByTestId('chapter-A1-02').click();
	await expect(page.getByTestId('free-mode')).toBeVisible();
	await expect(page.getByTestId('stepper')).toBeVisible();
	await page.screenshot({ path: 'test-results/a1-02-free.png', fullPage: true });
});
