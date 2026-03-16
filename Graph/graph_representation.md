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

A — B
|   |
C — D

Adjacency Matrix:

    A B C D
A   0 1 1 0
B   1 0 0 1
C   1 0 0 1
D   0 1 1 0

Advantages:
- Simple to implement
- Easy to check if edge exists

Disadvantages:
- Uses more memory
- Not efficient for sparse graphs

--------------------------------------------------
