/// <reference types="@sveltejs/kit" />
/// <reference no-default-lib="true"/>
/// <reference lib="esnext" />
/// <reference lib="webworker" />
// Offline support (PWA): app shell and static files are cached per build; pages are network-first with a cached fallback,
// so the course keeps working without a connection (progress lives in localStorage anyway).
import { assets, immutable } from '$app/manifest';
import { version } from '$app/env';

const sw = self as unknown as ServiceWorkerGlobalScope;
const CACHE = `speakaustrian-${version}`;
// Manifest paths are relative to the base path; the app is served from the root.
const abs = (path: string) => (path.startsWith('/') ? path : `/${path}`);
const PRECACHE = [...immutable, ...assets].map((f) => abs(f.path)).concat('/');

sw.addEventListener('install', (event) => {
	event.waitUntil(caches.open(CACHE).then((c) => c.addAll(PRECACHE)).then(() => sw.skipWaiting()));
});

sw.addEventListener('activate', (event) => {
	event.waitUntil(
		caches
			.keys()
			.then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
			.then(() => sw.clients.claim())
	);
});

sw.addEventListener('fetch', (event) => {
	const req = event.request;
	const url = new URL(req.url);
	if (req.method !== 'GET' || url.origin !== sw.location.origin) return;

	// Build output and static files never change within a version: cache first.
	if (PRECACHE.includes(url.pathname)) {
		event.respondWith(caches.match(url.pathname).then((hit) => hit ?? fetch(req)));
		return;
	}
	// Everything else (pages, data): network first, keep a copy, fall back to the cache or the start page offline.
	event.respondWith(
		fetch(req)
			.then((res) => {
				if (res.ok) {
					const copy = res.clone();
					caches.open(CACHE).then((c) => c.put(req, copy));
				}
				return res;
			})
			.catch(async () => (await caches.match(req)) ?? (req.mode === 'navigate' ? await caches.match('/') : undefined) ?? Response.error())
	);
});
