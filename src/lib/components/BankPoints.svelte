<script lang="ts">
	import { onMount } from 'svelte';
	import { Flame } from '@lucide/svelte';
	import { accuracy } from '#lib/accuracy.svelte.ts';

	// End of a round/chapter: the flames of the round fly up into the header score, then get banked.
	let chip: HTMLElement | undefined = $state();
	const pot = accuracy.pot;

	onMount(() => {
		if (pot === 0) return;
		const target = [...document.querySelectorAll<HTMLElement>('[data-score-target]')].find((el) => el.offsetParent !== null);
		const still = matchMedia('(prefers-reduced-motion: reduce)').matches;
		if (!chip || !target || still) return void accuracy.bank();
		const t = setTimeout(() => {
			if (!chip) return accuracy.bank();
			const a = chip.getBoundingClientRect();
			const b = target.getBoundingClientRect();
			const dx = b.left + b.width / 2 - (a.left + a.width / 2);
			const dy = b.top + b.height / 2 - (a.top + a.height / 2);
			const fly = chip.animate(
				[{ transform: 'none', opacity: 1 }, { transform: `translate(${dx * 0.5}px, ${dy * 0.5 - 40}px) scale(1.15)`, opacity: 1 }, { transform: `translate(${dx}px, ${dy}px) scale(0.4)`, opacity: 0.2 }],
				{ duration: 750, easing: 'cubic-bezier(0.5, 0, 0.3, 1)', fill: 'forwards' }
			);
			fly.onfinish = () => accuracy.bank();
		}, 650);
		return () => {
			clearTimeout(t);
			accuracy.bank();
		};
	});
</script>

{#if pot > 0}
	<p class="flex justify-center" data-testid="bank-points">
		<span bind:this={chip} class="pop inline-flex items-center gap-1.5 rounded-full bg-orange-100 px-4 py-2 text-lg font-black text-orange-600 shadow-sm">
			<Flame size={22} strokeWidth={2.5} class="fill-orange-400" />+{pot}
		</span>
	</p>
{/if}
