"""
348. Design Tic-Tac-Toe

Design a Tic-tac-toe game that is played between two players on a n x n grid.

Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.
TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|

"""

class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.row = [0] * n
        self.col = [0] * n
        self.diag = 0
        self.anti_diag = 0
        self.n = n

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        # Player-A == -1 & player-B = +1
        offset = player * 2 - 3
        # player makes move, we increase offset into row & column. basically count
        # if A has alrady made move and B makes move into same row, then we nullify
        # that count from rows or column
        self.row[row] += offset
        self.col[col] += offset
        if row == col:
            # this is for diagonal
            self.diag += offset
        if row + col == self.n - 1:
            # anti-diagonal
            self.anti_diag += offset
        if self.n in [self.row[row], self.col[col], self.diag, self.anti_diag]:
            # if positive self.n (count of rows / column) is in anywhere,
            # we are sure B has won.
            return 2
        if -self.n in [self.row[row], self.col[col], self.diag, self.anti_diag]:
            # -ve for player A
            # check if all rows (count of row/column) is filled.
            return 1
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
