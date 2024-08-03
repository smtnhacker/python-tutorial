<script>
	import { marked } from 'marked';
    import { SERVER_HOST } from '../../lib/config';
    import IoItem from './IOItem.svelte';

    const inputItems = [
        {
            title: "Single String",
            code: "`a = input()`",
            description: "This takes in the entire line and saves it into a single variable.",
            example: "`The quick brown fox jumps over the lazy dog`"
        },
        {
            title :"Single Integer", 
            code: "`a = int(input())`",
            description: "This takes in a single integer and saves it into a single variable.", 
            example: "`100000000000000000000`"
        },
        {
            title: "Fixed-Amount Multiple Integer",
            code: "`a, b, c = map(int, input().split())`",
            description: "This takes in a fixed number of integers and saves them into the same number of variables.",
            example: "`10 20 25`"
        },
        {
            title: "Dynamic-Amount Multiple Integer",
            code: "`numbers = list(map(int, input().split()))`",
            description: "This takes in an \"unknown\" amount of integers and saves them into a single list variable.",
            example: "`1 2 3 4 5 6 7 8 9`"
        }
    ]

    const outputItems = [
        {
            title: "Single Variable",
            code: "`print(a)`",
            description: "The simplest way of printing. This prints the variable's value, or how Python thinks the value should look like.",
            example: "If `a = 5`, then `print(a)` will result to `5`"
        },
        {
            title: "Spaced-separated Variables",
            code: "`print(a, b, c)`",
            description: "This will print the variables with space between them added automatically.",
            example: "If `a=1,b=2,c=3`, then `print(a,b,c)` will result to `1 2 3`"
        },
        {
            title: "List",
            code: "`print(*a_list)`",
            description: "This will print the content of the list with spaces between them.",
            example: "If `a_list=[1,2,3,\"a\",\"b\"]`, then `print(*a_list)` will result to `1 2 3 a b`"
        }
    ]

    let question = '';
    let answer = '';
    let showAnswer = false;

    async function get_sample() {
        const response = await fetch(`${SERVER_HOST}/io`);
        const result = await response.json();
        console.log(result)
        question = result["testcase"];
        answer = result["answer"];
    }
</script>

<div class="flex justify-center content-stretch">
    <div class="flex bg-white rounded-2xl w-7/12 text-black">
        <div></div>
        <div class="flex flex-col items-center grow">
            <h2 class="text-5xl my-4 voyage-bold text-[var(--red-color)]">I/O</h2>
            <div class="border-solid border-8 border-black montserrat-ital mx-14 mb-14 p-4 rounded-lg">
                <p>In Python, you take input one line at a time. This can be confusing at first which is why here are some common ways to take input. You don't have to know the details on how each works right now. Just familiarize them until you are able to dissect how each works. Note that inputs can be a lot more complex and may need better understanding of python</p>
                <div>
                    {#each inputItems as {title, code, description, example}}
                    <div class="px-2 py-4">
                        <IoItem title={title} code={code} description={description} example={example} />
                    </div>
                    {/each}
                </div>
                <p>A common way of printing in Python is by using the print function. Here are some common ways of printing things.</p>
                <div>
                    {#each outputItems as {title, code, description, example}}
                        <div class="px-2 py-4">
                            <IoItem title={title} code={code} description={description} example={example} />
                        </div>
                    {/each}
                </div>
                <div>
                    <h1 class="font-semibold text-xl">Test Yourself</h1>
                    <button on:click={get_sample} class="bg-slate-200 px-3 py-1 rounded-lg">Generate Problem</button>
                    <div class="pl-8">
                        <div>
                            {@html marked(question)}
                        </div>
                    </div>
                    <div class>
                        Show Answer (likely incorrect): <input type="checkbox" bind:checked={showAnswer}>
                    </div>
                    {#if showAnswer}
                        Answer:
                        {@html marked(answer)}
                    {/if}
                </div>
            </div>
        </div>
        <div></div>
    </div>
</div>