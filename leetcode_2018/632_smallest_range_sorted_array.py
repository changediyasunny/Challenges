"""
632. Smallest Range

You have k lists of sorted integers in ascending order. Find the smallest range
that includes at least one number from each of the k lists.
We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.

Example 1:
Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
Output: [20,24]
Explanation:
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].

Keep a heap of the smallest elements. As we pop element A[i][j], we'll replace it with
A[i][j+1]. For each such element left, we want right, the maximum of the closest
value in each row of the array that is >= left, which is also equal to the current
maximum of our heap. We'll keep track of right as we proceed


Time complexity : O(n∗log(m)).
Heapification of M elements requires O(log(m)) time.
This step could be done for all the elements of the given lists in the worst case.
Here, N refers to the total number of elements in all the lists. M refers to the
total number of lists.

Space: O(M)
"""

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        # (number, i, j)
        heapmap = [(temp_list[0], i, 0) for i, temp_list in enumerate(nums)]
        heapq.heapify(heapmap)

        result = [-1e9, 1e9]
        max_num = max(temp_list[0] for temp_list in nums)
        while heapmap:
            min_num, i, j = heapq.heappop(heapmap)
            if max_num - min_num < result[1] - result[0]:
                result = [min_num, max_num]

            if j+1 == len(nums[i]):
                # exhausted atleast one list
                return result
            k = nums[i][j+1]
            max_num = max(max_num, k)
            heapq.heappush(heapmap, (k, i, j+1))
