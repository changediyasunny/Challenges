"""

"""
def pairWithEqualSum(A, n):

    # Map1 to store pairs and their sum,
    # An ordered map is used here to
    # avoid duplicate pairs of elements
    mp = {}
    for i in range(n – 1):
        for j in range(i + 1, n):
            mp[(A[i], A[j])] = A[i] + A[j]

    # Second map with key as sum and value
    # as list of pairs with that sum
    mp2 = {}

    # Start iterating first map mp and insert all
    # pairs with corresponding sum in second map mp2
    for itr in mp:
        Sum = mp[itr]
        if Sum not in mp2:
            mp2[Sum] = []
            mp2[Sum].append(itr)

    # Traverse the second map mp2, and for
    # sum with more than one pair, print
    # all pairs and the corresponding sum
    for itr in mp2:
        if len(mp2[itr]) > 1:
            print(“Pairs : “, end = “”)

    for i in range(0, len(mp2[itr])):
        print(“(“, mp2[itr][i][0], “,”,mp2[itr][i][1], “)”, end = ” “)
        print(“have sum :”, itr)

# Driver Code
A = [9, 4, 3, 1, 7, 12]
pairWithEqualSum(A, len(A))
