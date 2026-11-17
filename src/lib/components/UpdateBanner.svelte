<script lang="ts">
	import { onMount } from 'svelte';
	import { fly } from 'svelte/transition';
	import { RefreshCw } from '@lucide/svelte';
	import { m } from '#lib/paraglide/messages.js';

	// The service worker activates new builds right away (skipWaiting + claim). An open page notices the
	// controller change and offers a reload; the first install (no controller yet) stays silent.
	let available = $state(false);

	onMount(() => {
		const sw = navigator.serviceWorker;
		if (!sw) return;
		const hadController = !!sw.controller;
		const onChange = () => hadController && (available = true);
		sw.addEventListener('controllerchange', onChange);
		// Check for a new build whenever the app comes back to the foreground.
		const check = () => document.visibilityState === 'visible' && sw.getRegistration().then((r) => r?.update()).catch(() => {});
		document.addEventListener('visibilitychange', check);
		return () => {
			sw.removeEventListener('controllerchange', onChange);
			document.removeEventListener('visibilitychange', check);
		};
	});
</script>

{#if available}
	<div class="fixed inset-x-0 bottom-4 z-[58] flex justify-center px-4" transition:fly={{ y: 24, duration: 250 }}>
		<div class="toast !max-w-md" role="status" data-testid="update-banner">
			<span class="icon-tile !h-9 !w-9"><RefreshCw size={18} strokeWidth={2.5} /></span>
			<span class="flex-1 text-sm font-bold">{m.update_available()}</span>
			<button type="button" class="rounded-xl bg-brand px-3 py-2 text-sm font-extrabold text-white" onclick={() => location.reload()}>{m.update_reload()}</button>
		</div>
	</div>
{/if}
