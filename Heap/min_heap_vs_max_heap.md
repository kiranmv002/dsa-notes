Min Heap vs Max Heap

Heap is divided into two main types
based on the heap property.

1. Max Heap
2. Min Heap

1. Max Heap

- Parent node is greater than or equal to its children
- The largest element is always at the root

Example:

        50
       /  \
     30    40
    /  \
   10   20

In Max Heap:
Root contains the maximum value.

Used when:
- We need quick access to largest element
- Used in priority queues (highest priority first)

--------------------------------------------------

2. Min Heap

- Parent node is smaller than or equal to its children
- The smallest element is always at the root

Example:

        10
       /  \
     20    30
    /  \
   40   50

In Min Heap:
Root contains the minimum value.

Used when:
- We need quick access to smallest element
- Used in scheduling systems

--------------------------------------------------

Comparison:

Max Heap:
- Root = Maximum value
- Used for largest element problems

Min Heap:
- Root = Minimum value
- Used for smallest element problems

Time Complexity (Both):
Insertion: O(log n)
Deletion: O(log n)
Access Root: O(1)

Key Points:
- Both are Complete Binary Trees
- Only difference is heap property
- Selection depends on problem requirement
