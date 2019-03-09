"""
Optimal travel distance:

Given max. travel distance and forward and backward route list, return pair of ids of
forward and backward routes that optimally utilized the max travel distance.:

target = 9000
forward = [[1,3000],[2,5000],[3,4000],[4,10000]]
backward = [[1,2000],[2,3000],[3,4000]]
"""

# Using min-heap:
# to sort: (n log n) + M (backward array length)
# Space: O(M) for heap
def optimal_travel_heap(forward, backward, target):
    forward.sort(key=lambda x:x[1])
    print("forward: %s" %forward)
    print("backward: %s" %backward)
    temp_list = []
    for ind, val in backward:
        if (target-val) <= 0:
            continue
        heapq.heappush(temp_list, (target-val, ind))
    print(temp_list)
    closest = forward[0][1]
    fwd_ind = forward[0][0]
    for ind, val in forward[1:]:
        print(ind, val)
        if closest < val <= temp_list[0][0]:
            closest = val
            fwd_ind = ind
    return [fwd_ind, temp_list[0][1]]


# Time: O(nlog(n) + mlog(n)) = O((n+m) * log(n))
# where n is the number of forward routes and m the number of backward routes.
# Space: O(1)
def optimal_travel_binary(forward, backward, target):
    result = [0, 0, 0]
    forward.sort(key=lambda x:x[1])
    print("forward: %s" %forward)
    print("backward: %s" %backward)

    def binary_search(dist):
        low = 0
        high = len(forward) - 1
        while low < high:
            mid = (low+high)//2
            if dist < forward[mid][1]:
                high = mid - 1
            elif dist > forward[mid][1]:
                low = mid + 1
            else:
                return mid
        if forward[high][1] <= dist:
            return high
        return high - 1

    result = 0
    ids =[0, 0]
    for ind, val in backward:
        k = binary_search(target-val)
        if result < val + forward[k][1] <= target:
            result = val + forward[k][1]
            ids = [forward[k][0], ind]
    return ids

target = 11000
forward = [[1,3000],[2,5000],[3,4000],[4,10000]]
backward = [[2,3000],[3,4000], [1,2000]]

optimal_travel_heap(forward, backward, target)
#optimal_travel_binary(forward, backward, target)
