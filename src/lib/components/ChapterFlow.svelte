<script lang="ts">
	import { resolve } from '$app/paths';
	import type { Snippet } from 'svelte';
	import { getLocale } from '#lib/paraglide/runtime.js';
	import { m } from '#lib/paraglide/messages.js';
	import Runner from './Runner.svelte';
	import { chapterContent, findItem, poolItems, PREVIEW_CHAPTER } from '#lib/content/index.ts';
	import type { Item } from '#lib/core/content/schema.ts';
	import { gateDraw, nextGateItem, targetedItems, testDraw } from '#lib/core/flow.ts';
	import type { game } from '#lib/game.svelte.ts';

	// Everything after the lessons of a chapter attempt (04a §4.2): practice → readiness round → test → correction → error review.
	// The state machine lives in the core; this component only shows the current state and sends events.
	type Props = { store: typeof game; chapterId: string };
	let { store, chapterId }: Props = $props();

	const helpLocale: 'de' | 'en' | 'tl' = getLocale();
	const content = $derived(chapterContent(chapterId));
	const practicePool = $derived(poolItems(chapterId, 'practice'));
	const testPool = $derived(poolItems(chapterId, 'test'));
	const s = $derived(store.state);
	const run = $derived(s.course.chapter?.id === chapterId ? s.course.chapter : null);
	const attempt = $derived(run?.attempt);
	const completed = $derived(chapterId in s.course.completed);
	const tlMachine = $derived(content?.tlReviewStatus === 'machine');
	const backHref = $derived(resolve('/chapter/[id]', { id: chapterId }));

	const practice = $derived(attempt?.kind === 'PRACTICE' ? attempt : null);
	const gate = $derived(attempt?.kind === 'GATE' ? attempt : null);
	const targeted = $derived(attempt?.kind === 'TARGETED_PRACTICE' ? attempt : null);
	const ready = $derived(attempt?.kind === 'TEST_READY' ? attempt : null);
	const test = $derived(attempt?.kind === 'TEST' ? attempt : null);
	const correction = $derived(attempt?.kind === 'CORRECTION' ? attempt : null);
	const review = $derived(attempt?.kind === 'ERROR_REVIEW' ? attempt : null);

	const practiceItem = $derived(practice ? findItem(practicePool[practice.answered]?.id ?? '') : undefined);
	const gateItem = $derived.by(() => {
		if (!gate || !run) return undefined;
		return findItem(nextGateItem(gateDraw(store.policy, s, run, practicePool, gate.block), gate.items) ?? '');
	});
	const targetedList = $derived(targeted ? targetedItems(practicePool, targeted.goalIds).flatMap((id) => findItem(id) ?? []) : []);
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
	<p class="chip" data-testid="flow-phase" data-phase={phase}>{text}</p>
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
			bare
			examMode={exam}
			top={header}
			{tlMachine}
			{backHref}
			backLabel={m.back_chapter()}
			nextLabel={m.next()}
			onchecked={(_, ok) => (checked = ok)}
			onfinish={(correct) => done(correct === 1)}
		/>
	{/key}
{/snippet}

{#snippet practiceTop()}
	{@render label(m.flow_practice({ current: (practice?.answered ?? 0) + 1, total: practice?.total ?? 0 }), 'PRACTICE')}
{/snippet}
{#snippet gateTop()}
	{@render label(m.flow_gate({ block: gate?.block ?? 1, current: (gate?.answered ?? 0) + 1, total: store.policy.config.GATE_ITEMS }), 'GATE')}
	<p class="text-sm text-muted">{m.flow_gate_note({ min: store.policy.config.GATE_MIN_CORRECT, total: store.policy.config.GATE_ITEMS })}</p>
{/snippet}
{#snippet testTop()}
	<div class="flex items-center justify-between gap-3">
		{@render label(m.flow_test({ current: (test?.idx ?? 0) + 1, total: test?.items.length ?? 0 }), 'TEST')}
		<p class="text-lg" data-testid="lives" data-lives={test?.lives} aria-label={m.flow_lives({ count: test?.lives ?? 0 })}>{'❤️'.repeat(Math.max(0, (test?.lives ?? 0) - Number(checked === false)))}</p>
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
	{@render label(m.flow_targeted_title(), 'TARGETED_PRACTICE')}
{/snippet}

<section class="space-y-4" data-testid="chapter-flow">
	{#if chapterId === PREVIEW_CHAPTER}<p class="text-sm text-muted">{m.flow_demo_note()}</p>{/if}

	{#if practice && practiceItem}
		{@render ask(practiceItem, practiceTop, (ok) => store.dispatch({ type: 'PRACTICE_ANSWERED', itemId: practiceItem.id, correct: ok }), false)}
	{:else if gate && gateItem}
		{@render ask(gateItem, gateTop, (ok) => store.dispatch({ type: 'GATE_ANSWERED', itemId: gateItem.id, correct: ok }), false)}
	{:else if targeted}
		<div class="card space-y-2">
			<p class="font-bold">{m.flow_targeted_text()}</p>
			{@render goalList(targeted.goalIds)}
		</div>
		{#if targetedList.length > 0}
			{#key targeted.block}
				<Runner
					items={targetedList}
					bare
					top={targetedTop}
					{tlMachine}
					{backHref}
					backLabel={m.back_chapter()}
					onfinish={() => store.dispatch({ type: 'TARGETED_PRACTICE_DONE', goalIds: targeted.goalIds })}
				/>
			{/key}
		{:else}
			<button type="button" class="btn-primary" data-testid="flow-targeted-done" onclick={() => store.dispatch({ type: 'TARGETED_PRACTICE_DONE', goalIds: targeted.goalIds })}>{m.flow_targeted_go()}</button>
		{/if}
	{:else if ready && run}
		<div class="card space-y-3">
			<h2 class="h2">{m.flow_ready_title()}</h2>
			<p>{m.flow_ready_text({ count: testDraw(store.policy, s, run, testPool, 'preview').length, lives })}</p>
			<p class="text-lg" aria-label={m.flow_lives({ count: lives })}>{'❤️'.repeat(lives)}</p>
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
		<div class="card space-y-3 text-center" data-testid="flow-passed">
			<p class="text-5xl">🎉</p>
			<h2 class="h2">{m.flow_passed_title()}</h2>
			{#if s.course.nextChapterBonus > 0}<p class="font-bold text-ok">{m.flow_bonus({ count: s.course.nextChapterBonus })}</p>{/if}
			{#if s.course.phase.kind === 'CHAPTER'}
				<a href={resolve('/chapter/[id]', { id: s.course.phase.id })} class="btn-primary" data-testid="flow-next-chapter">{m.flow_next_chapter()}</a>
			{:else if chapterId === PREVIEW_CHAPTER}
				<button type="button" class="btn-secondary" data-testid="flow-restart" onclick={() => store.reset()}>{m.flow_demo_restart()}</button>
			{/if}
		</div>
	{/if}
</section>
