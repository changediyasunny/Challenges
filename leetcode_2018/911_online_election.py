"""
911. Online Election

In an election, the i-th vote was cast for persons[i] at time times[i].
Now, we would like to implement the following query function: TopVotedCandidate.q(int t)
will return the number of the person that was leading the election at time t.
Votes cast at time t will count towards our query.  In the case of a tie, the most recent vote (among tied candidates) wins.


Example 1:

Input: ["TopVotedCandidate","q","q","q","q","q","q"], [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
Output: [null,0,1,1,0,0,1]
Explanation:
At time 3, the votes are [0], and 0 is leading.
At time 12, the votes are [0,1,1], and 1 is leading.
At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
This continues for 3 more queries at time 15, 24, and 8.

Time Complexity: O(N+QlogN), where N is the number of votes, and Q is the number of queries.
Space Complexity: O(N).
"""


class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.winner = []
        self.times = times
        leader = -1
        count = {}
        for p in persons:
            count[p] = count.get(p, 0) + 1
            if count[p] >= count.get(leader, 0):
                leader = p
            self.winner.append(leader)

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        return self.winner[bisect.bisect(self.times, t)-1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
