"""
227. Basic Calculator II

Implement a basic calculator to evaluate a simple expression string.
The expression string contains only non-negative integers, +, -, *, / operators
and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5

"""

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        sign = 1
        tokens = iter(re.findall('\d+|\S', s))
        for token in tokens:
            if token in '+-':
                total += sign * term
                sign = ' +'.find(token)
            elif token in '*/':
                n = int(next(tokens))
                term = term * n if token == '*' else term//n
            else:
                term = int(token)
        return total + sign * term

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        sign = '+'
        num = 0
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if (not s[i].isspace() and not s[i].isdigit()) or i ==len(s)-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-1 * num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    if stack[-1]//num < 0 and stack[-1]%num != 0:
                        # "14-3/2" --> 1st & 2nd condition needed
                        stack.append(stack.pop()//num + 1)
                    else:
                        # "10000-1000/10+100*1" --> negative division only if remainder == 0
                        # normal + division
                        stack.append(stack.pop()//num)
                sign = s[i]
                num = 0
        return sum(stack)
