"""
50. Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

The trick is to evalute a**n as (a**(n/2))**2 when n is even, and as a*(a**((n-1)/2))**2 when n is odd.

Time complexity: O(log n)
space complexity: O(1)
"""

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        flag = True
        if n == 0:
            return 1
        if x == 0:
            return 0

        if n < 0:
            flag = False
            n = -n
        result = 1
        while n > 0:
            if n % 2 == 1:
                # odd power
                result = result * x
                n = n - 1
            else:
                x = x * x
                n = n // 2
        if flag:
            return result
        return 1/result
