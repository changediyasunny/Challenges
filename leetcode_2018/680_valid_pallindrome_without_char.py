"""
680. Valid Palindrome II

Given a non-empty string s, you may delete at most one character. Judge whether
you can make it a palindrome.

Example 1:
Input: "aba"
Output: True

Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

Running time: O(N)
"""

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one = s[left:right]
                two = s[left+1: right+1]
                # Whenever there is a mismatch, we can either exclude the character
                # at the left or the right pointer. We #then take the two remaining substrings
                # and compare against its reversed and see if either one is a #palindrome
                return one == one[::-1] or two == two[::-1]
            left += 1
            right -= 1
        return True
