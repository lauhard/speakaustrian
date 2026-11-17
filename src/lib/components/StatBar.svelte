<script lang="ts">
	import { Flame, Heart, Snowflake, Star, Zap } from '@lucide/svelte';
	import { m } from '#lib/paraglide/messages.js';
	import { deriveStats } from '#lib/core/stats.ts';
	import { accuracy } from '#lib/accuracy.svelte.ts';
	import { game } from '#lib/game.svelte.ts';

	// `vertical` is the desktop sidebar variant with labels; the header uses compact pills.
	let { vertical = false }: { vertical?: boolean } = $props();
	const s = $derived(deriveStats(game.state));
</script>

{#if game.ready && game.state.profile}
	<ul class={vertical ? 'space-y-2' : 'flex items-center gap-1.5'} data-testid="stats">
		<li class="stat" title={m.stat_streak()} data-testid="stat-streak">
			<Flame size={18} strokeWidth={2.25} class={s.streak > 0 ? 'flame fill-orange-400 text-orange-500' : 'text-stone-400'} />
			{#key s.streak}<b class="pop">{s.streak}</b>{/key}
			{#if vertical}<span class="stat-label">{m.stat_streak()} · {m.stat_best()} {s.best}</span>{/if}
		</li>
		<li class="stat" title={m.stat_flawless()} data-testid="stat-flawless">
			<Zap size={18} strokeWidth={2.25} class={accuracy.current > 0 ? 'fill-amber-400 text-amber-500' : 'text-stone-400'} />
			{#key accuracy.current}<b class="pop">{accuracy.current}</b>{/key}
			{#if vertical}<span class="stat-label">{m.stat_flawless()} · {m.stat_best()} {accuracy.best}</span>{/if}
		</li>
		{#if vertical || s.freezes > 0}
			<li class="stat" title={m.stat_freezes()}>
				<Snowflake size={18} strokeWidth={2.25} class="text-sky-500" /><b>{s.freezes}</b>
				{#if vertical}<span class="stat-label">{m.stat_freezes()}</span>{/if}
			</li>
		{/if}
		{#if s.lives !== null}
			<li class="stat" data-testid="stat-lives">
				<Heart size={18} strokeWidth={2.25} class="fill-brand text-brand" />{#key s.lives}<b class="shake">{s.lives}</b>{/key}
			</li>
		{/if}
		{#if s.points !== null}
			<li class="stat"><Star size={18} strokeWidth={2.25} class="fill-amber-400 text-amber-500" /><b>{s.points}</b></li>
		{/if}
	</ul>
{/if}
