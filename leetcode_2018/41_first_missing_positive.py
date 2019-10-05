"""
41. First Missing Positive
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3

Example 2:

Input: [3,4,-1,1]
Output: 2

Example 3:

Input: [7,8,9,11,12]
Output: 1

Time: O(N)
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if n < 0:
                # idea is, 1st positive number exists between 1...len(nums)
                # ignore all -ve numbers
                continue
            else:
                while n <= len(nums) and n > 0:
                    tmp = nums[n-1]
                    nums[n-1] = float('inf')
                    n = tmp

        for i in range(len(nums)):
            if nums[i] != float('inf'):
                return i+1
        # if all numbers are positive, return len(nums)+1 as nearest positive
        return len(nums)+1
