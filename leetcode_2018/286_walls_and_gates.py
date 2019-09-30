"""
286. Walls and Gates

You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent

INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible
to reach a gate, it should be filled with INF.

Example:

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4

Running time: O(mn)
"""
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        stack = []
        for i, row in enumerate(rooms):
            for j, r in enumerate(row):
                if not r:
                    stack.append((i, j))

        while stack:
            i, j = stack.pop(0)
            for m, n in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                if 0<= m < len(rooms) and 0<= n < len(rooms[0]) and rooms[m][n]>2**30:
                    rooms[m][n] = rooms[i][j] + 1
                    stack.append((m, n))
