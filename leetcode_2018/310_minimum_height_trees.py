"""
310. Minimum Height Trees

For an undirected graph with tree characteristics, we can choose any node as the root.
The result graph is then a rooted tree. Among all possible rooted trees, those with
minimum height are called minimum height trees (MHTs). Given such a graph, write a
function to find all the MHTs and return a list of their root labels.


Example 1 :

Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3

Output: [1]
Example 2 :

Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5

Output: [3, 4]

Hints:
We start from every end, by end we mean vertex of degree 1 (aka leaves). We let
the pointers move the same speed. When two pointers meet, we keep only one of them,
until the last two pointers meet or one step away we then find the roots.
It is easy to see that the last two pointers are from the two ends of the longest path in the graph.


"""
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        graph = collections.defaultdict(set)
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)
        leaves = [i for i in range(n) if len(graph[i]) == 1]

        while n > 2:
            new_leaves = []
            n -= len(leaves)
            for k in leaves:
                p = graph[k].pop()
                graph[p].remove(k)
                if len(graph[p]) == 1:
                    new_leaves.append(p)
                leaves = new_leaves
        return leaves
