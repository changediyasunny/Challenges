"""
669. Trim a Binary Search Tree

Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L).
You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.

Example 1:
Input:
    1
   / \
  0   2

  L = 1
  R = 2

Output:
    1
      \
       2
Example 2:
Input:
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output:
      3
     /
   2
  /
 1

Time: O(N)
Space: O(N)
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Recursive
def trimBST_recursive(root, L, R):
    """
    :type root: TreeNode
    :type L: int
    :type R: int
    :rtype: TreeNode
    """
    if root is None:
        return None
    root.left = trimBST(root.left, L, R)
    root.right = trimBST(root.right, L, R)
    if root.val < L:
        return root.right
    elif root.val > R:
        return root.left
    else:
        return root

# Iterative
def trimBST(root, L, R):
    """
    :type root: TreeNode
    :type L: int
    :type R: int
    :rtype: TreeNode
    """
    if root is None:
        return None

    while(root.val < L or root.val > R):
        if root.val < L:
            root = root.right
        if root.val > R:
            root = root.left

    curr = root
    # remove from left subtree
    while curr:
        while(curr.left and curr.left.val < L):
            curr.left = curr.left.right
        curr = curr.left

    curr = root
    # remove from right subtree
    while curr:
        while(curr.right and curr.right.val > R):
            curr.right = curr.right.left
        curr = curr.right
    return root
