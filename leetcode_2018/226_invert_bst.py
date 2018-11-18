"""
226. Invert Binary Tree

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1


"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def invertTree(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    import queue
    que = queue.Queue()
    if root is not None:
        que.put(root)
    while not que.empty():
        curr = que.get()
        temp = curr.left
        curr.left = curr.right
        curr.right = temp
        if curr.left is not None:
            que.put(curr.left)
        if curr.right is not None:
            que.put(curr.right)
    return root
