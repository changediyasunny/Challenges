"""
144. Binary Tree Preorder Traversal

Given a binary tree, return the preorder traversal of its nodes' values.
Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]

Running Time: O(N)
Space: O(N)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# DFS & Stack
class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if not root:
            return result
        stack = [root]
        while stack:
            node = stack.pop()
            if node is not None:
                result.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return result
