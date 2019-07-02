"""
79. Word Search

Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where
"adjacent" cells are those horizontally or vertically neighboring. The same letter
cell may not be used more than once.

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, i, j):
                    return True
        return False

    def dfs(self, board, word, i, j):
        res = ''
        if not word:
            return True

        if i<0 or i==len(board) or j<0 or j==len(board[0]) or not board[i][j] or board[i][j] != word[0]:
            return False

        board[i][j] = None
        res = self.dfs(board, word[1:], i+1, j) or \
              self.dfs(board, word[1:], i-1, j) or \
              self.dfs(board, word[1:], i, j-1) or \
              self.dfs(board, word[1:], i, j+1)
        board[i][j] = word[0]
        return res
