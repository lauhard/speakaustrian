<script lang="ts">
	import { resolve } from '$app/paths';
	import { getLocale, locales, setLocale } from '#lib/paraglide/runtime.js';
	import { m } from '#lib/paraglide/messages.js';
	import './layout.css';
	import favicon from '#lib/assets/favicon.svg';
	import type { LayoutProps } from './$types';

	let { children }: LayoutProps = $props();
	const labels: Record<string, string> = { de: 'DE', en: 'EN', tl: 'TL' };
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
	<title>{m.app_title()}</title>
	<meta name="theme-color" content="#c8102e" />
</svelte:head>

<div class="mx-auto flex min-h-dvh max-w-md flex-col px-4">
	<header class="flex items-center justify-between gap-3 py-4">
		<a href={resolve('/')} class="flex items-center gap-2 no-underline">
			<!-- Small Austrian flag as logo mark -->
			<span class="flex h-8 w-8 flex-col overflow-hidden rounded-lg shadow-sm" aria-hidden="true">
				<span class="flex-1 bg-brand"></span><span class="flex-1 bg-white"></span><span class="flex-1 bg-brand"></span>
			</span>
			<span class="text-xl font-black tracking-tight text-ink">{m.app_title()}</span>
		</a>
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
	</header>
	<main class="flex-1 pb-6">
		{@render children()}
	</main>
</div>
