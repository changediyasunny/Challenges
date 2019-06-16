"""
32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length of the
longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

Time: O(N)
"""

class Solution(object):
    def longestValidParentheses(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif stack and s[stack[-1]] == '(':
                stack.pop()
            else:
                stack.append(i)
        print(stack)
        stack = [-1] + stack + [len(s)]
        print(stack)
        ans = 0
        for i in range(len(stack)-1):
            ans = max(ans, stack[i+1]-stack[i]-1)
        return ans
