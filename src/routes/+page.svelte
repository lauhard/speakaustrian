<script lang="ts">
	import { onMount } from 'svelte';
	import { resolve } from '$app/paths';
	import { m } from '#lib/paraglide/messages.js';
	import { newProfile, storage } from '#lib/profile.ts';
	import type { Profile } from '#lib/ports/storage.ts';

	let profile = $state<Profile | null>(null);
	let ready = $state(false);
	let name = $state('');

	const last = $derived(profile?.results.at(-1));

	onMount(() => {
		profile = storage()?.load() ?? null;
		ready = true;
	});

	const start = (event: SubmitEvent) => {
		event.preventDefault();
		if (name.trim() === '') return;
		profile = newProfile(name, new Date());
		storage()?.save(profile);
	};

	const reset = () => {
		storage()?.clear();
		profile = null;
		name = '';
	};
</script>

<section class="space-y-6 pt-6">
	<p class="text-stone-700">{m.home_intro()}</p>

	{#if !ready}
		<p aria-busy="true" class="text-stone-500">…</p>
	{:else if profile}
		<h1 class="text-2xl font-bold">{m.welcome_back({ name: profile.name })}</h1>
		{#if last}
			<p class="text-stone-700" data-testid="last-result">
				{m.last_result({ correct: last.correct, total: last.total })}
			</p>
		{/if}
		<a
			href={resolve('/lesson')}
			data-testid="start-lesson"
			class="block rounded-xl bg-red-700 px-4 py-4 text-center text-lg font-semibold text-white no-underline"
		>
			{m.start_lesson()}
		</a>
		<button type="button" class="text-sm text-stone-600 underline" onclick={reset}>{m.change_name()}</button>
	{:else}
		<form class="space-y-4" onsubmit={start}>
			<label class="block space-y-2">
				<span class="text-lg font-semibold">{m.name_label()}</span>
				<input
					data-testid="name-input"
					class="w-full rounded-xl border-stone-300 text-lg"
					bind:value={name}
					placeholder={m.name_placeholder()}
					autocomplete="given-name"
					maxlength="40"
				/>
			</label>
			<button
				data-testid="start"
				class="w-full rounded-xl bg-red-700 px-4 py-4 text-lg font-semibold text-white disabled:opacity-40"
				disabled={name.trim() === ''}
			>
				{m.start()}
			</button>
		</form>
	{/if}

	<p class="text-sm text-stone-500">{m.local_note()}</p>
</section>
