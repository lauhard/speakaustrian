<script lang="ts">
	import { fly } from 'svelte/transition';
	import { cubicOut } from 'svelte/easing';
	import { flip } from 'svelte/animate';
	import { Info, LockOpen } from '@lucide/svelte';
	import { dismiss, toasts } from '#lib/toast.svelte.ts';
</script>

<div class="pointer-events-none fixed inset-x-0 top-16 z-[55] flex flex-col items-center gap-2 px-4" aria-live="polite">
	{#each toasts.list as t (t.id)}
		<button
			type="button"
			class="toast pointer-events-auto"
			data-tone={t.tone}
			data-testid={t.testid}
			onclick={() => dismiss(t.id)}
			in:fly={{ y: -16, duration: 260, easing: cubicOut }}
			out:fly={{ y: -10, duration: 180 }}
			animate:flip={{ duration: 200 }}
		>
			<span class="icon-tile !h-8 !w-8">{#if t.icon === 'unlock'}<LockOpen size={16} strokeWidth={2.5} />{:else}<Info size={16} strokeWidth={2.5} />{/if}</span>
			<span class="text-left text-sm font-bold">{t.text}</span>
		</button>
	{/each}
</div>
