import { expect, test } from '@playwright/test';

test('PWA: manifest, icons, service worker and offline start page', async ({ page, context }) => {
	await page.goto('/');
	const manifest = await (await page.request.get('/manifest.webmanifest')).json();
	expect(manifest.display).toBe('standalone');
	for (const icon of manifest.icons) expect((await page.request.get(icon.src)).ok(), icon.src).toBe(true);
	await page.evaluate(() => navigator.serviceWorker.ready);
	await page.reload();
	await context.setOffline(true);
	await page.reload();
	await expect(page.getByTestId('settings-link')).toBeVisible();
	await context.setOffline(false);
});
