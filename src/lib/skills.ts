import { BookOpen, Headphones, Landmark, Mic, PenLine, Puzzle } from '@lucide/svelte';
import type { Discipline } from './core/content/schema.ts';
import { m } from './paraglide/messages.js';

// One color and icon per exam skill, used as accent in tasks (tile = soft background, solid = strong fill).
export const skills = {
	hoeren: { icon: Headphones, label: m.skill_hoeren, tile: 'bg-sky-100 text-sky-700', solid: 'bg-sky-600 text-white shadow-sky-600/30' },
	lesen: { icon: BookOpen, label: m.skill_lesen, tile: 'bg-emerald-100 text-emerald-700', solid: 'bg-emerald-600 text-white shadow-emerald-600/30' },
	schreiben: { icon: PenLine, label: m.skill_schreiben, tile: 'bg-violet-100 text-violet-700', solid: 'bg-violet-600 text-white shadow-violet-600/30' },
	sprechen: { icon: Mic, label: m.skill_sprechen, tile: 'bg-amber-100 text-amber-700', solid: 'bg-amber-500 text-white shadow-amber-500/30' },
	grammatikWortschatz: { icon: Puzzle, label: m.skill_grammatikWortschatz, tile: 'bg-brand-soft text-brand', solid: 'bg-brand text-white shadow-brand/30' },
	werte: { icon: Landmark, label: m.skill_werte, tile: 'bg-indigo-100 text-indigo-700', solid: 'bg-indigo-600 text-white shadow-indigo-600/30' }
} satisfies Record<Discipline, unknown>;
