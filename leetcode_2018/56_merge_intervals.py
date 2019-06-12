"""
56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.


Time complexity : O(nlgn)
Other than the sort invocation, we do a simple linear scan of the list, so the runtime is dominated by the O(nlgn)
complexity of sorting.

Space complexity : O(1) or O(n)
If we can sort intervals in place, we do not need more than constant additional space. Otherwise, we must allocate linear space to store a copy of intervals and sort that.


"""
# inputs changed as of April 15th
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x:x[0])
        merged = []
        for interval in intervals:
            if not merged or interval[0] > merged[-1][1]:
                # insert
                merged.append(interval)
            else:
                merged[-1][1] = max(interval[1], merged[-1][1])
        return merged

def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    intervals.sort(key=lambda x: x.start)
    merged = []
    for interval in intervals:
        if not merged or interval.start > merged[-1].end:
            # no overlap or beginning of merged-list
            merged.append(interval)
        else:
            # overlap
            merged[-1].end = max(merged[-1].end, interval.end)
    return merged
