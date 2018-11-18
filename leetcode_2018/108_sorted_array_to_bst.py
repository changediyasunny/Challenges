"""
108. Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two
subtrees of every node never differ by more than 1.

Example:
Given the sorted array: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

Output: [0,-10,5,null,-3,null,9]

Input: [1,2,3,4,5,6]
Output: [3,1,5,null,2,4,6]

"""



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sortedArrayToBST(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    if not nums:
        return []
    start = 0
    end = len(nums) - 1
    stack = []
    root = TreeNode(0)
    stack.append((root, start, end))
    while stack:
        curr, left, right = stack.pop()
        mid = left + (right - left)//2
        curr.val = nums[mid]
        curr.left = curr.right = None

        if left <= mid-1:
            curr.left = TreeNode(0)
            stack.append((curr.left, left, mid-1))
        if mid+1 <= right:
            curr.right = TreeNode(0)
            stack.append((curr.right, mid+1, right))
    return root
