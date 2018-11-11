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
Note:

Time complexity :O(log(n)). Each time we apply the formula (x ^ n) ^ 2 = x ^ {2 * n}, n is reduced by half. 
Thus we need at most O(log(n)) computations to get the result.

Space complexity : O(log(n)). For each computation, we need to store the result of x ^ {n / 2}. 
We need to do the computation for O(log(n)) times, so the space complexity is O(log(n)). 

"""

def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    result = 1
    if n < 0:
        x = 1/x
        n = -n
    while n:
        if((n&1) == 1):
            result = result * x
        n = n >> 1
        x = x * x
    return result

print(myPow(2, 9))