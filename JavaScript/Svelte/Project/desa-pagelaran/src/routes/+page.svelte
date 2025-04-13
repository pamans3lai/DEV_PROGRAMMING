<script lang="ts">
	import Events from '$components/Events.svelte';
	import Siren from '$componensts/Siren.svelte';
	import type { PageData } from './$types';
	export let data: PageData;
</script>

<section
	class="mx-auto grid gap-4 lg:gap-16 lg:flex lg:my-36 place-items-center text-center lg:text-left"
>
	<Siren classess="max-w-[400px] w-full motion-safe:animate-float" />
	<div class="max-w-xl grid gap-6 place-items-center lg:place-items-start">
		<h1 class="lg:text-left gradient-text">Desa Pagelaran</h1>

		<h2 class="text-lg">Kecamatan Ciomas Kabupaten Bogor</h2>

		<div class="grid lg:flex w-full gap=4 justify-center lg:justify-start">
			<a 

					class="btn btn-primary"
					rel="noopener noreferrer"
					target="_blank"
					href="https://discord.gg/hahaha"
			>
					Gabung Komunitas
			</a>
			<a
			
					data-sveltekit-preload-code
					class="btn btn-secondary"
					rel="noopener noreferrer"
					></a>



</section>

<!-- <nav>
	<a href="/">home</a>
	<a href="/about">about</a>
</nav>

<h1>Selamat datang di to SvelteKit</h1>
<p>Visit <a href="https://svelte.dev/docs/kit">svelte.dev/docs/kit</a> to read the documentation</p> -->
