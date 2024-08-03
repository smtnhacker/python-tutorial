<script>
    import { onMount } from 'svelte';
    import { goto } from '$app/navigation';
    import { userId } from '../lib/stores/auth';
    import "../app.css";

    const pages = [
        // { url: "/", title: "Home" },
        { url: "/io", title: "IO" },
        { url: "/functions", title: "Functions" },
        { url: "/operations", title: "Operations" },
        { url: "/flow", title: "Flow, Loops, and Lists" }
    ]

    onMount(() => {
        userId.subscribe(val => {
            if (!val) {
                goto('/login')
            } 
        });
    });

    function logout() {
        $userId = ''
    }
</script>

<div class="bg-black min-h-lvh text-white">
    <nav class="flex justify-end p-4">
    {#if $userId}
        <button on:click={() => goto('/')} class="m-2">Home</button>
        <button on:click={logout} class="m-2">Logout</button>
    {:else}
        <button on:click={() => goto('/login')}>Login</button>
        {/if}
    </nav>
    <header class="flex flex-col items-center">
        <h1 class="text-5xl mb-2 font-semibold highlight">DCS Bootcamp 11.0</h1>
        <div class="text-2xl">Python Basics Crash Course</div>
        <ul class="flex flex-col m-8">
        {#each pages as page, index}
            <button on:click={() => goto(page.url)} class={`my-1 py-1 px-8 rounded-lg text-xl font-semibold hover:bg-stone-800 ${index%2 ? 'highlight' : ''}`}>{page.title}</button>
        {/each}
        </ul>
    </header>

    <slot />

    <footer class="m-2 flex justify-center">Made by Ron Surara 2024</footer>
</div>

<style>
    :root {
        --highlight-color: rgb(195, 160, 79)
    }

    .highlight {
        color: var(--highlight-color);
    }
</style>