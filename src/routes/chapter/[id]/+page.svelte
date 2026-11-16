<script lang="ts">
	import { onMount } from 'svelte';
	import { resolve } from '$app/paths';
	import { page } from '$app/state';
	import { getLocale } from '#lib/paraglide/runtime.js';
	import { m } from '#lib/paraglide/messages.js';
	import { chapterContent, course } from '#lib/content/index.ts';
	import { dueQueue } from '#lib/core/review.ts';
	import ChapterFlow from '#lib/components/ChapterFlow.svelte';
	import { game, isFreeMode, storeFor } from '#lib/game.svelte.ts';
	import { chapterStatus } from '#lib/core/status.ts';
	import { settings } from '#lib/settings.svelte.ts';

	const helpLocale: 'de' | 'en' | 'tl' = getLocale();
	const id = $derived(page.params.id ?? '');
	const content = $derived(chapterContent(id));
	const meta = $derived(course.chapters.find((c) => c.id === id));

	// The preview chapter runs in its own sandbox state, the course chapters in the course state.
	const store = $derived(storeFor(id));
	const run = $derived(store.state.course.chapter?.id === id ? store.state.course.chapter : null);
	const inFlow = $derived(run !== null && run.attempt.kind !== 'LESSONS');
	const passed = $derived(id in store.state.course.completed);
	const free = $derived(isFreeMode(id));
	const showTr = $derived(helpLocale !== 'de' && settings.value.showTranslations);
	const status = $derived(chapterStatus(store.state, id, content?.lessons.map((l) => l.id) ?? []));
	// The four stages of a chapter attempt (04a §4.2) as a stepper; the test stage includes correction and error review.
	const steps = $derived([
		{ key: ['new', 'lessons'], label: m.step_lessons() },
		{ key: ['practice'], label: m.step_practice() },
		{ key: ['gate'], label: m.step_gate() },
		{ key: ['test', 'review'], label: m.step_test() }
	]);
	const stepIndex = $derived(status.phase === 'passed' ? steps.length : steps.findIndex((st) => st.key.includes(status.phase)));

	// Lessons count as done once the attempt is past them (practice, test …) or the chapter is passed.
	const done = $derived.by(() => {
		const run = store.state.course.chapter;
		if (run?.id === id && run.attempt.kind === 'LESSONS') return run.attempt.done;
		return status.lessonsDone === status.lessonsTotal ? (content?.lessons.map((l) => l.id) ?? []) : [];
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
		{#if meta && showTr}<p class="text-muted">{meta.title[helpLocale]}</p>{/if}
		{#if free}<p class="card !bg-brand-soft text-sm" data-testid="free-mode">🔓 {m.free_mode()}</p>{/if}
		{#if meta}
			<ol class="flex gap-1" aria-label={m.lessons()} data-testid="stepper">
				{#each steps as st, i (st.label)}
					<li class="flex-1 text-center">
						<span class="block h-2 rounded-full {i < stepIndex ? 'bg-ok' : i === stepIndex ? 'bg-brand' : 'bg-line'}"></span>
						<span class="mt-1 block text-xs font-bold {i === stepIndex ? 'text-brand' : i < stepIndex ? 'text-ok' : 'text-muted'}">{i < stepIndex ? '✓ ' : ''}{st.label}</span>
					</li>
				{/each}
			</ol>
		{/if}

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
		<details open={!inFlow && !passed} class="group space-y-2">
		<summary class="h2 flex cursor-pointer list-none items-center justify-between">{m.lessons()} <span class="text-sm text-muted">{done.length}/{content.lessons.length} <span class="inline-block transition group-open:rotate-90">›</span></span></summary>
		<ol class="mt-2 space-y-2">
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
							{#if showTr}<span class="block text-sm text-muted">{lesson.title[helpLocale]}</span>{/if}
						</span>
						<span class="text-sm font-bold {isDone ? 'text-ok' : 'text-muted'}">{isDone ? `✓ ${m.lesson_done()}` : '›'}</span>
					</a>
				</li>
			{/each}
		</ol>
		</details>
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
