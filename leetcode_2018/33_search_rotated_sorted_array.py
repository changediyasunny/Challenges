"""
33. Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

"""


def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    low = 0
    high = len(nums) - 1
    while low < high:
        mid = (low + high)//2
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid

    rot = low
    low = 0
    high = len(nums) - 1
    print("rot: %s" %rot)
    while low <= high:
        mid = (low+high)//2
        realmid = (mid+rot)%len(nums)
        print(mid, realmid)
        if nums[realmid] == target:
            return realmid
        if nums[realmid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Single pass solution
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low + high)//2

            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:
                # <= is necessary because [3,1], low & mid falls on same index
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
