Selection Sort Algorithm

Selection Sort is a simple sorting technique.
It works by repeatedly selecting the smallest element
from the unsorted part of the list and placing it at the beginning.

How it works:
- Divide the list into sorted and unsorted parts
- Find the minimum element from the unsorted part
- Swap it with the first unsorted element
- Move the boundary of the sorted part forward
- Repeat until the list is sorted

Example:
Array: [6, 3, 5, 2]

Pass 1:
Minimum element is 2 → swap with 6
Array becomes: [2, 3, 5, 6]

Pass 2:
Minimum element is 3 → already in correct position

Pass 3:
Minimum element is 5 → already in correct position

Sorted Array:
[2, 3, 5, 6]

Pseudo Code:
SelectionSort(arr):
    for i from 0 to n-1:
        minIndex = i
        for j from i+1 to n-1:
            if arr[j] < arr[minIndex]:
                minIndex = j
        swap(arr[i], arr[minIndex])

Time Complexity:
Best Case: O(n²)
Worst Case: O(n²)

Selection Sort is easy to understand
but not suitable for large datasets.
