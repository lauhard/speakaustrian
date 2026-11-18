<script lang="ts">
	import { Dumbbell, Flame, House, RotateCcw, Snowflake, Zap } from '@lucide/svelte';
	import { resolve } from '$app/paths';
	import { page } from '$app/state';
	import { m } from '#lib/paraglide/messages.js';
	import { flames, TIER_CLASS } from '#lib/flames.svelte.ts';
	import { dueQueue } from '#lib/core/review.ts';
	import { game } from '#lib/game.svelte.ts';

	// Desktop only (lg+): brand, navigation and the three game numbers with a one-line explanation each.
	const links = [
		{ href: resolve('/'), icon: House, label: m.nav_course },
		{ href: resolve('/review'), icon: RotateCcw, label: m.nav_review },
		{ href: resolve('/practice'), icon: Dumbbell, label: m.free_practice }
	];
	const due = $derived(game.ready ? dueQueue(game.state, game.today).length : 0);
	const st = $derived(game.state.streak);
</script>

<div class="sticky top-0 flex max-h-dvh flex-col gap-7 overflow-y-auto py-8">
	<a href={resolve('/')} class="flex items-center gap-3 no-underline">
		<img src="/icons/logo.svg" alt="" class="h-12 w-12 drop-shadow-sm" width="48" height="48" />
		<span>
			<span class="display block text-2xl leading-none text-ink">{m.app_title()}</span>
			<span class="mt-1 block text-xs font-bold text-muted">{m.app_tagline()}</span>
		</span>
	</a>

	<nav class="space-y-1">
		{#each links as l (l.href)}
			{@const active = page.url.pathname === l.href}
			<a href={l.href} class="side-link" aria-current={active ? 'page' : undefined}>
				<l.icon size={20} strokeWidth={2.25} />
				<span class="flex-1">{l.label()}</span>
				{#if l.icon === RotateCcw && due > 0}<span class="rounded-full bg-brand px-2 py-0.5 text-xs font-extrabold text-white">{due}</span>{/if}
			</a>
		{/each}
	</nav>

	{#if game.ready && game.state.profile}
		<section class="space-y-2">
			<h2 class="list-label">{m.side_progress()}</h2>
			<div class="side-stat">
				<span class="icon-tile !bg-amber-100 !text-amber-500"><Zap size={20} strokeWidth={2.25} class={st.current > 0 ? 'fill-amber-400' : ''} /></span>
				<span class="min-w-0">
					<span class="tile-title">{st.current} <span class="text-sm font-semibold text-muted">{m.stat_streak()} · {m.stat_best()} {st.best}</span></span>
					<span class="side-note">{m.streak_explain()}</span>
				</span>
			</div>
			<div class="side-stat">
				<span class="icon-tile !bg-orange-100 !text-orange-500" data-score-target><Flame size={20} strokeWidth={2.25} class="{TIER_CLASS[flames.tier]} {flames.chapterFlames > 0 ? 'flame' : ''}" /></span>
				<span class="min-w-0">
					<span class="tile-title">{flames.chapterFlames} <span class="text-sm font-semibold text-muted">{m.stat_flawless()} · {m.stat_best()} {flames.best}</span></span>
					<span class="side-note">{m.score_explain()}</span>
				</span>
			</div>
			<div class="side-stat">
				<span class="icon-tile !bg-sky-100 !text-sky-600"><Snowflake size={20} strokeWidth={2.25} /></span>
				<span class="min-w-0">
					<span class="tile-title">{st.freezes}/2 <span class="text-sm font-semibold text-muted">{m.stat_freezes()}</span></span>
					<span class="side-note">{m.freeze_explain()}</span>
				</span>
			</div>
		</section>
	{/if}
</div>
