<script>
    import { marked } from 'marked';

    export let title = "";
    export let code = "";
    export let description = "";
    export let example = "";
</script>

<div>
    <div class="font-semibold">{title}</div>
    <div class="pl-4">{@html marked(code)}</div>
    <div class="pl-4">{description}</div>
    <div class="font-semibold highlight">Example:</div>
    <div class="pl-4">{@html marked(example)}</div>
</div>