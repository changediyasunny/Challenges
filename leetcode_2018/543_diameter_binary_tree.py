"""
543. Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

Example:
Given a binary tree

         1
        / \
       2   3
      / \
     4   5

Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

time: O(N)
space: O(N)
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Iterative Stack
class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        import sys
        max_length = 0
        depth = {None: -1}
        stack = [(root, 0)]
        while stack:
            node, visited = stack.pop()
            if node is None:
                continue
            if not visited:
                stack.extend([(node, 1), (node.right, 0), (node.left, 0)])
            else:
                left_d = depth[node.left] + 1
                right_d = depth[node.right] + 1
                depth[node] = max(left_d, right_d)
                max_length = max(max_length, left_d + right_d)
        return max_length

# Recursive
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.fd = 1

        def height(node):
            if node is None:
                return 0
            L = height(node.left)
            R = height(node.right)
            self.fd = max(L+R+1, self.fd)
            return max(L,R) + 1

        height(root)
        return self.fd - 1
