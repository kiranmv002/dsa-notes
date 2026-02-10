Applications of Stack

A Stack is a data structure that follows
the Last In, First Out (LIFO) principle.
Because of this behavior, stacks are widely
used in many real-life and programming applications.

How it works:
- Elements are added to the top of the stack
- The most recently added element is accessed first
- Operations follow LIFO order

Common Applications of Stack:

1. Function Calls
When a function is called, its details are stored
in a stack. After execution, it is removed from the stack.

2. Undo and Redo Operations
Actions performed by a user are stored in a stack.
Undo removes the latest action, redo restores it.

3. Expression Evaluation
Stacks are used to evaluate expressions
such as postfix and prefix expressions.

4. Reversing Data
Stacks can reverse strings, arrays, or lists
by pushing elements and popping them out.

Example:
Reversing a string "ABC"

Push:
A → Stack: [A]
B → Stack: [A, B]
C → Stack: [A, B, C]

Pop:
C → B → A

Reversed string: "CBA"

Pseudo Code:
ReverseString(str):
    for each character ch in str:
        push(ch)
    while stack is not empty:
        pop and print character

Time Complexity:

Push Operation: O(1)
Pop Operation: O(1)

Key Points:
- Stack is useful when last action matters
- Simple and efficient data structure
- Widely used in real-time applications

Stacks play an important role
in both system-level and application-level programming.
