<script>
    import { marked } from 'marked';

    export let title = "";
    export let code = "";
    export let description = "";
    export let example = "";
</script>

<div>
    <div>{title}</div>
    <div>{@html marked(code)}</div>
    <div>{description}</div>
    Example:
    <div>{@html marked(example)}</div>
</div>