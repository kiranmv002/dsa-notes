Graph traversal means visiting all the vertices
of a graph in a systematic way.

There are two main traversal methods:

1. Breadth First Search (BFS)
2. Depth First Search (DFS)

--------------------------------------------------

1. Breadth First Search (BFS)

- Visits nodes level by level
- Uses Queue data structure

How it works:
- Start from a node
- Visit all its neighbors first
- Then move to next level

Example:

Graph:
A — B — C
|       |
D — — — E

BFS starting from A:
A → B → D → C → E
 
Pseudo Code:

BFS(start):
    create queue
    mark start as visited
    enqueue start

   while queue not empty:
        node = dequeue
        print node
        for each neighbor:
            if not visited:
                mark visited
                enqueue

--------------------------------------------------
