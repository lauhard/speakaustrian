<script lang="ts">
	import { onMount } from 'svelte';
	import { Languages, LockOpen, Play, Subtitles, Trash2, Volume2 } from '@lucide/svelte';
	import InstallButton from '#lib/components/InstallButton.svelte';
	import { getLocale, locales, setLocale } from '#lib/paraglide/runtime.js';
	import { m } from '#lib/paraglide/messages.js';
	import { createDeviceTts } from '#lib/adapters/web/device-tts.ts';
	import { game, resetAll } from '#lib/game.svelte.ts';
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
		resetAll();
	};
</script>

<div class="space-y-6">
	<section>
		<h3 class="list-label">{m.set_group_learn()}</h3>
		<div class="list">
			<label class="list-row cursor-pointer">
				<span class="icon-tile"><LockOpen size={20} strokeWidth={2.25} /></span>
				<span class="flex-1">
					<span class="tile-title">{m.settings_unlock()}</span>
					<span class="tile-sub">{m.settings_unlock_note()}</span>
				</span>
				<input type="checkbox" class="switch" data-testid="setting-unlock" checked={settings.value.unlockAll} onchange={(e) => settings.set('unlockAll', e.currentTarget.checked)} />
			</label>
		</div>
	</section>

	<section>
		<h3 class="list-label">{m.set_group_audio()}</h3>
		<div class="list">
			<div class="list-row flex-col !items-stretch">
				<span class="flex items-center gap-3">
					<span class="icon-tile"><Volume2 size={20} strokeWidth={2.25} /></span>
					<span class="tile-title flex-1">{m.settings_tts()}</span>
				</span>
				<div class="seg">
					{#each rates as r (r.value)}
						<button type="button" aria-pressed={settings.value.ttsRate === r.value} onclick={() => settings.set('ttsRate', r.value)}>{r.label()}</button>
					{/each}
				</div>
			</div>
			<button type="button" class="list-row" onclick={() => tts?.speak('Grüß Gott! Das kostet drei Euro fünfzig.')}>
				<span class="icon-tile"><Play size={18} strokeWidth={2.5} class="fill-current" /></span>
				<span class="tile-title flex-1">{m.settings_test_voice()}</span>
			</button>
		</div>
	</section>

	<section>
		<h3 class="list-label">{m.set_group_lang()}</h3>
		<div class="list">
			<div class="list-row flex-col !items-stretch">
				<span class="flex items-center gap-3">
					<span class="icon-tile"><Languages size={20} strokeWidth={2.25} /></span>
					<span class="tile-title flex-1">{m.settings_language()}</span>
				</span>
				<div class="seg">
					{#each locales as locale (locale)}
						<button type="button" aria-pressed={locale === getLocale()} onclick={() => setLocale(locale)}>{names[locale] ?? locale}</button>
					{/each}
				</div>
			</div>
			<label class="list-row cursor-pointer">
				<span class="icon-tile"><Subtitles size={20} strokeWidth={2.25} /></span>
				<span class="tile-title flex-1">{m.settings_translations()}</span>
				<input type="checkbox" class="switch" checked={settings.value.showTranslations} onchange={(e) => settings.set('showTranslations', e.currentTarget.checked)} />
			</label>
		</div>
	</section>

	<InstallButton />

	<section>
		<h3 class="list-label">{m.set_group_data()}</h3>
		<div class="list">
			<button type="button" class="list-row {armed ? '!bg-bad-soft' : ''}" data-testid="setting-reset" onclick={reset}>
				<span class="icon-tile !bg-bad-soft !text-bad"><Trash2 size={20} strokeWidth={2.25} /></span>
				<span class="flex-1">
					<span class="tile-title text-bad">{armed ? m.settings_reset_confirm() : m.settings_reset()}</span>
					<span class="tile-sub">{m.settings_reset_note()}</span>
				</span>
			</button>
		</div>
		<p class="mt-3 px-1 text-center text-sm font-semibold text-muted">{m.local_note()}</p>
	</section>
</div>
