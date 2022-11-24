<script>
    /** @type {import('./$types').PageData} */
    import Message from "$lib/message.svelte";
    import { onMount } from 'svelte';
    

    let msgBody = ""
    let sock
    let allMsg = []
    let msgCount = 0

    onMount(async () => {
        sock = new WebSocket("ws://localhost:5000/ws")
        
        sock.addEventListener("message", (event) => {
            allMsg = allMsg.concat(JSON.parse(event.data))
            msgCount++
        })        
    })

    let sendMsg = (event) => {
        event.preventDefault()
        const msg = {
            timestamp: Date.now(),
            body: msgBody
        }
        
        sock.send(JSON.stringify(msg))
    }
</script>


<h2>Messages</h2>

<form action="" on:submit={sendMsg} class="input-group">
    <input type="text" bind:value={msgBody} class="form-control">
    <button class="btn btn-primary">Send Message</button>
</form>

<div>
    <p>Amount: {msgCount}</p>
    {#each allMsg as msg}
        <Message timestamp={msg.timestamp} content={msg.body}/> 
    {/each}
</div>