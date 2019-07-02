"""
Robot in Maze:

Initially a robot is placed in at the bottom left corner of rows x cols matrix.
The exit is at the bottom right corner. From any point in the matrix, the robot
can make a move to one of the 3 blocks - the block to its right, the block at its
top-right and the block at its bottom right. Though it must not go out of the matrix area.
Find out the total number of ways for the robot to move from bottom left to bottom right of the matrix.

Expected complexity: O(rows * cols) time and O(cols) space.

Input: rows = 3, cols = 4
Output: 4
Explanation:
1: (2, 0) - (2, 1) - (2, 2) - (2, 3)
2: (2, 0) - (1, 1) - (2, 2) - (2, 3)
3: (2, 0) - (2, 1) - (1, 2) - (2, 3)
4: (2, 0) - (1, 1) - (1, 2) - (2, 3)

Example 2:
Input: rows = 4, cols = 5
Output: 9
"""

def robot(grid):
    rows = len(grid)
    cols = len(grid[0])
    dp = [[0]*cols for _ in range(rows)]
    # bottom left
    for i in range(cols):
        dp[-1][i] = 1

    for c in range(1, cols):
        for r in range(rows-1, -1, -1):
            top_left = dp[r-1][c-1] if r > 0 else 0
            left = dp[r][c-1]
            bottom_right = dp[r+1][c-1] if r < rows-1 else 0
            dp[r][c] = top_left + left + bottom_right
    return dp[-1][-1]


"""
Follow-up 1:
A robot is at the bottom left corner. It can walk to one of the 3 locations as a next
step - the bock to it's right, top-right and bottom-right. Some of the blocks are tranches
that the root must not cross. The input is an int matrix of 0 and 1. Trenches are denoted
by 0. The robot may only cross a block with value 1. Without stepping on trenches
find out the total number of ways from bottom left to bottom right of the matrix.
You may assume thar bottom left has no trench.

Expected complexity: O(rows * cols) time, O(1) space.

Input:
grid = [
[1, 1, 1, 1, 1],
[1, 1, 0, 1, 1],
[1, 1, 1, 1, 1],
[1, 0, 1, 1, 1]]
Output: 4

"""
def robot(grid):
    rows = len(grid)
    cols = len(grid[0])
    # add trenches as we are not going to visit
    # 1st column anyways given the directions
    for k in range(rows-1):
        grid[k][0] = 0

    for c in range(1, cols):
        for r in range(rows-1, -1, -1):
            if grid[r][c] != 0:
                top_left = grid[r-1][c-1] if r > 0 else 0
                left = grid[r][c-1]
                bottom_right = grid[r+1][c-1] if r < rows-1 else 0
                grid[r][c] = top_left + left + bottom_right
    return grid[-1][-1]
