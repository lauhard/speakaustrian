import { expect, test, type Page } from '@playwright/test';
import { readFileSync } from 'node:fs';

type Item = { id: string; type: 'choice' | 'cloze' | 'short'; answer?: number; options?: string[]; gaps?: Record<string, { accept: string[] }>; accept?: string[] };
const a101 = JSON.parse(readFileSync('src/lib/content/a1-01.json', 'utf8'));
const items: Record<string, Item> = Object.fromEntries(a101.lessons.flatMap((l: { items: Item[] }) => l.items).map((i: Item) => [i.id, i]));

const answer = async (page: Page, correct: boolean) => {
	const item = items[(await page.locator('form[data-item]').getAttribute('data-item')) ?? ''];
	if (item.type === 'choice') await page.getByRole('radio').nth(correct ? item.answer! : ((item.answer ?? 0) + 1) % item.options!.length).check();
	else if (item.type === 'short') await page.getByTestId('short-input').fill(correct ? item.accept![0] : 'xyz');
	else for (const [gap, g] of Object.entries(item.gaps!)) await page.getByTestId(`gap-${gap}`).fill(correct ? g.accept[0] : 'xyz');
	await page.getByTestId('check').click();
	await page.getByTestId('next').click();
};
const headerFlames = (page: Page) => page.locator('header [data-testid="stat-flames"]');

test('flames v2 (K8) + XP (K9): a perfect lesson banks its flames and earns a shield; the shield catches the 2nd mistake', async ({ page }) => {
	await page.goto('/');
	await page.getByTestId('name-input').fill('Maria');
	await page.getByTestId('start').click();
	await page.getByTestId('chapter-A1-01').click();
	await page.getByTestId('lesson-A1-01-L01').click();
	await page.getByTestId('to-tasks').click();
	await expect(page.getByTestId('flame-pot')).toBeVisible();
	for (let i = 0; i < 8; i++) {
		if (i === 0) {
			// K9: XP pop right at the answer.
			const item = items[(await page.locator('form[data-item]').getAttribute('data-item')) ?? ''];
			if (item.type === 'choice') {
				await page.getByRole('radio').nth(item.answer!).check();
				await page.getByTestId('check').click();
				await expect(page.getByTestId('xp-gain')).toHaveText('+5 XP');
				await page.getByTestId('next').click();
				continue;
			}
		}
		await answer(page, true);
	}
	await expect(page.getByTestId('bank-points')).toBeVisible();
	await expect(headerFlames(page)).toHaveText('2');
	await expect(page.locator('header [data-testid="stat-shields"] b')).toHaveText('1');
	// K9: 8 × 5 XP + 20 first pass + 10 for 3 stars = 70 XP, level 1.
	await expect(page.getByTestId('level-ring')).toHaveAttribute('aria-label', /Level 1 · 70\/100/);

	await page.getByTestId('back').click();
	await page.getByTestId('lesson-A1-01-L02').click();
	await page.getByTestId('to-tasks').click();
	await answer(page, false);
	await answer(page, false);
	// The shield broke, the chapter flames stay.
	await expect(headerFlames(page)).toHaveText('2');
	await expect(page.locator('header [data-testid="stat-shields"] b')).toHaveText('0');
});

test('flames v2 (K8): the demo and the review earn no flames', async ({ page }) => {
	await page.goto('/');
	await page.getByTestId('name-input').fill('Maria');
	await page.getByTestId('start').click();
	await page.goto('/chapter/DEMO');
	await page.getByTestId('lesson-DEMO-01').click();
	await expect(page.locator('form[data-item]')).toBeVisible();
	await expect(page.getByTestId('flame-pot')).toHaveCount(0);
});
