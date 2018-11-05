"""


"""

class TrieNode():
    def __init__(self):
        self.data = {}
        self.isEnd = False

def insert(root, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = root
        for w in word:
            temp_node = current.data.get(w, None)
            if temp_node is None:
                temp_node = TrieNode()
                current.data[w] = temp_node
            current = temp_node
        current.isEnd = True

def findWords(board, words):
    """
    :type board: List[List[str]]
    :type words: List[str]
    :rtype: List[str]
    """
    # create TRIE
    root = TrieNode()
    for word in words:
        insert(root, word)
    
    # search Trie & DFS
    rows = len(board)
    cols = len(board[0])
    result = []
    for i in range(rows):
        for j in range(cols):
            dfs(board, root, i, j, "", result)
    return result

def dfs(board, root, i, j, strs, result):
    # print(board)
    # print(i, j, strs, result)
    # print("=======================")
    node = root
    # end of word reached & string found
    if node.isEnd:
        result.append(strs)
        node.isEnd = False
    if (i < 0 or i >= len(board) or j <0 or j >= len(board[0])):
        return
    w = board[i][j]    # valid cahracter
    node = node.data.get(w, None)
    if node is None:
        return
    board[i][j] = '#'
    dfs(board, node, i+1, j, strs+w, result)
    dfs(board, node, i-1, j, strs+w, result)
    dfs(board, node, i, j+1, strs+w, result)
    dfs(board, node, i, j-1, strs+w, result)
    board[i][j] = w


words = ["oath","pea","eat","rain"]
board = [
    ['o','a','a','n'],
    ['e','t','a','e'],
    ['i','h','k','r'],
    ['i','f','l','v']
]
findWords(board, words)







