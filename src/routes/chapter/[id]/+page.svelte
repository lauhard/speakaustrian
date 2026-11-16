<script lang="ts">
	import { onMount } from 'svelte';
	import { resolve } from '$app/paths';
	import { page } from '$app/state';
	import { getLocale } from '#lib/paraglide/runtime.js';
	import { m } from '#lib/paraglide/messages.js';
	import { chapterContent, course } from '#lib/content/index.ts';
	import { dueQueue } from '#lib/core/review.ts';
	import ChapterFlow from '#lib/components/ChapterFlow.svelte';
	import { game, storeFor } from '#lib/game.svelte.ts';

	const helpLocale: 'de' | 'en' | 'tl' = getLocale();
	const id = $derived(page.params.id ?? '');
	const content = $derived(chapterContent(id));
	const meta = $derived(course.chapters.find((c) => c.id === id));

	// The preview chapter runs in its own sandbox state, the course chapters in the course state.
	const store = $derived(storeFor(id));
	const run = $derived(store.state.course.chapter?.id === id ? store.state.course.chapter : null);
	const inFlow = $derived(run !== null && run.attempt.kind !== 'LESSONS');
	const passed = $derived(id in store.state.course.completed);

	const done = $derived.by(() => {
		const run = store.state.course.chapter;
		return run?.id === id && run.attempt.kind === 'LESSONS' ? run.attempt.done : [];
	});
	// R-W8: the due queue comes before new material.
	const dueCount = $derived(store.ready ? dueQueue(store.state, store.today).length : 0);
	onMount(() => {
		game.init();
		store.init();
	});
</script>

<a href={resolve('/')} class="backlink">‹ {m.course()}</a>

{#if content}
	<section class="space-y-4 pt-4">
		{#if meta}<span class="chip">{meta.id}</span>{/if}
		<h1 class="h1" lang="de">{meta ? meta.title.de : m.preview()}</h1>
		{#if meta && helpLocale !== 'de'}<p class="text-muted">{meta.title[helpLocale]}</p>{/if}

		{#if dueCount > 0}
			<a href={meta ? resolve('/review') : `${resolve('/review')}?store=demo`} class="btn-primary">
				{m.review_first()} {m.review_due({ count: dueCount })}
			</a>
		{/if}

		{#if inFlow || passed}
			<ChapterFlow {store} chapterId={id} />
		{/if}

		{#if !inFlow && content.lessons.length > 0}
			<div class="bar"><span style="width: {(done.length / content.lessons.length) * 100}%"></span></div>
		{/if}
		{#if !inFlow}
		<h2 class="h2">{m.lessons()}</h2>
		<ol class="space-y-2">
			{#each content.lessons as lesson, i (lesson.id)}
				{@const isDone = done.includes(lesson.id)}
				<li>
					<a
						href={resolve('/chapter/[id]/[lesson]', { id, lesson: lesson.id })}
						data-testid="lesson-{lesson.id}"
						class="card-link flex items-center gap-3"
					>
						<span class="badge {isDone ? '!bg-ok-soft !text-ok' : ''}">{isDone ? '✓' : i + 1}</span>
						<span class="flex-1">
							<span class="block text-lg font-extrabold" lang="de">{lesson.title.de}</span>
							{#if helpLocale !== 'de'}<span class="block text-sm text-muted">{lesson.title[helpLocale]}</span>{/if}
						</span>
						<span class="text-sm font-bold {isDone ? 'text-ok' : 'text-muted'}">{isDone ? `✓ ${m.lesson_done()}` : '›'}</span>
					</a>
				</li>
			{/each}
		</ol>
		{/if}
		{#if meta}<p class="text-sm text-muted">{m.chapter_more_soon()}</p>{/if}
	</section>
{:else if meta}
	<section class="space-y-4 pt-4">
		<span class="chip">{meta.id}</span>
		<h1 class="h1" lang="de">{meta.title.de}</h1>
		<p class="card text-muted" data-testid="chapter-soon">{m.flow_next_soon()}</p>
	</section>
{:else}
	<p class="pt-6">{m.not_found()}</p>
{/if}
