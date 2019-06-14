"""
349. Intersection of Two Arrays

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) < len(nums2):
            return self.intersection(nums2, nums1)

        nums1 = set(nums1)
        nums2 = set(nums2)
        result = set()
        for n in nums2:
            if n in nums1:
                result.add(n)
        return result
