<script>
    let visible = $state(true);
</script>

<label>
    <input type="checkbox" bind:checked={visible} />
    visible
</label>

{#if visible}
<p>
    Fades in and out
</p>
{/if}