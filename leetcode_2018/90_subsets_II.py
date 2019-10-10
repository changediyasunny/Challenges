"""
90. Subsets II

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

Time: O(2^n)
Space: O(2^n)

"""
# Iterative
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        maps = collections.Counter(nums)

        for k, v in maps.items():
            temp = []
            print(k, v , res)
            for lst in res:
                for p in range(1, v+1):
                    temp.append(lst + [k] * p)
            res += temp
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
                if i > start and nums[i] == nums[i-1]:
                    continue
                dfs(nums, i+1, path + [nums[i]], result)


        result = []
        nums.sort()
        dfs(nums, 0, [], result)
        return result
