"""
128. Longest Consecutive Sequence

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Time: O(n)
Space: O(n)

This optimized algorithm contains only two changes from the brute force approach: the numbers are stored in a 
HashSet (or Set, in Python) to allow O(1) lookups, and we only attempt to build sequences from numbers 
that are not already part of a longer sequence. This is accomplished by first ensuring that the number that would 
immediately precede the current number in a sequence is not present, as that number would necessarily be part of 
a longer sequence.

"""


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest_range = 0
        nums_set = set(nums)
        
        for num in nums_set:
            if num-1 not in nums_set:
                current_num = num
                current_streak = 1
                while current_num+1 in nums_set:
                    current_num += 1
                    current_streak += 1
                longest_range = max(longest_range, current_streak)
        return longest_range