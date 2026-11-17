<script lang="ts">
	import { ChevronLeft, ChevronRight } from '@lucide/svelte';
	import { practiceKinds } from '#lib/skills.ts';
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
		<ChevronLeft size={18} strokeWidth={2.5} />{m.free_practice()}
	</button>
{:else if round}
	{#key roundNo}
		<Runner items={round} {tlMachine} backHref={resolve('/practice')} backLabel={m.free_practice()} onback={() => (round = null)} />
	{/key}
	<button type="button" class="backlink mt-6" onclick={() => (round = null)}>
		<ChevronLeft size={18} strokeWidth={2.5} />{m.free_practice()}
	</button>
{:else}
	<section class="space-y-4 pt-4">
		<h1 class="h1">{m.free_practice()}</h1>
		<p class="text-muted">{m.free_practice_intro()}</p>
		<ul class="list">
			<li>
				<button type="button" data-testid="practice-woerter" class="list-row" onclick={startWords}>
					<span class="grid h-10 w-10 shrink-0 place-items-center rounded-xl {practiceKinds.woerter.tile}"><practiceKinds.woerter.icon size={20} strokeWidth={2.25} /></span>
					<span class="tile-title flex-1">{m.skill_woerter()}</span>
					<ChevronRight size={18} class="text-muted" />
				</button>
			</li>
			{#each filters as filter (filter)}
				{@const kind = practiceKinds[filter]}
				<li>
					<button type="button" data-testid="practice-{filter}" class="list-row" onclick={() => start(filter)}>
						<span class="grid h-10 w-10 shrink-0 place-items-center rounded-xl {kind.tile}"><kind.icon size={20} strokeWidth={2.25} /></span>
						<span class="flex-1">
							<span class="tile-title">{label[filter]()}</span>
							<span class="tile-sub">{m.tasks_available({ count: items.filter((i) => matchesFilter(i, filter)).length })}</span>
						</span>
						<ChevronRight size={18} class="text-muted" />
					</button>
				</li>
			{/each}
		</ul>
	</section>
{/if}
