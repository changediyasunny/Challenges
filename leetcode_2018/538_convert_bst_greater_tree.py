"""
538. Convert BST to Greater Tree

Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original
key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13


"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        total = 0
        if not root:
            return None
        curr = root
        stack = []
        while stack or curr is not None:
            while curr is not None:
                stack.append(curr)
                curr = curr.right
            curr = stack.pop()
            total += curr.val
            curr.val = total
            curr = curr.left
        return root
