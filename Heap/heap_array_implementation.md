
Heap Implementation using Array

Heap is usually implemented using an array
because it is a Complete Binary Tree.

In array representation:
- Root is stored at index 0
- For any element at index i:

Parent index = (i - 1) / 2
Left child index = 2i + 1
Right child index = 2i + 2

This makes heap efficient and easy to manage.

Example:

Array representation of Max Heap:

Index:  0   1   2   3   4
Value: [50, 30, 40, 10, 20]

Tree form:

         50
        /  \
      30    40
     /  \
    10   20

How it works:

1. Insertion
- Add element at the end of array
- Perform heapify up
- Maintain heap property

2. Deletion
- Remove root element
- Replace root with last element
- Perform heapify down
- Maintain heap property

Advantages of Array Implementation:
- No need for pointers
- Easy parent-child calculation
- Memory efficient

Time Complexity:
Insertion: O(log n)
Deletion: O(log n)
Access root: O(1)

Key Points:
- Heap is always a Complete Binary Tree
- Array representation is efficient
- Used in Priority Queue and Heap Sort
