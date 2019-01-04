"""
128. Longest Consecutive Sequence

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


Time complexity : O(n)O(n).
Although the time complexity appears to be quadratic due to the while loop nested within the for loop, closer inspection reveals it to be linear.
Because the while loop is reached only when currentNum marks the beginning of a sequence (i.e. currentNum-1 is not present in nums), the while
loop can only run for n iterations throughout the entire runtime of the algorithm. This means that despite looking like O(n^2) complexity,
the nested loops actually run in O(n + n) = O(n+n)=O(n) time. All other computations occur in constant time, so the overall runtime is linear.

Space complexity : O(n).
In order to set up O(1) containment lookups, we allocate linear space for a hash table to store the O(n) numbers in nums.
Other than that, the space complexity is identical to that of the brute force solution.

"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest_range = 0
        # set allows O(1) lookup
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
