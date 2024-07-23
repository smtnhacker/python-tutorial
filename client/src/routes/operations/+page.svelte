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

</script>

<div>
    <div>
        Operations
    </div>
    <div>
        <div>
            Basic Operators
        </div>
        <div>
            Python has numerous common binary operators. These are usually of the form:
            <div>{@html marked("`<result> = <operandA> <operator> <operandB>`")}</div>
            <p>
                Of course, you can make the equation a bit more complex by having multiple operators in a single line. Just be careful and be mindful of <a href="https://docs.python.org/3/reference/expressions.html#operator-precedence">operator precedence</a> which basically tells the computer in which order the operators will be processed, just liked PEMDAS!
            </p>
            <p>
                The following are some common operators that you might find yourself using. Many of them are just from math. There are other operators that you may see for the first time such as "and" and "or" logical operators, but they will be shown more in detail in the control flow module. For an exhaustive list, refer <a href="https://docs.python.org/3/reference/expressions.html">here</a>.
            </p>
            <ul>
                {#each examples as example}
                    <li><OperatorExample 
                            title={example.title} 
                            description={example.description} 
                            examples={example.examples} 
                        />
                    </li>
                {/each}
            </ul>
        </div>
    </div>
    <p>
        To further help in understanding operators, you can make a function that takes in a single integer x and returns a valid number and submit the function. A graph will be generated plotting the results of the function for x values 1 to 100. Use the following template:a
    </p>
    <div>{@html marked("```python\ndef compute_y(x):\n\treturn 2*x (or whatever you want to compute)")}</div>
    <form on:submit|preventDefault={uploadFile}>
        <input type="file" bind:this={fileInput} on:change={() => file = fileInput.files[0]} />
        <button type="submit">Upload</button>
        <p>Result:
            <img src={output} alt="Resulting Graph">
        </p>
    </form>
</div>