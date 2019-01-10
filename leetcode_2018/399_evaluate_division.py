"""
399. Evaluate Division

Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real
number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

According to the example above:
equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].

"""

# Using floyd warshall algorithm by precomputing values
# runnign time: O(V^2)
class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        result = collections.defaultdict(dict)
        for (nur, den), val in zip(equations, values):
            result[nur][nur] = result[den][den] = 1.0
            result[nur][den] = val
            result[den][nur] = 1/val

        for st in result:
            for i in result[st]:
                for j in result[st]:
                    result[i][j] = result[i][st] * result[st][j]
        return [ result[n].get(d, -1.0) for n, d in queries ]

# DFS + Stack
# running time: O(V + E)
class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = collections.defaultdict(set)
        for (numr, den), val in zip(equations, values):
            graph[numr].add((den, val))
            graph[den].add((numr, 1/val))

        def find_total(n, d):
            if n not in graph or d not in graph:
                return -1.0
            stack = [(n, 1.0)]
            visited = set()
            while stack:
                numr, val = stack.pop()
                if numr == d:
                    return val
                visited.add(numr)
                for nei, v in graph[numr]:
                    if nei not in visited:
                        stack.append((nei, val * v))
            return -1.0

        result = []
        for n, d in queries:
            result.append(find_total(n,d))
        return result
