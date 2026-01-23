// Binary Search Algorithm

Binary Search is an efficient technique used to search an element in a sorted array.
Instead of scanning elements one by one, it repeatedly divides the search space into half.

How it works:
- Identify the middle element of the array
- If the element matches the key → success
- If the key is smaller → move to left subarray
- If the key is greater → move to right subarray
- Continue until element is found or range becomes empty

⚠️ Note: Binary Search only works on sorted arrays.

Example:
Array: [3, 5, 7, 9, 11, 13]
Key: 9

Process:
Middle = 7 → key is greater → shift right
Middle = 11 → key is smaller → shift left
Middle = 9 → element found

Pseudo Code:
BinarySearch(arr, key):
    start = 0
    end = size(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == key:
            return mid
        else if key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return -1

Time Complexity:
- Best Case: O(1)
- Worst Case: O(log n)

Used widely in large datasets for faster searching.
