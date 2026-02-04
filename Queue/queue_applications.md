Applications of Queue

A Queue is a data structure that follows
the First In, First Out (FIFO) principle.
Because of this behavior, queues are widely
used in many real-life and computing applications.

How it works:
- Elements are added at the rear of the queue
- Elements are removed from the front
- The first inserted element is processed first

Common Applications of Queue:

1. CPU Scheduling
Processes waiting for CPU time are stored in a queue
and are executed in the order they arrive.

2. Printer Queue
Print jobs are placed in a queue and printed
one after another in FIFO order.

3. Breadth First Search (BFS)
Queues are used to traverse graphs and trees level by level.

4. Ticket Booking Systems
People waiting to buy tickets are managed using a queue
to ensure fair service.

5. Data Buffers
Queues are used to store data temporarily
during data transfer between devices.

Example:
Queue of tasks: [Task1, Task2, Task3]

Process Task1 → Queue becomes [Task2, Task3]
Process Task2 → Queue becomes [Task3]

Pseudo Code:

ProcessQueue():
    while queue is not empty:
        task = dequeue()
        process(task)

Time Complexity:
Enqueue Operation: O(1)
Dequeue Operation: O(1)

Key Points:
- Queue maintains order of processing
- Useful for scheduling and resource management
- Ensures fairness in data handling

Queues play an important role
in both system-level and application-level programming.
