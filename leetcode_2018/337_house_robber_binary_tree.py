"""
337. House Robber III

The thief has found himself a new place for his thievery again. There is only one entrance to this area,
called the "root." Besides the root, each house has one and only one parent house. After a tour,
the smart thief realized that "all houses in this place forms a binary tree". It will automatically
contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
Input: [3,2,3,null,3,null,1]

     3*
    / \
   2   3
    \   \
     3*   1*

Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:
Input: [3,4,5,1,3,null,1]

     3
    / \
   4*   5*
  / \   \
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

Space: O(N)
running time: O(N)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Iterative
def rob(self, root):
    stack = [(0, root)]
    # {Node: (rob, don't rob)}
    data = {None: (0, 0)}
    while stack:
        seen, node = stack.pop()
        if node is None:
            continue
        if not seen:
            stack.extend([(1, node), (0, node.left), (0, node.right)])
        else:
            rob_root = node.val + data[node.left][1] + data[node.right][1]
            dont_rob_root = max(data[node.left]) + max(data[node.right])
            data[node] = (rob_root, dont_rob_root)
    return max(data[root])

# Recursive
class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node):
            # 0th index: if root value not selected
            # 1st index: if root is selected
            if node is None:
                return [0, 0]
            if not node.left and not node.right:
                return [0, node.val]
            left = helper(node.left)
            right = helper(node.right)
            result = []
            result.insert(0, max(left) + max(right) )
            result.insert(1, node.val + left[0] + right[0])
            return result

        result = helper(root)
        return max(result[0], result[1])
