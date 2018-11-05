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

"""
import sys, os
from collections import defaultdict

def isPalld(word):
    # print("word for pall check: %s" %word)
    if len(word) == 0 or len(word) == 1:
        return True
    return word[0] == word[-1] and isPalld(word[1:-1])

class Trie:
    def __init__(self):
        self.paths = defaultdict(Trie)
        self.isWordEnd = -1
        self.restpall = []

    def insert(self, word, index):
        current = self
        # print(current.paths)
        # print("===============================")
        for j, char in enumerate(reversed(word)):
            # print(j, char)
            if isPalld(word[ 0: len(word)-j ]):
                # print("\t=====>%s" %word[0:len(word)-j])
                current.restpall.append(index)
            current = current.paths[char]
        current.isWordEnd = index

# create TRIE DS
def makeTrie(word_list):
    current = Trie()
    for index, word in enumerate(word_list):
        # print("===== %s ======" %word)
        current.insert(word, index)
    return current

def get_pallindrome(node, word, index):
    output = []
    while word:
        # print(node.paths.keys())
        if node.isWordEnd >= 0:
            # print("===word==> %s" %word)
            if isPalld(word):
                output.append(node.isWordEnd)
        if not word[0] in node.paths:
            return output
        node = node.paths[word[0]]
        word = word[1:]
    
    if node.isWordEnd >=0:
        # print("==paths===> %s" %node.paths.keys())
        # print("==isWordEnd===> %s" %node.isWordEnd)
        output.append(node.isWordEnd)
    # print("==restPall===> %s" %node.restpall)
    output.extend(node.restpall)
    return output

def palindromePairs(words):
    """
    :type words: List[str]
    :rtype: List[List[int]]
    """
    current = makeTrie(words)
    output = []
    # print("============================")
    for i, word in enumerate(words):
        # print("\n .......... %s .........." %word)
        index_lists = get_pallindrome(current, word, i)
        output.extend([[i, c] for c in index_lists if i != c ])
    return output

# words = ["abcd","dcba","lls","s","sssll"]
# words = ["bat","tab","cat"]
words = ["aab", "ebaa", "pqrs", "srqp", "tuu", "vuut"]
print(words)
print(palindromePairs(words))


