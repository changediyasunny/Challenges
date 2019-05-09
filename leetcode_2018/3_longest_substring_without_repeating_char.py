"""
3. Longest substring without repeating character

Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = {}
        maxlen = 0
        start = 0
        for i in range(len(s)):
            if s[i] in hashmap and start <= hashmap[s[i]]:
                start = hashmap[s[i]] + 1
            else:
                maxlen = max(maxlen, i-start+1)
            hashmap[s[i]] = i
        return maxlen
