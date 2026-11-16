<script lang="ts">
	import { resolve } from '$app/paths';
	import { m } from '#lib/paraglide/messages.js';
	import { onMount } from 'svelte';
	import CardRunner, { type Task } from '#lib/components/CardRunner.svelte';
	import Runner from '#lib/components/Runner.svelte';
	import { allVocab } from '#lib/content/index.ts';
	import { game } from '#lib/game.svelte.ts';
	import { allItems, availableFilters, chapters, matchesFilter, pickPractice, type PracticeFilter } from '#lib/content/index.ts';
	import type { Item } from '#lib/core/content/schema.ts';

	const ROUND = 8;
	// D22: every task of every lesson and chapter, also of chapters that are still locked; nothing here counts for the course.
	const items = allItems();
	const filters = availableFilters(items);
	const tlMachine = chapters.some((c) => c.tlReviewStatus === 'machine');

	const label: Record<PracticeFilter, () => string> = {
		lesen: m.skill_lesen,
		hoeren: m.skill_hoeren,
		schreiben: m.skill_schreiben,
		sprechen: m.skill_sprechen,
		grammatikWortschatz: m.skill_grammatikWortschatz,
		werte: m.skill_werte,
		bild: m.skill_bild
	};

	let round = $state<Item[] | null>(null);
	let words = $state<Task[] | null>(null);

	onMount(() => game.init());

	// D22: all words of all chapters are available in free practice.
	const startWords = () => {
		const pool = allVocab();
		words = [...pool]
			.sort(() => Math.random() - 0.5)
			.slice(0, 10)
			.map((vocab) => {
				const directions = vocab.article ? (['recognize', 'produce', 'genus'] as const) : (['recognize', 'produce'] as const);
				return { cardId: vocab.id, direction: directions[Math.floor(Math.random() * directions.length)], vocab };
			});
		roundNo += 1;
	};
	let roundNo = $state(0);

	const start = (filter: PracticeFilter) => {
		round = pickPractice(items, filter, ROUND, Math.random);
		roundNo += 1;
	};
</script>

{#if words}
	{#key roundNo}
		<CardRunner tasks={words} pool={allVocab()} backHref={resolve('/practice')} backLabel={m.free_practice()} onback={() => (words = null)} />
	{/key}
	<button type="button" class="backlink mt-6" onclick={() => (words = null)}>
		‹ {m.free_practice()}
	</button>
{:else if round}
	{#key roundNo}
		<Runner items={round} {tlMachine} backHref={resolve('/practice')} backLabel={m.free_practice()} onback={() => (round = null)} />
	{/key}
	<button type="button" class="backlink mt-6" onclick={() => (round = null)}>
		‹ {m.free_practice()}
	</button>
{:else}
	<a href={resolve('/')} class="backlink">‹ {m.course()}</a>
	<section class="space-y-4 pt-4">
		<h1 class="h1">{m.free_practice()}</h1>
		<p class="text-muted">{m.free_practice_intro()}</p>
		<ul class="space-y-2">
			<li>
				<button
					type="button"
					data-testid="practice-woerter"
					class="card-link flex w-full items-center justify-between text-left text-lg font-extrabold"
					onclick={startWords}
				>
					<span>{m.skill_woerter()}</span>
				</button>
			</li>
			{#each filters as filter (filter)}
				<li>
					<button
						type="button"
						data-testid="practice-{filter}"
						class="card-link flex w-full items-center justify-between text-left text-lg font-extrabold"
						onclick={() => start(filter)}
					>
						<span>{label[filter]()}</span>
						<span class="chip">
							{m.tasks_available({ count: items.filter((i) => matchesFilter(i, filter)).length })}
						</span>
					</button>
				</li>
			{/each}
		</ul>
	</section>
{/if}
