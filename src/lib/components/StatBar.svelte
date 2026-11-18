<script lang="ts">
	import { Flame, Heart, Shield, Snowflake, Star, Zap } from '@lucide/svelte';
	import { getLocale } from '#lib/paraglide/runtime.js';
	import { m } from '#lib/paraglide/messages.js';
	import { deriveStats } from '#lib/core/stats.ts';
	import { flames, TIER_CLASS } from '#lib/flames.svelte.ts';
	import { game } from '#lib/game.svelte.ts';

	// `vertical` is the desktop sidebar variant with labels; the header uses compact pills.
	let { vertical = false }: { vertical?: boolean } = $props();
	const s = $derived(deriveStats(game.state));
</script>

{#if game.ready && game.state.profile}
	<ul class={vertical ? 'space-y-2' : 'flex items-center gap-1.5'} data-testid="stats">
		<li class="stat" title={m.stat_streak()} data-testid="stat-streak">
			<Zap size={18} strokeWidth={2.25} class={s.streak > 0 ? 'fill-amber-400 text-amber-500' : 'text-stone-400'} />
			{#key s.streak}<b class="pop">{s.streak}</b>{/key}
			{#if vertical}<span class="stat-label">{m.stat_streak()} · {m.stat_best()} {s.best}</span>{/if}
		</li>
		<li class="stat" title={m.stat_flawless()} data-testid="stat-score" data-score-target>
			<!-- K8: chapter flames in their tier colour, the multiplier small next to them, shields as a badge. -->
			{#key flames.fx.seq}
				<span class="flex items-center gap-1 {flames.fx.kind === 'lostScore' ? 'shake text-bad' : flames.fx.kind === 'bank' ? 'pop' : ''}" data-tier={flames.tier}>
					<Flame size={18} strokeWidth={2.25} class="{TIER_CLASS[flames.tier]} {flames.chapterFlames > 0 ? 'flame' : ''}" /><b data-testid="stat-flames">{flames.chapterFlames}</b>
					{#if flames.multiplier > 1}<span class="text-[0.65rem] font-bold text-muted" data-testid="stat-multiplier">×{flames.multiplier.toLocaleString(getLocale())}</span>{/if}
				</span>
				{#if flames.shields > 0 || flames.fx.kind === 'shieldBroken'}
					<span class="flex items-center gap-0.5 text-sky-600 {flames.fx.kind === 'shieldBroken' ? 'shake text-bad' : flames.fx.kind === 'shieldEarned' ? 'pop' : ''}" title={m.stat_shields()} data-testid="stat-shields">
						<Shield size={15} strokeWidth={2.5} class="fill-sky-200" /><b class="text-xs">{flames.shields}</b>
					</span>
				{/if}
			{/key}
			{#if vertical}<span class="stat-label">{m.stat_flawless()} · {m.stat_best()} {flames.best}</span>{/if}
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
