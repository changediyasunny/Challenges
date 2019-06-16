"""
674. Longest Continuous Increasing Subsequence

Given an unsorted array of integers, find the length of longest continuous increasing
subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous
one where 5 and 7 are separated by 4.

Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1.

Time: O(N)
"""
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        maxlen = 1
        end = 0
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                end = i
            maxlen = max(maxlen, i-end+1)
        return maxlen
