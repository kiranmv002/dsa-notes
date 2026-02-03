Queue Implementation Using Array

A Queue can be implemented using an array.
In this approach, elements are stored in a fixed-size array
and two variables are used to manage the queue.

Key Components:
- Array to store queue elements
- Front variable to point to the first element
- Rear variable to point to the last element

How it works:
- Enqueue inserts an element at the rear position
- Dequeue removes an element from the front position
- FIFO order is maintained

Enqueue Operation:
- Check if the queue is full
- Increment rear
- Insert the element at rear position

Dequeue Operation:
- Check if the queue is empty
- Remove the element at front
- Increment front

Example:
Queue size = 5

Initial Queue:
Front = -1, Rear = -1
Queue = [ , , , , ]

Enqueue 10:
Front = 0, Rear = 0
Queue = [10, , , , ]

Enqueue 20:
Front = 0, Rear = 1
Queue = [10, 20, , , ]

Dequeue:
Removes 10
Front = 1
Queue = [ , 20, , , ]

Pseudo Code:

Enqueue(x):
    if rear == size - 1:
        print "Queue is full"
    else:
        if front == -1:
            front = 0
        rear = rear + 1
        queue[rear] = x

Dequeue():
    if front == -1 or front > rear:
        print "Queue is empty"
    else:
        front = front + 1

Time Complexity:
Enqueue Operation: O(1)
Dequeue Operation: O(1)

Key Points:
- Simple to implement
- Uses fixed-size memory
- Not flexible when queue size increases

Array-based queue is suitable
when the maximum size is known in advance.
