"""
655. Print Binary Tree

Print a binary tree in an m*n 2D string array following these rules:
The row number m should be equal to the height of the given binary tree.
The column number n should always be an odd number.

Example 1:
Input:
     1
    /
   2
Output:
[["", "1", ""],
 ["2", "", ""]]

Example 2:
Input:
     1
    / \
   2   3
    \
     4
Output:
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        def height(node):
            if node is None:
                return 0
            return 1 + max(height(node.left), height(node.right))

        depth = height(root)
        width = 2 ** depth - 1
        output = [[''] * width for i in range(depth)]
        stack = [(root, 0, 0, width-1)]
        while stack:
            node, row, left, right = stack.pop(0)
            mid = (left + right)//2
            output[row][mid] = str(node.val)
            if node.left:
                stack.append((node.left, row+1, left, mid-1))
            if node.right:
                stack.append((node.right, row+1, mid+1, right))
        return output


class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        def height(node):
            return 0 if not node else 1 + max(height(node.left), height(node.right))

        def update_output(node, row, left, right):
            if not node:
                return
            mid = (left + right) // 2
            self.output[row][mid] = str(node.val)
            update_output(node.left, row + 1 , left, mid - 1)
            update_output(node.right, row + 1 , mid + 1, right)

        depth = height(root)
        width = 2 ** depth - 1
        self.output = [[''] * width for i in range(depth)]
        update_output(node=root, row=0, left=0, right=width - 1)
        return self.output
