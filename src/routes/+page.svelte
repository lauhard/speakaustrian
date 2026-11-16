<script lang="ts">
	import { onMount } from 'svelte';
	import { resolve } from '$app/paths';
	import { m } from '#lib/paraglide/messages.js';
	import { getLocale } from '#lib/paraglide/runtime.js';
	import { chapterContent, course, PREVIEW_CHAPTER } from '#lib/content/index.ts';
	import { planDay } from '#lib/core/reducer.ts';
	import { dueQueue } from '#lib/core/review.ts';
	import type { PensumMin } from '#lib/core/state.ts';
	import { game, isFreeMode, policy, storeFor } from '#lib/game.svelte.ts';
	import { chapterStatus, type ChapterStatus } from '#lib/core/status.ts';
	import { settings } from '#lib/settings.svelte.ts';

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
	const pensumLabel = $derived(pensumOptions.find((o) => o.value === profile?.pensumMin)?.label ?? '');
	const showTr = $derived(helpLocale !== 'de' && settings.value.showTranslations);
	const statusOf = (chapterId: string): ChapterStatus =>
		chapterStatus(storeFor(chapterId).state, chapterId, chapterContent(chapterId)?.lessons.map((l) => l.id) ?? []);
	const phaseLabel = (st: ChapterStatus) =>
		({
			new: m.phase_new(),
			lessons: m.phase_lessons({ done: st.lessonsDone, total: st.lessonsTotal }),
			practice: m.phase_practice(),
			gate: m.phase_gate(),
			test: m.phase_test(),
			review: m.phase_review(),
			passed: m.phase_passed()
		})[st.phase];
	// Smart continue: the next open lesson, or the chapter page once the lessons are done (practice, test …).
	const current = $derived.by(() => {
		const content = run ? chapterContent(run.id) : undefined;
		const meta = course.chapters.find((c) => c.id === run?.id);
		if (!run || !content || !meta) return null;
		const done = run.attempt.kind === 'LESSONS' ? run.attempt.done : [];
		const next = run.attempt.kind === 'LESSONS' ? content.lessons.find((l) => !done.includes(l.id)) : undefined;
		return { meta, status: statusOf(run.id), next };
	});

	onMount(() => game.init());
	// Free-mode chapters keep their own state; load it so the list shows their progress.
	$effect(() => {
		if (!game.ready) return;
		for (const c of course.chapters) if (chapterContent(c.id) && isFreeMode(c.id)) storeFor(c.id).init();
	});

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

