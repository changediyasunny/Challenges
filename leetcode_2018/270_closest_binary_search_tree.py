"""
270. Closest Binary Search Tree Value
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:
Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Recursive
def closestValue_rr(root, target):
    """
    :type root: TreeNode
    :type target: float
    :rtype: int
    """
    x = root.val
    child = root.left if target < x else root.right
    if not child:
        return x
    y = self.closestValue(child, target)
    if abs(x - target) < abs(y - target):
        return x
    return y

# iterative
def closestValue_it(root, target):
    """
    :type root: TreeNode
    :type target: float
    :rtype: int
    """
    diff = float('inf')
    final_result = None
    while root:
        if root.val == target:
            return root.val
        curDiff = abs(root.val - target)
        if curDiff < diff:
            diff = curDiff
            final_result = root.val
        root = root.left if target < root.val else root.right
    return res
