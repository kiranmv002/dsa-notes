Recursion vs Iteration

Recursion and Iteration are two different
approaches to solve problems in programming.

Both are used to repeat a set of instructions,
but they work in different ways.

Recursion:

- A function calls itself
- Uses base case and recursive case
- Uses call stack memory
- Suitable for tree and divide-and-conquer problems

Example (Factorial using Recursion):

factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

--------------------------------------------------

Iteration:

- Uses loops (for, while)
- No function calls involved
- Does not use extra stack memory
- Generally faster and memory efficient

Example (Factorial using Iteration):

factorial(n):
    result = 1
    for i from 1 to n:
        result = result * i
    return result

--------------------------------------------------

Comparison:

Recursion:
- Easier to write for complex problems
- Uses extra memory (call stack)
- Can cause stack overflow if too deep

Iteration:
- More memory efficient
- Slightly faster in most cases
- Sometimes harder to write for tree problems

Time Complexity:
Both approaches usually have the same time complexity.

Space Complexity:
Recursion: O(n) due to call stack
Iteration: O(1)

Key Points:

- Recursion is elegant and clean
- Iteration is efficient and practical
- Choose based on problem requirement
- Many recursive problems can be converted to iterative form
