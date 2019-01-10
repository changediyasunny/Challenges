"""
647. Palindromic Substrings

Given a string, your task is to count how many palindromic substrings in this string.
The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

time: O(N^2)
"""

# Expand Around Center
# result stores all palindromes
class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        ans = 0
        result = []
        for center in range(2*N - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < N and s[left] == s[right]:
                result.append(s[left: right+1])
                ans += 1
                left -= 1
                right += 1
        return ans

# Odd - Even length strings
# Example:
# Input: DATTAP & DATXTAP
class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.count = 0
        N = len(s)
        if not s:
            return 0

        def helper(s, left, right):
            while(left>=0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1
                self.count += 1
        for i in range(N):
            helper(s, i, i)    # odd length
            helper(s, i, i+1)    # even length
        return self.count

# DP
class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        if not s:
            return 0
        count = 0
        table = [[False for i in range(N)] for _ in range(N)]

        # single character is pall
        for i in range(N):
            table[i][i] = True
            count += 1

        # check for character of length 2
        for i in range(N-1):
            if s[i] == s[i+1]:
                table[i][i+1] = True
                count += 1
        # for more lenght >= 3
        for k in range(3, N+1):
            for i in range(N-k+1):
                j = i + k - 1
                if table[i+1][j-1] and s[i]==s[j]:
                    table[i][j] = True
                    count += 1
        return count
