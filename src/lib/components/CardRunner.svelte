<script lang="ts">
	import { onMount, untrack } from 'svelte';
	import { getLocale } from '#lib/paraglide/runtime.js';
	import { m } from '#lib/paraglide/messages.js';
	import { createDeviceTts } from '#lib/adapters/web/device-tts.ts';
	import type { Vocab } from '#lib/core/content/schema.ts';
	import type { Verdict } from '#lib/core/grading.ts';
	import { buildQuestion, fullForm, gradeProduce, type Direction, type Question } from '#lib/core/review.ts';
	import type { SpeechOutPort } from '#lib/ports/speech-out.ts';

	export type Task = { cardId: string; direction: Direction; vocab: Vocab };
	type Props = {
		tasks: Task[];
		pool: Vocab[];
		backHref: string;
		backLabel: string;
		// Called for the first answer of each card only; repeats in the same round have no box effect (R-W5).
		onanswer?: (task: Task, correct: boolean) => void;
	};
	let { tasks, pool, backHref, backLabel, onanswer }: Props = $props();

	const locale = getLocale();
	const meaning = (v: Vocab) => (locale === 'tl' ? v.tl : v.en);
	const articles = ['der', 'die', 'das'] as const;

	// The round is fixed when the component mounts; later prop changes must not reshuffle it.
	const initial = untrack(() => ({ tasks: [...tasks], pool }));
	let queue = $state<Task[]>(initial.tasks);
	let repeated = $state<string[]>([]);
	let question = $state<Question | null>(
		initial.tasks[0] ? buildQuestion(initial.tasks[0].direction, initial.tasks[0].vocab, initial.pool, Math.random) : null
	);
	let selected = $state<number | null>(null);
	let text = $state('');
	let verdict = $state<Verdict | null>(null);
	let tts = $state<SpeechOutPort | null>(null);

	const task = $derived(queue[0]);
	const hasAnswer = $derived(question?.direction === 'produce' ? text.trim() !== '' : selected !== null);

	onMount(() => {
		tts = createDeviceTts(window);
		return () => tts?.stop();
	});

	const check = (event: SubmitEvent) => {
		event.preventDefault();
		if (!question || !task || verdict || !hasAnswer) return;
		verdict =
			question.direction === 'produce'
				? gradeProduce(text, question.vocab)
				: question.direction === 'genus'
					? articles[selected ?? -1] === question.vocab.article
						? 'correct'
						: 'wrong'
					: selected === question.answer
						? 'correct'
						: 'wrong';
		if (!repeated.includes(task.cardId)) onanswer?.(task, verdict !== 'wrong');
	};

	const next = () => {
		if (!task) return;
		tts?.stop();
		const wrong = verdict === 'wrong';
		if (wrong && !repeated.includes(task.cardId)) repeated = [...repeated, task.cardId];
		// A wrong card comes back at the end of the same round until it is right.
		queue = wrong ? [...queue.slice(1), task] : queue.slice(1);
		question = queue[0] ? buildQuestion(queue[0].direction, queue[0].vocab, pool, Math.random) : null;
		selected = null;
		text = '';
		verdict = null;
	};
</script>

{#if !task || !question}
	<section class="space-y-6 pt-10 text-center" data-testid="cards-done">
		<h1 class="text-3xl font-bold">{m.review_done()}</h1>
		<a href={backHref} class="block text-stone-700 underline">{backLabel}</a>
	</section>
{:else}
	<form class="space-y-5" onsubmit={check}>
		<p class="text-sm text-stone-600">{m.cards_left({ count: queue.length })}</p>

		{#if question.direction === 'recognize'}
			<p class="font-semibold">{m.q_meaning()}</p>
			<div class="flex items-center gap-3">
				<p class="text-2xl font-bold" lang="de" data-testid="card-word">{fullForm(question.vocab)}</p>
				<button type="button" class="rounded-full bg-stone-200 px-3 py-1" onclick={() => tts?.speak(fullForm(question?.vocab ?? task.vocab))}>🔊</button>
			</div>
			<fieldset class="space-y-2" disabled={verdict !== null}>
				{#each question.options as option, i (option.id)}
					<label
						class="flex items-center gap-3 rounded-xl border bg-white px-4 py-3 text-lg {verdict && i === question.answer
							? 'border-green-600 bg-green-50'
							: verdict && i === selected
								? 'border-red-600 bg-red-50'
								: 'border-stone-300'}"
					>
						<input type="radio" name="option" value={i} bind:group={selected} data-correct={i === question.answer} />
						<span>{meaning(option)}</span>
					</label>
				{/each}
			</fieldset>
		{:else if question.direction === 'produce'}
			<p class="font-semibold">{m.q_produce()}</p>
			<p class="text-2xl font-bold">{meaning(question.vocab)}</p>
			{#if question.vocab.article}<p class="text-sm text-stone-600">{m.article_hint()}</p>{/if}
			<input
				data-testid="card-input"
				class="w-full rounded-xl text-lg"
				bind:value={text}
				placeholder={m.answer_placeholder()}
				disabled={verdict !== null}
				lang="de"
				autocomplete="off"
				autocapitalize="off"
				autocorrect="off"
				spellcheck="false"
			/>
		{:else}
			<!-- R-W7: no audio before the answer, it would give the article away. -->
			<p class="font-semibold">{m.q_genus()}</p>
			<p class="text-2xl font-bold" lang="de">… {question.vocab.lemma}</p>
			<fieldset class="grid grid-cols-3 gap-2" disabled={verdict !== null}>
				{#each articles as article, i (article)}
					<label
						class="rounded-xl border px-2 py-3 text-center text-lg {selected === i ? 'border-red-700 bg-red-50 font-semibold' : 'border-stone-300 bg-white'}"
					>
						<input type="radio" class="sr-only" name="article" value={i} bind:group={selected} />
						{article}
					</label>
				{/each}
			</fieldset>
		{/if}

		{#if verdict}
			<div
				data-testid="card-feedback"
				data-verdict={verdict}
				role="status"
				class="space-y-2 rounded-xl border p-4 {verdict === 'correct'
					? 'border-green-600 bg-green-50'
					: verdict === 'near'
						? 'border-amber-500 bg-amber-50'
						: 'border-red-600 bg-red-50'}"
			>
				<p class="text-lg font-bold">
					{verdict === 'correct' ? m.verdict_correct() : verdict === 'near' ? m.verdict_near() : m.verdict_wrong()}
				</p>
				<p class="flex items-center gap-3 text-lg">
					<span lang="de" class="font-semibold">{fullForm(question.vocab)}</span>
					<span>– {meaning(question.vocab)}</span>
					<button type="button" class="rounded-full bg-stone-200 px-3 py-1" onclick={() => tts?.speak(fullForm(question?.vocab ?? task.vocab))}>🔊</button>
				</p>
			</div>
			<button type="button" data-testid="card-next" class="w-full rounded-xl bg-red-700 px-4 py-4 text-lg font-semibold text-white" onclick={next}>
				{m.next()}
			</button>
		{:else}
			<button data-testid="card-check" class="w-full rounded-xl bg-red-700 px-4 py-4 text-lg font-semibold text-white disabled:opacity-40" disabled={!hasAnswer}>
				{m.check()}
			</button>
		{/if}
	</form>
{/if}
