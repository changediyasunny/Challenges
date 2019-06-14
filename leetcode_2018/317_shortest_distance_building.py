"""
317. Shortest Distance from All Buildings

You want to build a house on an empty land which reaches all buildings in the shortest
amount of distance. You can only move up, down, left and right. You are given a 2D
grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.

Example:
Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7

Explanation:
Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
the point (1,2) is an ideal empty land to build a house, as the total
travel distance of 3+3+1=7 is minimal. So return 7.

k = The number of buildings in the grid, and
l = The number of empty lands in the grid.
Time complexity: O(k*l)

space complexity: O(m*n*k), where m = len(grid), n = len(grid[0])

"""

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def bfs(x, y):
            visited = [[0]*n for _ in range(m)]
            stack = [(x,y,0)]
            while stack:
                x, y, d = stack.pop(0)
                for p, q in {(x-1, y), (x+1, y), (x, y-1), (x, y+1)}:
                    if 0<= p < m and 0<=q<n and grid[p][q] == 0 and visited[p][q] == 0:
                        visited[p][q] = 1
                        if not dist[p][q]:
                            dist[p][q] = [d + 1]
                        else:
                            dist[p][q].append(d+1)
                        stack.append((p,q,d+1))

        m = len(grid)
        n = len(grid[0])
        # count of buildings
        building = 0
        # distance matrix
        dist = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    building += 1
                    bfs(i, j)

        print(dist)
        min_val = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if dist[i][j] and len(dist[i][j]) == building:
                        min_val = min(sum(dist[i][j]), min_val)

        return min_val if min_val != float('inf') else -1
