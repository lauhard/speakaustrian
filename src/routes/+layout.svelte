<script lang="ts">
	// Registers the install-prompt listener early: the browser fires it once, soon after load.
	import '#lib/install.svelte.ts';
	import { onNavigate } from '$app/navigation';
	import { resolve } from '$app/paths';
	import { m } from '#lib/paraglide/messages.js';
	import { ChevronLeft } from '@lucide/svelte';
	import { onMount } from 'svelte';
	import { page } from '$app/state';
	import { game, startActivityClock } from '#lib/game.svelte.ts';
	import Menu from '#lib/components/Menu.svelte';
	import UpdateBanner from '#lib/components/UpdateBanner.svelte';
	import Toaster from '#lib/components/Toaster.svelte';
	import Sidebar from '#lib/components/Sidebar.svelte';
	import Splash from '#lib/components/Splash.svelte';
	import StatBar from '#lib/components/StatBar.svelte';
	import LevelRing from '#lib/components/LevelRing.svelte';
	import { xp } from '#lib/xp.svelte.ts';
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

	onMount(() => {
		game.init();
		startActivityClock();
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
	// K9: the day goal pays +25 XP once per day.
	$effect(() => {
		if (game.ready && game.state.days[game.today]?.goalMet) xp.dayGoal(game.today);
	});
</script>

<svelte:head>
	<title>{m.app_title()}</title>
</svelte:head>

<Splash />
<Toaster />
<UpdateBanner />

<!-- Mobile first: one column. From lg on, a sticky sidebar joins on the left; pages stay unchanged. -->
<div class="mx-auto min-h-dvh max-w-md px-4 lg:grid lg:max-w-6xl lg:grid-cols-[17rem_minmax(0,40rem)] lg:justify-center lg:gap-14">
	<aside class="hidden lg:block">
		<Sidebar />
	</aside>
	<div class="flex min-h-dvh flex-col">
		<header class="app-header sticky top-0 z-30 -mx-4 bg-paper/95 px-4 py-3">
			<div class="app-header-row">
			{#if back}
				<a href={back.href} class="backpill" data-testid="header-back">
					<ChevronLeft size={18} strokeWidth={2.5} /><span class="back-label">{back.label()}</span>
				</a>
			{:else}
				<a href={resolve('/')} class="flex items-center gap-2 no-underline lg:invisible">
					<img src="/icons/logo.svg" alt="" class="h-9 w-9" width="36" height="36" />
					<span class="display text-xl text-ink">{m.app_title()}</span>
				</a>
			{/if}
			<div class="flex min-w-0 items-center justify-end gap-2">
				{#if page.url.pathname !== '/'}<span class="min-w-0 lg:hidden"><StatBar /></span>{/if}
				{#if game.ready && game.state.profile && page.url.pathname !== '/'}<LevelRing />{/if}
				<Menu />
			</div>
		</div>
		</header>
		<main class="page flex-1 pt-3 pb-8">
			{@render children()}
		</main>
	</div>
</div>
