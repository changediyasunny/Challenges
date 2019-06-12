"""
621. Task Scheduler

Given a char array representing tasks CPU need to do. It contains capital letters
A to Z where different letters represent different tasks. Tasks could be done without
original order. Each task could be done in one interval. For each interval, CPU
could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks,
there must be at least n intervals that CPU are doing different tasks or just be idle.
You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

https://leetcode.com/problems/task-scheduler/discuss/305519/Simple-Python-O(n)-time-and-O(1)-space-in-1-Pass

"""


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_counts = collections.Counter(tasks).values()
        freq = max(task_counts)
        max_count = task_counts.count(freq)
        maps = {}
        for t in tasks:
            try:
                maps[t] += 1
            except:
                maps[t] = 1

        if len(maps) <= n+1:
            return max_count + (freq - 1) * (n+1)
        else:
            return max(len(tasks), max_count + (freq - 1) * (n+1))
