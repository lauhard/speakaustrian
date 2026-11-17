<script lang="ts">
	import { untrack } from 'svelte';
	import { toast } from '#lib/toast.svelte.ts';
	import { Check, ChevronLeft, ChevronRight, LockOpen, Star } from '@lucide/svelte';
	import { lessonScores } from '#lib/lesson-scores.svelte.ts';
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
	// Free mode is announced once per opened chapter, as a toast instead of a box.
	$effect(() => {
		if (free && store.ready) untrack(() => toast(m.free_mode(), { icon: 'unlock', testid: 'free-mode' }));
	});
</script>

{#if content}
	<section class="space-y-4 pt-1">
		{#if meta}
			<header class="hero space-y-4">
				<div class="space-y-1">
					<p class="flex items-center gap-2 text-xs font-extrabold tracking-wider text-white/75 uppercase">
						{meta.id}
						{#if free}<span class="inline-flex items-center gap-1 rounded-full bg-white/20 px-2 py-0.5 normal-case"><LockOpen size={12} strokeWidth={2.75} />{m.free_label()}</span>{/if}
					</p>
					<h1 class="display text-2xl leading-tight" lang="de">{meta.title.de}</h1>
					{#if showTr}<p class="text-sm font-semibold text-white/80">{meta.title[helpLocale]}</p>{/if}
				</div>
				<ol class="flex gap-1.5" aria-label={m.lessons()} data-testid="stepper">
					{#each steps as st, i (st.label)}
						<li class="flex-1">
							<span class="block h-1.5 rounded-full {i <= stepIndex ? 'bg-white' : 'bg-white/25'} {i === stepIndex ? 'animate-pulse' : ''}"></span>
							<span class="mt-1.5 flex items-center gap-1 text-xs font-bold {i <= stepIndex ? 'text-white' : 'text-white/60'}">{#if i < stepIndex}<Check size={12} strokeWidth={3} />{/if}{st.label}</span>
						</li>
					{/each}
				</ol>
			</header>
		{:else}
			<h1 class="h1" lang="de">{m.preview()}</h1>
		{/if}

		{#if dueCount > 0}
			<a href={meta ? resolve('/review') : `${resolve('/review')}?store=demo`} class="btn-primary">
				{m.review_first()} {m.review_due({ count: dueCount })}
			</a>
		{/if}

		{#if inFlow || passed}
			<ChapterFlow {store} chapterId={id} />
		{/if}

		<details open={!inFlow && !passed} class="group space-y-2">
		<summary class="h2 flex cursor-pointer list-none items-center justify-between">{m.lessons()} <span class="text-sm text-muted">{done.length}/{content.lessons.length} <ChevronRight size={16} class="inline transition group-open:rotate-90" /></span></summary>
		<ol class="mt-2 space-y-2">
			{#each content.lessons as lesson, i (lesson.id)}
				{@const isDone = done.includes(lesson.id)}
				{@const pct = lessonScores.of(lesson.id)}
				<li>
					<a
						href={resolve('/chapter/[id]/[lesson]', { id, lesson: lesson.id })}
						data-testid="lesson-{lesson.id}"
						data-done={isDone}
						class="card-link flex items-center gap-3"
					>
						<span class="node {isDone ? 'is-passed' : ''}">{#if isDone}<Check size={18} strokeWidth={3} />{:else}{i + 1}{/if}</span>
						<span class="flex-1">
							<span class="block text-lg font-extrabold" lang="de">{lesson.title.de}</span>
							{#if showTr}<span class="block text-sm text-muted">{lesson.title[helpLocale]}</span>{/if}
						</span>
						{#if pct !== undefined}
							<span class="flex shrink-0 flex-col items-end gap-0.5" data-testid="lesson-score">
								<span class="flex gap-px" aria-hidden="true">{#each [50, 70, 90] as min (min)}<Star size={13} strokeWidth={2.25} class={pct >= min ? 'fill-amber-400 text-amber-500' : 'text-line'} />{/each}</span>
								<span class="rounded-full px-2 py-0.5 text-xs font-extrabold {pct === 100 ? 'bg-amber-100 text-amber-700' : pct >= 70 ? 'bg-ok-soft text-ok' : 'bg-warn-soft text-warn'}">{pct}%</span>
							</span>
						{:else}<ChevronRight size={18} class="text-muted" />{/if}
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
