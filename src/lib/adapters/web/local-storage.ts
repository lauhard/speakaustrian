import { Profile, type StoragePort } from '../../ports/storage';

const KEY = 'speakaustrian.profile.v1';

export const createLocalStorage = (store: Storage): StoragePort => ({
	load: () => {
		try {
			const parsed = Profile.safeParse(JSON.parse(store.getItem(KEY) ?? 'null'));
			return parsed.success ? parsed.data : null;
		} catch {
			return null;
		}
	},
	save: (profile) => {
		try {
			store.setItem(KEY, JSON.stringify(profile));
		} catch {
			// Storage full or blocked: the app keeps working for this session.
		}
	},
	clear: () => {
		try {
			store.removeItem(KEY);
		} catch {
			// ignore
		}
	}
});
