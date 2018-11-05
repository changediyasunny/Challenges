"""

211. Add and Search Word - Data structure design

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. 
A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

Note:
You may assume that all words are consist of lowercase letters a-z.


"""


class TrieNode():
    def __init__(self):
        self.data = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        current = self.root
        for w in word:
            temp_node = current.data.get(w, None)
            if temp_node is None:
                temp_node = TrieNode()
                current.data[w] = temp_node
            current = temp_node
        current.isEnd = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        current = self.root
        self.result = False
        self.dfs(current, word)
        return self.result
    
    def dfs(self, node, word):
        """ traverse nodes """
        if not word:
            if node.isEnd:
                self.result = True
            return
        if word[0] == '.':
            for child in node.data.values():
                self.dfs(child, word[1:])
        else:
            node = node.data.get(word[0])
            if not node:
                return
            self.dfs(node, word[1:])


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)