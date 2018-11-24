"""
250. Count Univalue Subtrees
Given a binary tree, count the number of uni-value subtrees.
A Uni-value subtree means all nodes of the subtree have the same value.

Example :

Input:  root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

Output: 4
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        hashmap = {None:True}
        stack = []
        prev = None
        curr = root
        count = 0
        while stack or curr is not None:
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            elif stack[-1].right != prev:
                curr = stack[-1].right
                prev = None
            else:
                prev = stack.pop()
                if hashmap.get(prev.left) and hashmap.get(prev.right):
                    if prev.left is not None and prev.left.val != prev.val:
                        hashmap[prev] = False
                    elif prev.right is not None and prev.right.val != prev.val:
                        hashmap[prev] = False
                    else:
                        hashmap[prev] = True
                        count += 1
                else:
                    hashmap[prev] = True
        return count
