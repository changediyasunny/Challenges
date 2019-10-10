"""
221. Maximal Square

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

[
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]
Output: 4

Time: O(mn)
space: O(mn)
"""
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        m = len(matrix)
        n = len(matrix[0])
        max_result = 0
        dp = [[0] * n for _ in range(m)]
        for i in range(0, m):
            for j in range(0, n):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                elif matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_result = max(dp[i][j], max_result)
        return max_result * max_result


# Space: O(n)
# Time: O(mn)
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        m = len(matrix)
        n = len(matrix[0])
        max_result = 0
        dp = [0] * (n+1)
        prev = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                temp = dp[j]
                if matrix[i-1][j-1] == "1":
                    dp[j] = min(dp[j-1], dp[j], prev) + 1
                    max_result = max(dp[j], max_result)
                else:
                    dp[j] = 0
                prev = temp
        return max_result * max_result
