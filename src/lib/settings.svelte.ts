// Device-local UI preferences (not game state): kept apart from the course progress and never exported with it.
export type Settings = {
	// Andi, 16.11.2026: open every chapter with content. Chapters that are not yet due run in their own free-mode state.
	unlockAll: boolean;
	// Speech rate of the device voice (1 = normal).
	ttsRate: number;
	// Show the English/Tagalog title under German headings.
	showTranslations: boolean;
};

const KEY = 'speakaustrian.settings.v1';
const defaults: Settings = { unlockAll: false, ttsRate: 0.75, showTranslations: true };

const load = (): Settings => {
	try {
		return { ...defaults, ...JSON.parse(localStorage.getItem(KEY) ?? '{}') };
	} catch {
		return defaults;
	}
};

let current = $state<Settings>(typeof window === 'undefined' ? defaults : load());

export const settings = {
	get value() {
		return current;
	},
	set<K extends keyof Settings>(key: K, value: Settings[K]) {
		current = { ...current, [key]: value };
		try {
			localStorage.setItem(KEY, JSON.stringify(current));
		} catch {
			// Private mode or full storage: the setting lasts for this visit only.
		}
	}
};
export const ttsRate = () => current.ttsRate;