{#if !game.ready}
	<p aria-busy="true" class="pt-10 text-center text-muted">…</p>
{:else if profile}
	<section class="space-y-5">
		<div>
			<h1 class="h1">{m.welcome_back({ name: profile.name })}</h1>
			<p class="mt-2 flex flex-wrap gap-2">
				<span class="chip" data-testid="plan-day">📅 {m.day_x({ day: planDay(profile.startDate, game.today) })}</span>
				<span class="chip !bg-white !text-muted ring-1 ring-line">⏱ {m.per_day({ time: pensumLabel })}</span>
			</p>
		</div>

		{#if dueCount > 0}
			<a href={resolve('/review')} data-testid="review-due" class="btn-primary">🔁 {m.review_due({ count: dueCount })}</a>
		{/if}

		{#if current}
			<div class="card space-y-3 !border-brand/30">
				<p class="text-sm font-bold text-muted">{m.your_chapter()} · {current.meta.id}</p>
				<p class="text-xl leading-tight font-black" lang="de">{current.meta.title.de}</p>
				{#if showTr}<p class="text-sm text-muted">{current.meta.title[helpLocale]}</p>{/if}
				<p><span class="chip" data-testid="current-phase">{phaseLabel(current.status)}</span></p>
				<div class="flex items-center gap-3">
					<div class="bar"><span style="width: {(current.status.lessonsDone / Math.max(1, current.status.lessonsTotal)) * 100}%"></span></div>
					<span class="text-sm font-bold text-muted">{current.status.lessonsDone}/{current.status.lessonsTotal}</span>
				</div>
				<a
					href={current.next
						? resolve('/chapter/[id]/[lesson]', { id: current.meta.id, lesson: current.next.id })
						: resolve('/chapter/[id]', { id: current.meta.id })}
					data-testid="continue"
					class={dueCount > 0 ? 'btn-secondary' : 'btn-primary'}
				>
					▶ {m.continue_learning()}
				</a>
			</div>
		{/if}

		<a href={resolve('/practice')} data-testid="free-practice" class="btn-secondary">🎯 {m.free_practice()}</a>

		<h2 class="h2 pt-2">{m.all_chapters()}</h2>
		{#each levels as level (level)}
			<details class="group" open={level === 'A1'}>
				<summary class="flex cursor-pointer list-none items-center justify-between rounded-2xl bg-white px-4 py-3 font-black ring-1 ring-line">
					<span>{level}</span>
					<span class="text-muted transition group-open:rotate-90">›</span>
				</summary>
				<ol class="mt-2 space-y-2">
					{#each course.chapters.filter((c) => c.id.startsWith(level)) as chapter, i (chapter.id)}
						{@const content = chapterContent(chapter.id)}
						{@const access = policy.canAccessChapter(game.state, chapter.id)}
						{@const free = content && isFreeMode(chapter.id)}
						{@const st = content ? statusOf(chapter.id) : null}
						{@const passed = st?.phase === 'passed'}
						<li>
							{#if content && st && (access.allowed || free)}
								<a href={resolve('/chapter/[id]', { id: chapter.id })} data-testid="chapter-{chapter.id}" class="card-link flex items-center gap-3">
									<span class="badge {passed ? '!bg-ok-soft !text-ok' : ''}">{passed ? '✓' : free ? '🔓' : i + 1}</span>
									<span class="flex-1 space-y-1">
										<span class="block leading-tight font-extrabold" lang="de">{chapter.title.de}</span>
										{#if showTr}<span class="block text-xs text-muted">{chapter.title[helpLocale]}</span>{/if}
										<span class="flex items-center gap-2">
											<span class="text-sm font-bold {passed ? 'text-ok' : 'text-muted'}" data-testid={passed ? 'chapter-passed' : 'chapter-phase'}>{phaseLabel(st)}</span>
											{#if !passed && st.phase !== 'new'}<span class="bar !h-1.5 max-w-24"><span style="width: {(st.lessonsDone / Math.max(1, st.lessonsTotal)) * 100}%"></span></span>{/if}
										</span>
									</span>
									<span class="text-muted">›</span>
								</a>
							{:else}
								<div class="card-muted flex items-center gap-3">
									<span class="badge !bg-stone-100 !text-stone-400">{content ? '🔒' : i + 1}</span>
									<span class="flex-1">
										<span class="block leading-tight font-bold" lang="de">{chapter.title.de}</span>
										<span class="text-sm">{content ? m.chapter_locked() : m.chapter_soon()}</span>
									</span>
								</div>
							{/if}
						</li>
					{/each}
				</ol>
			</details>
		{/each}

		<a href={resolve('/chapter/[id]', { id: PREVIEW_CHAPTER })} data-testid="chapter-preview" class="card-link flex items-center gap-3">
			<span class="badge">🧪</span>
			<span class="flex-1 font-extrabold" lang="de">{chapterContent(PREVIEW_CHAPTER)?.lessons[0].title.de}</span>
			<span class="text-muted">›</span>
		</a>

		<p class="text-center text-sm text-muted">{m.local_note()}</p>
		<p class="text-center"><button type="button" class="backlink" onclick={reset}>{m.change_name()}</button></p>
	</section>
{:else}
	<section class="space-y-6 pt-4">
		<div class="space-y-2 text-center">
			<p class="text-6xl">👋</p>
			<h1 class="text-3xl font-black">Grüß Gott!</h1>
			<p class="text-muted">{m.home_intro()}</p>
		</div>
		<form class="card space-y-5" onsubmit={start}>
			<label class="block space-y-2">
				<span class="h2">{m.name_label()}</span>
				<input data-testid="name-input" class="field w-full" bind:value={name} placeholder={m.name_placeholder()} autocomplete="given-name" maxlength="40" />
			</label>
			<fieldset class="space-y-2">
				<legend class="h2">{m.pensum_label()}</legend>
				<div class="grid grid-cols-4 gap-2">
					{#each pensumOptions as option (option.value)}
						<label class="option justify-center !px-1">
							<input type="radio" class="sr-only" name="pensum" value={option.value} bind:group={pensumMin} />
							{option.label}
						</label>
					{/each}
				</div>
			</fieldset>
			<button data-testid="start" class="btn-primary" disabled={name.trim() === ''}>{m.start()}</button>
		</form>
		<p class="text-center text-sm text-muted">{m.local_note()}</p>
	</section>
{/if}
