"""
238. Product of Array Except Self

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

"""


class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1] * len(nums)
        output[0] = 1
        for i in range(1, len(nums)):
            output[i] = output[i-1] * nums[i-1]
        print(output)
        right = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] = output[i] * right
            right = right * nums[i]
        return output
