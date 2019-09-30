"""
845. Longest Mountain in Array

Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

    B.length >= 3
    There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]

(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain.

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.

"""
class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        up = 0
        down = 0
        result = 0
        for i in range(1, len(A)):
            if down and A[i-1] < A[i] or A[i-1] == A[i]:
                up = down = 0
            up += A[i-1] < A[i]
            down += A[i-1] > A[i]
            if up and down:
                result = max(result, up+down+1)
        return result
