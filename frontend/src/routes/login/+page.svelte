<script>
    /** @type {import('./$types').PageData} */

    let username = ""
    let password = ""
    let error = ""

    const loginSubmit = async () => {
        const response = await fetch("http://localhost:5000/api/user/login", {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            credentials: 'include',
            body: JSON.stringify({"username": username, "password": password})
        })
        const result = await response.json()
        if (!response.ok) {
            error = result.message
            return
        }
        location.replace("/")
    }

</script>

<form action="" method="post" on:submit|preventDefault={loginSubmit} class="w-75 mx-auto">
    <label for="usernameField">Username</label>
    <input id="usernameField" type="text" bind:value={username} class="form-control mb-2">

    <label for="passwordField">Password</label>
    <input id="passwordField" type="password" bind:value={password} class="form-control mb-2">
    <button class="btn btn-primary">Login</button>
    {#if error}
        <p class="text-danger">{error}</p>
    {/if}
</form>