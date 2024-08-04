<script>
    import { marked } from 'marked'
    import { SERVER_HOST } from '../../lib/config';
    import OperatorExample from './OperatorExample.svelte';

    let examples = [
        {
            title: "Addition (+)",
            description: "Adds two expressions",
            examples: ["c=a+b", "current_age=prev_age+time_elapsed", "total=a+b+c+d+e"]
        },
        {
            title: "Subtraction (-)",
            description: "Subtracts an expression from another expression",
            examples: ["diff=a-b"]
        },
        {
            title: "Multiplication (*)",
            description: "Multiplies two expressions",
            examples: ["discount=total*rate", "num_possibilities=a*b*c"]
        },
        {
            title: "Division (/)",
            description: "Performs the division that you usually do",
            examples: ["percentage=part/whole", "probability=chance/total", "slope=delta_y/delta_x"]
        },
        {
            title: "Floor Division (//)",
            description: "Performs a division that floors the result, so it results to an integer",
            examples: ["num_pie_each=num_pies/num_guests", "person_per_group=total_persons/num_groups"]
        },
        {
            title: "Parenthesis (())",
            description: "Used to group expressions which can be used for ordering operator evaluation.",
            examples: ["num_grids=(num_row+1)*(num_col+1)", "money_left=current_money-(cost_a+cost_b+cost_c)"]
        },
        {
            title: "Modulo (%)",
            description: "Usually used on integers. Commonly used to get the remainder after performing standard division",
            examples: ["excess_pie=total_pie%num_people", "remainder=number%2"]
        },
        {
            title: "Power (**)",
            description: "Raises an expression by another expression",
            examples: ["squared=n**2", "sqrt_root=n**0.5", "result=e**(alpha*k)"]
        }
    ]

    let file;
    let fileInput;
    let output = '';

    async function uploadFile() {
        const formData = new FormData();
        formData.append('file', file);

        const response = await fetch(`${SERVER_HOST}/generate_graph`, {
            method: 'POST',
            body: formData
        });

        const result = await response.blob();
        const imageURL = URL.createObjectURL(result)
        console.log(imageURL);
        output = imageURL;
    }

    const line_intersection_template = `
# these 4 are just utility functions that can help
# make your code cleaner, but are not required
# to do this exercise

def get_product_def(p1, q1, p2, q2):
    "A utility function to minimize confusing expressions"
    return p1*q2 - p2*q1

def get_ab(a1, b1, a2, b2):
    "A hint: 2 other functions follow this format"
    return get_product_def(a1, b1, a2, b2)

def get_bc(b1, c1, b2, c2):
    # fill in this function
    return 0

def get_ca(c1, a1, c2, a2):
    # fill in this function
    return 0

# these functions are what matters here
# you can use whatever method you want
# just make sure that these two works

def get_x(a1, b1, c1, a2, b2, c2):
    # use the formula to compute this
    return 0

def get_y(a1, b1, c1, a2, b2, c2):
    # use the formula to compute this
    return 0

# nothing to fill in this part
# this is only to show how to write clean
# code for the long term

class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def __str__(self):
        return f"<Line ({self.a})x+({self.b})y+({self.c})=0>"

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"

def find_intersection(line1: Line, line2: Line) -> Point:
    x = get_x(line1.a, line1.b, line1.c, line2.a, line2.b, line2.c)
    y = get_y(line1.a, line1.b, line1.c, line2.a, line2.b, line2.c)
    return Point(x, y)
    `;

    let lineFile;
    let lineFileInput;
    let accuracy = 0;

    async function uploadLine() {
        const formData = new FormData();
        formData.append('file', lineFile);

        const response = await fetch(`${SERVER_HOST}/find_intersection`, {
            method: 'POST',
            body: formData
        });

        const result = await response.json();
        console.log(result)
        accuracy = result["AC"] / result["total_cases"]
    }

</script>

<div class="flex justify-center content-stretch">
    <div class="flex bg-white rounded-2xl w-7/12 text-black">
        <div></div>
        <div class="flex flex-col items-center grow">
            <h2 class="text-5xl my-4 voyage-bold text-[var(--red-color)]">Operations</h2>
            <div class="border-solid border-8 border-black montserrat-ital mx-14 mb-14 p-4 rounded-lg">
                Python has numerous common binary operators. These are usually of the form:
                <div>{@html marked("`<result> = <operandA> <operator> <operandB>`")}</div>
                <p class="my-2">
                    Of course, you can make the equation a bit more complex by having multiple operators in a single line. Just be careful and be mindful of <a href="https://docs.python.org/3/reference/expressions.html#operator-precedence">operator precedence</a> which basically tells the computer in which order the operators will be processed, just liked PEMDAS!
                </p>
                <p class="my-2">
                    The following are some common operators that you might find yourself using. Many of them are just from math. There are other operators that you may see for the first time such as "and" and "or" logical operators, but they will be shown more in detail in the control flow module. For an exhaustive list, refer <a href="https://docs.python.org/3/reference/expressions.html">here</a>.
                </p>
                <ul>
                    {#each examples as example}
                        <li class="py-4"><OperatorExample 
                                title={example.title} 
                                description={example.description} 
                                examples={example.examples} 
                            />
                        </li>
                    {/each}
                </ul>
                <h1 class="font-semibold text-xl">Test Yourself</h1>
                 <p>
                    To further help in understanding operators, you can make a function that takes in a single integer x and returns a valid number and submit the function. A graph will be generated plotting the results of the function for x values 1 to 100. Use the following template:
                </p>
                <div class="pl-2">{@html marked("```python\ndef compute_y(x):\n\treturn 2*x (or whatever you want to compute)")}</div>
                <form on:submit|preventDefault={uploadFile} class="my-4">
                    <input type="file" bind:this={fileInput} on:change={() => file = fileInput.files[0]} />
                    <button type="submit" class="bg-slate-200 px-3 py-1 rounded-lg">Upload</button>
                    {#if output}
                    <p>Result:
                        <img src={output} alt="Resulting Graph">
                    </p>
                    {/if}
                </form>
                <p class="my-2">
                    Typically, algorithms are not written in isolation. Instead, they are made to solve a particular problem. For this activity, you must solve the line intersection problem by using the following formula and filling up the following template:
                </p>
                <div>{@html marked("Given lines of the form `a1x+b1y+c1=0` and `a2x+b2y+c2=0`, assuming that an intersection exists, the formula for the intersection is `x=(b1c2-b2c1)/(a1b2-a2b1), y=(c1a2-c2a1)/(a1b2-a2b1)`. This may not be the best way for solving this problem, but fill in the following template to try and get the intersection of two lines.")}</div>
                <div>{@html marked(`\`\`\`python\n${line_intersection_template}`)}</div>
                <form on:submit|preventDefault={uploadLine}>
                    <input type="file" bind:this={lineFileInput} on:change={() => lineFile = lineFileInput.files[0]} />
                    <button type="submit" class="bg-slate-200 px-3 py-1 rounded-lg">Submit</button>
                    <p>Score: {accuracy * 100}</p>
                </form>
            </div>
        </div>
        <div></div>
    </div>
</div>
