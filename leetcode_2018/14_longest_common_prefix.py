"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""

# Using Trie Node structure
# Trie build: O(N * M): N=length of strs array & M=longest string length
# finding prefix: O(k): where k: length of prefix
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

    def insert(self, word):
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.end = True

    def longest_prefix(self):
        curr = self
        prefix = []
        while curr:
            if curr.end or len(curr.children)>1:
                return ''.join(prefix)
            k = list(curr.children)[0]
            prefix.append(k)
            curr = curr.children[k]
        return ''.join(prefix)

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        root = TrieNode()
        for st in strs:
            root.insert(st)
        return root.longest_prefix()


# Using min index prefix
# runing time O(n) where n=length of all characters in strs array
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        max_idx = min([len(s) for s in strs])
        for i in range(max_idx, 0, -1):
            flag = True
            for temp in strs[1:]:
                print(temp)
                if temp[:i] != strs[0][:i]:
                    flag = False
            if flag:
                return strs[0][:i]
        return ''
