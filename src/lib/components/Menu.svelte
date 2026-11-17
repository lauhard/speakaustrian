<script lang="ts">
	import { fade, fly } from 'svelte/transition';
	import { cubicOut } from 'svelte/easing';
	import { afterNavigate } from '$app/navigation';
	import { resolve } from '$app/paths';
	import { page } from '$app/state';
	import { m } from '#lib/paraglide/messages.js';
	import { chapterContent, PREVIEW_CHAPTER } from '#lib/content/index.ts';
	import SettingsPanel from './SettingsPanel.svelte';
	import StatBar from './StatBar.svelte';

	let open = $state(false);
	afterNavigate(() => (open = false));

	const links = [
		{ href: resolve('/'), icon: '🏠', label: m.nav_course },
		{ href: resolve('/review'), icon: '🔁', label: m.nav_review },
		{ href: resolve('/practice'), icon: '🎯', label: m.free_practice },
		{ href: resolve('/chapter/[id]', { id: PREVIEW_CHAPTER }), icon: '🧪', label: m.preview_label }
	];
	const onkey = (e: KeyboardEvent) => open && e.key === 'Escape' && (open = false);
</script>

<svelte:window onkeydown={onkey} />
<svelte:body style:overflow={open ? 'hidden' : null} />

<button
	type="button"
	class="burger"
	class:is-open={open}
	aria-expanded={open}
	aria-controls="app-menu"
	aria-label={open ? m.menu_close() : m.menu_open()}
	data-testid="settings-link"
	onclick={() => (open = !open)}
>
	<span></span><span></span><span></span>
</button>

{#if open}
	<button type="button" class="fixed inset-0 z-40 bg-ink/30 backdrop-blur-[2px]" aria-label={m.menu_close()} transition:fade={{ duration: 200 }} onclick={() => (open = false)}></button>
	<div
		id="app-menu"
		role="dialog"
		aria-modal="true"
		aria-label={m.settings()}
		class="fixed inset-y-0 right-0 z-50 flex w-[min(24rem,92vw)] flex-col overflow-y-auto bg-paper px-4 pt-4 pb-8 shadow-2xl"
		transition:fly={{ x: 320, duration: 280, easing: cubicOut }}
	>
		<div class="mb-4 flex items-center justify-between">
			<span class="display text-lg">{m.app_title()}</span>
			<button type="button" class="burger is-open" aria-label={m.menu_close()} onclick={() => (open = false)}><span></span><span></span><span></span></button>
		</div>
		<div class="mb-4 lg:hidden"><StatBar /></div>
		<nav class="mb-6 grid grid-cols-2 gap-2">
			{#each links as l, i (l.href)}
				{#if l.icon !== '🧪' || chapterContent(PREVIEW_CHAPTER)}
					<a href={l.href} class="navtile rise" style:animation-delay="{60 + i * 40}ms" aria-current={page.url.pathname === l.href ? 'page' : undefined}>
						<span class="text-xl">{l.icon}</span>{l.label()}
					</a>
				{/if}
			{/each}
		</nav>
		<h2 class="h2 mb-3">{m.settings()}</h2>
		<SettingsPanel />
	</div>
{/if}
