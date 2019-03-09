"""
7. Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        tmp = x
        if x < 0:
            x = x * (-1)
        while x != 0:
            rev = (rev * 10) + (x%10)
            x = x // 10
        if tmp < 0:
            rev = rev * (-1)
        # Handling overflow
        if -2 ** 31 <= rev <= 2 ** 31 - 1:
            return rev
        return 0
