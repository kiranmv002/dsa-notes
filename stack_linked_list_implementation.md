Stack Using Linked List

Stack using Linked List is an implementation of stack
where elements are stored as nodes.
It follows the Last In, First Out (LIFO) principle.

Instead of using an array, a linked list is used
to dynamically manage memory.

How it works:
- The top of the stack is represented by the head node
- New elements are added at the beginning of the list
- Elements are removed from the beginning of the list

Push Operation:
- Create a new node
- Store data in the node
- Link the node to the current top
- Update top to the new node

Pop Operation:
- Check if the stack is empty
- Remove the top node
- Update top to the next node

Example:
Initial Stack:
Top → null

Push 10:
Top → 10 → null

Push 20:
Top → 20 → 10 → null

Pop:
Element removed: 20
Top → 10 → null

Pseudo Code:

Push(x):
    create newNode
    newNode.data = x
    newNode.next = top
    top = newNode

Pop():
    if top == null:
        print "Stack is empty"
    else:
        temp = top
        top = top.next
        delete temp

Time Complexity:
Push Operation: O(1)
Pop Operation: O(1)

Key Points:
- No fixed size limitation
- Efficient insertion and deletion
- Uses dynamic memory allocation

Stack using linked list is flexible
and suitable when stack size is not known in advance.
