Linked List Implementation

A Linked List is implemented using nodes.
Each node contains two parts:
- Data
- A reference to the next node

The list is accessed using a pointer called head
which points to the first node.

How it works:
- Memory is allocated dynamically for each node
- Nodes are connected using links
- The last node points to null

Node Structure:
Data | Next

Implementation Steps:
1. Create a node structure
2. Allocate memory for a new node
3. Assign data to the node
4. Link the node to the list

Example:
Creating a Linked List

Create node with data 10:
Head → 10 → null

Add node with data 20:
Head → 10 → 20 → null

Add node with data 30:
Head → 10 → 20 → 30 → null

Pseudo Code:

CreateNode(x):
    newNode = allocate memory
    newNode.data = x
    newNode.next = null
    return newNode

InsertAtEnd(x):
    newNode = CreateNode(x)
    if head == null:
        head = newNode
    else:
        temp = head
        while temp.next != null:
            temp = temp.next
        temp.next = newNode

Time Complexity:
Insertion at end: O(n)
Traversal: O(n)

Key Points:
- Dynamic memory allocation
- Efficient insertion and deletion
- No need to define size in advance

Linked List implementation is useful
when memory flexibility is required.
