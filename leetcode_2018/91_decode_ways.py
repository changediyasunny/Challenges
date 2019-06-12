"""
91. Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Input: "106"
Output: 1

A digit from index 1 have three condition
'?10' or '?20' this can only divide into '10' or '20' , f(n) = f(n-2)
'?26' this can divide into '6' or '26', f(n) = f(n-2)+f(n-1)
'?09', '?27' this can only divide into '9' or '7' , f(n) = f(n-1)

Running time: O(N)
"""

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # no. of ways for empty-string & single-char string
        stack = [1, 1]
        if not s or s.startswith('0'):
            return 0
        # Here stack[-1] is ways for current character because we consider
        # 0th index char as empty string inside stack
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i-1] == '0' or s[i-1] > '2':
                    # string of type 30 is excluded
                    return 0
                # only 10 & 20 allowed
                stack.append(stack[-2])
            elif 9 < int(s[i-1:i+1]) < 27:
                # string of type 11 to 16 allowed
                # 01-09 not allowed
                stack.append(stack[-2]+stack[-1])
            else:
                stack.append(stack[-1])
        return stack[-1]
