"""
593. Valid Square
Given the coordinates of four points in 2D space, return whether the four points could construct a square.
The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True

"""

# Using side length & diagonal distance
class Solution:
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        if p1==p2==p3==p4:
            return False
        def dist(x, y):
            return (x[0]-y[0])**2 + (x[1]-y[1])**2

        ls = [dist(p1,p2), dist(p1,p3), dist(p1,p4), dist(p2,p3), dist(p2,p4), dist(p3,p4)]
        ls.sort()
        if ls[0] == ls[1] == ls[2] == ls[3]:
            if ls[4] == ls[5]:
                return True
        return False

# determine last two points only.
class Solution:
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        if p1==p2==p3==p4:
            return False
        x = 0
        y = 1
        p1, p2, p3, p4 = sorted([p1, p2, p3, p4])
        if p2[y] < p3[y]:
            p2, p3 = p3, p2

        return p3 == [p1[x] + (p2[y] - p1[y]), p1[y] - (p2[x] - p1[x])]\
                and p4 == [p2[x] + (p2[y]-p1[y]), p2[y] - (p2[x]-p1[x])]
