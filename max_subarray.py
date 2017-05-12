"""
Count Strictly Increasing Subarrays

Given an array of integers, count number of subarrays (of size more than one) that are strictly increasing.
Expected Time Complexity : O(n)
Expected Extra Space: O(1)

Examples:

Input: arr[] = {1, 4, 3}
Output: 1
There is only one subarray {1, 4}

Input: arr[] = {1, 2, 3, 4}
Output: 6
There are 6 subarrays {1, 2}, {1, 2, 3}, {1, 2, 3, 4}
                      {2, 3}, {2, 3, 4} and {3, 4}

Input: arr[] = {1, 2, 2, 4}
Output: 2
There are 2 subarrays {1, 2} and {2, 4}
"""


"""
def max_subarray(array):
	
	count = 0
	
	#This is O(m) solution as m = no. of subarrays...
	
	for i in range(len(array)):
		for j in range(i+1, len(array)):
			if array[j] > array[j-1]: 
				#check for immediate one, if not true, 
				#then whole array seq is not in increasing order...
				count = count + 1
			else:
				break
	
	return count
"""


#1. In general, for an array/string of size n, there are n*(n+1)/2 non-empty subarrays/subsrings
"""
2. for subarray of length > 1, ad increasing subarray, there are len * (len-1)/2 numbre of subarrays
3. we use 2nd method for this purpose
it takes O(n) time...
"""

def max_subarray(array):

	count = 0
	lent = 1
        print("helloooo...")	
	array.sort()
	
	for i in range(len(array) - 1):
	
		if array[i+1] > array[i]:
			lent = lent + 1
		
		else:
			count = count + (lent * (lent-1)/2)
			lent = 1
	
	if lent > 1:
		count = count + (lent * (lent-1)/2)
	
	return count

def main():
	arr = ['10','20','60','40']#,'5']
	print max_subarray(arr)
	
if __name__ == '__main__':
    main()
    
    
    
