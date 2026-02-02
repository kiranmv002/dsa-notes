Stack Time Complexity

Time complexity describes how much time
stack operations take based on input size.

Stack operations are generally very efficient
because they work on only one end of the data structure.

How it works:
- All stack operations are performed at the top
- No shifting of elements is required
- Access is restricted to the top element only

Push Operation:
- Adds an element to the top of the stack
- Takes constant time

Pop Operation:
- Removes the top element from the stack
- Takes constant time

Peek Operation:
- Returns the top element without removing it
- Takes constant time

Example:
Stack: [5, 10, 15]

Push 20:
Stack becomes: [5, 10, 15, 20]

Pop:
Removes 20
Stack becomes: [5, 10, 15]

Pseudo Code:

Push(x):
    top = top + 1
    stack[top] = x

Pop():
    if top == -1:
        print "Stack is empty"
    else:
        top = top - 1

Time Complexity:
Push Operation: O(1)
Pop Operation: O(1)
Peek Operation: O(1)

Key Points:
- Stack operations are very fast
- No traversal is required
- Performance does not depend on stack size

Stack is an efficient data structure
when insertion and deletion are needed frequently.
