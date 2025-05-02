<script>
	let count = $state(0);

	$effect(() => {
		alert('count is dangerously high!');
		count = 9;
	});

	function handleClick() {
		count += 1;
	}
</script>

<button onclick={handleClick}>
	KLIK {count}
	{count === 1 ? 'time' : 'times'}
</button>
