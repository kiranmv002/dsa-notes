Linked List Operations

A Linked List is a linear data structure
where elements are stored in nodes.
Each node contains data and a reference
to the next node in the list.

Linked lists allow easy insertion
and deletion of elements.

How it works:
- Each node stores data and a link to the next node
- The first node is called the head
- The last node points to null

Insertion Operation:
Insertion means adding a new node to the linked list.

Types of Insertion:
1. At the beginning
2. At the end
3. At a specific position

Example (Insert at Beginning):
Initial List:
10 → 20 → 30 → null

Insert 5 at beginning:
5 → 10 → 20 → 30 → null

Deletion Operation:
Deletion means removing a node from the linked list.

Types of Deletion:
1. Delete from beginning
2. Delete from end
3. Delete a specific node

Example (Delete from Beginning):
Initial List:
5 → 10 → 20 → 30 → null

Delete first node:
10 → 20 → 30 → null

Pseudo Code:

InsertAtBeginning(x):
    create newNode
    newNode.data = x
    newNode.next = head
    head = newNode

DeleteFromBeginning():
    if head == null:
        print "List is empty"
    else:
        head = head.next

Time Complexity:
Insertion at beginning: O(1)
Deletion at beginning: O(1)

Key Points:
- Linked List allows dynamic memory allocation
- Insertion and deletion are efficient
- No shifting of elements is required

Linked list operations are widely used
when frequent insertions and deletions are needed.
