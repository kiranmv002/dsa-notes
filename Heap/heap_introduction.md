Heap Introduction

A Heap is a special type of Binary Tree
that follows a specific property called the Heap Property.

Heap is mainly used to implement Priority Queue
and for efficient sorting.

Basic Properties of Heap:

1. It is a Complete Binary Tree
   - All levels are completely filled
   - Last level is filled from left to right

2. It follows Heap Property

There are two types of Heap:

1. Max Heap
   - Parent node is greater than or equal to its children
   - The largest element is at the root

Example (Max Heap):

        50
       /  \
     30    40
    /  \
   10   20

2. Min Heap
   - Parent node is smaller than or equal to its children
   - The smallest element is at the root

Example (Min Heap):

        10
       /  \
     20    30
    /  \
   40   50

How it works:
- Heap is represented as a Complete Binary Tree
- It is usually implemented using an array
- Parent and child relationships are calculated using index

Applications of Heap:
- Priority Queue
- Heap Sort
- Finding kth largest/smallest element

Key Points:
- Heap is a Complete Binary Tree
- Root contains the highest or lowest value
- Very efficient for priority-based problems
