"""
116. Populating Next Right Pointers in Each Node

Given a binary tree, populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

    You may only use constant extra space.
    Recursive approach is fine, implicit stack space does not count as extra space for this problem.
    You may assume that it is a perfect binary tree (ie, all leaves are at the same level,
    and every parent has two children).

Example:

Given the following perfect binary tree,

     1
   /  \
  2    3
 / \  / \
4  5  6  7

After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL


"""

from collections import deque

# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

# Queue
class Solution:
    def connect(self, root):
        if not root:
            return
        queue = deque([root])
        while queue:
            level_len = len(queue)
            while level_len > 0:
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level_len -= 1
                if level_len == 0:
                    node.next = None
                else:
                    next_node = queue[0]
                    node.next = next_node

# Stack
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return

        stack = [root]
        while stack:
            size = len(stack)
            for i in range(size):
                node = stack.pop(0)
                if i < size -1:
                    node.next = stack[0]
                else:
                    node.next = None

                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
