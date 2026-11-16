import { createLocalStorage } from './adapters/web/local-storage.ts';
import { course } from './content/index.ts';
import { legacyEvents } from './core/migrate.ts';
import { makeDefaultPolicy } from './core/policy.ts';
import { localDate, makeReducer, newGame, type GameEvent } from './core/reducer.ts';
import type { GameState } from './core/state.ts';
import type { StoragePort } from './ports/storage.ts';

// Composition root: the only place that touches clock, random ids and storage.
// Everything below `dispatch` is the pure core.
const order = course.chapters.map((c) => c.id);
export const policy = makeDefaultPolicy(order, undefined, (c) => course.chapters.find((ch) => ch.id === c)?.focus);
const reduce = makeReducer(policy, order);

type Input = GameEvent extends infer E ? (E extends GameEvent ? Omit<E, 'id' | 'at' | 'tzOffsetMin'> : never) : never;

let state = $state.raw<GameState>(newGame(policy));
let ready = $state(false);
let storage: StoragePort | null = null;

const tzOffsetMin = () => -new Date().getTimezoneOffset();

export const game = {
	get state() {
		return state;
	},
	get ready() {
		return ready;
	},
	get today() {
		return localDate(new Date().toISOString(), tzOffsetMin());
	},
	// Call once in the browser (onMount). Loads the saved state or migrates the v1 profile.
	init() {
		if (ready || typeof window === 'undefined') return;
		storage = createLocalStorage(window.localStorage);
		const saved = storage.load();
		const legacy = saved ? null : storage.loadLegacy();
		state = saved ?? (legacy ? legacyEvents(legacy, tzOffsetMin()).reduce(reduce, newGame(policy)) : newGame(policy));
		if (legacy) storage.save(state);
		ready = true;
	},
	dispatch(input: Input) {
		const event = { ...input, id: crypto.randomUUID(), at: new Date().toISOString(), tzOffsetMin: tzOffsetMin() } as GameEvent;
		state = reduce(state, event);
		storage?.save(state);
	},
	reset() {
		storage?.clear();
		state = newGame(policy);
	}
};
