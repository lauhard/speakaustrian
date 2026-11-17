<script lang="ts">
	import { onMount } from 'svelte';
	import InstallButton from '#lib/components/InstallButton.svelte';
	import { resolve } from '$app/paths';
	import { getLocale, locales, setLocale } from '#lib/paraglide/runtime.js';
	import { m } from '#lib/paraglide/messages.js';
	import { createDeviceTts } from '#lib/adapters/web/device-tts.ts';
	import { game } from '#lib/game.svelte.ts';
	import { settings, ttsRate } from '#lib/settings.svelte.ts';
	import type { SpeechOutPort } from '#lib/ports/speech-out.ts';

	const rates = [
		{ value: 0.6, label: m.tts_slow },
		{ value: 0.75, label: m.tts_normal },
		{ value: 0.95, label: m.tts_fast }
	];
	const names: Record<string, string> = { de: 'Deutsch', en: 'English', tl: 'Tagalog' };
	let tts: SpeechOutPort | null = null;
	let armed = $state(false);

	onMount(() => {
		game.init();
		tts = createDeviceTts(window, ttsRate);
		return () => tts?.stop();
	});

	// Two taps instead of confirm(): a stray tap never deletes progress.
	const reset = () => {
		if (!armed) return (armed = true);
		game.reset();
		armed = false;
	};
</script>

<a href={resolve('/')} class="backlink">‹ {m.course()}</a>
<section class="space-y-4 pt-4">
	<h1 class="h1">⚙️ {m.settings()}</h1>

	<label class="card flex cursor-pointer items-start gap-3">
		<input type="checkbox" class="mt-1 h-5 w-5 accent-brand" data-testid="setting-unlock" checked={settings.value.unlockAll} onchange={(e) => settings.set('unlockAll', e.currentTarget.checked)} />
		<span>
			<span class="block font-extrabold">🔓 {m.settings_unlock()}</span>
			<span class="block text-sm text-muted">{m.settings_unlock_note()}</span>
		</span>
	</label>

	<div class="card space-y-3">
		<p class="font-extrabold">🔊 {m.settings_tts()}</p>
		<div class="grid grid-cols-3 gap-2">
			{#each rates as r (r.value)}
				<button type="button" class="option justify-center {settings.value.ttsRate === r.value ? '!border-brand !bg-brand-soft' : ''}" aria-pressed={settings.value.ttsRate === r.value} onclick={() => settings.set('ttsRate', r.value)}>{r.label()}</button>
			{/each}
		</div>
		<button type="button" class="btn-secondary" onclick={() => tts?.speak('Grüß Gott! Das kostet drei Euro fünfzig.')}>▶ {m.settings_test_voice()}</button>
	</div>

	<div class="card space-y-3">
		<p class="font-extrabold">🌐 {m.settings_language()}</p>
		<div class="grid grid-cols-3 gap-2">
			{#each locales as locale (locale)}
				<button type="button" class="option justify-center {locale === getLocale() ? '!border-brand !bg-brand-soft' : ''}" aria-pressed={locale === getLocale()} onclick={() => setLocale(locale)}>{names[locale] ?? locale}</button>
			{/each}
		</div>
		<label class="flex cursor-pointer items-center gap-3 text-sm">
			<input type="checkbox" class="h-5 w-5 accent-brand" checked={settings.value.showTranslations} onchange={(e) => settings.set('showTranslations', e.currentTarget.checked)} />
			{m.settings_translations()}
		</label>
	</div>

	<InstallButton />

	<div class="card space-y-2">
		<button type="button" class={armed ? 'btn-primary' : 'btn-secondary'} data-testid="setting-reset" onclick={reset}>🗑 {armed ? m.settings_reset_confirm() : m.settings_reset()}</button>
		<p class="text-sm text-muted">{m.settings_reset_note()}</p>
	</div>
</section>
