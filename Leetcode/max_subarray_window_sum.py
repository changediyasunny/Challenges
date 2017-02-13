"""
Given an array of integer & window size K, Find the sum of elements from that window.

Input = [4, 2, 73, 11, -5]
Output >> [6, 75, 84, 6]

"""

import sys

def max_sum_subarray(temp_list, k):

	n = len(temp_list)
	print("list length is: %s" %len(temp_list))
	i = 0
	if not temp_list:
		return temp_list

	result_sum = 0
	final_list = []
	for i in range(k):
		result_sum += temp_list[i]

	print("very first sum is: %s" %result_sum)
	final_list.append(result_sum)

	print("Final list is: %s" %final_list)
	lengths = n - k + 1
	print("length remained is: %s" %lengths)
	for i in range(1, lengths):
		# new-sum = (last total sum) - (first number from last window) + (last number from new window)
		temp_sum = final_list[i-1] - temp_list[i-1] + temp_list[i+k-1]
		final_list.append(temp_sum)
	return final_list

def main():
	#list1 = [4, 2, 73, 11, -5]
	list1 = [1,2,3,4,2,3,4,5,2,3,4]
	k = 3
	result = max_sum_subarray(list1, k)
	print(result)

if __name__ == '__main__':
	main()