<script lang="ts">
	import { m } from '#lib/paraglide/messages.js';
	import { xp } from '#lib/xp.svelte.ts';

	// K9: level number in a ring that fills with the XP towards the next level; pops on a level-up.
	let { large = false }: { large?: boolean } = $props();
	const lv = $derived(xp.level);
	const R = 15;
	const C = 2 * Math.PI * R;
	const label = $derived(m.level_title({ level: lv.level, into: lv.into, need: lv.need }));
</script>

<span class="relative grid shrink-0 place-items-center {large ? 'h-14 w-14' : 'h-10 w-10'}" title={label} aria-label={label} data-testid={large ? 'home-level-ring' : 'level-ring'} data-level={lv.level}>
	<svg viewBox="0 0 36 36" class="absolute inset-0 -rotate-90" aria-hidden="true">
		<circle cx="18" cy="18" r={R} fill="white" class="stroke-line" stroke-width="3.5" />
		<circle cx="18" cy="18" r={R} fill="none" class="stroke-amber-400 transition-[stroke-dashoffset] duration-700" stroke-width="3.5" stroke-linecap="round" stroke-dasharray={C} stroke-dashoffset={C * (1 - lv.into / lv.need)} />
	</svg>
	{#key xp.fx.levelUp ? xp.fx.seq : 0}
		<b class="relative font-black {large ? 'text-xl' : 'text-sm'} {xp.fx.levelUp ? 'pop text-amber-600' : ''}">{lv.level}</b>
	{/key}
</span>
