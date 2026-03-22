Dijkstra Algorithm is used to find
the shortest path from a source node
to all other nodes in a weighted graph.

It works only for graphs with
non-negative edge weights.

Basic Idea:

- Start from the source node
- Assign distance = 0 to source
- Assign infinity to all other nodes
- Update distances of neighbors
- Always choose the node with smallest distance

Example:

Graph:

A —1— B
|     |
4     2
|     |
C —3— D

Goal:
Find shortest path from A

Steps:

Initial distances:
A = 0
B = ∞
C = ∞
D = ∞

Step 1:
Visit A
Update neighbors:
B = 1
C = 4

Step 2:
Visit B (smallest distance = 1)
Update:
D = 1 + 2 = 3

Step 3:
Visit D (distance = 3)
Update:
C = min(4, 3 + 3 = 6) → 4

Step 4:
Visit C

Final shortest distances:
A = 0
B = 1
C = 4
D = 3

Pseudo Code:

Dijkstra(source):
    set distance[source] = 0
    for all other nodes:
        distance = infinity

    while unvisited nodes exist:
        pick node with smallest distance
        mark it as visited

        for each neighbor:
            newDist = currentDist + weight
            if newDist < neighbor distance:
                update distance
