"""
212. Word Search II

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:

Input:
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

Output: ["eat","oath"]

time:
O(m * n * avg-len-of-words)
O(len(words) * avg-len-words): build a TRIE

space: O(len(words) * avg-len-words)
"""

class Trie(object):
    def __init__(self):
        self.data = {}
        self.end = False

    def insert(self, word):
        current = self
        for w in word:
            if w not in current.data:
                current.data[w] = Trie()
            current = current.data[w]
        current.end = True

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        def dfs(board, node, i, j, path, output):

            if node.end:
                output.append(path)
                node.end = False
            if (i<0 or i >=len(board) or j<0 or j>= len(board[0])):
                return
            w = board[i][j]
            node = node.data.get(w, None)
            if node is None:
                return

            board[i][j] = '#'
            dfs(board, node, i+1, j, path+w, output)
            dfs(board, node, i-1, j, path+w, output)
            dfs(board, node, i, j-1, path+w, output)
            dfs(board, node, i, j+1, path+w, output)
            board[i][j] = w

        # create Trie
        root = Trie()
        for word in words:
            root.insert(word)

        rows = len(board)
        cols = len(board[0])
        result = []
        for i in range(rows):
            for j in range(cols):
                dfs(board, root, i, j, "", result)
        return result

words = ["oath","pea","eat","rain"]
board = [
    ['o','a','a','n'],
    ['e','t','a','e'],
    ['i','h','k','r'],
    ['i','f','l','v']
]
findWords(board, words)
