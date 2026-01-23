Linear Search Algorithm

Linear Search is the simplest searching technique.
It searches for an element by checking each value one after another.

How it works:
- Start from the first element of the list
- Compare each element with the target value
- If a match is found, stop the search
- If the end is reached, the element is not present

Important Note:
Linear Search works on both sorted and unsorted data.

Example:
Array: [10, 25, 30, 45, 60]
Key: 45

Process:
10 → not match  
25 → not match  
30 → not match  
45 → match found  

Element found at index 3

Pseudo Code:
LinearSearch(arr, key):
    for i from 0 to length(arr) - 1:
        if arr[i] == key:
            return i
    return -1

Time Complexity:
Best Case: O(1)
Worst Case: O(n)

This method is easy to understand but slow for large data sets.
