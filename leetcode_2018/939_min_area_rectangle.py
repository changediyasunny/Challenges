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
    graph = defaultdict(list)
    for x, y in points:
        graph[x].append(y)
        graph[y].append(x)

    ans = float('-inf')
    points.sort(key=lambda x:x[0])
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            p = points[i]
            q = points[j]
            if p[0] != q[0] and p[1] != q[1] and q[1] in graph[p[0]] and p[1] in graph[q[0]]:
                # chekc for diagonals and then find top-left & right points
                ans = min(ans, abs(p[0]-q[0])*abs(p[1]*q[1]))
    return ans if ans != float('-inf') else 0
