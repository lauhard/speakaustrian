// Tiny toast queue for transient hints (free mode etc.). Feedback on answers stays in the answer sheet.
export type Toast = { id: number; text: string; tone: 'info' | 'ok' | 'warn'; icon?: 'unlock' | 'info'; testid?: string };

let seq = 0;
export const toasts = $state<{ list: Toast[] }>({ list: [] });

export const dismiss = (id: number) => (toasts.list = toasts.list.filter((t) => t.id !== id));

export const toast = (text: string, opts: Partial<Omit<Toast, 'id' | 'text'>> & { ms?: number } = {}) => {
	const t: Toast = { id: ++seq, text, tone: opts.tone ?? 'info', icon: opts.icon, testid: opts.testid };
	toasts.list = [...toasts.list.filter((x) => x.text !== text), t];
	setTimeout(() => dismiss(t.id), opts.ms ?? 4000);
};
