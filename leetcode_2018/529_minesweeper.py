"""
529. Minesweeper

You are given a 2D char matrix representing the game board. 'M' represents an unrevealed
mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank
square that has no adjacent (above, below, left, right, and all 4 diagonals) mines,
digit ('1' to '8') represents how many mines are adjacent to this revealed square,
and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed
squares ('M' or 'E'), return the board after revealing this position according
to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'.
If an empty square ('E') with no adjacent mines is revealed, then change it to
revealed blank ('B') and all of its adjacent unrevealed squares should be revealed
recursively. If an empty square ('E') with at least one adjacent mine is revealed,
then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.

Input:

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

"""


class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        row, col = click[0], click[1]
        m, n = len(board), len(board[0])
        directions = ((-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (-1, -1), (1, 1), (1, -1))

        if 0<= row < m and 0<= col < n:
            if board[row][col] == 'M':
                board[row][col] = 'X'
            elif board[row][col] == 'E':
                mines = sum(board[row+p][col+q]=='M' for p, q in directions if 0<=row+p<m and 0<=col+q<n)
                board[row][col] = str(mines or 'B')
                if not mines:
                    for r, c in directions:
                        self.updateBoard(board, [row+r, col+c])
        return board
