Types of Linked List

A Linked List can be classified into different types
based on how the nodes are connected.

Each type of linked list is used
for different purposes and requirements.

How it works:
- Data is stored in nodes
- Nodes are connected using links
- The structure depends on the type of linked list

Types of Linked List:

1. Singly Linked List
- Each node contains data and a link to the next node
- Traversal is possible in one direction only

Example:
10 → 20 → 30 → null

2. Doubly Linked List
- Each node contains data, a link to the next node,
  and a link to the previous node
- Traversal is possible in both directions

Example:
null ← 10 ↔ 20 ↔ 30 → null

3. Circular Linked List
- The last node points back to the first node
- No node points to null

Example:
10 → 20 → 30
↑             ↓
← ← ← ← ← ← ←

Pseudo Code (Traversal in Singly Linked List):

TraverseList():

