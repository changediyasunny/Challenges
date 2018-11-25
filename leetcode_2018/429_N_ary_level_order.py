"""
429. N-ary Tree Level Order Traversal
Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

Same as 102.
"""

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        thisLevel = [root]
        result = []
        while thisLevel:
            result.append([node.val for node in thisLevel])
            nextLevel = []
            for node in thisLevel:
                for kid in node.children:
                    nextLevel.append(kid)
            thisLevel = nextLevel
        return result
