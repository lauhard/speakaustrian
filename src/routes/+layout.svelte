<script lang="ts">
	import { resolve } from '$app/paths';
	import { getLocale, locales, setLocale } from '#lib/paraglide/runtime.js';
	import { m } from '#lib/paraglide/messages.js';
	import './layout.css';
	import favicon from '#lib/assets/favicon.svg';
	import type { LayoutProps } from './$types';

	let { children }: LayoutProps = $props();
	const labels: Record<string, string> = { de: 'Deutsch', en: 'English', tl: 'Tagalog' };
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
	<title>{m.app_title()}</title>
</svelte:head>

<div class="mx-auto flex min-h-dvh max-w-md flex-col px-4 pb-8">
	<header class="flex items-center justify-between gap-3 py-4">
		<a href={resolve('/')} class="text-lg font-bold text-red-700 no-underline">{m.app_title()}</a>
		<nav aria-label={m.language()} class="flex gap-1">
			{#each locales as locale (locale)}
				<button
					type="button"
					class="rounded-full px-3 py-1 text-sm {locale === getLocale()
						? 'bg-red-700 text-white'
						: 'bg-stone-200 text-stone-800'}"
					aria-pressed={locale === getLocale()}
					onclick={() => setLocale(locale)}
				>
					{labels[locale] ?? locale}
				</button>
			{/each}
		</nav>
	</header>
	<main class="flex-1">
		{@render children()}
	</main>
</div>
