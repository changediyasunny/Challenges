"""
Word wrap and text justification
Write an algorithm for word wrap (width = 12) of a huge file.

space: O(n^2)
time: O(n^2)

"""
def word_wrap(input_strs, width):
    n = len(input_strs)
    cost = [[-1] * n for _ in range(n)]

    # fill up cost matrix
    for i in range(n):
        cost[i][i] = width - len(input_strs[i])
        for j in range(i+1, n):
            cost[i][j] = cost[i][j-1] - len(input_strs[j]) - 1
    # square matrix
    for i in range(n):
        for j in range(i, n):
            if cost[i][j] < 0:
                cost[i][j] = 99999
            else:
                cost[i][j] = cost[i][j]**2

    pp.pprint(cost)
    # find min cost
    mincost = [0] * n
    result = [0] * n
    for i in range(n-1, -1, -1):
        mincost[i] = cost[i][n-1]
        result[i] = n
        j = n-1
        while j > i:
            if cost[i][j-1] == 9999 or cost[i][j-1] == -1:
                continue
            if mincost[i] > mincost[j] + cost[i][j-1]:
                mincost[i] = mincost[j] + cost[i][j-1]
                result[i] = j
            j -= 1
    print(">>")
    print("minimum cost is: %s" %mincost[0])
    final_result = []
    j = 0
    i = 0
    while j < len(input_strs):
        j = result[i]
        strs = ''
        for k in range(i, j):
            strs += input_strs[k] + ' '
        print(strs)
        i = j

input_strs = ['sunnyc', 'cha', 'likes', 'to', 'code']
word_wrap(input_strs, 10)
