<script>
    export let timestamp
    export let content

    let time = new Date(timestamp).toLocaleString("en-GB", { timeZone: 'Asia/Singapore'})
</script>

<div class="msg-bubble px-2 py-2 my-3">
    <span class=text-start>bob {time}</span>
    <div class="text-end">
        <span>{content}</span>
    </div>
</div>

<style>
    .msg-bubble {
        background-color: aqua;
        border-radius: 0.5em;
    }
</style>