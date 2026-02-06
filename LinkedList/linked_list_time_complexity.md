Time Complexity of Linked List

Time complexity describes how the performance
of an operation changes with input size.

Understanding time complexity helps in choosing
the correct data structure for a problem.

How it works:
- Linked list operations depend on traversal
- Accessing elements requires moving through nodes
- Position of operation affects performance

Time Complexity of Operations:

Accessing an Element:
- Accessing any element requires traversal
- Time Complexity: O(n)

Insertion Operations:
- Insert at beginning: O(1)
- Insert at end: O(n)
- Insert at a given position: O(n)

Deletion Operations:
- Delete from beginning: O(1)
- Delete from end: O(n)
- Delete a specific node: O(n)

Traversal:
- Visiting all nodes one by one
- Time Complexity: O(n)

Pseudo Code (Traversal):

TraverseList():
    temp = head
    while temp != null:
        print temp.data
        temp = temp.next

Key Points:
- Fast insertion and deletion at beginning
- Slower access compared to arrays
- No direct indexing available

Linked lists are preferred when
frequent insertions and deletions are required,
and random access is not needed.
