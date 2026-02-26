Working of Recursion and Call Stack

Recursion works using the Call Stack.
Each time a function is called,
it is stored in memory until it finishes execution.

This memory structure is called the Call Stack.

How Recursion Works:

1. A function calls itself.
2. Each function call is added to the call stack.
3. When the base case is reached,
   the function starts returning values.
4. Functions are removed from the stack one by one.

Example: Factorial of 4

factorial(4)
= 4 × factorial(3)
= 4 × 3 × factorial(2)
= 4 × 3 × 2 × factorial(1)
= 4 × 3 × 2 × 1

Call Stack Flow:

Step 1:
factorial(4) → waiting for factorial(3)

Step 2:
factorial(3) → waiting for factorial(2)

Step 3:
factorial(2) → waiting for factorial(1)

Step 4:
factorial(1) → base case reached

Now returning:

factorial(1) returns 1
factorial(2) returns 2
factorial(3) returns 6
factorial(4) returns 24

Important Concept: Stack Memory

- Every recursive call uses stack memory
- If recursion is too deep,
  it may cause Stack Overflow
- Base case prevents infinite recursion

Time Complexity:
Depends on number of recursive calls.

Space Complexity:
O(n) due to call stack usage.

Key Points:

- Recursion uses Call Stack
- Base case is mandatory
- Each call waits for smaller call to finish
- Memory usage increases with recursion depth

Understanding call stack is very important
before solving advanced recursion problems.
