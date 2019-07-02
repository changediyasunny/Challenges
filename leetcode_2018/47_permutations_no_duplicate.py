"""
47. Permutations II

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

"""
class Solution(object):
    def permuteUnique(self, nums):
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
                    if k < len(comb) and comb[k] == n:
                        # remove duplicate if last number is same
                        # and index is small
                        break
                result = temp
        return result
