"""
308. Range Sum Query 2D- mutable

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined
by its upper left corner (row1, col1) and lower right corner (row2, col2).

Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
update(3, 2, 2)
sumRegion(2, 1, 4, 3) -> 10
"""

# O(n) for both update and sum
class RangeSum(object):
    def __init__(self, matrix):
        for row in matrix:
            for k in range(1, len(row)):
                row[k] += row[k-1]
        self.matrix = matrix

    def update(self, row, col, val):
        curr_val = self.matrix[row][col]
        if col != 0:
            curr_val -= self.matrix[row][col-1]
        diff = curr_val - val
        for k in range(col, len(self.matric[0])):
            self.matrix[row][k] -= diff

    def sumRegion(self, row1, col1, row2, col2):
        result = 0
        for x in range(row1, row2+1):
            # add last column only
            result += self.matrix[x][col2]
            if col1 != 0:
                # subtract first column
                result -= self.matrix[x][col1-1]
        return result

# Binary Indexed Tree
class NumMatrix:
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix:
            return
        self.M = len(matrix)
        self.N = len(matrix[0])
        self.BIT = [[0] * (self.N+1) for _ in range(self.M+1)]
        self.mat = [[0] * (self.N) for _ in range(self.M)]
        for i in range(self.M):
            for j in range(self.N):
                self.update(i, j, matrix[i][j])
        pp.pprint(self.BIT)

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        diff = val - self.mat[row][col]
        self.mat[row][col] = val
        i = row + 1
        print(">> %s -> %s" %(row, col))
        while i <= self.M:
            j = col + 1
            while j <= self.N:
                print(i, j, diff)
                self.BIT[i][j] += diff
                j += (j & -j)
            i += (i & -i)

    def add(self, row, col):
        result = 0
        i = row + 1
        while i:
            j = col + 1
            while j:
                result += self.BIT[i][j]
                j -= (j & -j)
            i -= (i & -i)
        return result

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.add(row2, col2) + self.add(row1-1, col1-1) - self.add(row1-1, col2) - self.add(row2, col1-1)
