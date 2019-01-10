"""
844. Backspace String Compare

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:
Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:
Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

running time: O(N)
"""

class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        m = len(S) - 1
        n = len(T) - 1
        back_s, back_t = 0, 0
        while True:
            while m >=0 and (back_s or S[m]=='#'):
                back_s += 1 if S[m] == '#' else -1
                m -= 1
            while n >=0 and (back_t or T[n]=='#'):
                back_t += 1 if T[n] == '#' else -1
                n -= 1

            if not (m >= 0 and n >= 0 and S[m] == T[n]):
                return m == n == -1
            m -= 1
            n -= 1
