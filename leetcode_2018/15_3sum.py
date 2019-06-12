"""
15. 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that
a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

Running time: O(n^2)
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        # sort numbers to find smallest element
        nums.sort()
        target = 0
        result = []
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                # it means that we have already consider nums[i] smallest
                # hense jump to next otherwise it leads to duplicate triplets
                continue
            j = i+1
            k = n-1
            while j < k:
                curr = nums[i] + nums[j] + nums[k]
                if curr < target:
                    # find next element if triplet doesn't match up
                    j += 1
                elif curr > target:
                    # sum is greater. need to decrement k as largest element
                    k -= 1
                else:
                    # sum found
                    result.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        # remove duplicate triplets
                        j += 1
                    while k > j and nums[k] == nums[k-1]:
                        # remove duplicate triplets
                        k -= 1
                    j += 1
                    k -= 1
        return result
