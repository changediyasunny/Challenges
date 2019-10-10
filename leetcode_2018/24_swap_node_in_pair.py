"""
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        curr = ListNode(0)
        dummy = curr
        curr.next = head
        while curr.next and curr.next.next:
            p1 = curr.next
            p2 = p1.next
            # change pointers here
            curr.next = p2
            p1.next = p2.next
            p2.next = p1
            curr = curr.next.next
        return dummy.next
