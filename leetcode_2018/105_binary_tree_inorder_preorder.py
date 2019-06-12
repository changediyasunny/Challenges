"""
105. Construct Binary Tree from Preorder and Inorder Traversal


Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

(a) Inorder (Left, Root, Right)
(b) Preorder (Root, Left, Right)
(c) Postorder (Left, Right, Root)

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        prev = None
        root = TreeNode(preorder.pop(0))
        stack = [root]
        while preorder:
            while stack and stack[-1].val == inorder[0]:
                prev = stack.pop()
                tmp = inorder.pop(0)
            curr = TreeNode(preorder.pop(0))
            if prev is not None:
                prev.right = curr
            elif stack:
                stack[-1].left = curr
            stack.append(curr)
            prev = None
        return root
