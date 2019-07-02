"""
332. Reconstruct Itinerary

Given a list of airline tickets represented by pairs of departure and arrival airports
[from, to], reconstruct the itinerary in order. All of the tickets belong to a man
who departs from JFK. Thus, the itinerary must begin with JFK.

If there are multiple valid itineraries, you should return the itinerary that has
the smallest lexical order when read as a single string. For example, the itinerary
["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].

Example 1:
Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

Example 2:
Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.

"""

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        targets = collections.defaultdict(list)
        # sorting & reversing because, smallest letter airport will
        # be at end and we can pop in stack to make it first
        for a, b in sorted(tickets)[::-1]:
            targets[a].append(b)

        route, stack = [], ['JFK']
        # print(targets)
        while stack:
            while targets[stack[-1]]:
                # get lexicographically smallest airport
                temp = targets[stack[-1]].pop()
                stack.append(temp)
            route.append(stack.pop())
        return route[::-1]
