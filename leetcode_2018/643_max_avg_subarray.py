"""
643. Maximum Average Subarray I

Given an array consisting of n integers, find the contiguous subarray of given length k
that has the maximum average value. And you need to output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

Running Time: O(N)
Space: O(1)
"""

# Sliding Window
class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if not nums:
            return 0
        target = sum(nums[:k])
        result = target
        for i in range(k, len(nums)):
            target += nums[i] - nums[i-k]
            result = max(result, target)
        return result/k
