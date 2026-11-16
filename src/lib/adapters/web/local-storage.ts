import { z } from 'zod';
import { GameState } from '../../core/state';
import type { LegacyProfile, StoragePort } from '../../ports/storage';

const KEY = 'speakaustrian.state.v2';
const LEGACY_KEY = 'speakaustrian.profile.v1';

const Legacy = z.object({ name: z.string().min(1), createdAt: z.string(), lessonsDone: z.array(z.string()).default([]) });

const read = (store: Storage, key: string): unknown => {
	try {
		return JSON.parse(store.getItem(key) ?? 'null');
	} catch {
		return null;
	}
};

export const createLocalStorage = (store: Storage): StoragePort => ({
	load: () => {
		const parsed = GameState.safeParse(read(store, KEY));
		return parsed.success ? parsed.data : null;
	},
	save: (state) => {
		try {
			store.setItem(KEY, JSON.stringify(state));
		} catch {
			// Storage full or blocked: the app keeps working for this session.
		}
	},
	clear: () => {
		try {
			store.removeItem(KEY);
			store.removeItem(LEGACY_KEY);
		} catch {
			// ignore
		}
	},
	loadLegacy: (): LegacyProfile | null => {
		const parsed = Legacy.safeParse(read(store, LEGACY_KEY));
		return parsed.success ? parsed.data : null;
	}
});
