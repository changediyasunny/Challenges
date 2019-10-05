"""
772. Basic Calculator III

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus +
or minus sign -, non-negative integers and empty spaces .
The expression string contains only non-negative integers, +, -, *, / operators ,
open ( and closing parentheses ) and empty spaces . The integer division should
truncate toward zero.
You may assume that the given expression is always valid. All intermediate results
will be in the range of [-2147483648, 2147483647].

Some examples:

"1 + 1" = 2
" 6-4 / 2 " = 4
"2*(5+5*2)/3+(6/2+8)" = 21
"(2+6* 3+5- (3*14/7+2)*5)+3"=-12

#TODO: doesn't work with -ve integers
-1+1
"1 - (-7)"

"""
class Solution(object):

    def calculate(self, s):
        return self.helper(list(s))

    def helper(self, array):
        if len(array) == 0:
            return 0
        sign = '+'
        num = 0
        stack = []
        while array:
            char = array.pop(0)
            if char.isdigit():
                num = num * 10 + int(char)
            if char == "(":
                num = self.helper(array)
            if char in '+-*/)' or len(array)==0:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-1*num)
                elif sign == '*':
                    stack[-1] = stack[-1] * num
                elif sign == '/':
                    stack[-1] = int(stack[-1]/float(num))
                sign = char
                num = 0
                if sign == ")":
                    break
        return sum(stack)
