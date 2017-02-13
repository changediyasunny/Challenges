"""
GOOGLE INTERVIEW:
=================================
A Product Array Puzzle
Given an array arr[] of n integers, construct a Product Array prod[] (of same size) such that prod[i] is equal to the product of all the elements of arr[] except arr[i]. Solve it without division operator and in O(n).

Example:
arr[] = {10, 3, 5, 6, 2}
prod[] = {180, 600, 360, 300, 900}

Logic:
Algorithm:
1) Get a temporary array left[] such that left[i] contains product of all elements on left of arr[i] excluding arr[i].
2) Get another temporary array right[] such that right[i] contains product of all elements on on right of arr[i] excluding arr[i].
3) To get prod[], multiply left[] and right[].

Time Complexity: O(n)
Space Complexity: O(n)
Auxiliary Space: O(1)



"""
import sys


def product_array(array):
	
	prod = []
	n = len(array)
	# temp: will have left multiplication result. 
	# Eventually it replaces number with left multiplication.
	temp = 1
	for i in range(n):
		prod.append(temp)
		temp = temp * array[i]

	# Get right Multiplicaiton...
	temp = 1
	i = n - 1
	while(i >= 0):
		prod[i] = prod[i] * temp
		temp = temp * array[i]
		i = i - 1
	return prod

def main():
	array = [10, 3, 5, 6, 2]
	print("Product Array: %s" %product_array(array))
	pass



if __name__ == '__main__':
	main()