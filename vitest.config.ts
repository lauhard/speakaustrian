import { defineConfig } from 'vitest/config';

// Unit tests cover the pure core only, so no SvelteKit plugin is needed here.
export default defineConfig({
	test: { include: ['src/**/*.test.ts'], environment: 'node' }
});
