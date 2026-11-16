import { Lesson } from '../core/content/schema';
import raw from './demo-lesson.json';

// Parsing at import time makes invalid content fail the build and the unit tests.
export const demoLesson: Lesson = Lesson.parse(raw);
