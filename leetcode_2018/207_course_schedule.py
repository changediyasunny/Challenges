"""
207. Course Schedule

There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have to first
take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible
for you to finish all courses?

Example 1:
Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
          To take course 1 you should have finished course 0, and to take course 0 you should
          also have finished course 1. So it is impossible.
"""
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(set)
        degree = [0] * numCourses
        for i, j in prerequisites:
            graph[j].add(i)
            degree[i] += 1

        bfs = [k for k in range(numCourses) if degree[k] == 0]
        for k in bfs:
            for j in graph[k]:
                degree[j] -= 1
                if degree[j] == 0:
                    bfs.append(j)
        return len(bfs) == numCourses



class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(set)
        for i, j in prerequisites:
            graph[j].add(i)
        color = [0] * numCourses
        def dfs(idx):
            color[idx] = 1
            if idx in graph:
                for j in graph[idx]:
                    if color[j] == 0:
                        if not dfs(j):
                            return False
                    elif color[j] == 1:
                        return False
            color[idx] = 2
            return True

        for k in range(numCourses):
            if color[k] == 0:
                if not dfs(k):
                    return False
        return True
