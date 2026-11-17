<script lang="ts">
	import SettingsPanel from '#lib/components/SettingsPanel.svelte';
	import { resolve } from '$app/paths';
	import { m } from '#lib/paraglide/messages.js';
</script>

<section class="space-y-4 pt-4">
	<h1 class="h1">{m.settings()}</h1>
	<SettingsPanel />
</section>
