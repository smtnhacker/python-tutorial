<script>
    import { onMount } from 'svelte';
    import { goto } from '$app/navigation';
    import { userId } from '../lib/stores/auth';
    import "../app.css";

    const pages = [
        { url: "/", title: "Home" },
        { url: "/io", title: "IO" },
        { url: "/functions", title: "Functions" },
        { url: "/operations", title: "Operations" }
    ]

    onMount(() => {
        userId.subscribe(val => {
            if (!val) {
                goto('/login')
            } 
        });
    });
</script>

<div>
    <nav>
        <div class="title">
            DCS Bootcamp 11.0: Python Basics Crash-Course
        </div>
        <ul>
            {#each pages as page}
                <li><button on:click={() => goto(page.url)}>{page.title}</button></li>
            {/each}
        </ul>
    </nav>
</div>

<slot />

<footer>Made by Ron Surara 2024</footer>