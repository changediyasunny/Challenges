"""
152. Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray


"""

# prefix and suffix sum of array and their maximum is
# max product amongst sub-array
def maxProduct(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    A = nums
    B = A[::-1]
    for i in range(1, len(A)):
        if A[i-1] != 0:
            A[i] *= A[i - 1]
        if B[i-1] != 0:
            B[i] *= B[i - 1]
    print(A)
    print(B)
    return max(A + B)

# using two pointers
def maxProduct(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    r = nums[0]
    imax = r
    imin = r
    for i in range(1, len(nums)):
        print(nums[i], imax, imin)
        # multiplied by a negative makes big number smaller, small number bigger
        # so we redefine the extremums by swapping them
        if nums[i]<0:
            imax, imin = imin, imax

        imax = max(nums[i], imax*nums[i])
        imin = min(nums[i], imin*nums[i])
        r = max(r, imax)
    return r
