<script lang="ts">
	import { onMount } from 'svelte';
	import { resolve } from '$app/paths';
	import { m } from '#lib/paraglide/messages.js';
	import CardRunner, { type Task } from '#lib/components/CardRunner.svelte';
	import { allVocab, vocabByRef } from '#lib/content/index.ts';
	import { dueQueue } from '#lib/core/review.ts';
	import { game } from '#lib/game.svelte.ts';

	// The round is fixed when the page opens: cards answered here must not reshuffle the queue.
	let tasks = $state<Task[] | null>(null);

	onMount(() => {
		game.init();
		tasks = dueQueue(game.state, game.today).flatMap((card) => {
			const vocab = vocabByRef(card.refId);
			return vocab ? [{ cardId: card.id, direction: card.nextDirection, vocab }] : [];
		});
	});

	const answer = (task: Task, correct: boolean) =>
		game.dispatch({ type: 'REVIEW_ANSWERED', cardId: task.cardId, direction: task.direction, correct });
</script>

<a href={resolve('/')} class="backlink">‹ {m.course()}</a>
<h1 class="h1 pt-4 pb-2">{m.review_title()}</h1>

{#if tasks && tasks.length > 0}
	<CardRunner {tasks} pool={allVocab()} backHref={resolve('/')} backLabel={m.home()} onanswer={answer} />
{:else if tasks}
	<p class="text-muted" data-testid="review-none">{m.review_none()}</p>
{/if}
