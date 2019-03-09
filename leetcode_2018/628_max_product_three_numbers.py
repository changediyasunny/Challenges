"""
628. Maximum Product of Three Numbers

Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6

Example 2:
Input: [1,2,3,4]
Output: 24

"""

# using sorting. We need to handle negative numbers too
# O(NlogN)
def maximumProduct(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])

# O(N) using single pointer
def maximumProduct(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max1 = max2 = max3 = float('-inf')
    min1 = min2 = float('inf')
    for n in nums:
        if n >= max1:
            max3 = max2
            max2 = max1
            max1 = n
        elif n >= max2:
            max3 = max2
            max2 = n
        elif n >= max3:
            max3 = n

        if n <= min1:
            min2 = min1
            min1 = n
        elif n <= min2:
            min2 = n
    return max (max1*max2*max3, min1*min2*max1)
