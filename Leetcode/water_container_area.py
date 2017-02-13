"""
WATER CONTAINER:
==========================
Given N non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example :

Input : [1, 5, 4, 3]
Output : 6

Explanation : 5 and 3 are distance 2 apart. So size of the base = 2. Height of container = min(5, 3) = 3. 
So total area = 3 * 2 = 6

"""

"""
TRAP RAINING WATER:
========================
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

Draw vertical lines on X-axis and see how it traps water.
"""

import sys

def water_container(temp_list):
	n = len(temp_list)
	i = 0
	j = n - 1
	final_area = 0
	# iterate through all points. each line represents a vertical line and consider An to be height of it.
	while(i < j):
		# find min_height & base so as to find area of container
		min_height = min(temp_list[i], temp_list[j])
		base = j - i
		area = min_height * base
		# get maximum area out of it.
		final_area = max(area, final_area)
		if temp_list[i] > temp_list[j]:
			j = j - 1
		else:
			i = i + 1
	return final_area


def trap_raining_water(height):
    """
    :type height: List[int]
    :rtype: int
    """
    p_left = 0
    p_right = 0
    n = len(height)
    left = 0
    water = 0
    right = n - 1
    while(left <= right):
        if height[left] <= height[right]:
            # do for left side
            if height[left] >= p_left:
                p_left = height[left]
            else:
                # only when p_left > 
                water = water + p_left - height[left]
            left = left + 1
        else:
            # do for right side
            if height[right] >= p_right:
                p_right = height[right]
            else:
                water = water + p_right - height[right]
            right = right - 1
    return water



def main():
	# temp_list = [1, 2, 3, 8, 7, 5, 4]
	# temp_list = [1, 2, 8, 7, 4, 3]
	temp_list = [1, 5, 4, 3]
	result = water_container(temp_list)
	print(result)

	# Trapping raining water 
	height_array = [0,1,0,2,1,0,1,3,2,1,2,1]
	water = trap_raining_water(height_array)
	print("Water trapped is: %s" %water)
	

if __name__ == '__main__':
	main()