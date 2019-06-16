"""

708. Insert into a Cyclic Sorted List

Given a node from a cyclic linked list which is sorted in ascending order, write
a function to insert a value into the list such that it remains a cyclic sorted list.
The given node can be a reference to any single node in the list, and may not be necessarily
the smallest value in the cyclic list.

If there are multiple suitable places for insertion, you may choose any place to
insert the new value. After the insertion, the cyclic list should remain sorted.

If the list is empty (i.e., given node is null), you should create a new single
cyclic list and return the reference to that single node. Otherwise, you should
return the original given node.

Running time: O(N)
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        temp = Node(insertVal, head)
        if not head:
            return temp

        node = head
        while True:
            if node.val > node.next.val and (insertVal <= node.next.val or insertVal >= node.val):
                # if new value is either 1st element
                # or last element in sorted list
                break
            elif node.val <= insertVal <= node.next.val:
                # middle case
                break
            elif node.next == head:
                # traversed complete list
                break
            node = node.next
        temp.next = node.next
        node.next = temp
        return head
