"""
224. Basic Calculator

Implement a basic calculator to evaluate a simple expression string.
The expression string may contain open ( and closing parentheses ), the plus +
or minus sign -, non-negative integers and empty spaces .

Example 1:
Input: "1 + 1"
Output: 2

Example 2:
Input: " 2-1 + 2 "
Output: 3

Example 3:
Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23

Explanation: Only + & - is allowed with brackets

If there are brackets, every -ve in-front of bracket changes signs inside bracket.
when adding digits, we check if previous sign was +ve or -ve. and number will be
added accordingly.
each bracket "(" adds new +ve sign and each closing ")" removes one from signs.

Example: 3-(2+(9-4))
at start signs = [1, -1]
when brackets start, everything after it becomes -ve
so signs = [1, -1, -1, -1, ...]

"""
# using magic switching of signs
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        i = 0
        sign = [1, 1]
        while i < len(s):
            char = s[i]
            if char.isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                # check last sign. could be +ve or negative
                total += sign.pop() * int(s[start:i])
                continue
            if char in '+(-':
                # if char == '-' then this returns True and 0th index is returned
                # otherwise on False, 1st index is returned
                sign += sign[-1] * (1, -1)[char == '-'],
            elif char == ')':
                sign.pop()
            i += 1
        return total


# Using Stack
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        i = 0
        sign = 1
        num = 0
        stack = []
        while i < len(s):
            char = s[i]
            if char.isdigit():
                num = num * 10 + int(char)
            elif char in '+-':
                total += sign * num
                sign = 1 if char == '+' else -1
                num = 0
            elif char == '(':
                stack.append(total)
                stack.append(sign)
                sign = 1
                total = 0
            elif char == ')':
                total += sign * num
                total *= stack.pop()    # sign is popped
                total += stack.pop()    # last sum is popped
                num = 0
            i += 1
        return total + num * sign
