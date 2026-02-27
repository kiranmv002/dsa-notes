Types of Recursion

Recursion can be classified into different types
based on how the recursive function calls itself.

Understanding types of recursion
helps in solving complex problems easily.

1. Direct Recursion

A function calls itself directly.

Example:

printNumbers(n):
    if n == 0:
        return
    print(n)
    printNumbers(n-1)

Here, the function directly calls itself.

--------------------------------------------------

2. Indirect Recursion

A function calls another function,
and that function calls the first one.

Example:

functionA(n):
    if n <= 0:
        return
    print(n)
    functionB(n-1)

functionB(n):
    if n <= 0:
        return
    print(n)
    functionA(n-1)

--------------------------------------------------

3. Tail Recursion

The recursive call is the last statement
in the function.

Example:

printNumbers(n):
    if n == 0:
        return
    print(n)
    return printNumbers(n-1)

Tail recursion is more memory efficient
in some programming languages.

--------------------------------------------------

4. Head Recursion

The recursive call happens first,
before other operations.

Example:

printNumbers(n):
    if n == 0:
        return
    printNumbers(n-1)
    print(n)

--------------------------------------------------

5. Tree Recursion

A function calls itself multiple times.

Example:

fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

Here, each call creates multiple recursive calls,
forming a tree-like structure.

--------------------------------------------------

Key Points:

- Direct recursion is most common
- Tail recursion can be optimized
- Head recursion processes after recursive call
- Tree recursion creates multiple branches
- Choice depends on problem requirement
