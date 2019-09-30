"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case,
6 units of rain water (blue section) are being trapped.

Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Time complexity: O(n).

    We store the maximum heights upto a point using 2 iterations of O(2n) each.
    We finally update ans using the stored values in O(n).

Space complexity: O(n) extra space. Additional O(n) space for left_max and right_max arrays
"""

# O(N) & O(1) solution
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = right = water = 0
        i = 0
        j = len(height) - 1
        while i <= j:
            left = max(left, height[i])
            right = max(right, height[j])
            while i <= j and height[i] <= left <= right:
                water += left - height[i]
                i += 1
            while i <= j and height[j] <= right <= left:
                water += right - height[j]
                j -= 1
        return water

# O(N) & O(N) solution
def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    if not height:
        return 0

    n = len(height)

    # left[i] contains height of tallest bar to the
    # left of i'th bar including itself
    left = [0]*n

    # Right [i] contains height of tallest bar to
    # the right of ith bar including itself
    right = [0]*n

    # Initialize result
    water = 0

    # Fill left array
    left[0] = height[0]
    for i in range( 1, n):
        left[i] = max(left[i-1], height[i])

    # Fill right array
    right[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i+1], height[i]);

    # Calculate the accumulated water element by element
    # consider the amount of water on i'th bar, the
    # amount of water accumulated on this particular
    # bar will be equal to min(left[i], right[i]) - arr[i] .
    for i in range(0, n):
        water += min(left[i],right[i]) - height[i]
    return water

def trap(self, height):
    waterLevel = []
    left = 0
    for h in height:
        left = max(left, h)
        waterLevel += [left] # over-fill it to left max height
    right = 0
    for i, h in reversed(list(enumerate(height))):
        right = max(right, h)
        waterLevel[i] = min(waterLevel[i], right) - h # drain to the right height
    return sum(waterLevel)

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxleft, maxright = 0, 0
        left = 0
        right = len(height) - 1
        result = 0
        while left <= right:
            if height[left] <= height[right]:
                if height[left] >= maxleft: maxleft = height[left]
                else: result += maxleft-height[left]
                left += 1
            else:
                if height[right] >= maxright: maxright = height[right]
                else: result += maxright - height[right]
                right -= 1
        return result
