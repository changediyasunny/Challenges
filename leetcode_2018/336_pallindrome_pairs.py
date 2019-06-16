"""
336. Pallindrome Pairs

Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:

Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]

Reference:
https://fizzbuzzed.com/top-interview-questions-5/

The complexity of this solution is O(k^2 n) where k is the length of the largest word and n
is the number of words in the word list. We can see this because we do k^2 work to put each
word into the trie (because we are doing isPalindrome checks that cost O(k) at each letter) and
also k^2 work to search the trie

"""
def ispall(word):
    return word == word[::-1]

class Trie(object):
    def __init__(self):
        self.paths = collections.defaultdict(Trie)
        self.restpall = []
        self.isEnd = -1

    def insert(self, word, idx):
        current = self
        for i, ch in enumerate(reversed(word)):
            if ispall(word[0 : len(word)-i]):
                current.restpall.append(idx)
            current = current.paths[ch]
        current.isEnd = idx

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        # create Trie DS
        current = Trie()
        for i, word in enumerate(words):
            current.insert(word, i)

        result = []
        for i, word in enumerate(words):
            indexes = self.get_pairs(current, word, i)
            result.extend([[i,c] for c in indexes if i != c])
        return result

    def get_pairs(self, node, word, idx):
        output = []
        while word:
            if node.isEnd >= 0:
                if ispall(word):
                    # needed if one of word ends in the middle of another word
                    # in True. Eg. a & ppa
                    output.append(node.isEnd)
            if word[0] not in node.paths:
                return output
            node = node.paths[word[0]]
            word = word[1:]

        if node.isEnd >= 0:
            # if actual single word ends
            output.append(node.isEnd)
        output.extend(node.restpall)
        return output

# words = ["abcd","dcba","lls","s","sssll"]
# words = ["bat","tab","cat"]
words = ["aab", "ebaa", "pqrs", "srqp", "tuu", "vuut"]
print(words)
print(palindromePairs(words))
