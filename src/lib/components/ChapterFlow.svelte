<script lang="ts">
	import BankPoints from './BankPoints.svelte';
	import FlamePot from './FlamePot.svelte';
	import { Check, Flame, Heart, Star, Trophy, X } from '@lucide/svelte';
	import { flames, TIER_CLASS } from '#lib/flames.svelte.ts';
	import { multiplier, tierOf } from '#lib/core/flames.ts';
	import { untrack } from 'svelte';
	import { accuracyPct, chapterStars } from '#lib/core/rating.ts';
	import { resolve } from '$app/paths';
	import type { Snippet } from 'svelte';
	import { getLocale } from '#lib/paraglide/runtime.js';
	import { m } from '#lib/paraglide/messages.js';
	import Runner from './Runner.svelte';
	import { chapterContent, findItem, poolItems, practiceParts, PREVIEW_CHAPTER } from '#lib/content/index.ts';
	import type { Item } from '#lib/core/content/schema.ts';
	import { gateDraw, nextGateItem, practiceItemAt, targetDraw, testDraw } from '#lib/core/flow.ts';
	import { demo, flameChapter, xpContext, type game } from '#lib/game.svelte.ts';
	import { xp } from '#lib/xp.svelte.ts';
	import { XP_ANSWER, XP_GATE_PASS, type XpKind } from '#lib/core/xp.ts';

	// Everything after the lessons of a chapter attempt (04a §4.2): practice → readiness round → test → correction → error review.
	// The state machine lives in the core; this component only shows the current state and sends events.
	type Props = { store: typeof game; chapterId: string };
	let { store, chapterId }: Props = $props();

	const helpLocale: 'de' | 'en' | 'tl' = getLocale();
	const content = $derived(chapterContent(chapterId));
	const practicePool = $derived(poolItems(chapterId, 'practice'));
	const parts = $derived(practiceParts(chapterId));
	const testPool = $derived(poolItems(chapterId, 'test'));
	const s = $derived(store.state);
	const run = $derived(s.course.chapter?.id === chapterId ? s.course.chapter : null);
	const attempt = $derived(run?.attempt);
	const completed = $derived(chapterId in s.course.completed);
	// K6: trophy numbers; chapters passed before K6 have none.
	const result = $derived(s.course.results[chapterId]);
	const stars = $derived(result ? chapterStars(result.chapter) : 0);

	// K8: flames only in the running course chapter; the error review after a failed test earns none.
	const flameId = $derived(flameChapter(chapterId));
	// K8: a round ends when the phase changes (practice round, readiness block, target stack, test) – the pot flies up.
	// Only a perfect practice round can earn a shield here; lessons bank on their own result screen.
	const phaseKey = $derived(`${run?.attemptNo ?? 0}:${attempt?.kind ?? (completed ? 'DONE' : '')}:${attempt && 'block' in attempt ? attempt.block : ''}`);
	let lastPhase = untrack(() => phaseKey);
	let lastKind = untrack(() => attempt?.kind);
	let banking = $state<{ seq: number; shield: boolean }>({ seq: 0, shield: false });
	$effect(() => {
		const key = phaseKey;
		if (key === lastPhase) return;
		const ended = lastKind;
		lastPhase = key;
		lastKind = untrack(() => attempt?.kind);
		untrack(() => {
			banking = { seq: banking.seq + 1, shield: ended === 'PRACTICE' };
			// K9: a passed readiness round pays +30.
			if (ended === 'GATE' && attempt?.kind === 'TEST_READY') xp.award(XP_GATE_PASS, xpContext(chapterId));
		});
	});
	// K9: XP per correct answer by phase; the error review pays none.
	const XP_KIND: Partial<Record<string, XpKind>> = { PRACTICE: 'practice', GATE: 'gate', TARGETED_PRACTICE: 'target', TEST: 'test', CORRECTION: 'test' };
	const answerXp = $derived.by(() => {
		const kind = attempt ? XP_KIND[attempt.kind] : undefined;
		const ctx = xpContext(chapterId);
		return kind && ctx ? { amount: XP_ANSWER[kind], ctx } : null;
	});
	// K8: passing closes the chapter's flames; K9: then the test XP and the flame bonus are paid, once per chapter.
	$effect(() => {
		if (!completed || !result) return;
		untrack(() => {
			flames.close(chapterId);
			const ctx = store === demo ? null : { chapterId: store.policy.id === 'free' ? null : chapterId, reduced: store.policy.id === 'free' };
			xp.chapterPassed(chapterId, result.test.total > 0 && result.test.correct === result.test.total, multiplier(flames.closedOf(chapterId) ?? 0), ctx);
		});
	});
	const closedXp = $derived(completed ? xp.closedOf(chapterId) : undefined);
	const closedFlames = $derived(completed ? flames.closedOf(chapterId) : undefined);
	const tlMachine = $derived(content?.tlReviewStatus === 'machine');
	// The flow is the chapter page itself, so "close" leads back to the course.
	const backHref = resolve('/');

	const practice = $derived(attempt?.kind === 'PRACTICE' ? attempt : null);
	const gate = $derived(attempt?.kind === 'GATE' ? attempt : null);
	const targeted = $derived(attempt?.kind === 'TARGETED_PRACTICE' ? attempt : null);
	const ready = $derived(attempt?.kind === 'TEST_READY' ? attempt : null);
	const test = $derived(attempt?.kind === 'TEST' ? attempt : null);
	const correction = $derived(attempt?.kind === 'CORRECTION' ? attempt : null);
	const review = $derived(attempt?.kind === 'ERROR_REVIEW' ? attempt : null);

	const practiceItem = $derived(practice && run ? findItem(practiceItemAt(parts.part, run.attemptNo, store.policy.config.PRACTICE_ROUND_ITEMS, practice.answered)?.id ?? '') : undefined);
	const gateItem = $derived.by(() => {
		if (!gate || !run) return undefined;
		return findItem(nextGateItem(gateDraw(store.policy, s, run, parts.rest, gate.block), gate.items) ?? '');
	});
	const targetItem = $derived(targeted && targeted.items.length > 0 ? findItem(targeted.items[targeted.answered] ?? '') : undefined);
	const startTarget = () => {
		if (!targeted || !run) return;
		store.dispatch({ type: 'TARGET_STARTED', itemIds: targetDraw(store.policy, run, practicePool, targeted.goalIds, targeted.block) });
	};
	const testItem = $derived(test ? findItem(test.items[test.idx]) : undefined);
	const twinItem = $derived(correction ? findItem(correction.twins[correction.idx]) : undefined);
	const lives = $derived(store.policy.startLives(s, chapterId));

	// Error review: a wrong answer just comes again, so the card to ask rotates with the number of tries.
	let tries = $state(0);
	const pending = $derived(review ? review.cardIds.filter((id) => !review.done.includes(id)) : []);
	const reviewCardId = $derived(pending.length > 0 ? pending[tries % pending.length] : undefined);
	const reviewItem = $derived(reviewCardId ? findItem(reviewCardId.replace(/^err-/, '')) : undefined);

	// Last checked answer of the running test item: drives the "life lost" note before the learner taps "next".
	let checked = $state<boolean | null>(null);

	const title = (goalId: string) => content?.goals?.[goalId];
	// R-K6: goals with the most error cards of this chapter (from the open error cards).
	const worstGoals = $derived.by(() => {
		const counts: Record<string, number> = {};
		for (const card of Object.values(s.review.cards)) {
			if (card.kind !== 'error') continue;
			for (const g of findItem(card.refId)?.goals ?? []) counts[g] = (counts[g] ?? 0) + 1;
		}
		return Object.entries(counts)
			.sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]))
			.slice(0, 3)
			.map(([id]) => id);
	});

	const startTest = () => {
		if (!run) return;
		const attemptId = crypto.randomUUID();
		store.dispatch({ type: 'TEST_STARTED', attemptId, itemIds: testDraw(store.policy, s, run, testPool, attemptId) });
	};
	const answerTest = (itemId: string, ok: boolean) => {
		if (!test) return;
		checked = null;
		store.dispatch({ type: 'TEST_ANSWERED', attemptId: test.attemptId, itemId, correct: ok });
	};
	const answerReview = (cardId: string, ok: boolean) => {
		if (ok) store.dispatch({ type: 'ERROR_REVIEW_ANSWERED', cardId, correct: true });
		else tries += 1;
	};
