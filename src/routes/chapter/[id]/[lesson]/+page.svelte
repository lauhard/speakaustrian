<script lang="ts">
	import { ChevronLeft, Headphones, Volume2 } from '@lucide/svelte';
	import { ttsRate } from '#lib/settings.svelte.ts';
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { resolve } from '$app/paths';
	import { page } from '$app/state';
	import { getLocale } from '#lib/paraglide/runtime.js';
	import { m } from '#lib/paraglide/messages.js';
	import { createDeviceTts } from '#lib/adapters/web/device-tts.ts';
	import Runner from '#lib/components/Runner.svelte';
	import { chapterContent, findLesson, introducedBy } from '#lib/content/index.ts';
	import type { SpeechOutPort } from '#lib/ports/speech-out.ts';
	import { game, storeFor } from '#lib/game.svelte.ts';

	const helpLocale: 'de' | 'en' | 'tl' = getLocale();
	const id = $derived(page.params.id ?? '');
	const store = $derived(storeFor(id));
	const lesson = $derived(findLesson(id, page.params.lesson ?? ''));
	const tlMachine = $derived(chapterContent(id)?.tlReviewStatus === 'machine');
	const cards = $derived(lesson?.cards ?? []);

	// Input first (hear and read the phrases), then retrieval practice.
	let learning = $state(true);
	let tts = $state<SpeechOutPort | null>(null);
	let ttsFailed = $state(false);

	onMount(() => {
		game.init();
		store.init();
		if (!game.state.profile) {
			goto(resolve('/'));
			return;
		}
		tts = createDeviceTts(window, ttsRate);
		return () => tts?.stop();
	});

	const listen = async (text: string) => {
		if (!tts) return;
		ttsFailed = !(await tts.speak(text)).ok;
	};

	const finish = () => {
		if (lesson) store.dispatch({ type: 'LESSON_COMPLETED', chapterId: id, lessonId: lesson.id, introduced: introducedBy(lesson) });
	};
</script>

{#if !lesson}
	<p class="pt-6">{m.not_found()}</p>
{:else if learning && cards.length > 0}
	<section class="space-y-4">
		<a href={resolve('/chapter/[id]', { id })} class="backlink"><ChevronLeft size={18} strokeWidth={2.5} />{m.back_chapter()}</a>
		<h1 class="h1" lang="de">{lesson.title.de}</h1>
		<p class="chip"><Headphones size={16} strokeWidth={2.5} />{m.learn_title()}</p>
		{#if ttsFailed}<p class="text-sm text-amber-700" role="status">{m.tts_failed()}</p>{/if}
		<ul class="space-y-3">
			{#each cards as card (card.phrase)}
				<li class="card">
					<button type="button" class="flex w-full items-start gap-3 text-left" onclick={() => listen(card.audioText ?? card.phrase)}>
						<span aria-hidden="true" class="icon-tile"><Volume2 size={20} strokeWidth={2.25} /></span>
						<span class="text-xl font-extrabold" lang="de">{card.phrase}</span>
					</button>
					<p class="mt-3 font-semibold" lang="de">{card.note.de}</p>
					{#if helpLocale !== 'de'}<p class="text-sm text-muted">{card.note[helpLocale]}</p>{/if}
				</li>
			{/each}
		</ul>
		<div class="actionbar">
		<button
			type="button"
			data-testid="to-tasks"
			class="btn-primary"
			onclick={() => {
				tts?.stop();
				learning = false;
			}}
		>
			{m.to_tasks()} →
		</button>
		</div>
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
