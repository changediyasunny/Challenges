"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and
ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Running time: O(log n)
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def helper(total):
            lo = 0
            hi = len(nums)
            while lo < hi:
                mid = (lo + hi)//2
                if nums[mid] >= total:
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        # find first lef tmost index
        start = helper(target)
        # find index of target+1 since that is the place before which
        # last index of actual target will end in sorted array
        # even if target+1 is not in nums, loop break at right index
        end = helper(target+1)
        return [start, end-1] if target in nums[start:start+1] else [-1, -1]

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def helper(total, is_left):
            lo = 0
            hi = len(nums)
            while lo < hi:
                mid = (lo + hi)//2
                if nums[mid] > total or (is_left and total == nums[mid]):
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        # send is_left to exact search into left / right half
        start = helper(target, True)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = helper(target, False)
        return [start, end-1]
