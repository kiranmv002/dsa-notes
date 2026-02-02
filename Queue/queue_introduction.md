Queue Introduction

A Queue is a linear data structure
that follows the First In, First Out (FIFO) principle.
The element added first is the first one to be removed.

How it works:
- Elements are inserted at the rear (end)
- Elements are removed from the front (beginning)
- Operations follow FIFO order

Basic Operations:
- Enqueue: Add an element to the queue
- Dequeue: Remove an element from the queue
- Front: View the front element

Example:
Initial Queue: [ ]

Enqueue 10:
Queue becomes: [10]

Enqueue 20:
Queue becomes: [10, 20]

Dequeue:
Removes 10
Queue becomes: [20]

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

Key Points:
- Queue works on FIFO principle
- Insertion and deletion are efficient
- Used in scheduling and resource management

Queue is widely used in real-life applications
such as ticket booking systems and printers.
