import { z } from 'zod';

export const LessonResult = z.object({
	lessonId: z.string(),
	at: z.string(),
	correct: z.number().int().nonnegative(),
	total: z.number().int().positive()
});

export const Profile = z.object({
	schema: z.literal(1),
	name: z.string().min(1),
	createdAt: z.string(),
	results: z.array(LessonResult)
});
export type Profile = z.infer<typeof Profile>;

// Progress lives on the device only (no login). Export/import comes with its own ticket.
export interface StoragePort {
	load(): Profile | null;
	save(profile: Profile): void;
	clear(): void;
}
