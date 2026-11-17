<script lang="ts">
	import { fade, fly } from 'svelte/transition';
	import { cubicOut } from 'svelte/easing';
	import { ChevronRight, Dumbbell, House, RotateCcw, X } from '@lucide/svelte';
	import { afterNavigate } from '$app/navigation';
	import { resolve } from '$app/paths';
	import { page } from '$app/state';
	import { m } from '#lib/paraglide/messages.js';
	import SettingsPanel from './SettingsPanel.svelte';

	let open = $state(false);
	afterNavigate(() => (open = false));

	const links = [
		{ href: resolve('/'), icon: House, label: m.nav_course },
		{ href: resolve('/review'), icon: RotateCcw, label: m.nav_review },
		{ href: resolve('/practice'), icon: Dumbbell, label: m.free_practice }
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
	<button type="button" class="fixed inset-0 z-40 hidden bg-ink/30 backdrop-blur-[2px] sm:block" aria-label={m.menu_close()} transition:fade={{ duration: 200 }} onclick={() => (open = false)}></button>
	<!-- Full screen on phones, side sheet from sm on. -->
	<div
		id="app-menu"
		role="dialog"
		aria-modal="true"
		aria-label={m.settings()}
		class="fixed inset-0 z-50 overflow-y-auto bg-paper sm:left-auto sm:w-[26rem] sm:shadow-2xl"
		transition:fly={{ x: 480, duration: 300, easing: cubicOut, opacity: 1 }}
	>
		<div class="sticky top-0 z-10 flex items-center justify-between bg-paper/95 px-4 py-3">
			<span class="flex items-center gap-2">
				<img src="/icons/logo.svg" alt="" class="h-9 w-9" width="36" height="36" />
				<span class="display text-xl">{m.app_title()}</span>
			</span>
			<button type="button" class="burger" aria-label={m.menu_close()} onclick={() => (open = false)}><X size={20} strokeWidth={2.5} /></button>
		</div>
		<div class="space-y-6 px-4 pt-2 pb-10">
			<nav class="list rise">
				{#each links as l (l.href)}
					<a href={l.href} class="list-row" aria-current={page.url.pathname === l.href ? 'page' : undefined}>
						<span class="icon-tile"><l.icon size={20} strokeWidth={2.25} /></span>
						<span class="flex-1 font-extrabold">{l.label()}</span>
						<ChevronRight size={18} class="text-muted" />
					</a>
				{/each}
			</nav>
			<div class="rise" style:animation-delay="80ms"><SettingsPanel /></div>
		</div>
	</div>
{/if}
