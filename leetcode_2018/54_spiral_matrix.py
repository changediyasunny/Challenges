"""
54. Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        result = []

        start_row, end_row = 0, len(matrix)-1
        start_col, end_col = 0, len(matrix[0])-1
        while start_row <= end_row and start_col <= end_col:

            # go Right
            for k in range(start_col, end_col+1):
                result.append(matrix[start_row][k])
            start_row += 1
            # print(result)
            # go down
            for k in range(start_row, end_row+1):
                result.append(matrix[k][end_col])
            end_col -= 1
            # print(result)
            # go left
            if start_row <= end_row:
                for k in range(start_col, end_col+1)[::-1]:
                    result.append(matrix[end_row][k])
            end_row -= 1
            # print(result)
            # go up
            if start_col <= end_col:
                for k in range(start_row, end_row+1)[::-1]:
                    result.append(matrix[k][start_col])
            start_col += 1
        return result
