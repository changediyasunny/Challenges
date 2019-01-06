"""
366. Find Leaves of Binary Tree
Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves,
repeat until the tree is empty.

Example:

Input: [1,2,3,4,5]

          1
         / \
        2   3
       / \
      4   5

Output: [[4,5,3],[2],[1]]

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        depths = {None: -1}
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if not node:
                continue
            if visited:
                # do something
                left_len = depths[node.left] + 1
                right_len = depths[node.right] + 1
                depths[node] = max(left_len, right_len)
            else:
                stack.extend([(node, True), (node.left, False), (node.right, False)])
        final_result = {}
        for n, d in depths.items():
            if n is None:
                continue
            try:
                final_result[d].append(n.val)
            except:
                final_result[d] = [n.val]
        return list(final_result.values())
