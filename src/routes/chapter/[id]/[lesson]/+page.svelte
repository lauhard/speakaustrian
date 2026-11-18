<script lang="ts">
	import { lessonScores } from '#lib/lesson-scores.svelte.ts';
	import { Headphones, Landmark, Lightbulb, Target, Volume2 } from '@lucide/svelte';
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
	import { flameChapter, game, storeFor, xpContext } from '#lib/game.svelte.ts';
	import { xp } from '#lib/xp.svelte.ts';
	import { XP_ANSWER } from '#lib/core/xp.ts';

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

	// K9: an already passed lesson pays half (no farming); the first pass pays +20 (+10 with 3 stars).
	const ctx = $derived.by(() => {
		const base = xpContext(id);
		return base && lesson ? { ...base, reduced: base.reduced || xp.hasLesson(lesson.id) } : base;
	});
	const finish = (correct: number, total: number) => {
		const percent = Math.round((correct / Math.max(1, total)) * 100);
		if (lesson) lessonScores.record(lesson.id, percent);
		if (lesson && store.policy.isLessonPassed({ correct, total })) xp.lessonPassed(lesson.id, percent, ctx);
		// The reducer books the lesson only when it is passed (K1).
		if (lesson) store.dispatch({ type: 'LESSON_COMPLETED', chapterId: id, lessonId: lesson.id, introduced: introducedBy(lesson), correct, total });
	};
</script>

{#if !lesson}
	<p class="pt-6">{m.not_found()}</p>
{:else if learning && cards.length > 0}
	<section class="space-y-4">
		<h1 class="h1" lang="de">{lesson.title.de}</h1>
		{#if lesson.intro}
			<!-- Content standard v2 §1: the situation and the can-do goal before the cards. -->
			<div class="card space-y-3 border-l-4 !border-l-brand" data-testid="lesson-intro">
				<div>
					<p class="text-sm font-bold text-muted">{m.learn_situation()}</p>
					<p class="font-semibold" lang="de">{lesson.intro.situation.de}</p>
					{#if helpLocale !== 'de'}<p class="text-sm text-muted">{lesson.intro.situation[helpLocale]}</p>{/if}
				</div>
				<div class="flex items-start gap-2.5">
					<span class="icon-tile !h-8 !w-8" aria-hidden="true"><Target size={17} strokeWidth={2.5} /></span>
					<div>
						<p class="text-sm font-bold text-muted">{m.learn_goal()}</p>
						<p class="font-bold" lang="de">{lesson.intro.goal.de}</p>
						{#if helpLocale !== 'de'}<p class="text-sm text-muted">{lesson.intro.goal[helpLocale]}</p>{/if}
					</div>
				</div>
			</div>
		{/if}
		<p class="chip"><Headphones size={16} strokeWidth={2.5} />{m.learn_title()}</p>
		{#if ttsFailed}<p class="text-sm text-amber-700" role="status">{m.tts_failed()}</p>{/if}
		<ul class="space-y-3">
			{#each cards as card (card.phrase)}
				{#if card.kind === 'rule' || card.kind === 'culture'}
					<li class="card space-y-2 {card.kind === 'rule' ? '!bg-amber-50 !border-amber-200' : '!bg-sky-50 !border-sky-200'}" data-testid="card-{card.kind}">
						<p class="flex items-center gap-2 text-sm font-bold {card.kind === 'rule' ? 'text-amber-700' : 'text-sky-700'}">
							{#if card.kind === 'rule'}<Lightbulb size={16} strokeWidth={2.5} />{m.card_rule()}{:else}<Landmark size={16} strokeWidth={2.5} />{m.card_culture()}{/if}
						</p>
						<p class="text-lg font-extrabold" lang="de">{card.phrase}</p>
						<p class="font-semibold" lang="de">{card.note.de}</p>
						{#if helpLocale !== 'de'}<p class="text-sm text-muted">{card.note[helpLocale]}</p>{/if}
						{#if card.examples}
							<ul class="space-y-1.5 pt-1">
								{#each card.examples as ex (ex)}
									<li>
										<button type="button" class="flex w-full items-center gap-2 rounded-lg bg-white/70 px-2.5 py-1.5 text-left" onclick={() => listen(ex)}>
											<Volume2 size={16} strokeWidth={2.25} class="shrink-0 text-brand" /><span class="font-semibold" lang="de">{ex}</span>
										</button>
									</li>
								{/each}
							</ul>
						{/if}
					</li>
				{:else}
					<li class="card">
						<button type="button" class="flex w-full items-start gap-3 text-left" onclick={() => listen(card.audioText ?? card.phrase)}>
							<span aria-hidden="true" class="icon-tile"><Volume2 size={20} strokeWidth={2.25} /></span>
							<span class="text-xl font-extrabold" lang="de">{card.phrase}</span>
						</button>
						<p class="mt-3 font-semibold" lang="de">{card.note.de}</p>
						{#if helpLocale !== 'de'}<p class="text-sm text-muted">{card.note[helpLocale]}</p>{/if}
					</li>
				{/if}
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
			passCheck={(correct, total) => store.policy.isLessonPassed({ correct, total })}
			flameChapter={flameChapter(id)}
			xp={ctx ? { amount: XP_ANSWER.lesson, ctx } : null}
		/>
	{/key}
{/if}
