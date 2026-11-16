<script lang="ts">
	import { onMount } from 'svelte';
	import { resolve } from '$app/paths';
	import { page } from '$app/state';
	import { getLocale } from '#lib/paraglide/runtime.js';
	import { m } from '#lib/paraglide/messages.js';
	import { chapterContent, course } from '#lib/content/index.ts';
	import { dueQueue } from '#lib/core/review.ts';
	import { game } from '#lib/game.svelte.ts';

	const helpLocale: 'de' | 'en' | 'tl' = getLocale();
	const id = $derived(page.params.id ?? '');
	const content = $derived(chapterContent(id));
	const meta = $derived(course.chapters.find((c) => c.id === id));

	const done = $derived.by(() => {
		const run = game.state.course.chapter;
		return run?.id === id && run.attempt.kind === 'LESSONS' ? run.attempt.done : [];
	});
	// R-W8: the due queue comes before new material.
	const dueCount = $derived(game.ready ? dueQueue(game.state, game.today).length : 0);
	onMount(() => game.init());
</script>

<a href={resolve('/')} class="text-sm text-stone-600 underline">← {m.course()}</a>

{#if content}
	<section class="space-y-4 pt-4">
		<h1 class="text-2xl font-bold" lang="de">{meta ? `${meta.id} · ${meta.title.de}` : m.preview()}</h1>
		{#if meta && helpLocale !== 'de'}<p class="text-stone-600">{meta.title[helpLocale]}</p>{/if}

		{#if dueCount > 0 && meta}
			<a href={resolve('/review')} class="block rounded-xl bg-red-700 px-4 py-3 text-center font-semibold text-white no-underline">
				{m.review_first()} {m.review_due({ count: dueCount })}
			</a>
		{/if}

		<h2 class="text-lg font-semibold">{m.lessons()}</h2>
		<ol class="space-y-2">
			{#each content.lessons as lesson, i (lesson.id)}
				{@const isDone = done.includes(lesson.id)}
				<li>
					<a
						href={resolve('/chapter/[id]/[lesson]', { id, lesson: lesson.id })}
						data-testid="lesson-{lesson.id}"
						class="flex items-center justify-between gap-3 rounded-xl border bg-white px-4 py-3 no-underline {isDone
							? 'border-green-600'
							: 'border-stone-300'}"
					>
						<span>
							<span class="block font-semibold" lang="de">{i + 1}. {lesson.title.de}</span>
							{#if helpLocale !== 'de'}<span class="block text-sm text-stone-600">{lesson.title[helpLocale]}</span>{/if}
						</span>
						{#if isDone}<span class="text-sm font-medium text-green-700">✓ {m.lesson_done()}</span>{/if}
					</a>
				</li>
			{/each}
		</ol>
		{#if meta}<p class="text-sm text-stone-500">{m.chapter_more_soon()}</p>{/if}
	</section>
{:else}
	<p class="pt-6">{m.not_found()}</p>
{/if}
