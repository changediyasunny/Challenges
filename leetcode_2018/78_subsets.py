"""
78. Subsets
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

Time: O(2^n)
Space: O(2^n)

"""

# iterative
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for n in nums:
            for i in range(len(res)):
                res.append(res[i]+[n])
        return res

# Recursive
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, start, path, result):
            result.append(path)
            for i in range(start, len(nums)):
                dfs(nums, i+1, path + [nums[i]], result)

        result = []
        nums.sort()
        dfs(nums, 0, [], result)
        return result
