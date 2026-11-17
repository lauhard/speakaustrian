<script lang="ts">
	import { onMount } from 'svelte';
	import { resolve } from '$app/paths';
	import { page } from '$app/state';
	import { m } from '#lib/paraglide/messages.js';
	import CardRunner, { type Task } from '#lib/components/CardRunner.svelte';
	import Runner from '#lib/components/Runner.svelte';
	import { allVocab, chapterContent, findItem, vocabByRef } from '#lib/content/index.ts';
	import type { Item } from '#lib/core/content/schema.ts';
	import { dueQueue } from '#lib/core/review.ts';
	import { demo, game } from '#lib/game.svelte.ts';

	// `?store=demo` reviews the cards of the DEMO sandbox (005c), otherwise the course cards.
	const store = $derived(page.url.searchParams.get('store') === 'demo' ? demo : game);

	// The round is fixed when the page opens: cards answered here must not reshuffle the queue.
	let tasks = $state<Task[] | null>(null);
	// R-W3/R-W5: error cards come first, as full tasks of their base item; wrong ones come again in the same round.
	let errorItems = $state<{ cardId: string; direction: Task['direction']; item: Item }[]>([]);
	let errorRound = $state<Item[]>([]);
	let errorsDone = $state(true);
	let wrongNow = $state<string[]>([]);
	let round = $state(0);

	onMount(() => {
		game.init();
		store.init();
		const queue = dueQueue(store.state, store.today);
		errorItems = queue.flatMap((card) => {
			const item = card.kind === 'error' ? findItem(card.refId) : undefined;
			return item ? [{ cardId: card.id, direction: card.nextDirection, item }] : [];
		});
		errorRound = errorItems.map((e) => e.item);
		errorsDone = errorItems.length === 0;
		tasks = queue.flatMap((card) => {
			const vocab = card.kind === 'error' ? undefined : vocabByRef(card.refId);
			return vocab ? [{ cardId: card.id, direction: card.nextDirection, vocab }] : [];
		});
	});

	const answer = (task: Task, correct: boolean) =>
		store.dispatch({ type: 'REVIEW_ANSWERED', cardId: task.cardId, direction: task.direction, correct });

	// Only the first answer of an error card is booked (the reducer ignores later ones, R-W5).
	const checked = (item: Item, correct: boolean) => {
		const entry = errorItems.find((e) => e.item.id === item.id);
		if (entry) store.dispatch({ type: 'REVIEW_ANSWERED', cardId: entry.cardId, direction: entry.direction, correct });
		if (!correct) wrongNow = [...wrongNow, item.id];
	};
	const roundFinished = () => {
		const again = errorRound.filter((i) => wrongNow.includes(i.id));
		wrongNow = [];
		if (again.length === 0) errorsDone = true;
		else {
			errorRound = again;
			round += 1;
		}
	};
	const tlMachine = $derived(errorRound.some((i) => chapterContent('DEMO')?.pools?.practice.some((p) => p.id === i.id)));
</script>

<h1 class="h1 pt-4 pb-2">{m.review_title()}</h1>

{#if tasks === null}
	<p aria-busy="true" class="text-muted">…</p>
{:else if !errorsDone}
	<p class="chip" data-testid="review-errors">{m.review_errors()}</p>
	{#key round}
		<Runner items={errorRound} {tlMachine} bare backHref={resolve('/')} backLabel={m.home()} onchecked={checked} onfinish={roundFinished} />
	{/key}
{:else if tasks.length > 0}
	{#if errorItems.length > 0}<p class="text-sm font-bold text-ok" data-testid="review-errors-done">{m.review_errors_done()}</p>{/if}
	<CardRunner {tasks} pool={allVocab()} backHref={resolve('/')} backLabel={m.home()} onanswer={answer} />
{:else}
	<p class="text-muted" data-testid="review-none">{m.review_none()}</p>
{/if}
