"""
498. Diagonal Traverse
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in
diagonal order as shown in the below image

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

"""

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        result = []
        hashmap = collections.defaultdict(list)
        # for diagonal elements, row+col is same
        # store them under hashmap adn they fall into same bucket
        # start at key 1, 'cause we need odd/even length to reverse values
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                hashmap[i+j+1].append(matrix[i][j])

        for k, v in hashmap.items():
            if k%2 == 1:
                result += v[::-1]
            else: result += v
        return result
