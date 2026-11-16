import type { SpeechOutPort, SpeechStatus } from '../../ports/speech-out';

// Device TTS hardened after prototype v4 (docs/spec/prototyp-erkenntnisse.md, E-P3):
// one utterance per call, cancel only when something is playing, resume a paused engine,
// start inside the user gesture, watchdog with one retry on the default German voice.
const WATCHDOG_MS = 2500;
const MAX_LOG = 40;

const pickVoice = (voices: SpeechSynthesisVoice[], lang: 'de-AT' | 'de'): SpeechSynthesisVoice | undefined => {
	const norm = (v: SpeechSynthesisVoice) => v.lang.replace('_', '-').toLowerCase();
	return lang === 'de-AT'
		? (voices.find((v) => norm(v) === 'de-at') ?? voices.find((v) => norm(v).startsWith('de')))
		: (voices.find((v) => norm(v) === 'de-de') ?? voices.find((v) => norm(v).startsWith('de')));
};

export const createDeviceTts = (win: Window): SpeechOutPort => {
	const synth: SpeechSynthesis | undefined = win.speechSynthesis;
	const lines: string[] = [];
	const note = (line: string) => {
		lines.push(`${new Date().toISOString().slice(11, 19)} ${line}`);
		if (lines.length > MAX_LOG) lines.shift();
	};

	const stop = () => {
		if (synth && (synth.speaking || synth.pending)) synth.cancel();
	};

	// A hidden page can leave the engine hanging until reload, so stop early.
	win.document.addEventListener('visibilitychange', () => {
		if (win.document.hidden) stop();
	});

	const attempt = (text: string, rate: number, lang: 'de-AT' | 'de'): Promise<SpeechStatus> =>
		new Promise((resolve) => {
			if (!synth) return resolve({ ok: false, reason: 'unsupported' });
			const utterance = new SpeechSynthesisUtterance(text);
			const voice = pickVoice(synth.getVoices(), lang);
			if (voice) utterance.voice = voice;
			utterance.lang = voice?.lang ?? (lang === 'de-AT' ? 'de-AT' : 'de-DE');
			utterance.rate = rate;

			let started = false;
			let settled = false;
			const settle = (status: SpeechStatus) => {
				if (settled) return;
				settled = true;
				win.clearTimeout(timer);
				resolve(status);
			};
			const timer = win.setTimeout(() => {
				if (started) return;
				note(`watchdog: no start after ${WATCHDOG_MS} ms`);
				synth.cancel();
				settle({ ok: false, reason: 'not-started' });
			}, WATCHDOG_MS);

			utterance.onstart = () => {
				started = true;
				note(`start voice=${voice?.name ?? 'default'} lang=${utterance.lang} rate=${rate}`);
			};
			utterance.onend = () => {
				note('end');
				settle({ ok: true });
			};
			utterance.onerror = (event) => {
				note(`error ${event.error}`);
				// 'interrupted'/'canceled' come from our own stop() and are not failures.
				settle(
					event.error === 'interrupted' || event.error === 'canceled'
						? { ok: true }
						: { ok: false, reason: 'error', detail: event.error }
				);
			};

			if (synth.paused) synth.resume();
			synth.speak(utterance);
		});

	return {
		isSupported: () => Boolean(synth),
		stop,
		log: () => lines,
		speak: async (text, options) => {
			if (!synth) return { ok: false, reason: 'unsupported' };
			const rate = options?.rate ?? 0.75;
			stop();
			const first = await attempt(text, rate, 'de-AT');
			if (first.ok || first.reason === 'unsupported') return first;
			note('retry with default German voice');
			const second = await attempt(text, rate, 'de');
			if (!second.ok && !synth.getVoices().some((v) => v.lang.toLowerCase().startsWith('de'))) {
				return { ok: false, reason: 'no-german-voice' };
			}
			return second;
		}
	};
};
