"""
There are an infinite number of train stops starting from station number 0.
There are an infinite number of trains. The nth train stops at all of the k * 2^(n - 1)
stops where k is between 0 and infinity. When n = 1, the first train stops at stops 0, 1, 2, 3, 4, 5, 6, etc.

When n = 2, the second train stops at stops 0, 2, 4, 6, 8, etc.
When n = 3, the third train stops at stops 0, 4, 8, 12, etc.
Given a start station number and end station number, return the minimum number of stops between them.
You can use any of the trains to get from one stop to another stop.

For example, the minimum number of stops between start = 1 and end = 4 is 2 because we can get from 1 to 2 to 4.

Algorithm:
https://stackoverflow.com/questions/48535741/minimum-number-of-train-station-stops

"""
def binary_subtract(x, y):
    if (y == 0):
        return x
    return binary_subtract(x ^ y, (~x & y) << 1)

def get_intermediate_stop(end):
    n = 1
    max_near = 1
    result = 1
    while result <= end:
        result <<= 1
        if result <= end:
            n += 1
    print("fastest train is: %s" %(n-1))
    train_num = n-1
    inter = temp = 1
    k = 1
    while temp <= end:
        if temp < end:
            inter = temp
        temp = k * (2**(train_num-1))
        k = k + 1
    print("intermediate stop:>> %s" %inter)
    return inter

def countSetBits(n):
    # gives number of stops required.
    count = 0
    while (n):
        n &= (n-1)
        count+=1
    return count

def find_min_train_stops(start, end):
    if start == end:
        return 0
    elif start == end-1:
        return 1
    # find intermediate stop
    print(">> Start: %s" %start)
    intermediate_stop = get_intermediate_stop(end)
    print(">> Intermediate: %s" %intermediate_stop)
    print(">> end: %s" %end)
    # steps from start to intermediate stop
    first_hop = binary_subtract(intermediate_stop, start)
    second_hop = binary_subtract(end, intermediate_stop)
    print(">>>> %s" %first_hop)
    print(">>>> %s" %second_hop)
    return countSetBits(first_hop) + countSetBits(second_hop)

find_min_train_stops(1, 4)
