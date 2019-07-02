"""
845. Longest Mountain in Array

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
