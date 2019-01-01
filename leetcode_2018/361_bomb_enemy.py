"""
361. Bomb Enemy

Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note: You can only put the bomb at an empty cell.

Input: [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
Output: 3
Explanation: For the given grid,

0 E 0 0
E 0 W E
0 E 0 0

Placing a bomb at (1,1) kills 3 enemies.

"""
def bomb_enemy(grid):
    rows = len(grid)
    colmns = len(grid[0])
    result = 0
    rowHits = 0
    col_hits = [0] * colmns
    for i in range(rows):
        for j in range(colmns):
            print(i, j)
            if grid[i][j] == 'W':
                continue
            if j == 0 or grid[i][j-1] == 'W':
                rowHits = 0
                k = j
                while k < colmns and grid[i][k] != 'W':
                    if grid[i][k] == 'E':
                        rowHits += 1
                    k += 1
                print(">>row hits: %s" %rowHits)
            if i == 0 or grid[i-1][j] == 'W':
                k = i
                while k < rows and grid[k][j] != 'W':
                    if grid[k][j] == 'E':
                        col_hits[j] += 1
                    k += 1
                print(">> col hits: %s" %col_hits)
            if grid[i][j] == '0':
                result = max(result, rowHits + col_hits[j])
            print("=============")
    print(col_hits)
    return result

grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
grid = [['W','E','0','0','E'],['W','0','E','W','0'],['W','0','0','W','E'],['E','0','E','W','0'],['E','0','E','E','0']]
bomb_enemy(grid)
