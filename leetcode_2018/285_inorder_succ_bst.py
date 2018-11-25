"""
285. Inorder Successor in BST

Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
Note: If the given node has no in-order successor in the tree, return null.

Example 1:
Input: root = [2,1,3], p = 1

  2
 / \
1   3

Output: 2
Example 2:

Input: root = [5,3,6,2,4,null,null,1], p = 6

      5
     / \
    3   6
   / \
  2   4
 /
1

Output: null

"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorderSuccessor(root, p):
    """
    :type root: TreeNode
    :type p: TreeNode
    :rtype: TreeNode
    """
    def find_min(p):
        while p.left is not None:
            p = p.left
        return p

    if p.right is not None:
        return find_min(p.right)
    succ = None
    while root:
        if p.val < root.val:
            succ = root
            root = root.left
        elif p.val > root.val:
            root = root.right
        else:
            break
    return succ
