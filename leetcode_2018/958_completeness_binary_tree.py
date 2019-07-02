"""
958. Check Completeness of a Binary Tree

Given a binary tree, determine if it is a complete binary tree.
In a complete binary tree every level, except possibly the last, is completely filled,
and all nodes in the last level are as far left as possible. It can have between 1 and
2h nodes inclusive at the last level h.


Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1}
and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.

Input: [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = [root]
        i = 0
        while stack:
            node = stack.pop(0)
            if node is None:
                return not any(stack)
            stack.append(node.left)
            stack.append(node.right)
        return True


def isCompleteTree(root):
        bfs = [root]
        i = 0
        while bfs[i]:
            bfs.append(bfs[i].left)
            bfs.append(bfs[i].right)
            i += 1
        return not any(bfs[i:])
