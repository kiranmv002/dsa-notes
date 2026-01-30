Stack Implementation Using Array

A stack can be implemented using an array.
In this method, elements are stored in a fixed-size array
and a variable is used to track the top of the stack.

Key Components:
- Array to store stack elements
- Top variable to point to the top element

Push Operation:
- Check if the stack is full
- Increment top
- Insert element at top position

Pop Operation:
- Check if the stack is empty
- Remove the element at top
- Decrement top

Example:
Initial Stack (size = 5):
Top = -1
Stack = [ , , , , ]

Push 10:
Top = 0
Stack = [10, , , , ]

Push 20:
Top = 1
Stack = [10, 20, , , ]

Pop:
Removes 20
Top = 0
Stack = [10, , , , ]

Array-based stack is easy to implement
but has a fixed size limitation.
