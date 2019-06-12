"""
215. Kth Largest Element in an Array

Find the kth largest element in an unsorted array. Note that it is the kth largest
element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Running time: (N) for quick select algorithm.
"""

class Solution(object):
    def partition(self, nums, lo, hi):
        t = lo
        pivot = nums[hi]
        for i in range(lo, hi):
            if nums[i] <= pivot:
                nums[t], nums[i] = nums[i], nums[t]
                t += 1
        nums[t], nums[hi] = nums[hi], nums[t]
        return t

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        # to find kth smallest using quick select
        k = len(nums) - k
        while True:
            idx = self.partition(nums, left, right)
            if idx == k:
                return nums[idx]
            elif idx < k:
                left = idx + 1
            else:
                right = idx - 1
        return -1
