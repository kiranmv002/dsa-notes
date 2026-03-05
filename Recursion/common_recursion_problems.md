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

3. Sum of First N Natural Numbers

Example:
Sum of first 5 numbers
= 5 + 4 + 3 + 2 + 1

Recursive Example:

sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)

--------------------------------------------------

4. Printing Numbers

Example: Print numbers from n to 1

printNumbers(n):
    if n == 0:
        return
    print(n)
    printNumbers(n-1)

--------------------------------------------------

Key Points:

- Recursion works best for problems
  that can be divided into smaller parts
- Base case is required to stop recursion
- Recursive call reduces the problem size
- Widely used in trees, graphs, and divide-and-conquer algorithms
