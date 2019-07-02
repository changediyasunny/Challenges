"""
138. Copy List with Random Pointer

A linked list is given such that each node contains an additional random pointer
which could point to any node in the list or null.
Return a deep copy of the list.


Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.


"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""

# Running time: O(n) & space: O(1)
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None

        # create interleaved copy of linked list
        curr = head
        while curr:
            temp = Node(curr.val, None, None)
            temp.next = curr.next
            curr.next = temp
            curr = temp.next
        # assign random & next pointers
        curr = head
        while curr:
            if curr.random is not None:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # restore both lists
        curr = head
        ptr = head.next
        temp_head = head.next
        while curr:
            curr.next = curr.next.next
            ptr.next = ptr.next.next if ptr.next else None
            curr = curr.next
            ptr = ptr.next
        return temp_head
