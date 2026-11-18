<script lang="ts">
	import { Flame } from '@lucide/svelte';
	import { m } from '#lib/paraglide/messages.js';
	import { flames } from '#lib/flames.svelte.ts';
	import { HITS_PER_FLAME } from '#lib/core/flames.ts';

	// Flames of the running round + progress dots to the next flame.
	const kind = $derived(flames.fx.kind);
</script>

<span class="flex items-center gap-1" title={m.stat_flames()} data-testid="flame-pot" data-pot={flames.pot}>
	{#key flames.fx.seq}
		<span class="flex items-center gap-0.5 {kind === 'flame' ? 'pop' : kind === 'lostPot' || kind === 'lostScore' ? 'shake' : ''} {flames.pot > 0 ? 'text-orange-500' : 'text-stone-400'}">
			<Flame size={16} strokeWidth={2.5} class={flames.pot > 0 ? 'fill-orange-400' : ''} />{flames.pot}
		</span>
	{/key}
	<span class="flex gap-0.5" aria-hidden="true">
		{#each { length: HITS_PER_FLAME - 1 } as _, i (i)}
			<span class="h-1.5 w-1.5 rounded-full transition-colors {i < flames.hits ? 'bg-orange-400' : 'bg-line'}"></span>
		{/each}
	</span>
</span>
