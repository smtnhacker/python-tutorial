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
        { url: "/flow", title: "Flow" }
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

<div class="bg-black min-h-lvh text-white main">
    <nav class="flex justify-end p-4">
    {#if $userId}
        <button on:click={() => goto('/')} class="m-2">Home</button>
        <button on:click={logout} class="m-2">Logout</button>
    {:else}
        <button on:click={() => goto('/login')}>Login</button>
        {/if}
    </nav>
    <header class="flex flex-col items-center">
        <h1 class="text-5xl mb-2 voyage-bold highlight">DCS Bootcamp 11.0</h1>
        <div class="text-xl montserrat-ital">Python Basics Crash Course</div>
        {#if $userId}
        <ul class="flex flex-col m-8">
        {#each pages as page, index}
            <button on:click={() => goto(page.url)} class={`my-1 py-1 px-8 rounded-lg text-xl font-semibold hover:bg-stone-800 ${index%2 ? 'highlight' : ''}`}>{page.title}</button>
        {/each}
        </ul>
        {/if}
    </header>

    <slot />

    <footer class="m-2 flex justify-center">Made by Ron Surara 2024</footer>
</div>

<style>
    .main {
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='52' height='52' viewBox='0 0 52 52'%3E%3Cpath fill='%23bc0b06' fill-opacity='0.08' d='M0 17.83V0h17.83a3 3 0 0 1-5.66 2H5.9A5 5 0 0 1 2 5.9v6.27a3 3 0 0 1-2 5.66zm0 18.34a3 3 0 0 1 2 5.66v6.27A5 5 0 0 1 5.9 52h6.27a3 3 0 0 1 5.66 0H0V36.17zM36.17 52a3 3 0 0 1 5.66 0h6.27a5 5 0 0 1 3.9-3.9v-6.27a3 3 0 0 1 0-5.66V52H36.17zM0 31.93v-9.78a5 5 0 0 1 3.8.72l4.43-4.43a3 3 0 1 1 1.42 1.41L5.2 24.28a5 5 0 0 1 0 5.52l4.44 4.43a3 3 0 1 1-1.42 1.42L3.8 31.2a5 5 0 0 1-3.8.72zm52-14.1a3 3 0 0 1 0-5.66V5.9A5 5 0 0 1 48.1 2h-6.27a3 3 0 0 1-5.66-2H52v17.83zm0 14.1a4.97 4.97 0 0 1-1.72-.72l-4.43 4.44a3 3 0 1 1-1.41-1.42l4.43-4.43a5 5 0 0 1 0-5.52l-4.43-4.43a3 3 0 1 1 1.41-1.41l4.43 4.43c.53-.35 1.12-.6 1.72-.72v9.78zM22.15 0h9.78a5 5 0 0 1-.72 3.8l4.44 4.43a3 3 0 1 1-1.42 1.42L29.8 5.2a5 5 0 0 1-5.52 0l-4.43 4.44a3 3 0 1 1-1.41-1.42l4.43-4.43a5 5 0 0 1-.72-3.8zm0 52c.13-.6.37-1.19.72-1.72l-4.43-4.43a3 3 0 1 1 1.41-1.41l4.43 4.43a5 5 0 0 1 5.52 0l4.43-4.43a3 3 0 1 1 1.42 1.41l-4.44 4.43c.36.53.6 1.12.72 1.72h-9.78zm9.75-24a5 5 0 0 1-3.9 3.9v6.27a3 3 0 1 1-2 0V31.9a5 5 0 0 1-3.9-3.9h-6.27a3 3 0 1 1 0-2h6.27a5 5 0 0 1 3.9-3.9v-6.27a3 3 0 1 1 2 0v6.27a5 5 0 0 1 3.9 3.9h6.27a3 3 0 1 1 0 2H31.9z'%3E%3C/path%3E%3C/svg%3E");
        background-attachment: fixed;
    }
</style>