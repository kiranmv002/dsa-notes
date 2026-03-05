Common Recursion Problems

Recursion is often used to solve problems
that can be broken into smaller subproblems.

Many classical algorithm problems
are naturally solved using recursion.

Below are some common recursion problems.

--------------------------------------------------

1. Factorial of a Number

Factorial of n (n!) is the product
of all positive integers up to n.

Example:
5! = 5 × 4 × 3 × 2 × 1 = 120

Recursive Example:

factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

--------------------------------------------------

2. Fibonacci Sequence

Fibonacci sequence is defined as:

F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2)

Example:

fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

--------------------------------------------------
