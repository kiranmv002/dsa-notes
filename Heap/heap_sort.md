Heap Sort

Heap Sort is a comparison-based sorting algorithm
that uses the Heap data structure.

It works by converting the array into a Max Heap
and repeatedly extracting the maximum element.

How Heap Sort Works:

Step 1:
Build a Max Heap from the given array.

Step 2:
Swap the root (maximum element)
with the last element of the heap.

Step 3:
Reduce the heap size by one.

Step 4:
Heapify the root to maintain heap property.

Step 5:
Repeat until heap size becomes 1.

Example:

Given Array:
[4, 10, 3, 5, 1]

After building Max Heap:
[10, 5, 3, 4, 1]

Swap 10 with last element:
[1, 5, 3, 4, 10]

Heapify remaining elements:
[5, 4, 3, 1, 10]

Repeat process until sorted:

Final Sorted Array:
[1, 3, 4, 5, 10]

Pseudo Code:

HeapSort(arr):
    BuildMaxHeap(arr)
    for i from n-1 to 1:
        swap arr[0] and arr[i]
        heapify(arr, 0, i)

Time Complexity:
Best Case: O(n log n)
Average Case: O(n log n)
Worst Case: O(n log n)

Space Complexity:
O(1) (In-place sorting)

Advantages:
- Efficient for large datasets
- Does not require extra memory

Disadvantages:
- Not stable
- Slightly slower than Quick Sort in practice

Key Points:
- Based on Max Heap
- Always takes O(n log n)
- Useful for priority-based sorting
