Recursion Introduction

Recursion is a programming technique
where a function calls itself
to solve a smaller part of a problem.

It is mainly used to solve problems
that can be broken down into smaller subproblems.

Basic Concept:

A recursive function has two main parts:

1. Base Case
- The condition where recursion stops
- Prevents infinite function calls

2. Recursive Case
- The function calls itself
- Works on a smaller version of the problem

How it works:

- Function calls itself
- Problem size becomes smaller each time
- Stops when base case is reached

Example: Factorial of a Number

Factorial of n (n!) =
n × (n-1) × (n-2) × ... × 1

Example:
5! = 5 × 4 × 3 × 2 × 1

Recursive Definition:

factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

Step-by-step:

factorial(5)
= 5 × factorial(4)
= 5 × 4 × factorial(3)
= 5 × 4 × 3 × factorial(2)
= 5 × 4 × 3 × 2 × factorial(1)
= 5 × 4 × 3 × 2 × 1

Key Points:

- Must have a base case
- Recursive call should reduce problem size
- Uses function call stack
- Very useful for tree and divide-and-conquer problems

Recursion is a powerful concept
in Data Structures and Algorithms.
