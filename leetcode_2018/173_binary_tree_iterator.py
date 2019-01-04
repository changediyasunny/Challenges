"""
173. Binary Search Tree Iterator

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
Calling next() will return the next smallest number in the BST.
Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

Input: [8,3,10,1,6,null,14,null,null,4,7,13,null]


        8
      /   |
      3    10
    /  |     |
   1   6      14
      / |    /
    4    7   13

Output: [1,3,4,6,7,8,10,13,14]
"""

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.find_left(root)


    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack:
            return True
        return False

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        self.find_left(node.right)
        return node.val

    def find_left(self, root):
        while root:
            self.stack.append(root)
            root = root.left


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
