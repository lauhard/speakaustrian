import type { GameState } from '../core/state';

// Progress lives on the device only (D19). Export/import comes with its own step.
export interface StoragePort {
	load(): GameState | null;
	save(state: GameState): void;
	clear(): void;
	// Profile of the first prototype (storage v1), if one is still on the device.
	loadLegacy(): LegacyProfile | null;
}

export type LegacyProfile = { name: string; createdAt: string; lessonsDone: string[] };
