Bubble Sort Algorithm

Bubble Sort is a simple sorting technique.
It works by repeatedly comparing adjacent elements
and swapping them if they are in the wrong order.

How it works:
- Start from the first element
- Compare it with the next element
- Swap if the first is greater than the next
- Repeat this process for all elements
- Continue passes until the list is sorted

Example:
Array: [5, 3, 8, 2]

Pass 1:
5 and 3 → swap → [3, 5, 8, 2]
5 and 8 → no swap
8 and 2 → swap → [3, 5, 2, 8]

Pass 2:
3 and 5 → no swap
5 and 2 → swap → [3, 2, 5, 8]

Pass 3:
3 and 2 → swap → [2, 3, 5, 8]

Sorted Array:
[2, 3, 5, 8]

Pseudo Code:
BubbleSort(arr):
    for i from 0 to n-1:
        for j from 0 to n-i-2:
            if arr[j] > arr[j+1]:
                swap(arr[j], arr[j+1])

Time Complexity:
Best Case: O(n)
Worst Case: O(n²)

Bubble Sort is easy to understand but not efficient
for large datasets.
