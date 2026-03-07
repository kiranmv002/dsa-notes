Time Complexity in Recursion

Time complexity in recursion measures
how the number of recursive calls grows
as the input size increases.

Understanding time complexity is important
to analyze the efficiency of recursive algorithms.

How Recursion Works:

- A recursive function calls itself
- Each call creates a new function call
- The number of calls determines time complexity

Example 1: Factorial

factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

Number of calls:
factorial(5) → factorial(4) → factorial(3) → factorial(2) → factorial(1)

Total calls = n

Time Complexity:
O(n)

--------------------------------------------------

Example 2: Fibonacci

fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

Recursive calls grow rapidly:

fibonacci(5)
→ fibonacci(4) + fibonacci(3)
→ fibonacci(3) + fibonacci(2) + fibonacci(2) + fibonacci(1)

Time Complexity:
O(2^n)

--------------------------------------------------

Space Complexity in Recursion

Recursion uses the call stack.

Example:
factorial(n)

Each recursive call uses stack memory.

Maximum stack depth = n

Space Complexity:
O(n)

--------------------------------------------------

Key Points:

- Time complexity depends on number of recursive calls
- Linear recursion usually gives O(n)
- Tree recursion can give exponential complexity
- Space complexity depends on recursion depth
- Efficient recursion requires proper base case

Understanding recursion complexity
helps in designing efficient algorithms.
