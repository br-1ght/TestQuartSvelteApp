<script>
	import Nav from "$lib/nav.svelte"
    import { getAuthState } from "$lib/helpers.js"
    import { authState } from "$lib/stores/auth-store.js"
    let currentYear = new Date().getFullYear()
    authState.set(getAuthState())
</script>

<Nav />

<div class="container">
    <slot />
</div>

<footer class="text-center">&copy; Test Quart App { currentYear }</footer>