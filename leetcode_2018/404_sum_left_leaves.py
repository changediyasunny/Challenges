"""
404. Sum of Left Leaves
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        total_sum = 0
        stack = [(root, False)]
        while stack:
            node, valid = stack.pop()
            if node.left:
                stack.append((node.left, True))
            if node.right:
                stack.append((node.right, False))

            if not node.left and not node.right:
                if valid:
                    total_sum += node.val
        return total_sum
