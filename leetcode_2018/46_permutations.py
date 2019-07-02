"""
46. Permutations
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""
# with duplicate permutations
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for n in nums:
            temp = []
            for comb in result:
                for k in range(len(comb)+1):
                    temp.append(comb[:k] + [n] + comb[k:])
            result = temp
        return result

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        def DFS(nums, path):
            if not nums:
                result.append(path)
            for i in range(len(nums)):
                DFS(nums[:i]+nums[i+1:], path+[nums[i]])
        DFS(nums, [])
        return result

def permute(self, nums):
    return [[n] + p
            for i, n in enumerate(nums)
            for p in self.permute(nums[:i] + nums[i+1:])] or [[]]
