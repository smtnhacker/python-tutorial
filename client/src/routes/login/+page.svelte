<script>
    import { userId } from "../../lib/stores/auth"
    import { SERVER_HOST } from "../../lib/config"

    let username = '';
    let password = '';

    async function login(e) {
        e.preventDefault()
        console.log(username, password)
        const response = await fetch(`${SERVER_HOST}/login`, {
            method: "POST",
            body: JSON.stringify({
                username: username,
                password: password
            }),
            headers: {
                "Content-Type": "application/json"
            }
        })

        if (response.ok) {
            const data = await response.json();
            console.log(data)
            $userId = data["userId"];
        } else {
            alert("Invalid credentials");
        }
    }

    function logout() {
        $userId = false
    }
</script>

<div>
    {#if !$userId}
        <div class="login">
            <h1>Login</h1>
            <form on:submit={login}>
                <label for="username">
                    Username:
                    <input type="text" name="username" bind:value={username}>
                </label>
                <label for="password">
                    Key:
                    <input type="text" name="password" bind:value={password}>
                </label>
                <input type="submit" value="submit">
            </form>
        </div>
    {:else}
        <div class="logout">
            <button on:click={logout}>Logout</button>
        </div>
    {/if}
</div>