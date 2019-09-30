"""
973. K Closest Points to Origin

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
(Here, the distance between two points on a plane is the Euclidean distance.)
You may return the answer in any order.  The answer is guaranteed to be unique
(except for the order that it is in.)

Example 1:
Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)

Running Time: O(N) quick sort method
Running TIme: O(N log K) using min-heap
"""

class Solution(object):
    def kClosest(self, points, K):
        self.quicksort(points, 0, len(points)-1, K)
        return points[:K]

    def quicksort(self, points, l, r, K):
        if l < r:
            p = self.partition(points, r)
            if p == K:
                return
            elif p < K:
                self.quicksort(points, p+1, r, K)
            else:
                self.quicksort(points, l, p-1, K)

    def partition(self, points, r):
        pivot = points[r]
        l = -1
        for i in range(r+1):
            if (points[i][0]**2 + points[i][1]**2) <= (pivot[0]**2 + pivot[1]**2):
                l += 1
                points[l], points[i] = points[i], points[l]
        return l

# Heap Solution
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        result = []
        heapq.heapify(result)
        for i, p in enumerate(points):
            heapq.heappush(result, [p[0]**2 + p[1]**2,p])
        print(result)
        return [heapq.heappop(result)[1] for t in range(K)]
