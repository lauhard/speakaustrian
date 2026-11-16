<script lang="ts">
	import { resolve } from '$app/paths';
	import { m } from '#lib/paraglide/messages.js';
	import Runner from '#lib/components/Runner.svelte';
	import { allItems, availableFilters, chapters, matchesFilter, pickPractice, type PracticeFilter } from '#lib/content/index.ts';
	import type { Item } from '#lib/core/content/schema.ts';

	const ROUND = 8;
	// D22: items from all chapters that have content; nothing here counts for the course.
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
	let roundNo = $state(0);

	const start = (filter: PracticeFilter) => {
		round = pickPractice(items, filter, ROUND, Math.random);
		roundNo += 1;
	};
</script>

{#if round}
	{#key roundNo}
		<Runner items={round} {tlMachine} backHref={resolve('/practice')} backLabel={m.free_practice()} />
	{/key}
	<button type="button" class="mt-6 text-sm text-stone-600 underline" onclick={() => (round = null)}>
		← {m.free_practice()}
	</button>
{:else}
	<a href={resolve('/')} class="text-sm text-stone-600 underline">← {m.course()}</a>
	<section class="space-y-4 pt-4">
		<h1 class="text-2xl font-bold">{m.free_practice()}</h1>
		<p class="text-stone-700">{m.free_practice_intro()}</p>
		<ul class="space-y-2">
			{#each filters as filter (filter)}
				<li>
					<button
						type="button"
						data-testid="practice-{filter}"
						class="flex w-full items-center justify-between rounded-xl border border-stone-300 bg-white px-4 py-4 text-left text-lg font-semibold"
						onclick={() => start(filter)}
					>
						<span>{label[filter]()}</span>
						<span class="text-sm font-normal text-stone-500">
							{m.tasks_available({ count: items.filter((i) => matchesFilter(i, filter)).length })}
						</span>
					</button>
				</li>
			{/each}
		</ul>
	</section>
{/if}
