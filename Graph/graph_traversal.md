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
```
A — B — C
|       |
D — — — E
```
BFS starting from A:
```
A → B → D → C → E
```
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
2. Depth First Search (DFS)

- Visits nodes as deep as possible first
- Uses Stack (or recursion)

How it works:
- Start from a node
- Go deep into one branch
- Backtrack and explore others

Example:

DFS starting from A:
```
A → B → C → E → D
```
Pseudo Code:

DFS(node):
    mark node as visited
    print node
    for each neighbor:
        if not visited:
            DFS(neighbor)

--------------------------------------------------

Time Complexity:

- BFS: O(V + E)
- DFS: O(V + E)

(V = Vertices, E = Edges)

--------------------------------------------------

Key Points:

- BFS uses Queue
- DFS uses Stack / Recursion
- Both visit all nodes
- BFS is useful for shortest path
- DFS is useful for exploring paths
