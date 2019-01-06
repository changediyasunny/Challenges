"""
323. Number of Connected Components in an Undirected Graph


Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4

Output: 2
Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1

"""
def countComponents(n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: int
    """
    graph = collections.defaultdict(set)
    for i, j in edges:
        graph[i].add(j)
        graph[j].add(i)
    visited = set()
    count = 0

    def DFS(u):
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                DFS(v)

    for u in range(n):
        if u not in visited:
            DFS(u)
            count += 1
    return count
