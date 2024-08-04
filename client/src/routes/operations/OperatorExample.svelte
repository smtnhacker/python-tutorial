<script>
    import { marked } from "marked";

    export let title="";
    export let description="";
    export let examples=[];
</script>

<div>
    <div class="font-semibold">{title}</div>
    <div class="pl-4">Description: {description}</div>
    <div class="font-semibold highlight">Examples: </div>
    <div class="pl-4">
        {#each examples as example}
            {@html marked(`\`${example}\`, `)}
        {/each}
    </div>
</div>