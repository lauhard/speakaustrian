<script lang="ts">
	import { Download, Share } from '@lucide/svelte';
	import { m } from '#lib/paraglide/messages.js';
	import { install } from '#lib/install.svelte.ts';
</script>

{#if install.canPrompt || install.showIosHint}
	<section>
		<h3 class="list-label">{m.set_group_app()}</h3>
		<div class="list">
			{#if install.canPrompt}
				<button type="button" class="list-row" data-testid="install-app" onclick={() => install.prompt()}>
					<span class="icon-tile"><Download size={20} strokeWidth={2.25} /></span>
					<span class="tile-title flex-1">{m.install_app()}</span>
				</button>
			{:else}
				<p class="list-row" data-testid="install-ios">
					<span class="icon-tile"><Share size={20} strokeWidth={2.25} /></span>
					<span class="tile-sub flex-1">{m.install_ios()}</span>
				</p>
			{/if}
		</div>
	</section>
{/if}
