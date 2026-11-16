import { defineConfig } from '@playwright/test';

export default defineConfig({
	webServer: { command: 'pnpm build && pnpm preview', port: 4173, timeout: 180_000 },
	testDir: 'e2e',
	testMatch: '**/*.e2e.ts',
	use: {
		// Optional: point to an already installed Chromium instead of downloading one.
		launchOptions: process.env.PW_CHROMIUM ? { executablePath: process.env.PW_CHROMIUM } : {},
		baseURL: 'http://localhost:4173', viewport: { width: 390, height: 844 } }
});
