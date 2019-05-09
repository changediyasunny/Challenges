"""
939. Minimum Area Rectangle

Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.
If there isn't any rectangle, return 0.

Example 1:
Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4

Example 2:
Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2

running time: O(N^2)
space: O(N)
"""

def minAreaRect(points):
    ans = float('inf')
    # need set object for different lookup
    S = set(map(tuple, points))
    for j, p2 in enumerate(points):
        for i in range(j):
            p1 = points[i]
            if p1[0] != p2[0] and p1[1] != p2[1] and (p1[0], p2[1]) in S and (p2[0], p1[1]) in S:
                # chekc for diagonals and then find top-left & right points
                ans = min(ans, abs(p1[0]-p2[0])*abs(p1[1]- p2[1]))
    return ans if ans < float('inf') else 0
