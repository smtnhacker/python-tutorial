<script>
    import { onMount } from 'svelte';
    import { goto } from '$app/navigation';
    import { userId } from '../lib/stores/auth';
    import "../app.css";

    const pages = [
        { url: "/", title: "Home" },
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
</script>

<div class="p-4">
    <nav>
        <div class="title font-bold text-5xl">
            DCS Bootcamp 11.0: Python Basics Crash-Course
        </div>
        {#if $userId}
        <ul>
            {#each pages as page}
                <li><button on:click={() => goto(page.url)}>{page.title}</button></li>
            {/each}
        </ul>
        {/if}
    </nav>
</div>

<slot />

<footer>Made by Ron Surara 2024</footer>