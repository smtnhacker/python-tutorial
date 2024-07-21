<script>
    import { onMount } from 'svelte';
    import { SERVER_HOST } from '../lib/config';

    let file;
    let fileInput;
    let output = '';

    async function uploadFile() {
        const formData = new FormData();
        formData.append('file', file);

        const response = await fetch(`${SERVER_HOST}/ask_question/`, {
            method: 'POST',
            body: formData
        });

        const result = await response.json();
        console.log(result);
        output = result;
    }
</script>

<form on:submit|preventDefault={uploadFile}>
    <input type="file" bind:this={fileInput} on:change={() => file = fileInput.files[0]} />
    <button type="submit">Upload</button>
    <p>Result: {output}</p>
</form>

<style>
    form {
        display: flex;
        flex-direction: column;
        width: 300px;
        margin: 0 auto;
    }

    input {
        margin-bottom: 10px;
    }
</style>