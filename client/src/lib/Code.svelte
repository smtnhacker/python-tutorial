<script>
    import { marked } from "marked";
    export let code = '';

    function copyToClipboard() {
        const lines = code.split('\n');
        const codeWithoutFirstLine = lines.slice(1).join('\n');
        navigator.clipboard.writeText(codeWithoutFirstLine).then(() => {
            alert("Code copied to clipboard!");
        }).catch(err => {
            console.error('Failed to copy: ', err);
        });
    }
</script>

<div class="bg-slate-900 text-white px-4 py-2 my-2 rounded-md relative">
    <button 
        class="absolute top-0 right-0 mt-1 mr-1 p-1 bg-slate-700 hover:bg-slate-600 rounded" 
        on:click={copyToClipboard}
    >
        Copy
    </button>
    <div>{@html marked(code)}</div>
</div>