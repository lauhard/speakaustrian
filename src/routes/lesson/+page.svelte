<script lang="ts">
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { resolve } from '$app/paths';
	import { getLocale } from '#lib/paraglide/runtime.js';
	import { m } from '#lib/paraglide/messages.js';
	import { createDeviceTts } from '#lib/adapters/web/device-tts.ts';
	import { demoLesson } from '#lib/content/demo.ts';
	import type { Localized } from '#lib/core/content/schema.ts';
	import { gradeItem, parseCloze, passes, type Grade, type Response } from '#lib/core/grading.ts';
	import type { SpeechOutPort } from '#lib/ports/speech-out.ts';
	import type { Profile } from '#lib/ports/storage.ts';
	import { storage, withResult } from '#lib/profile.ts';

	const lesson = demoLesson;
	const helpLocale: 'de' | 'en' | 'tl' = getLocale();

	let profile = $state<Profile | null>(null);
	let tts = $state<SpeechOutPort | null>(null);
	let ttsFailed = $state(false);

	let index = $state(0);
	let selected = $state<number | null>(null);
	let gaps = $state<Record<string, string>>({});
	let shortText = $state('');
	let grade = $state<Grade | null>(null);
	let correctCount = $state(0);
	let finished = $state(false);

	const item = $derived(lesson.items[index]);
	const segments = $derived(item.type === 'cloze' ? parseCloze(item.text) : []);
	const isLast = $derived(index === lesson.items.length - 1);

	const response = $derived.by((): Response | null => {
		if (item.type === 'choice') return selected === null ? null : { type: 'choice', selected };
		if (item.type === 'short') return shortText.trim() === '' ? null : { type: 'short', text: shortText };
		return Object.keys(item.gaps).every((id) => (gaps[id] ?? '').trim() !== '') ? { type: 'cloze', gaps } : null;
	});

	onMount(() => {
		profile = storage()?.load() ?? null;
		if (!profile) {
			goto(resolve('/'));
			return;
		}
		tts = createDeviceTts(window);
		return () => tts?.stop();
	});

	const check = (event: SubmitEvent) => {
		event.preventDefault();
		if (!response || grade) return;
		grade = gradeItem(item, response);
		// Practice mode: a near miss counts, with a spelling hint.
		if (passes(grade.verdict, { nearCounts: true })) correctCount += 1;
	};

	const next = () => {
		tts?.stop();
		if (isLast) {
			finished = true;
			if (profile) {
				profile = withResult(profile, lesson.id, correctCount, lesson.items.length, new Date());
				storage()?.save(profile);
			}
			return;
		}
		index += 1;
		selected = null;
		gaps = {};
		shortText = '';
		grade = null;
		ttsFailed = false;
	};

	const restart = () => {
		index = 0;
		selected = null;
		gaps = {};
		shortText = '';
		grade = null;
		correctCount = 0;
		finished = false;
	};

	// Called directly from the tap so the browser accepts it as a user gesture.
	const listen = async (text: string) => {
		if (!tts) return;
		const status = await tts.speak(text);
		ttsFailed = !status.ok;
	};

	const verdictText = (g: Grade) =>
		g.verdict === 'correct' ? m.verdict_correct() : g.verdict === 'near' ? m.verdict_near() : m.verdict_wrong();

	const gapClass = (id: string) =>
		!grade
			? 'border-stone-400'
			: grade.parts[id] === 'correct'
				? 'border-green-600 bg-green-50'
				: grade.parts[id] === 'near'
					? 'border-amber-500 bg-amber-50'
					: 'border-red-600 bg-red-50';
</script>

