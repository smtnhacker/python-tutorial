<script>
    import { onMount } from 'svelte';
    import { goto } from '$app/navigation';
    import { userId } from '../lib/stores/auth';
    import "../app.css";

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
            <li><button on:click={() => goto('/')}>Home</button></li>
            <li><button on:click={() => goto('/io')}>IO</button></li>
        </ul>
    </nav>
</div>

<slot />

<footer>Made by Ron Surara 2024</footer>