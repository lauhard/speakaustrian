export type SpeakOptions = { rate?: number };

export type SpeechStatus =
	| { ok: true }
	| { ok: false; reason: 'unsupported' | 'no-german-voice' | 'not-started' | 'error'; detail?: string };

// Speech output port (masterprompt 6.3). D17b: the only adapter for now is device TTS.
export interface SpeechOutPort {
	isSupported(): boolean;
	speak(text: string, options?: SpeakOptions): Promise<SpeechStatus>;
	stop(): void;
	// Last diagnostic lines (start/end/error, voice, rate) for the device check.
	log(): readonly string[];
}
