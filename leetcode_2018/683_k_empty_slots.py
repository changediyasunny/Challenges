"""
683. K Empty Slots

There is a garden with N slots. In each slot, there is a flower. The N flowers will
bloom one by one in N days. In each day, there will be exactly one flower blooming and
it will be in the status of blooming since then.

Given an array flowers consists of number from 1 to N. Each number in the array represents
the place where the flower will open in that day.

For example, flowers[i] = x means that the unique flower that blooms at day i will be at
position x, where i and x will be in the range from 1 to N.

Also given an integer k, you need to output in which day there exists two flowers in
the status of blooming, and also the number of flowers between them is k and these
flowers are not blooming.

If there isn't such day, output -1.

Example 1:
Input:
flowers: [1,3,2]
k: 1
Output: 2
Explanation: In the second day, the first and the third flower have become blooming.

Example 2:
Input:
flowers: [1,2,3]
k: 1
Output: -1

Time: O(N)
Space: O(N)
"""
import sys

def kEmptyslots(flowers, k):
    N = len(flowers)
    pots = [0] * N

    for i in range(N):
        pots[flower[i]-1] = i + 1

    result = float('inf')
    left = 0
    right = k + 1
    for i in range(1, N):
        if right >= len(pots):
            break

        if pots[i] > pots[left] and pots[i] > pots[right]:
            continue
        if i == right:
            result = min(result, max(pots[left], pots[right]))

        left = i
        right = left + k + 1
    return result if result < float('inf') else -1

flowers = [6,5,8,9,7,1,10,2,3,4]
k = 2
