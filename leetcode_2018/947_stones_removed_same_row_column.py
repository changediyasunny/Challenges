"""
947. Most Stones Removed with Same Row or Column

On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.
Now, a move consists of removing a stone that shares a column or row with another stone on the grid.
What is the largest possible number of moves we can make?

Example 1:
Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5

Example 2:
Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3

Example 3:
Input: stones = [[0,0]]
Output: 0

running time: O(N^2)
space: O(N^2)
"""

# we need to find how many connected components exists at this point in graph.
# finding number of island in a graph.
# at-max total components can be formed is len(stones). If they are disconnected then it forms a component.

#TODO: disjoint set data structure in O(N log N)

class Solution:
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        stones = list(map(tuple, stones))
        points = set(stones)
        graph = collections.defaultdict(list)

        for i, j in points:
            graph[i].append(j)
            graph[j].append(i)

        def dfs(i, j):
            points.remove((i,j))
            for y in graph[i]:
                if (i, y) in points:
                    dfs(i, y)
            for x in graph[j]:
                if (x, j) in points:
                    dfs(x, j)

        res = 0
        for i, j in stones:
            if (i, j) in points:
                dfs(i, j)
                res += 1
        return len(stones) - res
