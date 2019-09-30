"""
226. Invert Binary Tree

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1


"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def invertTree(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    stack = []
    if root is not None:
        stack.append(root)
    while stack:
        curr = stack.pop(0)
        temp = curr.left
        curr.left = curr.right
        curr.right = temp
        if curr.left is not None:
            stack.append(curr.left)
        if curr.right is not None:
            stack.append(curr.right)
    return root
