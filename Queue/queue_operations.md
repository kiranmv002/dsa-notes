Queue Operations

Queue supports basic operations that allow
insertion and removal of elements.
It follows the First In, First Out (FIFO) principle.

How it works:
- Elements are inserted at the rear of the queue
- Elements are removed from the front of the queue
- The first inserted element is removed first

Enqueue Operation:
- Adds an element to the rear of the queue

Example:
Initial Queue: [10, 20]
Enqueue 30
Queue becomes: [10, 20, 30]

Dequeue Operation:
- Removes the element from the front of the queue

Example:
Initial Queue: [10, 20, 30]
Dequeue
Queue becomes: [20, 30]

Front Operation:
- Returns the front element without removing it

Example:
Front element is 20

Pseudo Code:

Enqueue(x):
    rear = rear + 1
    queue[rear] = x

Dequeue():
    if queue is empty:
        print "Queue is empty"
    else:
        front = front + 1

Time Complexity:
Enqueue Operation: O(1)
Dequeue Operation: O(1)
Front Operation: O(1)

Key Points:
- Queue operations are simple and efficient
- FIFO order is always maintained
- Used in scheduling and data processing
