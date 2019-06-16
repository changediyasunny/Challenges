"""
200. Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally
or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input:
11110
11010
11000
00000
Output: 1

Example 2:
Input:
11000
11000
00100
00011
Output: 3

DFS & BFS: Find strongly connected components of graph

Time complexity : O(M * N) where M is the number of rows and N is the number of columns.

Space complexity : O(O(min(M,N)) because in worst case where the grid is filled with lands,
the size of queue can grow up to min(M,NM,N).
"""



def changeLandWater(grid, i, j):
    if(i< 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0'):
        return
    grid[i][j] = '0'
    changeLandWater(grid, i-1, j)
    changeLandWater(grid, i+1, j)
    changeLandWater(grid, i, j-1)
    changeLandWater(grid, i, j+1)

def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    count = 0
    if not grid:
        return 0;

    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                count += 1
                changeLandWater(grid, i, j)
    return count

# Using map function.
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = '0'
                map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
                return 1
            return 0
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))
