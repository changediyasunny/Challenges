"""
685. Redundant Connection II

n this problem, a rooted tree is a directed graph such that, there is exactly one node (the root)
for which all other nodes are descendants of this node, plus every node has exactly one parent, except
for the root node which has no parents.

The given input is a directed graph that started as a rooted tree with N nodes
(with distinct values 1, 2, ..., N), with one additional directed edge added. The added edge
has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v]
that represents a directed edge connecting nodes u and v, where u is a parent of child v.

Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes.
If there are multiple answers, return the answer that occurs last in the given 2D-array.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given directed graph will be like this:
  1
 / \
v   v
2-->3

Example 2:
Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
Output: [4,1]
Explanation: The given directed graph will be like this:
5 <- 1 -> 2
     ^    |
     |    v
     4 <- 3

Case-1:
There is a loop in the graph, and no vertex has more than 1 parent.
Example:
Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
Output: [4,1]

Case-2:
A vertex has more than 1 parent, but there isn't a loop in the graph.
Example:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]

Case-3:
A vertex has more than 1 parent, and is part of a loop.
Example:
Input: [[2,1], [3,1], [4,2], [1,4]]
Output: [2,1]

"""
class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parent = {}
        candidate = []

        k = list(range(len(edges)+1))
        def find(x):
            while k[x] != x:
                x = k[x]
            return x

        def detect_cycle(edge):
            u, v = edge
            while u != v and u in parent:
                u = parent[u]
            return u == v

        for u, v in edges:
            if v in parent:
                # these are culprits and assume to have multiple parents
                candidate.append((parent[v], v))
                candidate.append((u, v))
            else: parent[v] = u

        if candidate:
            # some node has multiple parents or cycle exists
            return candidate[0] if detect_cycle(candidate[0]) else candidate[1]
        else:
            # ususal redundant connections
            for edge in edges:
                u, v = edge
                u = find(u)
                v = find(v)
                if u == v:
                    return edge
                k[u] = k[v]


class Solution:
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parent = [0] + [i+1 for i in range(len(edges))]
        #print(parent)
        #print("=====================")
        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        temp1 = None
        temp2 = None
        for x, y in edges:
            #print("edge is: (%s, %s)" %(x, y))
            rootx = find(x-1)
            rooty = find(y-1)

            if rootx == rooty:
                temp2 = [x, y]
                #print("temp2: %s->%s" %(x,y))
            else:
                if rooty != y-1:
                    temp1 = [x, y]
                    #print("temp1: %s->%s" %(x,y))
                else:
                    parent[rooty] = rootx
                    #print(parent)

        if not temp1: return temp2
        if not temp2: return temp1

        for x, y in edges:
            if y == temp1[1]:
                #print('I am here and returning {},{}'.format(x, y))
                return [x,y]
