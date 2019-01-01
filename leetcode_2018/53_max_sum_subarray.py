"""
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

"""

# Kadane's algorithm in O(N)
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

# Kadane's algorithm: to find start & end index of subarray
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = nums[0]
        max_end = 0
        start = 0
        end = 0
        temp = 0
        for i in range(len(nums)):
            max_end = max_end + nums[i]
            if max_end > max_so_far:
                max_so_far = max_end
                start = temp
                end = i
            if max_end < 0:
                max_end = 0
                temp += 1
        print(start, end)
        return max_so_far
