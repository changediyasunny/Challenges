"""
480. Sliding Window Median

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value.
So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right.
You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

"""
def medianSlidingWindow(self, nums, k):
    lh,rh,rv = [],[],[]
    from heapq import heappush, heappop
    # create the initial left and right heap
    for i,n in enumerate(nums[:k]): heappush(lh, (-n,i))
    for i in range(k-k//2):
        heappush(rh, (-lh[0][0], lh[0][1]))
        heappop(lh)
    print(lh)
    print(rh)
    for i,n in enumerate(nums[k:]):
        print(i, n)
        rv.append(rh[0][0]/1 if k%2 else (rh[0][0] - lh[0][0])/2)
        if n >= rh[0][0]:
            heappush(rh,(n,i+k))        # rh +1
            if nums[i] <= rh[0][0]:     # lh-1, unbalanced
                print(">> rh: comparing %s" %nums[i])
                heappush(lh, (-rh[0][0], rh[0][1]))
                heappop(rh)
            # else: pass                # rh-1, balanced
        else:
            heappush(lh,(-n,i+k))        # rh +1
            if nums[i] >= rh[0][0]:     # rh-1, unbalanced
                print(">> lh: comparing %s" %nums[i])
                heappush(rh, (-lh[0][0], lh[0][1]))
                heappop(lh)
            # else: pass                # lh-1, balanced
        while(lh and lh[0][1] <= i): heappop(lh)  # lazy-deletion
        while(rh and rh[0][1] <= i): heappop(rh)  # lazy-deletion
    rv.append(rh[0][0]/1 if k%2 else (rh[0][0] - lh[0][0])/2)
    return rv
