"""
104. Maximum Depth of Binary Tree
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

Time complexity : O(N).
Space complexity : O(N).

"""



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxDepth_dfs(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    stack = []
    if root is not None:
        stack.append((root, 1))
    depth = 0
    while stack:
        root, curr_depth = stack.pop()
        if root is not None:
            depth = max(depth, curr_depth)
            stack.append((root.left, curr_depth+1))
            stack.append((root.right, curr_depth+1))
    return depth

# BST Solution
def maxDepth_bst(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    import queue
    q = queue.Queue()
    if root is not None:
        q.put(root)
    depth = 0
    while not q.empty():
        size = q.qsize()
        while size:
            node = q.get()
            if node.left is not None:
                q.put(node.left)
            if node.right is not None:
                q.put(node.right)
            size -= 1
        depth += 1
    return depth
