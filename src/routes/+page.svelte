<script lang="ts">
	import LevelRing from '#lib/components/LevelRing.svelte';
	import Popover from '#lib/components/Popover.svelte';
	import { xp } from '#lib/xp.svelte.ts';
	import { onMount } from 'svelte';
	import { resolve } from '$app/paths';
	import { m } from '#lib/paraglide/messages.js';
	import { getLocale } from '#lib/paraglide/runtime.js';
	import { chapterContent, course } from '#lib/content/index.ts';
	import { flames, TIER_CLASS } from '#lib/flames.svelte.ts';
	import { DAY_GOAL_SEC } from '#lib/core/day.ts';
	import { ArrowRight, CalendarDays, Check, Flame, ChevronDown, ChevronRight, CircleCheck, Clock, Dumbbell, Lock, LockOpen, RotateCcw, Zap, Snowflake, Info } from '@lucide/svelte';
	import { planDay } from '#lib/core/reducer.ts';
	import { dueQueue } from '#lib/core/review.ts';
	import type { PensumMin } from '#lib/core/state.ts';
	import { game, isFreeMode, policy, storeFor } from '#lib/game.svelte.ts';
	import { chapterStatus, type ChapterStatus } from '#lib/core/status.ts';
	import { settings } from '#lib/settings.svelte.ts';

	const helpLocale: 'de' | 'en' | 'tl' = getLocale();
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

	// Exam levels come from the chapter ids (A1-01 → A1), so a new level needs no UI change.
	// Up to 3 levels fit a segmented control, more switch to a picker popover.
	const levels = $derived([...new Set(course.chapters.map((c) => c.id.split('-')[0]))]);
	// Level tab follows the running chapter until the learner picks one.
	let picked = $state<string | null>(null);
	const level = $derived(picked ?? run?.id.split('-')[0] ?? levels[0]);
	const levelChapters = $derived(course.chapters.filter((c) => c.id.startsWith(level)));
	const passedCount = $derived(levelChapters.filter((c) => chapterContent(c.id) && statusOf(c.id).phase === 'passed').length);

	// R-S1 day goal: active minutes today; the bar fills to 20 min (due reviews are named in the sub line).
	const streak = $derived(game.state.streak.current);
	const goal = $derived.by(() => {
		const day = game.state.days[game.today];
		const min = Math.floor((day?.activeSec ?? 0) / 60);
		return { min, met: day?.goalMet ?? false, pct: Math.min(100, (min / (DAY_GOAL_SEC / 60)) * 100) };
	});

	onMount(() => game.init());
	// Free-mode chapters keep their own state; load it so the list shows their progress.
	$effect(() => {
		if (!game.ready || !game.state.profile) return; // no profile yet (e.g. right after a reset): nothing to load
		for (const c of course.chapters) if (chapterContent(c.id) && isFreeMode(c.id)) storeFor(c.id).init();
	});

	const start = (event: SubmitEvent) => {
		event.preventDefault();
		if (name.trim() === '') return;
		game.dispatch({ type: 'PROFILE_CREATED', name, pensumMin });
	};

</script>

