import { createLocalStorage } from './adapters/web/local-storage.ts';
import { contentInfo, course, PREVIEW_CHAPTER } from './content/index.ts';
import { legacyEvents } from './core/migrate.ts';
import { defaultConfig, demoConfig, makeDefaultPolicy, type RulePolicy } from './core/policy.ts';
import { localDate, makeReducer, newGame, settleChapter, type GameEvent } from './core/reducer.ts';
import type { GameState } from './core/state.ts';
import type { StoragePort } from './ports/storage.ts';
import { settings } from './settings.svelte.ts';

// Composition root: the only place that touches clock, random ids and storage.
// Everything below `dispatch` is the pure core.
const order = course.chapters.map((c) => c.id);
export const policy = makeDefaultPolicy(order, defaultConfig, (c) => course.chapters.find((ch) => ch.id === c)?.focus);
// DEMO sandbox (005c): own state, own small rules, so the whole chapter flow can be tried without touching course progress.
export const demoPolicy: RulePolicy = { ...makeDefaultPolicy([PREVIEW_CHAPTER], demoConfig), id: 'demo' };

type Input = GameEvent extends infer E ? (E extends GameEvent ? Omit<E, 'id' | 'at' | 'tzOffsetMin'> : never) : never;

const tzOffsetMin = () => -new Date().getTimezoneOffset();

type StoreOptions = { policy: RulePolicy; order: readonly string[]; storageKey?: string; legacy?: boolean; autoProfile?: () => string };

const createStore = (o: StoreOptions) => {
	const reduce = makeReducer(o.policy, o.order, contentInfo);
	const settle = settleChapter(contentInfo);
	let state = $state.raw<GameState>(newGame(o.policy));
	let ready = $state(false);
	let storage: StoragePort | null = null;

	const dispatch = (input: Input) => {
		const event = { ...input, id: crypto.randomUUID(), at: new Date().toISOString(), tzOffsetMin: tzOffsetMin() } as GameEvent;
		state = reduce(state, event);
		storage?.save(state);
	};

	return {
		policy: o.policy,
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
			storage = createLocalStorage(window.localStorage, o.storageKey);
			const saved = storage.load();
			const legacy = saved || !o.legacy ? null : storage.loadLegacy();
			state = settle(saved ?? (legacy ? legacyEvents(legacy, tzOffsetMin()).reduce(reduce, newGame(o.policy)) : newGame(o.policy)));
			if (legacy || saved) storage.save(state);
			ready = true;
			// The sandbox needs no sign-up of its own: it takes the name of the course profile.
			if (!state.profile && o.autoProfile) dispatch({ type: 'PROFILE_CREATED', name: o.autoProfile(), pensumMin: 90 });
		},
		dispatch,
		reset() {
			storage?.clear();
			state = newGame(o.policy);
			if (o.autoProfile) dispatch({ type: 'PROFILE_CREATED', name: o.autoProfile(), pensumMin: 90 });
		}
	};
};

export const game = createStore({ policy, order, legacy: true });
export const demo = createStore({ policy: demoPolicy, order: [PREVIEW_CHAPTER], storageKey: 'speakaustrian.demo.v1', autoProfile: () => game.state.profile?.name ?? 'Demo' });

// Free mode (setting "unlock all chapters"): a chapter that is not yet due runs with the real rules in its own state,
// so the course progress (D11: full scope in order) stays untouched.
const free = new Map<string, ReturnType<typeof createStore>>();
const freeStore = (chapterId: string) => {
	if (!free.has(chapterId)) {
		const p: RulePolicy = { ...makeDefaultPolicy([chapterId], defaultConfig, (c) => course.chapters.find((ch) => ch.id === c)?.focus), id: 'free' };
		free.set(chapterId, createStore({ policy: p, order: [chapterId], storageKey: `speakaustrian.free.${chapterId}.v1`, autoProfile: () => game.state.profile?.name ?? 'Free' }));
	}
	return free.get(chapterId)!;
};
export const isFreeMode = (chapterId: string) =>
	chapterId !== PREVIEW_CHAPTER && settings.value.unlockAll && !policy.canAccessChapter(game.state, chapterId).allowed;

// The store a chapter runs in: the DEMO sandbox for the preview chapter, free mode for unlocked chapters, else the course.
export const storeFor = (chapterId: string) => (chapterId === PREVIEW_CHAPTER ? demo : isFreeMode(chapterId) ? freeStore(chapterId) : game);
