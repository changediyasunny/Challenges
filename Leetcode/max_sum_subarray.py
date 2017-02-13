
"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""


import sys

#nums = [-2, 1, -3, 4, -1, 2, 1,-5, 4]
#nums = [-1, -2]
nums = [0]

n = len(nums)
max_val = -999999
result = 0

for i in nums:
	if result < 0:
		result = i
	else:
		result += i
	if result > max_val:
		max_val = result

print(max_val)
