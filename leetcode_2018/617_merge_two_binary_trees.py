"""
617. Merge Two Binary Trees

Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are
overlapped while the others are not.
You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values
up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7

Time complexity : O(n). We traverse over a total of n nodes. Here, N refers to the smaller of
the number of nodes in the two trees.
Space complexity : O(n). The depth of stack can grow upto N in case of a skewed tree.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Recursive
def mergeTrees(t1, t2):
    """
    :type t1: TreeNode
    :type t2: TreeNode
    :rtype: TreeNode
    """
    if t1 is None:
        return t2
    if t2 is None:
        return t1
    t1.val += t2.val
    t1.left = mergeTrees(t1.left, t2.left)
    t1.right = mergeTrees(t1.right, t2.right)
    return t1

# Iterative
# Time complexity : O(n). We traverse over a total of nn nodes. Here, N refers to the smaller of
# the number of nodes in the two trees.
# Space complexity : O(n). The depth of stack can grow upto N in case of a skewed tree.
def mergeTrees(t1, t2):
    """
    :type t1: TreeNode
    :type t2: TreeNode
    :rtype: TreeNode
    """
    if t1 is None:
        return t2

    stack = [(t1, t2)]
    while stack:
        tree1, tree2 = stack.pop()
        if(tree1 is None or tree2 is None):
            continue

        tree1.val += tree2.val
        if tree1.left is None:
            tree1.left = tree2.left
        else:
            stack.append((tree1.left, tree2.left))

        if tree1.right is None:
            tree1.right = tree2.right
        else:
            stack.append((tree1.right, tree2.right))
    return t1
