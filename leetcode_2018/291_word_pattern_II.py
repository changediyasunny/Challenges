"""
291. Word Pattern II

Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter
in pattern and a non-empty substring in str.

Example 1:
Input: pattern = "abab", str = "redblueredblue"
Output: true

Example 2:
Input: pattern = pattern = "aaaa", str = "asdasdasdasd"
Output: true

Example 3:
Input: pattern = "aabb", str = "xyzabcxzyabc"
Output: false

"""

class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        return self.backtrack(pattern, str, {})

    def backtrack(self, pattern, strs, data):
        if len(pattern) == 0 and len(strs) > 0:
            return False

        if len(pattern) == len(strs) == 0:
            # only empty strings check
            return True
        # When we find the match for pattern[0], we have len(pattern) - 1 letters
        # left to match, therefore the maximum length of pattern[0] can only be
        # len(str) - (len(pattern) - 1) = len(str) - len(pattern) + 1. For slicing
        # in Python, that would make the upper-bound len(str) - len(pattern) + 2
        for end in range(1, len(strs)-len(pattern)+2):
            if pattern[0] not in data and strs[:end] not in data.values():
                data[pattern[0]] = strs[:end]
                if self.backtrack(pattern[1:], strs[end:], data):
                    return True
                del data[pattern[0]]
            elif pattern[0] in data and data[pattern[0]] == strs[:end]:
                if self.backtrack(pattern[1:], strs[end:], data):
                    return True
        return False
