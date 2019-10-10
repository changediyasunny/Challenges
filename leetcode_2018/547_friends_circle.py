"""
547. Friend Circles

There are N students in a class. Some of them are friends, while some are not. Their
friendship is transitive in nature. For example, if A is a direct friend of B, and B is a
direct friend of C, then A is an indirect friend of C. And we defined a friend circle is
a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class.
If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not.
And you have to output the total number of friend circles among all the students.

Example 1:

Input:
[[1,1,0],
[1,1,0],
[0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
The 2nd student himself is in a friend circle. So return 2.


Input:
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.

Time: O(N*2)
Space: O(N)

Explanation:
Very trickey execution for DFS & BFS strategy. Problem reduces to finding conencted components without traversive matrix
up/down/left/right. In this case we introduce visited() set to note vertices indexes.
>> [
    [1,1],
    [1,1]
]
In above case, both indexes 0 & 1 would be already visited and we can exclude indixes from row = 1.
"""

# DFS Solution
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def dfs(i, M, visited):
            for j in range(len(M)):
                if M[i][j] and j not in visited:
                    visited.add(j)
                    dfs(j, M, visited)

        visited = set()
        count = 0
        for i in range(len(M)):
            if i not in visited:
                dfs(i, M, visited)
                count += 1
        return count

# BFS Solution
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        count = 0
        visited = set()
        stack = []
        for i in range(len(M)):
            if i not in visited:
                stack.append(i)
                while stack:
                    ind = stack.pop(0)
                    visited.add(ind)
                    for nei, val in enumerate(M[ind]):
                        if val and nei not in visited:
                            stack.append(nei)
                count += 1
        return count
