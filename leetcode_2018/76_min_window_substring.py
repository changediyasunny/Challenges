"""
76. Minimum Window Substring

Given a string S and a string T, find the minimum window in S which will contain
all the characters in T in complexity O(n).

Example:
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Running Time: O(N)
"""

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        n = len(s)
        hashmap = collections.Counter(t)
        chars_required = len(t)
        left, right = 0, 0
        min_window = n + 1
        actual_start = left
        while right < n:
            char = s[right]

            # check if it's in T and form window
            if char in hashmap:
                if hashmap[char] > 0:
                    chars_required -= 1
                hashmap[char] -= 1

            # all characters found and window formed
            while chars_required == 0:
                # update min window & actual start
                if (right-left+1) < min_window:
                    min_window = min(min_window, right-left+1)
                    actual_start = left

                # if desired characters found
                if s[left] in hashmap:
                    hashmap[s[left]] += 1
                    if hashmap[s[left]] > 0:
                        # this will make loop break
                        chars_required += 1

                left += 1
            right += 1
        if min_window == (n+1):
            return ""
        return s[actual_start: actual_start + min_window]
