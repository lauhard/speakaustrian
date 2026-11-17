<script lang="ts">
	import { Check, CircleCheck, CircleX, Flame, Star, Volume2, X } from '@lucide/svelte';
	import { ttsRate } from '#lib/settings.svelte.ts';
	import { onMount, type Snippet } from 'svelte';
	import { getLocale } from '#lib/paraglide/runtime.js';
	import { m } from '#lib/paraglide/messages.js';
	import { createDeviceTts } from '#lib/adapters/web/device-tts.ts';
	import type { Item, Localized } from '#lib/core/content/schema.ts';
	import { gradeItem, parseCloze, passes, type Grade, type Response } from '#lib/core/grading.ts';
	import type { SpeechOutPort } from '#lib/ports/speech-out.ts';

	type Props = {
		items: Item[];
		tlMachine: boolean;
		backHref: string;
		backLabel: string;
		// Set when "back" stays on the same page (free practice): called instead of following the link.
		onback?: () => void;
		onfinish?: (correct: number, total: number) => void;
		// Chapter flow (005c): the parent shows its own header and result, so the runner only asks and grades.
		bare?: boolean;
		// Exam mode: the instruction is German only, the translation is behind a button (04 V5); feedback keeps it.
		examMode?: boolean;
		// Extra header, e.g. phase label and lives.
		top?: Snippet;
		// Called when an answer is checked (before "next"), so the parent can show lives and similar.
		onchecked?: (item: Item, correct: boolean) => void;
		nextLabel?: string;
	};
	let { items, tlMachine, backHref, backLabel, onback, onfinish, bare = false, examMode = false, top, onchecked, nextLabel }: Props = $props();

	const helpLocale: 'de' | 'en' | 'tl' = getLocale();

	let tts = $state<SpeechOutPort | null>(null);
	let ttsFailed = $state(false);

	let index = $state(0);
	let selected = $state<number | null>(null);
	let gaps = $state<Record<string, string>>({});
	let shortText = $state('');
	let grade = $state<Grade | null>(null);
	let correctCount = $state(0);
	// Current run of correct answers and the misses of this round, for the header and the result screen.
	let streak = $state(0);
	let misses = $state<{ id: string; text: string; expected: string }[]>([]);
	let finished = $state(false);

	const item = $derived(items[index]);
	const segments = $derived(item.type === 'cloze' ? parseCloze(item.text) : []);
	const isLast = $derived(index === items.length - 1);

	const response = $derived.by((): Response | null => {
		if (item.type === 'choice') return selected === null ? null : { type: 'choice', selected };
		if (item.type === 'short') return shortText.trim() === '' ? null : { type: 'short', text: shortText };
		return Object.keys(item.gaps).every((id) => (gaps[id] ?? '').trim() !== '') ? { type: 'cloze', gaps } : null;
	});

	onMount(() => {
		tts = createDeviceTts(window, ttsRate);
		return () => tts?.stop();
	});

	const check = (event: SubmitEvent) => {
		event.preventDefault();
		if (!response || grade) return;
		grade = gradeItem(item, response);
		if (passes(grade.verdict)) {
			correctCount += 1;
			streak += 1;
		} else {
			streak = 0;
			misses = [...misses, { id: item.id, text: item.type === 'cloze' ? item.text : (item.prompt ?? item.audioText ?? ''), expected: Object.values(grade.expected).join(' · ') }];
		}
		onchecked?.(item, passes(grade.verdict));
	};

	const next = () => {
		tts?.stop();
		if (isLast) {
			finished = !bare;
			onfinish?.(correctCount, items.length);
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
		streak = 0;
		misses = [];
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
		!grade ? '' : grade.parts[id] === 'correct' ? 'is-right' : grade.parts[id] === 'near' ? 'is-near' : 'is-wrong';
	const percent = $derived(Math.round((correctCount / items.length) * 100));

	const back = (event: MouseEvent) => {
		if (!onback) return;
		event.preventDefault();
		onback();
	};
</script>

{#snippet help(text: Localized)}
	<p class="font-bold">{text.de}</p>
	{#if helpLocale !== 'de'}
		<p class="text-sm text-muted" lang={helpLocale}>{text[helpLocale]}</p>
	{/if}
{/snippet}

{#if finished && !bare}
	<section class="space-y-6 pt-10 text-center" data-testid="result">
		<div class="mx-auto flex h-32 w-32 items-center justify-center rounded-full border-8 {percent >= 80 ? 'border-ok text-ok' : 'border-warn text-warn'} bg-white text-3xl font-black">
			{percent}%
		</div>
		<p class="pop flex justify-center gap-1" aria-hidden="true">{#each [50, 70, 90] as min (min)}<Star size={40} strokeWidth={2} class={percent >= min ? 'fill-amber-400 text-amber-500' : 'text-line'} />{/each}</p>
		<h1 class="text-3xl font-black">{percent >= 90 ? m.result_great() : percent >= 70 ? m.result_good() : m.result_title()}</h1>
		<p class="text-xl font-semibold">{m.result_score({ correct: correctCount, total: items.length })}</p>
		{#if misses.length > 0}
			<div class="card space-y-2 text-left" data-testid="misses">
				<p class="font-extrabold">{m.result_misses()}</p>
				<ul class="space-y-2 text-sm">
					{#each misses as miss (miss.id)}
						<li class="border-t border-line pt-2"><span class="block text-muted" lang="de">{miss.text.replaceAll(/\{\{\d+\}\}/g, '…')}</span><span class="font-bold text-ok" lang="de">✓ {miss.expected}</span></li>
					{/each}
				</ul>
			</div>
		{/if}
		<button type="button" class="btn-secondary" onclick={restart}>
			{m.again()}
		</button>
		<a href={backHref} onclick={back} data-testid="back" class="btn-primary">{backLabel}</a>
	</section>
{:else}
	<form class="space-y-5" data-item={item.id} onsubmit={check}>
		{#if top}{@render top()}{/if}
		{#if !bare}
		<div>
			<div class="mb-2 flex items-center justify-between">
				<a href={backHref} onclick={back} class="burger" aria-label={backLabel}><X size={20} strokeWidth={2.5} /></a>
				<p class="flex items-center gap-3 text-sm font-bold text-muted">
					<span class="flex items-center gap-1 text-ok" data-testid="run-correct"><Check size={16} strokeWidth={3} />{correctCount}</span>
					{#if streak >= 3}<span class="pop flex items-center gap-1 text-orange-500" data-testid="streak"><Flame size={16} strokeWidth={2.5} class="fill-orange-400" />{streak}</span>{/if}
					<span>{m.task_count({ current: index + 1, total: items.length })}</span>
				</p>
			</div>
			<div class="bar" role="progressbar" aria-valuemin="0" aria-valuemax={items.length} aria-valuenow={index + (grade ? 1 : 0)}>
				<span style="width: {((index + (grade ? 1 : 0)) / items.length) * 100}%"></span>
			</div>
		</div>
		{/if}

		<div class="card">
			{#if examMode}
				<p class="font-bold">{item.instruction.de}</p>
				{#if helpLocale !== 'de' && !grade}
					<details class="mt-2 text-sm text-muted">
						<summary>{m.flow_show_translation()}</summary>
						<p lang={helpLocale}>{item.instruction[helpLocale]}</p>
					</details>
				{/if}
			{:else}
				{@render help(item.instruction)}
			{/if}
		</div>

		{#if item.image}
			<img
				data-testid="item-image"
				src={item.image.src}
				alt={item.image.alt[helpLocale]}
				class="w-full rounded-2xl border border-line shadow-sm"
				width="400"
				height="260"
			/>
		{/if}

		{#if item.audioText}
			<button
				type="button"
				data-testid="listen"
				class={item.audioOnly ? 'btn-secondary' : 'btn-ghost'}
				onclick={() => listen(item.audioText ?? '')}
			>
				<Volume2 size={20} strokeWidth={2.25} />{m.listen()}
			</button>
			{#if ttsFailed}
				<p class="text-sm text-amber-700" role="status">{m.tts_failed()}</p>
				<!-- Transcript fallback so a listening task stays solvable without speech output. -->
				{#if item.audioOnly}<p class="text-lg" lang="de" data-testid="transcript">{item.audioText}</p>{/if}
			{/if}
		{/if}

		{#if item.type === 'choice'}
			<fieldset class="space-y-2" disabled={grade !== null}>
				{#if item.prompt && !item.audioOnly}<legend class="mb-3 text-xl font-bold" lang="de">{item.prompt}</legend>{/if}
				{#each item.options as option, i (option)}
					<label
						class="option {grade && i === item.answer ? 'is-right' : grade && i === selected ? 'is-wrong' : ''}"
					>
						<input type="radio" name="choice" value={i} bind:group={selected} />
						<span lang="de">{option}</span>
					</label>
				{/each}
			</fieldset>
		{:else if item.type === 'short'}
			<label class="block space-y-2">
				<span class="text-xl font-bold" lang="de">{item.prompt}</span>
				<input
					data-testid="short-input"
					class="field w-full {gapClass('answer')}"
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
			<p class="text-xl leading-[3.4rem] font-semibold" lang="de">
				{#each segments as segment, i (i)}
					{#if segment.kind === 'text'}{segment.value}{:else}
						<input
							data-testid="gap-{segment.id}"
							class="field mx-1 inline-block w-36 px-2 py-1 {gapClass(segment.id)}"
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
				class="feedback pop {grade.verdict === 'wrong' ? 'shake' : ''}"
			>
				<p class="flex items-center gap-2 text-xl font-black">{#if grade.verdict === 'wrong'}<CircleX size={24} strokeWidth={2.5} />{:else}<CircleCheck size={24} strokeWidth={2.5} />{/if}{verdictText(grade)}</p>
				{#if grade.verdict !== 'correct'}
					<p lang="de">{m.expected({ answer: Object.values(grade.expected).join(' · ') })}</p>
				{/if}
				{#if item.audioOnly && item.audioText}<p lang="de">{m.you_hear({ text: item.audioText })}</p>{/if}
				{@render help(item.explanation)}
				{#if helpLocale === 'tl' && tlMachine}
					<p class="text-xs text-muted">{m.tl_machine_note()}</p>
				{/if}
			</div>
			<div class="actionbar">
			<button
				type="button"
				data-testid="next"
				class="btn-primary"
				onclick={next}
			>
				{nextLabel ?? (isLast ? m.finish() : m.next())}
			</button>
			</div>
		{:else}
			<div class="actionbar">
			<button
				data-testid="check"
				class="btn-primary"
				disabled={!response}
			>
				{m.check()}
			</button>
			</div>
		{/if}
	</form>
{/if}
