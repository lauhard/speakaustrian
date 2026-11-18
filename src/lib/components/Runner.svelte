<script lang="ts">
	import { flames } from '#lib/flames.svelte.ts';
	import BankPoints from './BankPoints.svelte';
	import FlamePot from './FlamePot.svelte';
	import { fly } from 'svelte/transition';
	import { cubicOut } from 'svelte/easing';
	import { AudioLines, Check, CircleCheck, CircleX, Flame, Star, Volume2, X } from '@lucide/svelte';
	import { STARS } from '#lib/lesson-scores.svelte.ts';
	import { skills } from '#lib/skills.ts';
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
		// Lessons (K1): decides pass/fail of the round; without it the result shows no verdict.
		passCheck?: (correct: number, total: number) => boolean;
		// K8: the running course chapter, where answers earn flames; null in free practice, demo and free mode.
		flameChapter?: string | null;
	};
	let { items, tlMachine, backHref, backLabel, onback, onfinish, bare = false, examMode = false, top, onchecked, nextLabel, passCheck, flameChapter = null }: Props = $props();

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
	let misses = $state<{ id: string; text: string; expected: string }[]>([]);
	let finished = $state(false);

	const item = $derived(items[index]);
	const sk = $derived(skills[item.skill]);
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
		flames.record(flameChapter, passes(grade.verdict));
		if (passes(grade.verdict)) {
			correctCount += 1;
		} else {
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
		misses = [];
		shortText = '';
		grade = null;
		correctCount = 0;
		finished = false;
	};

	// Called directly from the tap so the browser accepts it as a user gesture.
	let playing = $state(false);
	const listen = async (text: string) => {
		if (!tts) return;
		playing = true;
		const status = await tts.speak(text);
		playing = false;
		ttsFailed = !status.ok;
	};

	const verdictText = (g: Grade) =>
		g.verdict === 'correct' ? m.verdict_correct() : g.verdict === 'near' ? m.verdict_near() : m.verdict_wrong();

	const gapClass = (id: string) =>
		!grade ? '' : grade.parts[id] === 'correct' ? 'is-right' : grade.parts[id] === 'near' ? 'is-near' : 'is-wrong';
	const percent = $derived(Math.round((correctCount / items.length) * 100));
	const failed = $derived(passCheck ? !passCheck(correctCount, items.length) : false);
	const heading = $derived(
		failed ? m.result_failed() : percent >= 90 ? m.result_great() : percent >= 70 ? m.result_good() : passCheck ? m.result_passed() : ''
	);

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
	<section class="flex min-h-[calc(100dvh-10rem)] flex-col items-center justify-center gap-5 py-6 text-center" data-testid="result" data-passed={!failed}>
		{#if flameChapter}<BankPoints shield />{/if}
		<div
			class="flex h-32 w-32 items-center justify-center rounded-full border-8 bg-white leading-none font-black {failed ? 'border-bad text-bad' : percent >= 80 ? 'border-ok text-ok' : 'border-warn text-warn'}"
		>
			<span class="text-3xl">{percent}%</span>
		</div>
		{#if !failed}
			<p class="pop flex items-center justify-center gap-1" aria-hidden="true">{#each STARS as min (min)}<Star size={40} strokeWidth={2} class={percent >= min ? 'fill-amber-400 text-amber-500' : 'text-line'} />{/each}</p>
		{/if}
		{#if heading}<h1 class="text-3xl font-black {failed ? 'text-bad' : ''}" data-testid="result-heading">{heading}</h1>{/if}
		<p class="text-xl font-semibold">{m.result_score({ correct: correctCount, total: items.length })}</p>
		{#if misses.length > 0}
			<div class="card w-full space-y-2 text-left" data-testid="misses">
				<p class="font-extrabold">{m.result_misses()}</p>
				<ul class="space-y-2 text-sm">
					{#each misses as miss (miss.id)}
						<li class="border-t border-line pt-2">
							<span class="block text-muted" lang="de">{miss.text.replaceAll(/\{\{\d+\}\}/g, '…')}</span>
							<span class="text-xs font-bold text-muted">{m.result_solution()}</span> <span class="font-bold" lang="de">{miss.expected}</span>
						</li>
					{/each}
				</ul>
			</div>
		{/if}
		<div class="flex w-full flex-col gap-3">
			{#if failed}
				<button type="button" class="btn-primary" data-testid="again" onclick={restart}>{m.again()}</button>
				<a href={backHref} onclick={back} data-testid="back" class="btn-secondary">{backLabel}</a>
			{:else}
				<button type="button" class="btn-secondary" data-testid="again" onclick={restart}>{m.again()}</button>
				<a href={backHref} onclick={back} data-testid="back" class="btn-primary">{backLabel}</a>
			{/if}
		</div>
	</section>
{:else}
	<form class="space-y-5" data-item={item.id} onsubmit={check}>
		{#if top}{@render top()}{/if}
		{#if !bare}
		<div class="flex items-center gap-3">
			<a href={backHref} onclick={back} class="burger shrink-0" aria-label={backLabel}><X size={20} strokeWidth={2.5} /></a>
			<div class="bar !h-2.5 flex-1" role="progressbar" aria-valuemin="0" aria-valuemax={items.length} aria-valuenow={index + (grade ? 1 : 0)}>
				<span style="width: {((index + (grade ? 1 : 0)) / items.length) * 100}%"></span>
			</div>
			<p class="flex shrink-0 items-center gap-2 text-sm font-extrabold">
				{#if flameChapter}<FlamePot />{/if}
				<span class="flex items-center gap-0.5 text-ok" data-testid="run-correct"><Check size={16} strokeWidth={3} />{correctCount}</span>
				<span class="text-muted" aria-label={m.task_count({ current: index + 1, total: items.length })}>{index + 1}/{items.length}</span>
			</p>
		</div>
		{/if}

		<div class="card space-y-2 !p-5">
			<p class="flex items-center gap-2 text-xs font-extrabold tracking-wider uppercase">
				<span class="grid h-7 w-7 place-items-center rounded-lg {sk.tile}"><sk.icon size={16} strokeWidth={2.5} /></span>
				<span class="text-muted">{sk.label()}</span>
			</p>
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
			<button type="button" data-testid="listen" class="listen" onclick={() => listen(item.audioText ?? '')}>
				<span class="listen-btn {sk.solid}" class:is-playing={playing}>
					{#if playing}<AudioLines size={26} strokeWidth={2.5} />{:else}<Volume2 size={26} strokeWidth={2.5} />{/if}
				</span>
				<span class="text-left">
					<span class="block font-extrabold">{playing ? m.playing() : m.listen()}</span>
				</span>
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
						<input type="radio" name="choice" class="absolute inset-0 cursor-pointer opacity-0" value={i} bind:group={selected} />
						<span class="letter" aria-hidden="true">{'ABCDEFGH'[i]}</span>
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
			<p class="cloze" lang="de">
				{#each segments as segment, i (i)}
					{#if segment.kind === 'text'}{segment.value}{:else}
						<input
							data-testid="gap-{segment.id}"
							class="gap {gapClass(segment.id)}"
							style:width="{Math.max(4, item.type === 'cloze' ? Math.max(...item.gaps[segment.id].accept.map((a) => a.length)) : 6, (gaps[segment.id] ?? '').length) + 2}ch"
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
			<div class="sheet" data-verdict={grade.verdict} in:fly={{ y: 60, duration: 260, easing: cubicOut }}>
			<div
				data-testid="feedback"
				data-verdict={grade.verdict}
				role="status"
				class="max-h-[45dvh] space-y-2 overflow-y-auto {grade.verdict === 'wrong' ? 'shake' : ''}"
			>
				<p class="sheet-title">{#if grade.verdict === 'wrong'}<CircleX size={24} strokeWidth={2.5} />{:else}<CircleCheck size={24} strokeWidth={2.5} />{/if}{verdictText(grade)}</p>
				{#if grade.verdict !== 'correct'}
					<p lang="de">{m.expected({ answer: Object.values(grade.expected).join(' · ') })}</p>
				{/if}
				{#if item.audioOnly && item.audioText}<p lang="de">{m.you_hear({ text: item.audioText })}</p>{/if}
				{@render help(item.explanation)}
				{#if helpLocale === 'tl' && tlMachine}
					<p class="text-xs text-muted">{m.tl_machine_note()}</p>
				{/if}
			</div>
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
