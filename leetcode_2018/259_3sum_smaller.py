"""
259. 3Sum Smaller

Given an array of n integers nums and a target, find the number of index triplets
i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example:

Input: nums = [-2,0,1,3], and target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]
Follow up: Could you solve it in O(n2) runtime?

running time: O(N^2) since i & k traverse twise
"""

def sum_smaller(nums, target):
    # we sort because we only need count of index triplets and not
    # the actual indexes window
    nums.sort()
    count = 0
    for k in range(len(nums)):
        i = 0
        j = k -1
        while i < j:
            if nums[i] + nums[j] + nums[k] < target:
                count += j - i
                i += 1
            else:
                j -= 1
    return count
