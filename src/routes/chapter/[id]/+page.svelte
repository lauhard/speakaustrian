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

<a href={resolve('/')} class="backlink">‹ {m.course()}</a>

{#if content}
	<section class="space-y-4 pt-4">
		{#if meta}<span class="chip">{meta.id}</span>{/if}
		<h1 class="h1" lang="de">{meta ? meta.title.de : m.preview()}</h1>
		{#if meta && helpLocale !== 'de'}<p class="text-muted">{meta.title[helpLocale]}</p>{/if}

		{#if dueCount > 0 && meta}
			<a href={resolve('/review')} class="btn-primary">
				{m.review_first()} {m.review_due({ count: dueCount })}
			</a>
		{/if}

		{#if content.lessons.length > 0}
			<div class="bar"><span style="width: {(done.length / content.lessons.length) * 100}%"></span></div>
		{/if}
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
		{#if meta}<p class="text-sm text-muted">{m.chapter_more_soon()}</p>{/if}
	</section>
{:else}
	<p class="pt-6">{m.not_found()}</p>
{/if}
