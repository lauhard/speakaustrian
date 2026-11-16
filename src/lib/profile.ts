import { createLocalStorage } from './adapters/web/local-storage';
import type { Profile, StoragePort } from './ports/storage';

// Composition root for the storage port: the web adapter in the browser, nothing on the server.
export const storage = (): StoragePort | null => (typeof window !== 'undefined' ? createLocalStorage(window.localStorage) : null);

export const newProfile = (name: string, now: Date): Profile => ({
	schema: 1,
	name: name.trim(),
	createdAt: now.toISOString(),
	results: []
});

export const withResult = (profile: Profile, lessonId: string, correct: number, total: number, now: Date): Profile => ({
	...profile,
	results: [...profile.results, { lessonId, at: now.toISOString(), correct, total }]
});
