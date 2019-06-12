"""
560. Subarray Sum Equals K

Given an array of integers and an integer k, you need to find the total number of continuous
subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2

"""

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hashmap = collections.Counter()
        hashmap[0] = 1
        summ = 0
        res = 0
        for n in nums:
            summ += n
            if (summ - k) in hashmap:
                res += hashmap[summ-k]
            hashmap[summ] += 1
        return res