{#snippet help(text: Localized)}
	<p class="font-semibold">{text.de}</p>
	{#if helpLocale !== 'de'}
		<p class="text-sm text-stone-600" lang={helpLocale}>{text[helpLocale]}</p>
	{/if}
{/snippet}

{#if finished}
	<section class="space-y-6 pt-10 text-center" data-testid="result">
		<h1 class="text-3xl font-bold">{m.result_title()}</h1>
		<p class="text-xl">{m.result_score({ correct: correctCount, total: lesson.items.length })}</p>
		<button type="button" class="w-full rounded-xl bg-red-700 px-4 py-4 text-lg font-semibold text-white" onclick={restart}>
			{m.again()}
		</button>
		<a href={resolve('/')} class="block text-stone-700 underline">{m.home()}</a>
	</section>
{:else if profile}
	<form class="space-y-5" onsubmit={check}>
		<div>
			<p class="text-sm text-stone-600">{m.task_count({ current: index + 1, total: lesson.items.length })}</p>
			<progress class="h-2 w-full" max={lesson.items.length} value={index + (grade ? 1 : 0)}></progress>
		</div>

		<div>{@render help(item.instruction)}</div>

		{#if item.image}
			<img
				data-testid="item-image"
				src={item.image.src}
				alt={item.image.alt[helpLocale]}
				class="w-full rounded-xl border border-stone-200"
				width="400"
				height="260"
			/>
		{/if}

		{#if item.audioText}
			<button
				type="button"
				class="rounded-full bg-stone-200 px-4 py-2 text-sm font-medium"
				onclick={() => listen(item.audioText ?? '')}
			>
				🔊 {m.listen()}
			</button>
			{#if ttsFailed}<p class="text-sm text-amber-700" role="status">{m.tts_failed()}</p>{/if}
		{/if}

		{#if item.type === 'choice'}
			<fieldset class="space-y-2" disabled={grade !== null}>
				<legend class="mb-2 text-lg" lang="de">{item.prompt}</legend>
				{#each item.options as option, i (option)}
					<label
						class="flex items-center gap-3 rounded-xl border bg-white px-4 py-3 text-lg {grade && i === item.answer
							? 'border-green-600 bg-green-50'
							: grade && i === selected
								? 'border-red-600 bg-red-50'
								: 'border-stone-300'}"
					>
						<input type="radio" name="choice" value={i} bind:group={selected} />
						<span lang="de">{option}</span>
					</label>
				{/each}
			</fieldset>
		{:else if item.type === 'short'}
			<label class="block space-y-2">
				<span class="text-lg" lang="de">{item.prompt}</span>
				<input
					data-testid="short-input"
					class="w-full rounded-xl text-lg {gapClass('answer')}"
					bind:value={shortText}
					placeholder={m.answer_placeholder()}
					disabled={grade !== null}
					lang="de"
					autocomplete="off"
					autocapitalize="off"
					autocorrect="off"
					spellcheck="false"
				/>
			</label>
		{:else}
			<p class="text-lg leading-[3rem]" lang="de">
				{#each segments as segment, i (i)}
					{#if segment.kind === 'text'}{segment.value}{:else}
						<input
							data-testid="gap-{segment.id}"
							class="mx-1 inline-block w-32 rounded-lg px-2 py-1 text-lg {gapClass(segment.id)}"
							bind:value={gaps[segment.id]}
							aria-label="Lücke {segment.id}"
							disabled={grade !== null}
							autocomplete="off"
							autocapitalize="off"
							autocorrect="off"
							spellcheck="false"
						/>
					{/if}
				{/each}
			</p>
		{/if}

		{#if grade}
			<div
				data-testid="feedback"
				data-verdict={grade.verdict}
				role="status"
				class="space-y-2 rounded-xl border p-4 {grade.verdict === 'correct'
					? 'border-green-600 bg-green-50'
					: grade.verdict === 'near'
						? 'border-amber-500 bg-amber-50'
						: 'border-red-600 bg-red-50'}"
			>
				<p class="text-lg font-bold">{verdictText(grade)}</p>
				{#if grade.verdict !== 'correct'}
					<p lang="de">{m.expected({ answer: Object.values(grade.expected).join(' · ') })}</p>
				{/if}
				{@render help(item.explanation)}
				{#if helpLocale === 'tl' && lesson.tlReviewStatus === 'machine'}
					<p class="text-xs text-stone-500">{m.tl_machine_note()}</p>
				{/if}
			</div>
			<button
				type="button"
				data-testid="next"
				class="w-full rounded-xl bg-red-700 px-4 py-4 text-lg font-semibold text-white"
				onclick={next}
			>
				{isLast ? m.finish() : m.next()}
			</button>
		{:else}
			<button
				data-testid="check"
				class="w-full rounded-xl bg-red-700 px-4 py-4 text-lg font-semibold text-white disabled:opacity-40"
				disabled={!response}
			>
				{m.check()}
			</button>
		{/if}
	</form>
{/if}
