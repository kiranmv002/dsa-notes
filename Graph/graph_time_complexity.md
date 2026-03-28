Time Complexity of Graph Algorithms

Time complexity helps us understand
how graph algorithms perform
as the number of vertices and edges increase.

In graphs:
V = Number of vertices
E = Number of edges

--------------------------------------------------

1. Breadth First Search (BFS)

- Uses Queue
- Visits each vertex and edge once

Time Complexity:
O(V + E)

--------------------------------------------------

2. Depth First Search (DFS)

- Uses Stack or Recursion
- Visits each vertex and edge once

Time Complexity:
O(V + E)

--------------------------------------------------

3. Dijkstra Algorithm

- Finds shortest path in weighted graph

Time Complexity:
Simple method: O(V^2)
Using priority queue: O((V + E) log V)

--------------------------------------------------

4. Adjacency Matrix

- Space Complexity: O(V^2)
- Checking edge: O(1)

--------------------------------------------------

5. Adjacency List

- Space Complexity: O(V + E)
- Traversal: O(V + E)

--------------------------------------------------

Key Points:

- Graph algorithms depend on vertices and edges
- BFS and DFS are very efficient
- Adjacency list is better for sparse graphs
- Adjacency matrix is easier but uses more memory
- Choosing representation affects performance

Understanding time complexity
is important for selecting
the right graph algorithm.
