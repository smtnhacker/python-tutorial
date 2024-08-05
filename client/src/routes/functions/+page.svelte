<script>
    import { SERVER_HOST } from '../../lib/config';
	import { marked } from 'marked';

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

    const examples = [
        `
def sum(a: int, b :int) -> int:
    return a+b
        `,
        `
def say_hi():
    print("hi!")
        `,
        `
def swap(a, b):
    temp = a
    a = b
    b = temp
        `
    ]
</script>

<div class="flex justify-center content-stretch">
    <div class="flex bg-white rounded-2xl w-7/12 text-black">
        <div class="relative">
            <div class="absolute top-4 left-4 text-6xl text-[var(--red-color)]">
                ♥
            </div>
            <div class="absolute bottom-2 left-5 text-5xl text-[var(--red-color)] voyage-bold">
                Q
            </div>
        </div>
        <div class="flex flex-col items-center grow">
            <h2 class="text-5xl my-4 voyage-bold text-[var(--red-color)]">Functions</h2>
            <div class="border-solid border-8 border-black montserrat-ital mx-14 mb-14 p-4 rounded-lg">
                <p>Often, there are set of instructions that you'll reuse at different parts of the program. Instead of manually copy-pasting these code and possibly make your code harder to debug and maintain, you can use Python's functions. They have the following format:</p>
                <div>{@html marked("```python\ndef function_name(parameter1: type, parameter2: type) -> return_type:\n\t# function logic\n\treturn value")}</div>
                <div>Here are some examples:</div>
                <div>
                    {#each examples as example}
                        {@html marked(`\`\`\`python${example}`)}
                    {/each}
                </div>
                <h1 class="font-semibold text-xl">Test Yourself</h1>
                <p>For this activity, since we have not yet covered other parts of Python, you'll just be tasked with defining a function that returns a proper question. It should follow the following template:</p>
                <div>{@html marked("```python\ndef ask_question():\n\t# function logic\n\treturn \"Some question?\"")}</div>
                <div class="mt-4">
                    <form on:submit|preventDefault={uploadFile}>
                        <input type="file" bind:this={fileInput} on:change={() => file = fileInput.files[0]} />
                        <button type="submit" class="bg-[var(--red-color)] text-white px-3 py-1 rounded-lg">Upload</button>
                    </form>
                    {#if output}
                    <p>ChatGPT:</p>
                    <div>{output}</div>
                    {/if}
                </div>
            </div>
        </div>
        <div class="relative">
            <div class="absolute top-5 right-7 text-5xl text-[var(--red-color)] voyage-bold">
                Q
            </div>
            <div class="absolute bottom-2 right-4 text-6xl text-[var(--red-color)]">
                ♥
            </div>
        </div>
    </div>
</div>

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