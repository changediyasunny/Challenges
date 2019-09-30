"""
269. Alien Dictionary

There is a new alien language which uses the latin alphabet. However, the order
among letters are unknown to you. You receive a list of non-empty words from the
dictionary, where words are sorted lexicographically by the rules of this new language.
Derive the order of letters in this language.

Example 1:
Input:
["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Example 2:
Input:
["z", "x"]
Output: "zx"

Example 3:
Input:
["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".


"""

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        from collections import defaultdict
        chars = set()
        degree = {}
        graph = defaultdict(list)
        # create chars & in-degree
        for word in words:
            for c in word:
                chars.add(c)
                degree[c] = 0
        # create pred-graph
        for pair in zip(words, words[1:]):
            for p, r in zip(*pair):
                if p != r:
                    graph[p].append(r)
                    degree[r] += 1
                    break
        result = ''
        # there should only be one-letter having in-degree of 0
        stack = [c for c in degree if not degree[c]]
        while stack:
            k = stack.pop(0)
            result += k
            for n in graph[k]:
                degree[n] -= 1
                if not degree[n]:
                    # this is needed because for input >> ["ac","ab","b"]
                    # "b" is at 2 places. one having single-indegree and one at single letter
                    # which has indegree 0. We need to count actual in-degree.
                    stack.append(n)
        return result * (set(result) == chars)
