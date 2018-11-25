"""
426. Convert Binary Search Tree to Sorted Doubly Linked List

Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as synonymous
to the previous and next pointers in a doubly-linked list.

Let's take the following BST as an example, it may help you understand the problem better:
"""


# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return
        head = prev = Node(0, None, None)
        curr = root
        stack = []
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if head is None:
                head = curr
            if prev:
                prev.right = curr
            curr.left = prev
            prev = curr
            curr = curr.right
        head.left = prev
        prev.right = head
        return head
