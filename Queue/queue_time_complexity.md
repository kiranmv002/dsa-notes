Queue Time Complexity

Time complexity explains how much time
queue operations take based on input size.

Queue operations are efficient because
they are performed only at the front and rear.

How it works:
- Enqueue adds an element at the rear
- Dequeue removes an element from the front
- No shifting of elements is required

Enqueue Operation:
- Adds an element to the queue
- Takes constant time

Dequeue Operation:
- Removes the front element
- Takes constant time

Front Operation:
- Returns the front element without removing it
- Takes constant time

Example:
```
Queue: [10, 20, 30]

Enqueue 40:
Queue becomes: [10, 20, 30, 40]

Dequeue:
Removes 10
Queue becomes: [20, 30, 40]
```
Pseudo Code:

Enqueue(x):

if rear == MAX-1
    print "Queue Overflow"

else
    rear = rear + 1
    queue[rear] = x

  if front == -1
        front = 0

Dequeue():


if front == -1 OR front > rear
    print "Queue Underflow"

else
    item = queue[front]
    front = front + 1

return item
