<script lang="ts">
	import { onMount } from 'svelte';
	import { fade } from 'svelte/transition';
	import { m } from '#lib/paraglide/messages.js';

	// Shown once per browser session (cold start of the PWA); a tap skips it.
	const KEY = 'speakaustrian.splash.v1';
	let show = $state(false);

	onMount(() => {
		try {
			if (sessionStorage.getItem(KEY)) return;
			sessionStorage.setItem(KEY, '1');
		} catch {
			return;
		}
		if (navigator.webdriver) return; // keeps e2e runs fast and deterministic
		show = true;
		const t = setTimeout(() => (show = false), 1400);
		return () => clearTimeout(t);
	});
</script>

{#if show}
	<button
		type="button"
		class="fixed inset-0 z-[60] grid place-items-center bg-brand text-white"
		aria-label={m.app_title()}
		onclick={() => (show = false)}
		out:fade={{ duration: 350 }}
		data-testid="splash"
	>
		<span class="flex flex-col items-center gap-5">
			<img src="/icons/logo.svg" alt="" width="112" height="112" class="splash-logo h-28 w-28 rounded-[28px] ring-4 ring-white/30" />
			<span class="splash-text text-center">
				<span class="display block text-4xl">{m.app_title()}</span>
				<span class="mt-1 block text-base font-semibold text-white/85">{m.app_tagline()}</span>
			</span>
		</span>
	</button>
{/if}
