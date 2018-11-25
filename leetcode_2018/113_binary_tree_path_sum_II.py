"""
113. Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1

Return:

[
   [5,4,11,2],
   [5,8,4,5]
]


"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        target = sum
        result = []
        stack = [(root, target-root.val, [root.val,])]
        while stack:
            node, remain, path = stack.pop()
            if not node.left and not node.right:
                if remain == 0:
                    result.append(path)
            if node.left:
                stack.append((node.left, remain-node.left.val, path + [node.left.val] ))
            if node.right:
                stack.append((node.right, remain-node.right.val, path + [node.right.val] ))
        return result
