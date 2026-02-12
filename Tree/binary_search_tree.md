Binary Search Tree (BST)

A Binary Search Tree (BST) is a special type of Binary Tree
that follows a specific ordering property.

BST Property:
- All values in the left subtree are smaller than the root
- All values in the right subtree are greater than the root
- This property is applied recursively to all nodes

How it works:
- Start from the root
- Compare the value to be inserted
- If smaller, go to left
- If greater, go to right
- Repeat until correct position is found

Example:

        50
       /  \
     30    70
    / \    / \
  20  40  60  80

Here:
- Left subtree of 50 contains smaller values
- Right subtree of 50 contains larger values
- This rule applies to every node

Operations in BST:

1. Insertion
- Compare value with root
- Move left or right
- Insert at correct position

2. Searching
- Compare value with node
- Move left if smaller
- Move right if larger
- Stop when found or null

3. Deletion
- Remove the node
- Rearrange tree to maintain BST property

Pseudo Code (Search in BST):

Search(node, key):
    if node == null:
        return "Not Found"
    if key == node.data:
        return "Found"
    else if key < node.data:
        return Search(node.left, key)
    else:
        return Search(node.right, key)

Time Complexity:
Average Case: O(log n)
Worst Case: O(n)

Key Points:
- BST improves searching efficiency
- Works faster than normal Binary Tree (in average case)
- Important for many advanced data structures
