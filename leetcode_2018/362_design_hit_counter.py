"""
362. Design Hit Counter

Design a hit counter which counts the number of hits received in the past 5 minutes.
Each function accepts a timestamp parameter (in seconds granularity) and you may assume that
calls are being made to the system in chronological order (ie, the timestamp is
monotonically increasing). You may assume that the earliest timestamp starts at 1.
It is possible that several hits arrive roughly at the same time.

HitCounter counter = new HitCounter();

// hit at timestamp 1.
counter.hit(1);

// hit at timestamp 2.
counter.hit(2);

// hit at timestamp 3.
counter.hit(3);

// get hits at timestamp 4, should return 3.
counter.getHits(4);

// hit at timestamp 300.
counter.hit(300);

// get hits at timestamp 300, should return 4.
counter.getHits(300);

// get hits at timestamp 301, should return 3.
counter.getHits(301);

Explanation:
When timestamp is 300, the last 5 misn range is from 1 sec ... 300 sec.
When timestamp is 301, the last 5 mins range is from 2 sec ... 301 sec.
...

"""
class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_of_hits = 0
        self.time_hits = []    # (timestamp, frequency)

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        if not self.time_hits or self.time_hits[-1][0] != timestamp:
            self.time_hits.append([timestamp, 1])
        else:
            self.time_hits[-1][1] += 1
        self.num_of_hits += 1


    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        while self.time_hits and self.time_hits[0][0] <= (timestamp-300):
            self.num_of_hits -= self.time_hits.pop(0)[1]
        return self.num_of_hits


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
