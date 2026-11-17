<script lang="ts">
	import { ChevronLeft } from '@lucide/svelte';
	import SettingsPanel from '#lib/components/SettingsPanel.svelte';
	import { resolve } from '$app/paths';
	import { m } from '#lib/paraglide/messages.js';
</script>

<a href={resolve('/')} class="backlink"><ChevronLeft size={18} strokeWidth={2.5} />{m.course()}</a>
<section class="space-y-4 pt-4">
	<h1 class="h1">{m.settings()}</h1>
	<SettingsPanel />
</section>
