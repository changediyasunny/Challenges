"""
648. Replace Words

In English, we have a concept called root, which can be followed by some other words to form another longer word - 
let's call this word successor. For example, the root an, followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the 
sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.

Example 1:

Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"



Time Complexity: O(N) where N is the length of the sentence. Every query of a word is in linear time.
Space Complexity: O(N), the size of our trie.


"""
from collections import defaultdict
import sys

class TrieNode():
    def __init__(self):
        from collections import defaultdict
        self.data = defaultdict(TrieNode)
        self.isEnd = False
        self.prefix = None

class Solution:
    def replaceWords(self, wordDict, sentence):
        """
        :type wordDict: List[str]
        :type sentence: str
        :rtype: str
        """
        result = []
        self.root = TrieNode()
        # Insert into Trie DS
        for word in wordDict:
            self.insert(word)
        
        data_list = sentence.split()
        print(data_list)
        for word in data_list:
            flag = self.search(word)
            print(word, flag)
            if flag is None:
                result.append(word)
            else:
                result.append(flag)
        return ' '.join(result)

    def search(self, word):
        node = self.root
        #print("=========== %s ============" %word)
        for w in word:
            if w not in node.data:
                #print("=======> %s   & %s" %(w, node.prefix))
                break
            elif node.prefix is not None:
                return node.prefix
            else:
                node = node.data[w]
        return node.prefix

    def insert(self, word):
        current = self.root
        for w in word:
            current = current.data[w]
        current.isEnd = True
        current.prefix = word

wordDict = ["cat", "bat", "rat", "ca"]
sentence = "the cattle was rattled by the battery"
obj = Solution()
print(obj.replaceWords(wordDict, sentence))