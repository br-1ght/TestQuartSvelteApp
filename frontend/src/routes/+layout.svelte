<script>
	import Nav from "$lib/nav.svelte"
    let currentYear = new Date().getFullYear()
</script>

<Nav />

<div class="container">
    <slot />
</div>

<footer class="text-center">&copy; Test Quart App { currentYear }</footer>