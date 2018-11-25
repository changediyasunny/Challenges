"""
298. Binary Tree Longest Consecutive Sequence

Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections.
The longest consecutive path need to be from parent to child (cannot be the reverse).

Example 1:
Input:

   1
    \
     3
    / \
   2   4
        \
         5

Output: 3
Explanation: Longest consecutive sequence path is 3-4-5, so return 3.

Example 2:
Input:

   2
    \
     3
    /
   2
  /
 1

Output: 2 
Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Iterative - 1
class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        curr_path = [root]
        self.max_path = 0
        stack = [(root, curr_path)]
        while stack:
            node, path = stack.pop()
            if node.left:
                if node.left.val == node.val+1:
                    stack.append((node.left, path + [node.left]))
                else:
                    stack.append((node.left, [node.left]))
            if node.right:
                if node.right.val == node.val+1:
                    stack.append((node.right, path + [node.right]))
                else:
                    stack.append((node.right, [node.right]))
            self.max_path = max(self.max_path, len(path))
        return self.max_path

# Iterative - 2
def longestConsecutive(root):
    if not root:
        return 0
    ans, stack = 0, [[root, 1]]
    while stack:
        node, length = stack.pop()
        ans = max(ans, length)
        for child in [node.left, node.right]:
            if child:
                l = length + 1 if child.val == node.val + 1 else 1
                stack.append([child, l])
    return ans

# Recursive
class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node):
            if node is None:
                return 0
            L = helper(node.left) + 1
            R = helper(node.right) + 1

            if node.left is not None and node.val+1 != node.left.val:
                L = 1
            if node.right is not None and node.val+1 != node.right.val:
                R = 1
            total_len = max(L, R)
            self.maxlen = max(self.maxlen, total_len)
            return total_len

        self.maxlen = 0
        helper(root)
        return self.maxlen
