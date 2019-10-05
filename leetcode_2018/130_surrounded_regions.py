"""
130. Surrounded Regions
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of
the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected
to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent
cells connected horizontally or vertically.

Time: O(mn)
Space: O(mn)
"""

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board: return None

        queue = []
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if (i in [0, m-1] or j in [0, n-1]) and board[i][j] == "O":
                    queue.append((i, j))

        while queue:
            r, c = queue.pop(0)
            if 0<=r<len(board) and 0<=c<len(board[0]) and board[r][c] == "O":
                board[r][c] = "D"
                queue += (r+1, c), (r-1, c), (r, c+1), (r, c-1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "D":
                    board[i][j] = "O"
