"""
684. Redundant Connection

In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N),
with one additional edge added. The added edge has two different vertices chosen from 1 to N,
and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v]
with u < v, that represents an undirected edge connecting nodes u and v.

Return an edge that can be removed so that the resulting graph is a tree of N nodes.
If there are multiple answers, return the answer that occurs last in the given 2D-array.
The answer edge [u, v] should be in the same format, with u < v.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given undirected graph will be like this:
  1
 / \
2 - 3
Example 2:
Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
Output: [1,4]
Explanation: The given undirected graph will be like this:
5 - 1 - 2
    |   |
    4 - 3

"""

"""
Time Complexity: O(N^2) where N is the number of vertices (and also the number of edges) in the graph.
In the worst case, for every edge we include, we have to search every previously-occurring edge of the graph.
Space Complexity: O(N). The current construction of the graph has at most N nodes.

DFS
"""
def findRedundantConnection(self, edges):
    """
    :type edges: List[List[int]]
    :rtype: List[int]
    """
    graph = collections.defaultdict(set)

    def dfs(src, tgt):
        stack = [src]
        while stack:
            node = stack.pop()
            if node == tgt:
                return True
            if node not in visited:
                visited.add(node)
                for nei in graph[node]:
                    if nei not in visited:
                        stack.append(nei)
        return False

    for x, y in edges:
        visited = set()
        if x in graph and y in graph and dfs(x, y):
            return [x, y]
        graph[x].add(y)
        graph[y].add(x)

""" Time: O(N) and SPace: O(N)
Disjoint set data structure
"""
class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parent = [0] * len(edges)

        def find(x):
            if parent[x] == 0:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            if rootx == rooty:
                return False
            parent[rootx] = rooty
            return True

        for x, y in edges:
            print(parent)
            if not union(x-1, y-1):
                print(parent)
                return [x, y]
