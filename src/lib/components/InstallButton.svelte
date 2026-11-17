<script lang="ts">
	import { m } from '#lib/paraglide/messages.js';
	import { install } from '#lib/install.svelte.ts';
</script>

{#if install.canPrompt}
	<button type="button" class="btn-secondary" data-testid="install-app" onclick={() => install.prompt()}>📲 {m.install_app()}</button>
{:else if install.showIosHint}
	<p class="card text-sm text-muted" data-testid="install-ios">📲 {m.install_ios()}</p>
{/if}
