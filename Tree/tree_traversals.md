Tree Traversals

Tree Traversal means visiting each node
of the tree exactly once in a specific order.

Traversal is very important to process
or retrieve data from a tree.

Types of Tree Traversal:

1. Inorder Traversal (Left → Root → Right)
- Visit left subtree
- Visit root node
- Visit right subtree

2. Preorder Traversal (Root → Left → Right)
- Visit root node
- Visit left subtree
- Visit right subtree

3. Postorder Traversal (Left → Right → Root)
- Visit left subtree
- Visit right subtree
- Visit root node

Example Binary Tree:

        A
       / \
      B   C
     / \
    D   E

Inorder Traversal:
D → B → E → A → C

Preorder Traversal:
A → B → D → E → C

Postorder Traversal:
D → E → B → C → A

Pseudo Code:

Inorder(node):
    if node != null:
        Inorder(node.left)
        print node.data
        Inorder(node.right)

Preorder(node):
    if node != null:
        print node.data
        Preorder(node.left)
        Preorder(node.right)

Postorder(node):
    if node != null:
        Postorder(node.left)
        Postorder(node.right)
        print node.data

Time Complexity:
Traversal takes O(n)
because every node is visited once.

Key Points:
- Traversal is used to access tree elements
- Inorder is important for Binary Search Tree
- Preorder is useful for copying tree
- Postorder is useful for deleting tree
