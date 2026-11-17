<script lang="ts">
	// Registers the install-prompt listener early: the browser fires it once, soon after load.
	import '#lib/install.svelte.ts';
	import { onNavigate } from '$app/navigation';
	import { resolve } from '$app/paths';
	import { m } from '#lib/paraglide/messages.js';
	import { ChevronLeft } from '@lucide/svelte';
	import { page } from '$app/state';
	import Menu from '#lib/components/Menu.svelte';
	import Toaster from '#lib/components/Toaster.svelte';
	import Splash from '#lib/components/Splash.svelte';
	import StatBar from '#lib/components/StatBar.svelte';
	import './layout.css';
	import type { LayoutProps } from './$types';

	let { children }: LayoutProps = $props();

	// Header back target: lesson → its chapter, every other sub page → course.
	const back = $derived.by(() => {
		const parts = page.url.pathname.split('/').filter(Boolean);
		if (parts.length === 0) return null;
		if (parts[0] === 'chapter' && parts.length === 3) return { href: resolve('/chapter/[id]', { id: parts[1] }), label: m.nav_chapter };
		return { href: resolve('/'), label: m.course };
	});

	// Page fades via the View Transitions API (CSS in layout.css); browsers without it just navigate.
	onNavigate((navigation) => {
		if (!document.startViewTransition) return;
		return new Promise((done) => {
			document.startViewTransition(async () => {
				done();
				await navigation.complete;
			});
		});
	});
</script>

<svelte:head>
	<title>{m.app_title()}</title>
</svelte:head>

<Splash />
<Toaster />

<!-- Mobile first: one column. From lg on, a sticky sidebar joins on the left; pages stay unchanged. -->
<div class="mx-auto min-h-dvh max-w-md px-4 lg:grid lg:max-w-5xl lg:grid-cols-[15rem_minmax(0,36rem)] lg:justify-center lg:gap-12">
	<aside class="hidden lg:block">
		<div class="sticky top-0 space-y-8 py-8">
			<a href={resolve('/')} class="flex items-center gap-3 no-underline">
				<img src="/icons/logo.svg" alt="" class="h-12 w-12 drop-shadow-sm" width="48" height="48" />
				<span class="display text-2xl leading-none text-ink">{m.app_title()}</span>
			</a>
			<p class="text-sm font-semibold text-muted">{m.app_tagline()}</p>
			<StatBar vertical />
		</div>
	</aside>
	<div class="flex min-h-dvh flex-col">
		<header class="sticky top-0 z-30 -mx-4 flex items-center justify-between gap-3 bg-paper/95 px-4 py-3">
			{#if back}
				<a href={back.href} class="backpill" data-testid="header-back">
					<ChevronLeft size={18} strokeWidth={2.5} />{back.label()}
				</a>
			{:else}
				<a href={resolve('/')} class="flex items-center gap-2 no-underline lg:invisible">
					<img src="/icons/logo.svg" alt="" class="h-9 w-9" width="36" height="36" />
					<span class="display text-xl text-ink">{m.app_title()}</span>
				</a>
			{/if}
			<div class="flex items-center gap-2">
				<span class="lg:hidden"><StatBar /></span>
				<Menu />
			</div>
		</header>
		<main class="page flex-1 pb-8">
			{@render children()}
		</main>
	</div>
</div>
