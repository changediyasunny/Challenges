"""
289. Game of Life

Given a board with m by n cells, each cell has an initial state live (1) or dead (0).
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using
the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current
state. The next state is created by applying the above rules simultaneously to every
cell in the current state, where births and deaths occur simultaneously.

Input:
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output:
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]

"""

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        dirs = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                live_cells = 0
                for d in dirs:
                    r = i + d[0]
                    c = j + d[1]
                    if (r < len(board) and r >= 0) and (c < len(board[0]) and c >= 0)\
                    and abs(board[r][c]) == 1:
                        # because we make live cell dead with -1
                        # we restore live cell value for neighboring cells
                        live_cells += 1

                # rule 1 & 3
                if board[i][j] == 1 and (live_cells < 2 or live_cells > 3):
                    # board was live and now is dead
                    # because we need this live cell in abs() part above
                    board[i][j] = -1

                if board[i][j] == 0 and live_cells == 3:
                    # board was dead and now is live
                    board[i][j] = 2

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] > 0:
                    # mostly > 1 are alredy live & > 2 are live fomr dead
                    board[i][j] = 1
                else:
                    board[i][j] = 0
