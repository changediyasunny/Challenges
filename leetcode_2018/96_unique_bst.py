"""
96. Unique Binary Search Trees
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

Time: O(N^2)
Space: O(N)

"""


# Dynamic Programming
def numTrees(n):
    """
    :type n: int
    :rtype: int
    """
    T = [0]*(n + 1)
    T[0] = T[1] = 1
    for i in range(2, n+1):
        for j in range(0, i):
            T[i] += T[j] * T[i-j-1]
    return T[n]

# catalan number
def numTrees_catalan(n):
    """
    :type n: int
    :rtype: int
    """
    C = 1
    for i in range(0, n):
        C = C * 2*(2*i+1)/(i+2)
    return int(C)
