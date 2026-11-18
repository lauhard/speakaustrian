<script lang="ts">
	import type { Snippet } from 'svelte';
	import { X } from '@lucide/svelte';
	import { m } from '#lib/paraglide/messages.js';

	// Info popup on the native Popover API: top layer, light dismiss and ESC come from the browser.
	// Open it with any <button popovertarget={id}>. Phones get a bottom sheet, desktop a centered card (.sheet-pop).
	let { id, title, children, testid }: { id: string; title: string; children: Snippet; testid?: string } = $props();
</script>

<div {id} popover="auto" class="sheet-pop" data-testid={testid}>
	<div class="mb-3 flex items-center justify-between gap-3">
		<h2 class="h2">{title}</h2>
		<button type="button" class="burger !h-9 !w-9" popovertarget={id} popovertargetaction="hide" aria-label={m.popover_close()}>
			<X size={18} strokeWidth={2.5} />
		</button>
	</div>
	<div class="space-y-3 text-sm font-semibold text-muted">{@render children()}</div>
</div>
