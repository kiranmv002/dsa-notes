Time Complexity of Heap

Time complexity helps us understand
how heap operations perform
as the number of elements increases.

Heap is a Complete Binary Tree,
so its height is approximately log n.

Because operations depend on tree height,
most heap operations take O(log n) time.

Common Heap Operations:

1. Insertion
- Insert element at last position
- Perform heapify up
Time Complexity: O(log n)

2. Deletion (Remove Root)
- Replace root with last element
- Perform heapify down
Time Complexity: O(log n)

3. Heapify
- Adjust heap to maintain heap property
Time Complexity: O(log n)

4. Access Root
- Directly access first element
Time Complexity: O(1)

5. Build Heap
- Convert array into heap
Time Complexity: O(n)

Why Build Heap is O(n)?

Although heapify takes O(log n),
building heap from bottom-up
reduces total work,
so overall complexity becomes O(n).

Comparison with Other Structures:

Heap:
- Insert: O(log n)
- Delete: O(log n)
- Access max/min: O(1)

Binary Search Tree:
- Average: O(log n)
- Worst case: O(n)

Key Points:
- Performance depends on height of heap
- Height of heap is log n
- Build Heap is O(n)
- Very efficient for priority-based operations
