// PWA install offer. Chromium browsers fire `beforeinstallprompt` once the app is installable; we keep the event and
// show our own button. Safari (iOS) has no such event, so we only show how to add the app via "Share".
type InstallEvent = Event & { prompt: () => Promise<void>; userChoice: Promise<{ outcome: 'accepted' | 'dismissed' }> };

let deferred = $state<InstallEvent | null>(null);
let standalone = $state(false);
let ios = $state(false);

if (typeof window !== 'undefined') {
	standalone = window.matchMedia('(display-mode: standalone)').matches || (navigator as { standalone?: boolean }).standalone === true;
	ios = /iphone|ipad|ipod/i.test(navigator.userAgent);
	window.addEventListener('beforeinstallprompt', (e) => {
		e.preventDefault();
		deferred = e as InstallEvent;
	});
	window.addEventListener('appinstalled', () => {
		deferred = null;
		standalone = true;
	});
}

export const install = {
	get canPrompt() {
		return deferred !== null && !standalone;
	},
	get showIosHint() {
		return ios && !standalone;
	},
	async prompt() {
		if (!deferred) return;
		await deferred.prompt();
		await deferred.userChoice;
		deferred = null;
	}
};
