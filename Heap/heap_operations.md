Heap Operations

Heap supports basic operations
that maintain the heap property.

Main Operations in Heap:

1. Insertion
2. Deletion
3. Heapify

1. Insertion in Heap

Steps:
- Insert the new element at the last position
- Compare it with its parent
- If heap property is violated, swap them
- Repeat until heap property is restored

This process is called "Heapify Up".

Example (Max Heap):

Insert 60:

        50
       /  \
     30    40

After inserting 60 at last:

        50
       /  \
     30    40
    /
   60

Swap 60 with 30:

        50
       /  \
     60    40
    /
   30

Swap 60 with 50:

        60
       /  \
     50    40
    /
   30

Heap property restored.

2. Deletion in Heap

- Remove the root element
- Replace it with the last element
- Compare with children
- Swap with larger child (Max Heap)
- Repeat until heap property is restored

This process is called "Heapify Down".

3. Heapify

Heapify ensures that the heap
maintains its heap property
after insertion or deletion.

Time Complexity:

Insertion: O(log n)
Deletion: O(log n)
Heapify: O(log n)

Key Points:

- Heap is usually implemented using array
- Parent index = (i - 1) / 2
- Left child index = 2i + 1
- Right child index = 2i + 2
- Operations depend on tree height

Heap operations are efficient
for priority-based problems.
