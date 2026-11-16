import type { LegacyProfile } from '../ports/storage';
import type { GameEvent } from './reducer';

// Storage v1 -> v2: replay the old profile as events, so the new state is built by the same rules.
export const legacyEvents = (legacy: LegacyProfile, tzOffsetMin: number): GameEvent[] => {
	const at = Number.isNaN(Date.parse(legacy.createdAt)) ? new Date(0).toISOString() : legacy.createdAt;
	return [
		{ id: 'legacy-profile', at, tzOffsetMin, type: 'PROFILE_CREATED', name: legacy.name, pensumMin: 90 },
		...legacy.lessonsDone.map(
			(lessonId): GameEvent => ({
				id: `legacy-${lessonId}`,
				at,
				tzOffsetMin,
				type: 'LESSON_COMPLETED',
				chapterId: lessonId.slice(0, 5),
				lessonId
			})
		)
	];
};
