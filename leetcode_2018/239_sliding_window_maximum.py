"""
239. Sliding Window Maximum

Given an array nums, there is a sliding window of size k which is moving from the very left of
the array to the very right. You can only see the k numbers in the window. Each time the sliding
window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Time: O(N)
Space: O(N)
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = []
        if not nums: return []
        if k == 1: return nums
        result = []
        for i, n in enumerate(nums):
            while stack and nums[stack[-1]] < n:
                stack.pop()

            stack.append(i)
            if stack[0] == i-k:
                # window is complete. and this falls out of the window
                # eg: [7, 2, 4] >> stack = [0, 2] and stack[0] is beyond window
                stack.pop(0)
            if i >= k -1:
                # window reached max state, append number
                result.append(nums[stack[0]])
        return result
