"""
689. Maximum Sum of 3 Non-Overlapping Subarrays

In a given array nums of positive integers, find three non-overlapping subarrays
with maximum sum.
Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.
Return the result as a list of indices representing the starting position of each
interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

Example:
Input: [1,2,1,2,6,7,5,1], 2
Output: [0, 3, 5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.

"""

class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, K):
        W = [] #array of sums of windows
        sum_ = 0
        for i, x in enumerate(nums):
            sum_ += x
            if i >= K:
                sum_ -= nums[i-K]
            if i >= K-1:
                W.append(sum_)
        # max left sum subarray
        left = [0] * len(W)
        best = 0
        for i in range(len(W)):
            if W[i] > W[best]:
                best = i
            left[i] = best
        # max right sum subarray
        right = [0] * len(W)
        best = len(W) - 1
        for i in range(len(W) - 1, -1, -1):
            if W[i] >= W[best]:
                best = i
            right[i] = best
        ans = None
        for j in xrange(K, len(W) - K):
            i, k = left[j-K], right[j+K]
            if ans is None or (W[i] + W[j] + W[k] >
                    W[ans[0]] + W[ans[1]] + W[ans[2]]):
                ans = i, j, k
        return ans

class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        p = sum(nums[i] for i in range(k))
        q = sum(nums[i] for i in range(k, 2*k))
        r = sum(nums[i] for i in range(2*k, 3*k))

        prev_p = p
        p_ind = [0]
        prev_q = p + q
        q_ind = [0, k]
        prev_r = p + q + r
        r_ind = [0, k, 2*k]

        # last index for window 1
        for i in range(1, n-3*k+1):
            p += nums[i-1+k] - nums[i-1]
            q += nums[i-1+2*k] - nums[i-1+k]
            r += nums[i-1+3*k] - nums[i-1+2*k]

            if p > prev_p:
                prev_p = p
                p_ind = [i]
            if prev_p + q > prev_q:
                prev_q = prev_p + q
                q_ind = p_ind + [i+k]
            if prev_q + r > prev_r:
                prev_r = prev_q + r
                r_ind = q_ind + [i+2*k]

        return r_ind
