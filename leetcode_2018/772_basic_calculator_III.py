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
        """
        :type s: str
        :rtype: int
        """
        def calculate(ops, num1, num2):
            if ops == "+":
                return num1 + num2
            elif ops == "-":
                return num2 - num1
            elif ops == "*":
                return num2 * num1
            elif ops == "/":
                return num2 // num1

        def valid_pred(curr_op, old_op):
            if old_op in ['(', ')']:
                return False
            if curr_op in ['*', '/'] and old_op in ['+', '-']:
                return False
            return True

        if not s:
            return 0

        num = 0
        stack = []
        opers = []
        i = 0
        while i < len(s):
            char = s[i]
            if char.isspace():
                i += 1
                continue
            if char.isdigit():
                num = int(char)
                while i < len(s)-1 and s[i+1].isdigit():
                    num = num * 10 + int(s[i+1])
                    i += 1
                if not stack and len(opers)==1 and opers[-1] == '-':
                    num = -1 * num
                    opers.pop()
                stack.append(num)
            elif char == '(':
                # brackets start here
                opers.append(char)
            elif char == ')':
                # perform inplace operation till char != ')'
                while opers[-1] != '(':
                    stack.append(calculate(opers.pop(), stack.pop(), stack.pop()))
                opers.pop()
            elif char in '* / + -':
                while len(opers) != 0 and valid_pred(char, opers[-1]):
                    stack.append(calculate(opers.pop(), stack.pop(), stack.pop()))
                opers.append(char)
            i += 1
        while len(opers) > 0:
            stack.append(calculate(opers.pop(), stack.pop(), stack.pop()))
        return stack.pop()

# TODO: invalid inputs
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        s = s + '$'
        def helper(stack, i):
            total = 0
            sign = '+'
            while i < len(s):
                char = s[i]
                if char.isspace():
                    i += 1
                    continue

                if char.isdigit():
                    total = total * 10 + int(char)
                    i += 1
                elif char == '(':
                    total, i = helper([], i+1)
                else:
                    if sign == '+':
                        stack.append(total)
                    elif sign == '-':
                        stack.append(-total)
                    elif sign == '*':
                        stack.append(stack.pop() * total)
                    elif sign == '/':
                        stack.append(int(stack.pop() // total))
                    total = 0
                    i += 1
                    if char == ')':
                        return sum(stack), i
                    sign = char
            return sum(stack)
        return helper([], 0)
