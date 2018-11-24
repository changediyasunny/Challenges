"""
437. Path Sum III

You are given a binary tree in which each node contains an integer value.
Find the number of paths that sum to a given value.
The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

Solution using prefix-sum method which is similar to 1_two_sums.py problem
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
        :rtype: int
        """
        if not root:
            return 0
        hashmap = {0:1}
        total_paths = 0
        total_sum = 0
        target = sum
        stack = [(root, 0)]
        while stack:
            curr, visited = stack.pop()
            if curr is None:
                continue
            if not visited:
                stack.extend([(curr, 1), (curr.right, 0), (curr.left, 0)])
                total_sum = total_sum + curr.val
                total_paths = total_paths + hashmap.get(total_sum - target, 0)
                hashmap[total_sum] = hashmap.get(total_sum, 0) + 1
            else:
                hashmap[total_sum] -= 1
                total_sum -= curr.val
        return total_paths
