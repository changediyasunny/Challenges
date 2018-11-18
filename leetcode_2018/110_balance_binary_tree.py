"""
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:
a binary tree in which the depth of the two subtrees of every node never differ by more than 1.


Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Faster Stack + hash array
def isBalanced(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    node_list = [root]
    for node in node_list:
        if node:
            # new append method for lists
            node_list += node.left, node.right
    depth = {None: 0}
    for node in node_list[::-1]:
        if node:
            left, right = depth[node.left], depth[node.right]
            if abs(left-right)>1:
                return False
            depth[node] = 1 + max(left, right)
    return True

# Stack Solution
def isBalanced_stack(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if root is None:
        return True
    depth = {}
    last = None
    stack = [root]
    node = root.left
    while stack:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack[-1]
            if not node.right or last==node.right:
                node = stack.pop()
                left, right = depth.get(node.left, 0), depth.get(node.right, 0)
                if abs(left-right) > 1:
                    return False
                depth[node] = 1 + max(left, right)
                last = node
                node = None
            else:
                node = node.right
    return True

# Queue Solution
def isBalanced_queue(root):
    """
    :type root: TreeNode
    :rtype: bool
    """

    if not root:
        return True

    queue = [root]
    while queue:
        root = queue.pop(0)
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)
        if  getHeightDiff(root) > 1:
            return False
    return True

def getHeightDiff(root):
    h1 = findHeight(root.left)
    print("height1: %s" %h1)
    h2 = findHeight(root.right)
    print("height2: %s" %h2)
    return abs(h1 - h2)

def findHeight(root):
    if not root:
        return 0
    return max(findHeight(root.left), findHeight(root.right)) +1



root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

print(isBalanced_queue(root))
