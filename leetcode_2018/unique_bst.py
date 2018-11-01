import pprint
pp = pprint.PrettyPrinter(indent=4)

"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

"""

# Dynamic programming solution
# Time complexity: O(n^2)
# Space Complexity: O(n)
def numTrees(n):
    """ """
    G = [0] * (n+1)
    # BST for sequence of length 1 & 0
    G[0], G[1] = 1, 1

    for i in range(2, n+1):
        for j in range(1, i+1):
            G[i] += G[j-1] * G[i-j]
    return G[n]


# Catalan number
# Time complexity: O(n)
# Space Complexity: O(1)
def numTree_catalan(n):
    """
    catalan number formula.
    C(0) = 1
    C(n+1) = C(n) * 2 (2n+1)/(n+2)
    """
    c = 1
    for i in range(n):
        c = c * 2 * (2*i + 1)/(i+2)
    return int(c)
