"""
199. Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

Input: [1,2,3,4,5,null,6,null,7,null,null,8,null,null,9,null,null,null,10]
Output: [1,3,6,8,9,10]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Stack
class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = {}
        if not root:
            return []
        max_height = -1
        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()
            if node is not None:
                max_height = max(max_height, depth)
                result[depth] = node.val
                stack.append((node.right, depth+1))
                stack.append((node.left, depth+1))
        return [result[d] for d in range(max_height+1)]
