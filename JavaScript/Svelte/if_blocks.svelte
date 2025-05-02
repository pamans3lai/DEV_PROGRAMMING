<script>
	let user = $state({ loggedIn: false });

	function toggle() {
		user.loggedIn = !user.loggedIn;
	}
</script>

{#if user.loggedIn}
	<button onclick={toggle}> Log Out </button>
{/if}

{#if !user.loggedIn}
	<button onclick={toggle}> Log In </button>
{/if}
