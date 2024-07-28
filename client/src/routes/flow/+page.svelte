<script>

	import { marked } from "marked";

</script>
<div>
    <div>
        Control Flow, Loops, and Lists
    </div>
    <div>
        So far, we have been writing code that generally runs in a sequential manner. However, there are times where we want to only run code if some conditions are met. Other times, we would want to run a block of code multiple times. This is where conditional statements and loops come in!
        <div>
            Conditional Statements (If/Elif/Else)
        </div>
        <div>
            If we want to run a block of code only if a condition is satisfied, we use the "if" keyword. It has the following syntax:
            <div>{@html marked("```python\nif <condition>:\n\t# codeblock to run")}</div>
            For example, if we want to print a string only if it comprised of alphabet letters (a-z) and numbers (0-9) (also called alphanumeric characters), we can use the following code:
            <div>{@html marked("```python\nusername = input()\nif username.isalnum():\n\tprint(username)")}</div>
            Note that the method "isalnum" returns True if a string only consists of alphanumeric characters and returns False otherwise. So, if isalnum returns True, then we print the provided username.
            <br />
            If we want to run another block of code in case the condition failes, then we use the "else" keyword. It has the following syntax:
            <div>{@html marked("```python\nif <condition>:\n\t# codeblock to run if true\nelse:\n\t# codeblock to run if false")}</div>
            Continuing from the previous example, if the username is not alphanumeric, we may want to inform the user that the username is invalid. We can do that using the else statement.
            <div>{@html marked("```python\nusername = input()\nif username.isalnum():\n\tprint(username)\nelse:\n\tprint(\"Invalid username. Please only use alphanumeric characters.\")")}</div>
            Sometimes, we want to run a block of code if it fails a certain condition but also satisfies other conditions. In these scenarios, we use the "elif" keyword. It has the following syntax:
            <div>{@html marked("```python\nif <condition>:\n\t# codeblock to run if true\nelif <another condition>:\n\t# codeblock to run\nelse:\n\t# codeblock to run if false")}</div>
            Continuing from the previous example, we may want to reject usernames that are reserved, such as "admin" or contains reserved words. We can do that by modifying the code to be the following:
            <div>{@html marked("```python\nusername = input()\nif username == \"admin\" or \"riot\" in username:\n\tprint(\"Invalid username. Username mustn't contain reserved words or keywords\")\nelif username.isalnum():\n\tprint(username)\nelse:\n\tprint(\"Invalid username. Please only use alphanumeric characters.\")")}</div>
        </div>
        <div>
            Loops
        </div>
        <div>
            Sometimes, we want to run a block of code multiple times. For example, printing all square of numbers from 1 to 1000, or taking the input X times. For the first scenario, we may be able to do it through brute force and enough patience such as:
            <div>{@html marked("```python\nprint(1)\nprint(4)\nprint(9)\n# ...\nprint(1000000)\n")}</div>
            If we were to print square of numbers from 1 to 1000000, it would still be possible however this method is highly impractical. In fact, this cannot work for certain scenarios, such as the 2nd scenario. Think about it. How many lines of input do we make?
            <div>{@html marked("```python\nn = int(input())\ninput_1 = input()\ninput_2 = input()\ninput_3 = input()\n# how many more lines? What if n is only 1? What if n is 1000?")}</div>
            There are many ways of tackling these problems, and one common way is through the use of "for loops". It has the following syntax:
            <div>{@html marked("```python\nfor <element> in <sequence>:\n\t# do something with <element>")}</div>
            You'll often see it in the following way:
            <div>{@html marked("```python\nn = int(input())\nfor i in range(n):\n\tprint(n) # or something")}</div>
            Try to run the code above and see what it prints! This is important since beginners tend to overlook this standard of counting in programming called 0-based indexing.
        </div>
        <div>
            Lists
        </div>
        <div>
            Often times, we not only want to run a command multiple times. We'll also want to take the input multiple times. If you recall, the template that this module provides for taking in a dynamic number of input on a single line is:
            <div>{@html marked("```python\nnumbers = list(map(int, input().split()))")}</div>
            If you use it on the input "1 2 3 4 5 6 7" and print numbers, you may get an output such as "[1, 2, 3, 4, 5, 6, 7]". Notice that the numbers are surrounded by "[]". This indicates that "numbers" is a list. Lists are variables that can contain multiple values. You can access each of its elements using the index operator "[]". For example:
            <div>{@html marked("```python\nnumbers = [100, 200, 300]\nprint(numbers[0]) # outputs 100\nprint(numbers[-1]) # outputs 300")}</div>
            Index 0 refers to the 1st element, index 1 refers to the second, so on and so forth. You can also index starting from the end using -1. Lists are powerful data structures that have a lot nuances which you can get a hang of through practice. But for simplicity, you can consider list[index] to be a variable for a single value and perform operations as you normally would.
            <div>{@html marked("```python\nline = [1, 2, 3] # not the best, but it works\nslope = -line[0]/line[1]")}</div>
            You can also modify the elements of a list!
            <div>{@html marked("```python\nbatches_ranked = [2023, 2022, 2021, 2020]\nbatches_ranked[0] = 2024")}</div>
            And add new elements at the list!
            <div>{@html marked("```python\nreps = ['miko', 'paolo', 'krisha', 'drei']\nreps.push('kung sino iboto niyo')")}</div>
            And delete elements from the list!
            <div>{@html marked("```python\nreps = ['miko', 'paolo', 'krisha', 'drei']\ndel reps[0]")}</div>
        </div>
    </div>
</div>