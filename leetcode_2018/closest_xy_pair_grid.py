"""
Closest X - Y pair in a grid

Give a gird, and there are 'X',"Y" in this grid. find the shortest distance between X and Y. Example:

input:
[[X,0,0],
[0,Y,0],
[X,Y,0]]
Output: 1

input:
[[X,X,0],
[0,0,Y],
[Y,0,0]]
Output: 2

Given a 2D grid of characters, find the shortest Manhattan (L1) distance between an X and a Y.
Example 1:
XXOO
XOOO
OOYY

Output: 3
Explanation: The X (1, 0) and the Y (2, 2) form the closest XY pair: |1 - 2| + |0 - 2| = 3

Similar:
317. Shortest Distance from All Buildings

"""

grid = [['X', '0', '0'],
        ['X', '0', '0'],
        ['0', '0', '0'],
        ['0', '0', '0'],
        ['Y', '0', 'Y']
       ]

def bfs(grid):
    stack, visited = [], set()
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'X':
                stack.append(((i, j), 0))
                visited.add((i,j))

    while stack:
        (r, c), dist = stack.pop(0)
        if grid[r][c] == 'Y':
            return dist

        for k, v in dirs:
            if r+k<0 or c+v<0 or (r+k)>=len(grid) or (c+v)>=len(grid[0]) or \
            (r+k, c+v) in visited:
                continue
            else:
                stack.append(((r+k, c+v), dist+1))
            visited.add((r+k, c+v))
    return -1
