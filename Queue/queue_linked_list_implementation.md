Queue Implementation Using Linked List

A Queue can be implemented using a linked list.
In this approach, elements are stored as nodes
and dynamic memory is used.

Structure:
- Each node contains data and a link to the next node
- Front points to the first node
- Rear points to the last node

How it works:
- Enqueue inserts a new node at the rear
- Dequeue removes the node from the front
- FIFO order is always maintained

Enqueue Operation:
- Create a new node
- If the queue is empty, set both front and rear to the new node
- Otherwise, link the new node at the end and update rear

Dequeue Operation:
- Check if the queue is empty
- Remove the front node
- Update front to the next node

Example:
Initial Queue:
Front → null

Enqueue 10:
Front → 10 → null
Rear  → 10

Enqueue 20:
Front → 10 → 20 → null
Rear  → 20

Dequeue:
Removes 10
Front → 20 → null

Pseudo Code:

Enqueue(x):
    create newNode
    newNode.data = x
    newNode.next = null
    if rear == null:
        front = rear = newNode
    else:
        rear.next = newNode
        rear = newNode

Dequeue():
    if front == null:
        print "Queue is empty"
    else:
        temp = front
        front = front.next
        if front == null:
            rear = null
        delete temp

Time Complexity:

Enqueue Operation: O(1)
Dequeue Operation: O(1)

Key Points:
- No fixed size limitation
- Efficient insertion and deletion
- Uses dynamic memory

Linked list based queue is flexible
and suitable when queue size is not known in advance.
