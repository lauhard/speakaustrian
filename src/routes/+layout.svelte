<script lang="ts">
	// Registers the install-prompt listener early: the browser fires it once, soon after load.
	import '#lib/install.svelte.ts';
	import { resolve } from '$app/paths';
	import { getLocale, locales, setLocale } from '#lib/paraglide/runtime.js';
	import { m } from '#lib/paraglide/messages.js';
	import './layout.css';
	import type { LayoutProps } from './$types';

	let { children }: LayoutProps = $props();
	const labels: Record<string, string> = { de: 'DE', en: 'EN', tl: 'TL' };
</script>

<svelte:head>
	<title>{m.app_title()}</title>
</svelte:head>

<div class="mx-auto flex min-h-dvh max-w-md flex-col px-4">
	<header class="flex items-center justify-between gap-3 py-4">
		<a href={resolve('/')} class="flex items-center gap-2 no-underline">
			<img src="/icons/logo.svg" alt="" class="h-9 w-9 rounded-xl shadow-sm" width="36" height="36" />
			<span class="text-xl font-black tracking-tight text-ink">{m.app_title()}</span>
		</a>
		<div class="flex items-center gap-2">
		<a href={resolve('/settings')} class="grid h-9 w-9 place-items-center rounded-full bg-white text-lg ring-1 ring-line no-underline" aria-label={m.settings()} data-testid="settings-link">⚙️</a>
		<nav aria-label={m.language()} class="flex rounded-full bg-white p-1 ring-1 ring-line">
			{#each locales as locale (locale)}
				<button
					type="button"
					class="rounded-full px-3 py-1 text-sm font-extrabold {locale === getLocale() ? 'bg-brand text-white' : 'text-muted'}"
					aria-pressed={locale === getLocale()}
					onclick={() => setLocale(locale)}
				>
					{labels[locale] ?? locale}
				</button>
			{/each}
		</nav>
		</div>
	</header>
	<main class="flex-1 pb-6">
		{@render children()}
	</main>
</div>
