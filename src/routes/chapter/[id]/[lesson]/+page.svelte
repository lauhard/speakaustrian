<script lang="ts">
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { resolve } from '$app/paths';
	import { page } from '$app/state';
	import { getLocale } from '#lib/paraglide/runtime.js';
	import { m } from '#lib/paraglide/messages.js';
	import { createDeviceTts } from '#lib/adapters/web/device-tts.ts';
	import Runner from '#lib/components/Runner.svelte';
	import { chapterContent, findLesson } from '#lib/content/index.ts';
	import type { SpeechOutPort } from '#lib/ports/speech-out.ts';
	import { storage, withResult } from '#lib/profile.ts';

	const helpLocale: 'de' | 'en' | 'tl' = getLocale();
	const id = $derived(page.params.id ?? '');
	const lesson = $derived(findLesson(id, page.params.lesson ?? ''));
	const tlMachine = $derived(chapterContent(id)?.tlReviewStatus === 'machine');
	const cards = $derived(lesson?.cards ?? []);

	// Input first (hear and read the phrases), then retrieval practice.
	let learning = $state(true);
	let tts = $state<SpeechOutPort | null>(null);
	let ttsFailed = $state(false);

	onMount(() => {
		if (!storage()?.load()) {
			goto(resolve('/'));
			return;
		}
		tts = createDeviceTts(window);
		return () => tts?.stop();
	});

	const listen = async (text: string) => {
		if (!tts) return;
		ttsFailed = !(await tts.speak(text)).ok;
	};

	const finish = (correct: number, total: number) => {
		const store = storage();
		const profile = store?.load();
		if (store && profile && lesson) store.save(withResult(profile, lesson.id, correct, total, new Date()));
	};
</script>

{#if !lesson}
	<p class="pt-6">{m.not_found()}</p>
{:else if learning && cards.length > 0}
	<section class="space-y-4">
		<h1 class="text-2xl font-bold" lang="de">{lesson.title.de}</h1>
		<p class="text-stone-600">{m.learn_title()}</p>
		{#if ttsFailed}<p class="text-sm text-amber-700" role="status">{m.tts_failed()}</p>{/if}
		<ul class="space-y-3">
			{#each cards as card (card.phrase)}
				<li class="rounded-xl border border-stone-300 bg-white p-4">
					<button type="button" class="flex w-full items-start gap-3 text-left" onclick={() => listen(card.phrase)}>
						<span aria-hidden="true">🔊</span>
						<span class="text-lg font-semibold" lang="de">{card.phrase}</span>
					</button>
					<p class="mt-2" lang="de">{card.note.de}</p>
					{#if helpLocale !== 'de'}<p class="text-sm text-stone-600">{card.note[helpLocale]}</p>{/if}
				</li>
			{/each}
		</ul>
		<button
			type="button"
			data-testid="to-tasks"
			class="w-full rounded-xl bg-red-700 px-4 py-4 text-lg font-semibold text-white"
			onclick={() => {
				tts?.stop();
				learning = false;
			}}
		>
			{m.to_tasks()}
		</button>
	</section>
{:else}
	{#key lesson.id}
		<Runner
			items={lesson.items}
			{tlMachine}
			backHref={resolve('/chapter/[id]', { id })}
			backLabel={m.back_chapter()}
			onfinish={finish}
		/>
	{/key}
{/if}
