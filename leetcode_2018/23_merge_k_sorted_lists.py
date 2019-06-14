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

Time: O(kN): where k is number of linked lists
Space: O(N)
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

        if not lists:
            # adding this to validate input lists == []
            return

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


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Running TIme: O(n log k)
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        result = []
        heap = []
        if not lists:
            return
        for i in range(len(lists)):
            if lists[i]:
                node = lists[i]
                heapq.heappush(heap, (node.val, node))

        while heap:
            curr = heapq.heappop(heap)
            result.append(curr[0])
            if curr[1].next:
                heapq.heappush(heap, (curr[1].next.val, curr[1].next))
        return result
