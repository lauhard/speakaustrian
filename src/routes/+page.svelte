<script lang="ts">
	import { onMount } from 'svelte';
	import { resolve } from '$app/paths';
	import { m } from '#lib/paraglide/messages.js';
	import { getLocale } from '#lib/paraglide/runtime.js';
	import { chapterContent, course, PREVIEW_CHAPTER } from '#lib/content/index.ts';
	import { planDay } from '#lib/core/reducer.ts';
	import { dueQueue } from '#lib/core/review.ts';
	import type { PensumMin } from '#lib/core/state.ts';
	import { game, policy } from '#lib/game.svelte.ts';

	const helpLocale: 'de' | 'en' | 'tl' = getLocale();
	const levels = ['A1', 'A2'] as const;
	const pensumOptions: { value: PensumMin; label: string }[] = [
		{ value: 60, label: '1 h' },
		{ value: 90, label: '1,5 h' },
		{ value: 105, label: '1,75 h' },
		{ value: 120, label: '2 h' }
	];

	let name = $state('');
	let pensumMin = $state<PensumMin>(90);

	const profile = $derived(game.state.profile);
	const run = $derived(game.state.course.chapter);
	const dueCount = $derived(game.ready ? dueQueue(game.state, game.today).length : 0);
	const doneCount = (chapterId: string) => {
		const attempt = run?.id === chapterId ? run.attempt : null;
		const done = attempt?.kind === 'LESSONS' ? attempt.done : [];
		return chapterContent(chapterId)?.lessons.filter((l) => done.includes(l.id)).length ?? 0;
	};

	onMount(() => game.init());

	const start = (event: SubmitEvent) => {
		event.preventDefault();
		if (name.trim() === '') return;
		game.dispatch({ type: 'PROFILE_CREATED', name, pensumMin });
	};

	const reset = () => {
		game.reset();
		name = '';
	};
</script>

<section class="space-y-6 pt-6">
	<p class="text-stone-700">{m.home_intro()}</p>

	{#if !game.ready}
		<p aria-busy="true" class="text-stone-500">…</p>
	{:else if profile}
		<h1 class="text-2xl font-bold">{m.welcome_back({ name: profile.name })}</h1>
		<p class="text-stone-600" data-testid="plan-day">{m.day_x({ day: planDay(profile.startDate, game.today) })}</p>
		{#if dueCount > 0}
			<a
				href={resolve('/review')}
				data-testid="review-due"
				class="block rounded-xl bg-red-700 px-4 py-4 text-center text-lg font-semibold text-white no-underline"
			>
				{m.review_due({ count: dueCount })}
			</a>
		{/if}
		<a
			href={resolve('/practice')}
			data-testid="free-practice"
			class="block rounded-xl border-2 border-red-700 px-4 py-3 text-center text-lg font-semibold text-red-700 no-underline"
		>
			{m.free_practice()}
		</a>

		{#each levels as level (level)}
			<h2 class="pt-2 text-xl font-bold">{level}</h2>
			<ol class="space-y-2">
				{#each course.chapters.filter((c) => c.id.startsWith(level)) as chapter (chapter.id)}
					{@const content = chapterContent(chapter.id)}
					{@const access = policy.canAccessChapter(game.state, chapter.id)}
					<li>
						{#if content && access.allowed}
							<a
								href={resolve('/chapter/[id]', { id: chapter.id })}
								data-testid="chapter-{chapter.id}"
								class="block rounded-xl border border-stone-300 bg-white px-4 py-3 no-underline"
							>
								<span class="text-sm text-stone-500">{chapter.id} · {doneCount(chapter.id)}/{content.lessons.length} {m.lessons()}</span>
								<span class="block font-semibold" lang="de">{chapter.title.de}</span>
								{#if helpLocale !== 'de'}<span class="block text-sm text-stone-600">{chapter.title[helpLocale]}</span>{/if}
							</a>
						{:else}
							<div class="rounded-xl border border-stone-200 px-4 py-3 text-stone-500">
								<span class="text-sm">{chapter.id} · {content ? m.chapter_locked() : m.chapter_soon()}</span>
								<span class="block" lang="de">{chapter.title.de}</span>
							</div>
						{/if}
					</li>
				{/each}
			</ol>
		{/each}

		<h2 class="pt-2 text-xl font-bold">{m.preview()}</h2>
		<a
			href={resolve('/chapter/[id]', { id: PREVIEW_CHAPTER })}
			data-testid="chapter-preview"
			class="block rounded-xl border border-stone-300 bg-white px-4 py-3 no-underline"
		>
			<span class="block font-semibold" lang="de">{chapterContent(PREVIEW_CHAPTER)?.lessons[0].title.de}</span>
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
			<fieldset class="space-y-2">
				<legend class="font-semibold">{m.pensum_label()}</legend>
				<div class="grid grid-cols-4 gap-2">
					{#each pensumOptions as option (option.value)}
						<label
							class="rounded-xl border px-2 py-3 text-center {pensumMin === option.value
								? 'border-red-700 bg-red-50 font-semibold'
								: 'border-stone-300 bg-white'}"
						>
							<input type="radio" class="sr-only" name="pensum" value={option.value} bind:group={pensumMin} />
							{option.label}
						</label>
					{/each}
				</div>
			</fieldset>
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
