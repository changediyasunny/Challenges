"""
253. Meeting Rooms II

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1

Time Complexity: O(NlogN).

There are two major portions that take up time here. One is sorting of the array that takes O(NlogN)
considering that the array consists of N elements.

Then we have the min-heap. In the worst case, all N meetings will collide with each other. In any case we have N
add operations on the heap. In the worst case we will have N extract-min operations as well. Overall complexity
being (NlogN) since extract-min operation on a heap takes O(logN).

Space Complexity: O(N) because we construct the min-heap and that can contain N elements in the worst case as described
above in the time complexity section. Hence, the space complexity is O(N).
"""



# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

def minMeetingRooms(self, intervals):
    """
    :type intervals: List[Interval]
    :rtype: int
    """
    # If there is no meeting to schedule then no room needs to be allocated.
    if not intervals:
        return 0

    # The heap initialization
    free_rooms = []

    # Sort the meetings in increasing order of their start time.
    intervals.sort(key= lambda x: x.start)

    # Add the first meeting.
    heapq.heappush(free_rooms, intervals[0].end)

    # For all the remaining meeting rooms
    for i in intervals[1:]:

        # If the room due to free up the earliest is free, assign that room to this meeting.
        if free_rooms[0] <= i.start:
            heapq.heappop(free_rooms)

        # If a new room is to be assigned, then also we add to the heap,
        # If an old room is allocated, then also we have to add to the heap with updated end time.
        heapq.heappush(free_rooms, i.end)

    # The size of the heap tells us the minimum rooms required for all the meetings.
    return len(free_rooms)
