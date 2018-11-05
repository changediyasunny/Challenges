"""
23. Merge K sorted lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        k = len(lists)
        if not k:
            return lists
        self.result = lists[0]
        for ml in lists[1:]:
            self.result = self.mergeList(self.result, ml)
        return self.result
    
    def mergeList(self, l1, l2):
        head = temp = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        if not l1:
            temp.next = l2
        else:
            temp.next = l1
        return head.next