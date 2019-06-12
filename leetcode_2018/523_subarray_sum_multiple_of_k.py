"""
523. Continuous Subarray Sum

Given a list of non-negative numbers and a target integer k, write a function to
check if the array has a continuous subarray of size at least 2 that sums up to
a multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.

Example 2:
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.


if sum(nums[i:j]) % k == 0 for some i < j, then sum(nums[:j]) % k == sum(nums[:i]) % k.
So we just need to use a dictionary to keep track of sum(nums[:i]) % k and the corresponding
index i. Once some later sum(nums[:i']) % k == sum(nums[:i]) % k and i' - i > 1, we return True.

Time complexity: O(n), space complexity: O(min(k, n)) if k != 0, else O(n).
"""

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        summ = 0
        hashmap = {0:-1}
        for i, n in enumerate(nums):
            if k:
                summ = (summ+n) % k
            else:
                summ += n

            if summ not in hashmap:
                hashmap[summ] = i
            else:
                if i - hashmap[summ] >=2:
                    return True
        return False