{#if !game.ready}
	<p aria-busy="true" class="pt-10 text-center text-muted">…</p>
{:else if profile}
	<section class="space-y-6">
		<div class="hello rise space-y-2">
			<div class="hello-grid">
				<h1 class="h1 hello-name">{m.welcome_back({ name: profile.name })}</h1>
				<p class="hello-meta text-sm font-bold text-muted">
					<span class="nowrap-item"><CalendarDays size={16} strokeWidth={2.25} /><span data-testid="plan-day">{m.day_x({ day: planDay(profile.startDate, game.today) })}</span></span>
					<span class="nowrap-item"><Clock size={16} strokeWidth={2.25} />{m.per_day({ time: pensumLabel })}</span>
				</p>
				<!-- Level badge: total XP, level ring and the way to the next level; a tap explains XP. -->
				<button type="button" class="hello-xp flex shrink-0 cursor-pointer items-center gap-2.5 rounded-(--r-card) text-right transition active:scale-[0.97] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-brand/40" popovertarget="xp-pop" data-testid="home-xp">
					<span class="space-y-0.5">
						<b class="block text-base leading-tight font-black" data-testid="home-xp-total">{xp.total.toLocaleString(getLocale())} XP</b>
						<span class="block text-xs font-bold whitespace-nowrap text-muted">{m.xp_to_next({ xp: (xp.level.need - xp.level.into).toLocaleString(getLocale()), level: xp.level.level + 1 })}</span>
					</span>
					<LevelRing large />
				</button>
			</div>
		</div>

		<div class="tile goal-tile !flex-row !flex-wrap !items-center rise" style:animation-delay="40ms" data-testid="day-goal">
			<span class="grid h-12 w-12 shrink-0 place-items-center rounded-2xl {streak > 0 ? 'bg-amber-100 text-amber-500' : 'bg-stone-100 text-stone-400'}">
				<Zap size={26} strokeWidth={2.25} class={streak > 0 ? 'fill-amber-400' : ''} />
			</span>
			<span class="min-w-0 flex-1 space-y-1.5">
				<span class="flex items-baseline justify-between gap-2">
					<span class="tile-title flex flex-wrap gap-x-1.5"><span class="whitespace-nowrap">{streak} {m.stat_streak()}</span><span class="text-sm font-semibold whitespace-nowrap text-muted">· {m.stat_best()} {game.state.streak.best}</span></span>
					<span class="goal-label text-xs font-extrabold tracking-wider whitespace-nowrap text-muted uppercase">{m.goal_title()}</span>
				</span>
				<span class="bar !h-2 block"><span class={goal.met ? '!bg-ok' : '!bg-amber-400'} style="width: {goal.pct}%"></span></span>
				<span class="flex flex-wrap items-center justify-between gap-x-2 gap-y-0.5">
					<span class="tile-sub">{goal.met ? m.goal_met() : dueCount > 0 && goal.min >= DAY_GOAL_SEC / 60 ? m.goal_due({ count: dueCount }) : m.goal_progress({ done: goal.min, goal: DAY_GOAL_SEC / 60 })}</span>
					<span class="flex items-center gap-1 text-sm font-extrabold whitespace-nowrap text-muted" title={m.stat_flawless()} data-testid="flawless-run">
						<Flame size={15} strokeWidth={2.5} class={TIER_CLASS[flames.tier]} />{flames.chapterFlames}{#if flames.multiplier > 1}<span class="font-semibold">· ×{flames.multiplier.toLocaleString(getLocale())}</span>{/if}
					</span>
				</span>
			</span>
			<button type="button" class="flex w-full cursor-pointer items-center gap-2 border-t border-line pt-2.5 text-sm font-bold text-muted lg:hidden" popovertarget="freeze-pop" data-testid="freeze-info">
				<Snowflake size={16} strokeWidth={2.25} class="text-sky-500" />{game.state.streak.freezes}/2 {m.stat_freezes()}
				<Info size={14} strokeWidth={2.5} class="ml-auto" />
			</button>
		</div>

		{#if current}
			<div class="hero rise" style:animation-delay="60ms">
				<div class="lg:flex lg:items-end lg:justify-between lg:gap-6">
					<div class="min-w-0 flex-1 space-y-2">
						<p class="text-xs font-extrabold tracking-wider text-white/75 uppercase">{m.your_chapter()} · {current.meta.id}</p>
						<p class="display text-2xl leading-tight" lang="de">{current.meta.title.de}</p>
						{#if showTr}<p class="text-sm font-semibold text-white/80">{current.meta.title[helpLocale]}</p>{/if}
						<div class="flex items-center gap-3 pt-1">
							<div class="bar !h-2 !bg-white/25"><span class="!bg-white" style="width: {(current.status.lessonsDone / Math.max(1, current.status.lessonsTotal)) * 100}%"></span></div>
							<span class="text-sm font-extrabold whitespace-nowrap text-white/90">{current.status.lessonsDone}/{current.status.lessonsTotal}</span>
						</div>
						<p class="text-sm font-bold text-white/85" data-testid="current-phase">{phaseLabel(current.status)}</p>
					</div>
					<a
						href={current.next
							? resolve('/chapter/[id]/[lesson]', { id: current.meta.id, lesson: current.next.id })
							: resolve('/chapter/[id]', { id: current.meta.id })}
						data-testid="continue"
						class="btn-hero mt-4 lg:mt-0"
					>
						{m.continue_learning()}<ArrowRight size={20} strokeWidth={2.5} />
					</a>
				</div>
			</div>
		{/if}

		<div class="grid grid-cols-2 gap-3 rise" style:animation-delay="120ms">
			<a href={resolve('/review')} data-testid={dueCount > 0 ? 'review-due' : 'review-none'} class="tile">
				{#if dueCount > 0}<span class="attn-count" aria-hidden="true">{dueCount}</span>{/if}
				<span class="icon-tile {dueCount > 0 ? 'is-attn' : '!bg-ok-soft !text-ok'}">
					{#if dueCount > 0}<RotateCcw size={20} strokeWidth={2.25} />{:else}<CircleCheck size={20} strokeWidth={2.25} />{/if}
				</span>
				<span class="min-w-0">
					<span class="tile-title">{m.tile_review()}</span>
					<span class="tile-sub">{dueCount > 0 ? m.tile_review_due({ count: dueCount }) : m.tile_review_none()}</span>
				</span>
			</a>
			<a href={resolve('/practice')} data-testid="free-practice" class="tile">
				<span class="icon-tile"><Dumbbell size={20} strokeWidth={2.25} /></span>
				<span class="min-w-0">
					<span class="tile-title">{m.free_practice()}</span>
					<span class="tile-sub">{m.tile_practice_sub()}</span>
				</span>
			</a>
		</div>

		<div class="space-y-3 rise" style:animation-delay="180ms">
			<div class="flex items-end justify-between gap-3">
				<div>
					<h2 class="h2">{m.all_chapters()}</h2>
					<p class="text-sm font-semibold text-muted">{m.chapters_passed({ done: passedCount, total: levelChapters.length })}</p>
				</div>
				{#if levels.length <= 3}
					<div class="seg" style:width="{levels.length * 4}rem" role="group" aria-label={m.all_chapters()}>
						{#each levels as l (l)}
							<button type="button" aria-pressed={level === l} onclick={() => (picked = l)}>{l}</button>
						{/each}
					</div>
				{:else}
					<button type="button" class="btn-ghost" popovertarget="level-pop" data-testid="level-picker">{level}<ChevronDown size={16} strokeWidth={2.5} /></button>
				{/if}
			</div>
			<ol class="path">
				{#each levelChapters as chapter, i (chapter.id)}
					{@const content = chapterContent(chapter.id)}
					{@const access = policy.canAccessChapter(game.state, chapter.id)}
					{@const free = content && isFreeMode(chapter.id)}
					{@const st = content ? statusOf(chapter.id) : null}
					{@const passed = st?.phase === 'passed'}
					{@const isCurrent = chapter.id === run?.id && !passed}
					<li class="rise" style:animation-delay="{200 + i * 25}ms">
						{#if content && st && (access.allowed || free)}
							<a href={resolve('/chapter/[id]', { id: chapter.id })} data-testid="chapter-{chapter.id}" class="path-row" class:is-current={isCurrent}>
								<span class="node" class:is-passed={passed} class:is-current={isCurrent}>
									{#if passed}<Check size={18} strokeWidth={3} />{:else if free && !isCurrent}<LockOpen size={16} strokeWidth={2.5} />{:else}{i + 1}{/if}
								</span>
								<span class="min-w-0 flex-1">
									<span class="block leading-tight font-extrabold" lang="de">{chapter.title.de}</span>
									{#if showTr}<span class="block text-sm font-semibold text-muted">{chapter.title[helpLocale]}</span>{/if}
									<span class="mt-1 flex items-center gap-2">
										<span class="text-sm font-bold {passed ? 'text-ok' : 'text-muted'}" data-testid={passed ? 'chapter-passed' : 'chapter-phase'}>{phaseLabel(st)}</span>
										{#if !passed && st.phase !== 'new'}<span class="bar !h-1.5 max-w-20"><span style="width: {(st.lessonsDone / Math.max(1, st.lessonsTotal)) * 100}%"></span></span>{/if}
									</span>
								</span>
								<ChevronRight size={18} class="text-muted" />
							</a>
						{:else}
							<div class="path-row text-muted">
								<span class="node is-locked">{#if content}<Lock size={15} strokeWidth={2.5} />{:else}{i + 1}{/if}</span>
								<span class="min-w-0 flex-1">
									<span class="block leading-tight font-bold" lang="de">{chapter.title.de}</span>
									<span class="text-sm font-semibold">{content ? m.chapter_locked() : m.chapter_soon()}</span>
								</span>
							</div>
						{/if}
					</li>
				{/each}
			</ol>
		</div>
	</section>

	<Popover id="xp-pop" title={m.xp_title()} testid="home-xp-info">
		<div class="flex items-center gap-3 text-ink">
			<LevelRing large />
			<span class="space-y-0.5">
				<b class="block text-lg font-black">{xp.total.toLocaleString(getLocale())} XP</b>
				<span class="block text-sm font-bold text-muted">{m.xp_to_next({ xp: (xp.level.need - xp.level.into).toLocaleString(getLocale()), level: xp.level.level + 1 })}</span>
			</span>
		</div>
		<p>{m.xp_explain()}</p>
	</Popover>
	<Popover id="freeze-pop" title={m.stat_freezes()}>
		<p>{m.freeze_explain()}</p>
	</Popover>
	{#if levels.length > 3}
		<Popover id="level-pop" title={m.all_chapters()}>
			<div class="grid gap-2">
				{#each levels as l (l)}
					<button type="button" class="option justify-between" popovertarget="level-pop" popovertargetaction="hide" onclick={() => (picked = l)}>{l}{#if level === l}<Check size={18} strokeWidth={3} />{/if}</button>
				{/each}
			</div>
		</Popover>
	{/if}
{:else}
	<section class="space-y-6 pt-6">
		<div class="space-y-3 text-center">
			<img src="/icons/logo.svg" alt="" width="88" height="88" class="splash-logo mx-auto h-24 w-24 drop-shadow-md" />
			<h1 class="display text-4xl rise" style:animation-delay="120ms" lang="de">Grüß Gott!</h1>
			<p class="text-muted rise" style:animation-delay="180ms">{m.home_intro()}</p>
		</div>
		<form class="card space-y-5 rise" style:animation-delay="240ms" onsubmit={start}>
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
