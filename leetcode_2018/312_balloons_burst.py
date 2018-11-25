"""
312. Burst Balloons

Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. 
You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. 
Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

"""

import sys
import pprint
pp = pprint.PrettyPrinter(indent=4)

def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    N = len(nums)
    dp = [[1]*N for _ in range(N)]
    for gap in range(1, N+1):
        for i in range(0, N-gap+1):
            j = i + gap - 1
            for k in range(i, j+1):
                print(i, j, k)
                left_val = 1
                right_val = 1
                if i != 0:
                    left_val = nums[i-1]

                if j != (len(nums)-1):
                    rigth_val = nums[j+1]
                print(len(nums)-1)
                print(">>left=%s| num=%s| right=%s" %(left_val, nums[k], right_val))
                # if k is i, then proceeed
                before = 0
                after = 0
                if i != k:
                    before = dp[i][k-1]
                print("before: %s" %before)
                if j != k:
                    after = dp[k+1][j]
                print("after: %s" %after)

                result = before + (left_val * nums[k] * right_val) + after
                print("result : %s" %result)
                dp[i][j] = max(dp[i][j], result)
                print(dp)
                print("===========================")
    pp.pprint(dp)
    return dp[0][N-1]

print([3,1,5,8])
print(maxCoins([3,1,5,8]))