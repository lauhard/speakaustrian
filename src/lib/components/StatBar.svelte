<script lang="ts">
	import { m } from '#lib/paraglide/messages.js';
	import { deriveStats } from '#lib/core/stats.ts';
	import { game } from '#lib/game.svelte.ts';

	// `vertical` is the desktop sidebar variant with labels; the header uses compact pills.
	let { vertical = false }: { vertical?: boolean } = $props();
	const s = $derived(deriveStats(game.state));
</script>

{#if game.ready && game.state.profile}
	<ul class={vertical ? 'space-y-2' : 'flex items-center gap-1.5'} data-testid="stats">
		<li class="stat" title={m.stat_streak()} data-testid="stat-streak">
			<span class="stat-icon {s.streak > 0 ? 'flame' : 'grayscale'}">🔥</span>
			{#key s.streak}<b class="pop">{s.streak}</b>{/key}
			{#if vertical}<span class="stat-label">{m.stat_streak()} · {m.stat_best()} {s.best}</span>{/if}
		</li>
		{#if vertical || s.freezes > 0}
			<li class="stat" title={m.stat_freezes()}>
				<span class="stat-icon">❄️</span><b>{s.freezes}</b>
				{#if vertical}<span class="stat-label">{m.stat_freezes()}</span>{/if}
			</li>
		{/if}
		{#if s.lives !== null}
			<li class="stat" data-testid="stat-lives">
				<span class="stat-icon">❤️</span>{#key s.lives}<b class="shake">{s.lives}</b>{/key}
			</li>
		{/if}
		{#if s.points !== null}
			<li class="stat"><span class="stat-icon">⭐</span><b>{s.points}</b></li>
		{/if}
	</ul>
{/if}
