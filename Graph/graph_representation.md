Graphs can be represented in different ways
inside a computer system.

The two most common methods are:

1. Adjacency Matrix
2. Adjacency List

--------------------------------------------------

1. Adjacency Matrix

An Adjacency Matrix is a 2D array
used to represent connections between vertices.

Rows and columns represent vertices.

If there is an edge between two vertices,
the value is 1, otherwise it is 0.

Example Graph:
```
A — B
|   |
C — D
```
Adjacency Matrix:
```
    A B C D
A   0 1 1 0
B   1 0 0 1
C   1 0 0 1
D   0 1 1 0
```
Advantages:
- Simple to implement
- Easy to check if edge exists

Disadvantages:
- Uses more memory
- Not efficient for sparse graphs

--------------------------------------------------

2. Adjacency List

An Adjacency List represents the graph
as a list of connected vertices.

Each vertex stores a list
of its neighboring vertices.

Example Graph:
```
A — B
|   |
C — D
```
Adjacency List:
```
A → B, C
B → A, D
C → A, D
D → B, C
```
Advantages:
- Memory efficient
- Better for sparse graphs

Disadvantages:
- Slightly more complex implementation

--------------------------------------------------

Key Points

- Graphs can be represented using
  adjacency matrix or adjacency list
- Matrix is easier but uses more memory
- List is memory efficient
- Choice depends on graph density
