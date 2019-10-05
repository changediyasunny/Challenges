"""
1. Two sums

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""
import sys

# One-pass solution
def two_sums(nums, target):
    """ One-Pass solution using hash-map """
    N = len(nums)
    hash_map = {}
    for i in range(N):
        t = target - nums[i]
        if nums[i] in hash_map:
            return [ hash_map[nums[i]], i ]
        else:
            hash_map[t] = i
