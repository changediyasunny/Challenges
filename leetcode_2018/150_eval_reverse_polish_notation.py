"""
150. Evaluate Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and
there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation:
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

"""

import operator
class Solution(object):
    def evalRPN_ops(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "/": operator.truediv,
            "*": operator.mul
        }

        for token in tokens:
            if token in ops:
                y = stack.pop()
                x = stack.pop()
                stack.append(int(ops[token](x, y)))
            else:
                stack.append(int(token))
        return stack.pop()

class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        ops = ['+', '-', '*', '/']
        for t in tokens:
            if t in ops:
                n1 = stack.pop()
                n2 = stack.pop()
                if t == '+':
                    stack.append(n1+n2)
                elif t == '-':
                    stack.append(n2-n1)
                elif t == '/':
                    stack.append(int(n2/float(n1)))
                elif t == '*':
                    stack.append(n1*n2)
            else:
                stack.append(int(t))
        return stack.pop()
