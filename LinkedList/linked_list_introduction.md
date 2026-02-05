
A Linked List is a linear data structure
where elements are stored in nodes.
Each node contains data and a reference to the next node.

Unlike arrays, linked lists do not store elements
in contiguous memory locations.

How it works:
- Each node has two parts: data and next pointer
- The first node is called the head
- The last node points to null

Types of Linked List:
- Singly Linked List
- Doubly Linked List
- Circular Linked List

Example:
Nodes: 10 → 20 → 30 → null

Here,
10 is the head node
30 is the last node

Pseudo Code:

CreateNode(x):
    node.data = x
    node.next = null
    return node

Time Complexity:
Accessing an element: O(n)
Insertion at beginning: O(1)

Key Points:
- Dynamic size
- Efficient insertion and deletion
- Extra memory needed for pointers

Linked List is useful
when frequent insertion and deletion are required.
