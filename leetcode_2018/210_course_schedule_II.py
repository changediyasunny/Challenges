"""
210. Course Schedule II

There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have to first
take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, return the ordering
of courses you should take to finish all courses.
There may be multiple correct orders, you just need to return one of them. If it is
impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
             course 0. So the correct course order is [0,1] .

Example 2:
Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
             
"""
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(set)
        degree = [0] * numCourses
        result = []
        for i, j in prerequisites:
            graph[j].add(i)
            degree[i] += 1

        bfs = [k for k in range(numCourses) if degree[k] == 0]
        print(bfs)
        for k in bfs:
            result.append(k)
            for j in graph[k]:
                degree[j] -= 1
                if degree[j] == 0:
                    bfs.append(j)
        return result if len(bfs) == numCourses else []
