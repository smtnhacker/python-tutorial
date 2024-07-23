<script>
    import { marked } from "marked";

    export let title="";
    export let description="";
    export let examples=[];
</script>

<div>
    <div>{title}</div>
    <div>Description: {description}</div>
    <div>Examples: 
        {#each examples as example}
            {@html marked(`\`${example}\`, `)}
        {/each}
    </div>
</div>