</script>

{#snippet label(text: string, phase: string)}
	<div class="flex items-center justify-between gap-3">
		<p class="chip" data-testid="flow-phase" data-phase={phase}>{text}</p>
		{#if flameId && phase !== 'ERROR_REVIEW'}<FlamePot />{/if}
	</div>
{/snippet}

{#snippet goalList(ids: readonly string[])}
	<ul class="list-disc space-y-1 pl-5">
		{#each ids as id (id)}
			<li>
				<span lang="de" class="font-semibold">{title(id)?.de ?? id}</span>
				{#if helpLocale !== 'de' && title(id)}<span class="text-sm text-muted"> – {title(id)?.[helpLocale]}</span>{/if}
			</li>
		{/each}
	</ul>
{/snippet}

<!-- One task at a time; the answer is booked when the learner taps "next", so the feedback stays visible. -->
{#snippet ask(item: Item, header: Snippet, done: (ok: boolean) => void, exam: boolean)}
	{#key item.id + (reviewCardId ?? '') + tries}
		<Runner
			items={[item]}
			xp={attempt?.kind === 'ERROR_REVIEW' ? null : answerXp}
			flameChapter={attempt?.kind === 'ERROR_REVIEW' ? null : flameId}
			bare
			examMode={exam}
			top={header}
			{tlMachine}
			{backHref}
			backLabel={m.course()}
			nextLabel={m.next()}
			onchecked={(_, ok) => (checked = ok)}
			onfinish={(correct) => done(correct === 1)}
		/>
	{/key}
{/snippet}

{#snippet practiceTop()}
	<div class="flex items-center justify-between gap-3">
		{@render label(m.flow_practice({ current: (practice?.answered ?? 0) + 1, total: practice?.total ?? 0 }), 'PRACTICE')}
		<button type="button" class="text-sm font-bold text-muted underline underline-offset-4 hover:text-brand" data-testid="flow-skip-practice" onclick={() => store.dispatch({ type: 'PRACTICE_SKIPPED' })}>{m.flow_practice_skip()} →</button>
	</div>
{/snippet}
{#snippet gateTop()}
	{@render label(m.flow_gate({ block: gate?.block ?? 1, current: (gate?.answered ?? 0) + 1, total: store.policy.config.GATE_ITEMS }), 'GATE')}
	<p class="font-bold" data-testid="gate-score"><span class="inline-flex items-center gap-1 text-ok"><Check size={16} strokeWidth={3} />{gate?.correct ?? 0}</span> · <span class="inline-flex items-center gap-1 text-warn"><X size={16} strokeWidth={3} />{(gate?.answered ?? 0) - (gate?.correct ?? 0)}</span></p>
	<p class="text-sm text-muted">{m.flow_gate_note({ min: store.policy.config.GATE_MIN_CORRECT, total: store.policy.config.GATE_ITEMS })}</p>
{/snippet}
{#snippet testTop()}
	<div class="flex items-center justify-between gap-3">
		{@render label(m.flow_test({ current: (test?.idx ?? 0) + 1, total: test?.items.length ?? 0 }), 'TEST')}
		<p class="flex gap-1" data-testid="lives" data-lives={test?.lives} aria-label={m.flow_lives({ count: test?.lives ?? 0 })}>{#each { length: Math.max(0, (test?.lives ?? 0) - Number(checked === false)) } as _, h (h)}<Heart size={22} strokeWidth={2.25} class="fill-brand text-brand" />{/each}</p>
	</div>
	{#if checked === false}<p class="font-bold text-warn" data-testid="life-lost" role="status">{m.flow_life_lost()}</p>{/if}
{/snippet}
{#snippet correctionTop()}
	{@render label(m.flow_correction_count({ current: (correction?.idx ?? 0) + 1, total: correction?.twins.length ?? 0 }), 'CORRECTION')}
{/snippet}
{#snippet reviewTop()}
	{@render label(m.flow_review_left({ count: pending.length }), 'ERROR_REVIEW')}
{/snippet}
{#snippet targetedTop()}
	{@render label(m.flow_target_count({ current: (targeted?.answered ?? 0) + 1, total: targeted?.items.length ?? 0 }), 'TARGETED_PRACTICE')}
	<!-- K4: the list of weak goals stays visible while the stack runs. -->
	<details class="card-muted text-sm" data-testid="target-goals">
		<summary class="cursor-pointer font-bold">{m.flow_targeted_text()} ({targeted?.goalIds.length ?? 0})</summary>
		<div class="mt-2">{@render goalList(targeted?.goalIds ?? [])}</div>
	</details>
{/snippet}

<section class="space-y-4" data-testid="chapter-flow">
	{#key banking.seq}
		{#if banking.seq > 0}<BankPoints shield={banking.shield} />{/if}
	{/key}
	{#if chapterId === PREVIEW_CHAPTER}<p class="text-sm text-muted">{m.flow_demo_note()}</p>{/if}

	{#if practice && practiceItem}
		{@render ask(practiceItem, practiceTop, (ok) => store.dispatch({ type: 'PRACTICE_ANSWERED', itemId: practiceItem.id, correct: ok }), false)}
	{:else if gate && gateItem}
		{@render ask(gateItem, gateTop, (ok) => store.dispatch({ type: 'GATE_ANSWERED', itemId: gateItem.id, correct: ok }), false)}
	{:else if targeted && targetItem}
		{@render ask(targetItem, targetedTop, (ok) => store.dispatch({ type: 'TARGET_ANSWERED', itemId: targetItem.id, correct: ok }), false)}
	{:else if targeted}
		{@render label(m.flow_targeted_title(), 'TARGETED_PRACTICE')}
		<div class="card space-y-3" data-testid="target-intro">
			<p>{m.flow_target_intro({ max: store.policy.config.TARGET_MAX })}</p>
			<p class="font-bold">{m.flow_targeted_text()}</p>
			{@render goalList(targeted.goalIds)}
		</div>
		<div class="actionbar">
			<button type="button" class="btn-primary" data-testid="flow-target-start" onclick={startTarget}>{m.flow_target_start()}</button>
		</div>
	{:else if ready && run}
		<div class="card space-y-3">
			<h2 class="h2">{m.flow_ready_title()}</h2>
			<p>{m.flow_ready_text({ count: testDraw(store.policy, s, run, testPool, 'preview').length, lives })}</p>
			<p class="flex gap-1" aria-label={m.flow_lives({ count: lives })}>{#each { length: lives } as _, h (h)}<Heart size={22} strokeWidth={2.25} class="fill-brand text-brand" />{/each}</p>
		</div>
		<div class="actionbar">
			<button type="button" class="btn-primary" data-testid="flow-start-test" onclick={startTest}>{m.flow_start_test()}</button>
		</div>
	{:else if test && testItem}
		{@render ask(testItem, testTop, (ok) => answerTest(testItem.id, ok), true)}
	{:else if correction && twinItem}
		<div class="card space-y-1">
			<p class="font-bold">{m.flow_correction_title()}</p>
			<p class="text-sm text-muted">{m.flow_correction_text()}</p>
		</div>
		{@render ask(
			twinItem,
			correctionTop,
			(ok) => store.dispatch({ type: 'CORRECTION_ANSWERED', attemptId: correction.attemptId, twinId: twinItem.id, correct: ok }),
			true
		)}
	{:else if review && run}
		<div class="card space-y-2">
			<p class="font-bold">{m.flow_review_title()}</p>
			<p>{m.flow_review_text()}</p>
			<!-- R-K6: from the 2nd failed attempt on, name the goals with the most mistakes. -->
			{#if run.attemptNo >= 2 && worstGoals.length > 0}
				<div class="space-y-1" data-testid="flow-rk6">
					<p class="font-bold">{m.flow_rk6_title()}</p>
					{@render goalList(worstGoals)}
					<p class="text-sm text-muted">{m.flow_rk6_text()}</p>
				</div>
			{/if}
		</div>
		{#if reviewItem && reviewCardId}
			{@const cardId = reviewCardId}
			{@render ask(reviewItem, reviewTop, (ok) => answerReview(cardId, ok), false)}
		{/if}
	{:else if completed}
		<div class="card space-y-4 text-center" data-testid="flow-passed">
			<p class="pop mx-auto grid h-20 w-20 place-items-center rounded-full bg-amber-100 text-amber-600"><Trophy size={40} strokeWidth={2} /></p>
			<h2 class="h2">{m.flow_passed_title()}</h2>
			{#if result}
				<!-- K6, G-019 A: stars from the accuracy over the whole chapter. -->
				<p class="flex items-center justify-center gap-1.5" data-testid="trophy-stars" data-stars={stars} aria-label={m.trophy_stars({ count: stars })}>
					{#each [1, 2, 3] as n (n)}<Star size={34} strokeWidth={2} class={n <= stars ? 'fill-amber-400 text-amber-500' : 'text-line'} />{/each}
				</p>
				{#if closedFlames !== undefined}
					<!-- K6/K8: the chapter flames and their multiplier (applied to XP in 030). -->
					<p class="flex items-center justify-center gap-2 text-lg font-extrabold" data-testid="trophy-flames">
						<Flame size={24} strokeWidth={2.25} class={TIER_CLASS[tierOf(closedFlames)]} />{m.trophy_flames({ count: closedFlames })}
						<span class="text-sm font-bold text-muted">×{multiplier(closedFlames).toLocaleString(getLocale())}</span>
					</p>
				{/if}
				{#if closedXp}
					<p class="flex items-center justify-center gap-2 font-extrabold" data-testid="trophy-xp">
						<span class="rounded-full bg-amber-100 px-3 py-1 text-amber-700">+{closedXp.xp + closedXp.bonus} XP</span>
						{#if closedXp.bonus > 0}<span class="text-sm font-bold text-muted">{m.trophy_xp_bonus({ bonus: closedXp.bonus })}</span>{/if}
					</p>
				{/if}
				<div class="grid grid-cols-2 gap-3 text-left" data-testid="trophy">
					<div class="rounded-2xl bg-ok-soft p-3">
						<p class="text-sm font-bold text-ok">{m.trophy_test()}</p>
						<p class="text-3xl font-black text-ok" data-testid="trophy-test">{accuracyPct(result.test)}%</p>
						<p class="text-sm font-semibold">{m.trophy_right_wrong({ correct: result.test.correct, wrong: result.test.total - result.test.correct })}</p>
					</div>
					<div class="rounded-2xl bg-paper p-3">
						<p class="text-sm font-bold text-muted">{m.trophy_error_rate()}</p>
						<p class="text-3xl font-black" data-testid="trophy-error-rate">{100 - accuracyPct(result.chapter)}%</p>
						<p class="text-sm font-semibold">{m.trophy_error_detail({ wrong: result.chapter.total - result.chapter.correct, total: result.chapter.total })}</p>
					</div>
				</div>
			{/if}
			{#if s.course.nextChapterBonus > 0}<p class="font-bold text-ok">{m.flow_bonus({ count: s.course.nextChapterBonus })}</p>{/if}
			{#if s.course.phase.kind === 'CHAPTER' && !chapterContent(s.course.phase.id)}
				<p class="text-muted" data-testid="flow-next-soon">{m.flow_next_soon()}</p>
				<a href={resolve('/')} class="btn-primary">{m.course()}</a>
			{:else if s.course.phase.kind === 'CHAPTER'}
				<a href={resolve('/chapter/[id]', { id: s.course.phase.id })} class="btn-primary" data-testid="flow-next-chapter">{m.flow_next_chapter()}</a>
			{:else if chapterId === PREVIEW_CHAPTER}
				<button type="button" class="btn-secondary" data-testid="flow-restart" onclick={() => store.reset()}>{m.flow_demo_restart()}</button>
			{/if}
		</div>
	{/if}
</section>
