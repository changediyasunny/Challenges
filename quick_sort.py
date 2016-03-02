
"""
	Simple quick sort...
	
	
	Time taken by QuickSort in general can be written as following.

	T(n) = T(k) + T(n-k-1) + O(n)

	The first two terms are for two recursive calls, the last term is for the partition process. k is the
	number of elements which are smaller than pivot.
	The time taken by QuickSort depends upon the input array and partition strategy. Following are three cases.

	Worst Case: The worst case occurs when the partition process always picks greatest or smallest element as 
	pivot. If we consider above partition strategy where last element is always picked as pivot, the worst case 
	would occur when the array is already sorted in increasing or decreasing order. 
	
	Following is recurrence for worst case.

		T(n) = T(0) + T(n-1) + O(n)
		which is equivalent to  
 		T(n) = T(n-1) + O(n)

	The solution of above recurrence is O(n2).

	Best Case: The best case occurs when the partition process always picks the middle element as pivot. 
	Following is recurrence for best case.

	T(n) = 2T(n/2) + O(n)	
"""

def quickSort(alist):
	quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):

	if first<last:
	
		pivot = partition(alist, first, last)
		quickSortHelper(alist, first, pivot-1)
		quickSortHelper(alist, pivot+1, last)


def partition(alist,first,last):
	
	# alist = [1,26,93,17,77,31,44,55,20]
	
	pivotvalue = alist[first]
	leftmark = first+1
	rightmark = last
	
	done = False
	
	while not done:
		while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
			leftmark = leftmark + 1
		
		while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
			rightmark = rightmark -1
		
		if rightmark < leftmark:
			done = True
		else:
			temp = alist[leftmark]
			alist[leftmark] = alist[rightmark]
			alist[rightmark] = temp
	
	temp = alist[first]
	alist[first] = alist[rightmark]
	alist[rightmark] = temp
	
	return rightmark
	
	
def main():

	alist = [1,26,93,17,77,31,44,55,20]
	quickSort(alist)
	print(alist)

if __name__ == '__main__':
	main()
