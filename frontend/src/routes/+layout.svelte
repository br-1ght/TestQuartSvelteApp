<script>
	import Nav from "$lib/nav.svelte";
    let currentYear = new Date().getFullYear()
</script>

<Nav />

<div class="w-50 mx-auto">
    <slot />
</div>

<footer class="text-center">&copy; Test Quart App { currentYear }</footer>