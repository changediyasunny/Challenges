"""
4. Median of two sorted Arrays:

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5

complexity: Log(min(m, n))
"""

def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    if (len(nums1) > len(nums2)):
        return findMedianSortedArrays(nums2, nums1)

    x = len(nums1)
    y = len(nums2)

    low = 0
    high = x
    while (low <= high):
        partitionX = (low + high) // 2
        partitionY = ((x + y + 1) // 2) - partitionX

        max_left_X = float("-inf") if partitionX == 0 else nums1[partitionX - 1]
        max_left_Y = float("-inf") if partitionY == 0 else nums2[partitionY - 1]

        min_right_X = float("inf") if partitionX == x else nums1[partitionX]
        min_right_Y = float("inf") if partitionY == y else nums2[partitionY]

        if (max_left_X <= min_right_Y and max_left_Y <= min_right_X):
            if ((x + y) % 2 == 0):
                return (max(max_left_X, max_left_Y) + min(min_right_X, min_right_Y)) / 2
            else:
                return max(max_left_X, max_left_Y)
        elif (max_left_X > min_right_Y):
            # move towards left side
            high = partitionX - 1
        else:
            # move towards right side
            low = partitionX + 1
