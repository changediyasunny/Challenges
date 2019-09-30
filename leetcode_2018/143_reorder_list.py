"""
143. Reorder List


Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        slow = head
        fast = head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # base cases to get middle element
        slow = slow.next
        if fast.next:
            fast = fast.next

        # reverse second part of the list
        prev = slow
        curr = slow.next
        prev.next = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

            # turn into zig-zag manner
        trav = head
        while fast.next:
            m = trav.next
            n = fast.next
            trav.next = fast
            fast.next = m
            trav = m
            fast = n
        return head


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        def reverse_list(node):
            prev = None
            while node:
                m = node.next
                node.next = prev
                prev = node
                node = m
            return prev


        if head is None or head.next is None:
            return

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head2 = reverse_list(slow.next)
        slow.next = None
        p = head
        q = head2
        while q:
            m = p.next
            n = q.next
            p.next = q
            q.next = m
            p = m
            q = n
