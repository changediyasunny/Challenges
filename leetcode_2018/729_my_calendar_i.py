"""
729. My Calendar I

Implement a MyCalendarTwo class to store your events. A new event can be added if
adding the event will not cause a double booking. Your class will have one method,
book(int start, int end). Formally, this represents a booking on the half open interval
[start, end), the range of real numbers x such that start <= x < end. A double booking happens
when three events have some non-empty intersection (ie., there is some time that is common to all 3 events.)

For each call to the method MyCalendar.book, return true if the event can be added to
the calendar successfully without causing a double booking. Otherwise, return false and do
not add the event to the calendar.
Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)

MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation:
The first event can be booked.  The second can't because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.


Time Complexity: O(N^2) where N is the number of events booked. For each new event, we process
every previous event to decide whether the new event can be booked.
Space Complexity: O(N), the size of the calendar

"""

class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for i, j in self.calendar:
            if start < j and end > i:
                return False

        self.calendar.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
