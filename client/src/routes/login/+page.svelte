<script>
    import { goto } from "$app/navigation"
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
            goto('/')
        } else {
            alert("Invalid credentials");
        }
    }

    function logout() {
        $userId = ''
    }
</script>

<div class="p-4">
    {#if !$userId}
        <div class="login flex my-12 flex-col items-center">
            <form on:submit={login} class="flex flex-col">
                <label for="username" class="my-2 flex">
                    Username:
                    <input type="text" name="username" bind:value={username} class="text-black px-2 rounded-md grow mx-2">
                </label>
                <label for="password" class="flex">
                    Key:
                    <input type="text" name="password" bind:value={password} class="text-black px-2 rounded-md grow mx-2">
                </label>
                <input type="submit" value="Submit" class="px-3 py-1 rounded-lg cursor-pointer mt-8 bg-[var(--red-color)]">
            </form>
        </div>
    {:else}
        <div class="logout">
            <button on:click={logout}>Logout</button>
        </div>
    {/if}
</div>