"""
133. Clone Graph

Given a reference of a node in a connected undirected graph, return a deep copy (clone)
of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

Input:
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3",
"neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],
"val":3}],"val":2},{"$ref":"4"}],"val":1}

"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
# BFS Iterative
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return

        visited = {}
        visited[node] = Node(node.val, [])
        stack = [node]
        while stack:
            curr = stack.pop(0)
            for nei in curr.neighbors:
                if nei not in visited:
                    visited[nei] = Node(nei.val, [])
                    stack.append(nei)
                visited[curr].neighbors.append(visited[nei])
        return visited[node]


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
# DFS Iterative
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return

        hashmap = {}
        source = Node(node.val, [])
        hashmap[source.val] = source
        stack = [node]
        while stack:
            curr = stack.pop()
            for nei in curr.neighbors:
                if nei.val not in hashmap:
                    knode = Node(nei.val, [])
                    hashmap[nei.val] = knode
                    stack.append(nei)
                hashmap[curr.val].neighbors.append(hashmap[nei.val])
        return source
