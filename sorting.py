
from collections import defaultdict


def swap(x, y):
	
	temp = x
	x = y
	y = temp


def binary_search(array, left, right, num):
	
	# Binary search works only on sorted array...
	array.sort()
	
	if left <= right:
		
		mid = (left + right)//2
		
		if array[mid] == num:
			print("Binary Search:", mid) 
			
		elif num < array[mid]:
			binary_search(array, left, mid-1, num)
			
		elif num > array[mid]:
			binary_search(array, mid+1, right, num)
			
	else:
		print("Binary search: not found")
	
	"""
		Binary Search: T(n) = T(n/2) + C
		and running time is O(log n)
	
	"""
	

def selection_sort(array):
	
	for i in range(0, len(array)-1):
		min_idx = i
		
		for j in range(i+1, len(array)-1):
			
			if array[j] < array[min_idx]:
				min_idx = j
				temp = array[min_idx]
				array[min_idx] = array[i]
				array[i] = temp
	
	print(array)
	"""
		Selection Sort: Runnign time is O(n * n)
	"""

def bubble_sort(array):

	n = len(array)
	
	for i in range(n):
		
		for j in range(0, n-i-1):
			
			"""
				This (n-i-1) is used because larger element is going to be last element in a single pass
				Each pass transfers largest element to last of array...
				
				Check Wiki for more animation 
			"""
			
			if array[j] > array[j+1]:
				temp = array[j]
				array[j] = array[j+1]
				array[j+1] = temp
				
	# It does not know even is array is sorted, always makes extra pass
	# Use Flag to denote whether swap is made or not ? if not then terminate loop
	
	print(array)
	
	"""
		The Above Prog takes O(n ^ 2) time to run...

		Worst and Average Case Time Complexity: O(n*n). Worst case occurs when array is reverse sorted.
		Best Case Time Complexity: O(n). Best case occurs when array is already sorted.
	"""


def insertion_sort(array):
	
	for i in range(1, len(array)):
		
		key = array[i]
		j = i-1
		
		while j >= 0 and array[j] > key:
			array[j+1] = array[j]
			j = j-1
		
		array[j+1] = key
	
	print(array)
	
	"""
		 Insertion sort takes maximum time to sort if elements are sorted in reverse order. 
		 And it takes minimum time (Order of n) when elements are already sorted.
		 
		 Running Time = O(n*n)
	
	"""

	
def merge_sort(array):
	
	result = []
	
	
	if len(array) <= 1:
		return array
	
	mid = len(array)//2
	left = merge_sort(array[:mid])
	right = merge_sort(array[mid:])
	
	
	i = 0
	j = 0
	
	#print(left, right)
	
	try:
		while i < len(left) and j < len(right):
	
			if left[i] > right[j]:
				result.append(right[j])
				j += 1
			else:
				result.append(left[i])
				i += 1
	
		result = result + left[i:]
		result = result + right[j:]
		
	except TypeError:
		pass
	
	print(result)


def max_heapify(array, root, heap_size):
	
	largest = root
	
	# left Child
	left = 2*root + 1
	
	# Right Child
	right = 2*root + 2 
	
	if left < heap_size and array[left] > array[largest]:
		largest = left
	
	if right < heap_size and array[right] > array[largest]:
		largest = right
	
	if largest != root:
		
		temp = array[root]
		array[root] = array[largest]
		array[largest] = temp
		max_heapify(array, largest, heap_size)


def build_max_heap(array, heap_size):
	
	rightmost = (heap_size - 2)//2
	
	for i in range( rightmost, -1, -1):
		max_heapify(array, i, heap_size)


def heap_sort(array, heap_size):
	
	build_max_heap(array, heap_size)
	
	while heap_size > 1:
		
		temp = array[heap_size - 1]
		array[heap_size - 1] = array[0]
		array[0] = temp
		
		heap_size -= 1
		
		max_heapify(array, 0, heap_size)
		
	print(array)
	
	"""
		Time Complexity: Time complexity of heapify is O(Logn). Time complexity of createAndBuildHeap() is O(n)
		and overall time complexity of Heap Sort is O(nLogn).
	
	"""
	
		
# MAIN FUNCTION....

def main():
	
	array = [9,7,3,2,1,5,6,8,4]
	#array = [12, 11, 13, 5, 6, 7]
	num = 7
	
	
	# Binary Search
	#binary_search(array, 0, len(array)-1, num)
	
	# Selection Sort
	#selection_sort(array)
	
	# Bubble Sort
	#bubble_sort(array)
	
	
	# Insertion Sort
	#insertion_sort(array)
	
	# Merge Sort
	#merge_sort(array)
	
	# Binary Heap Sort
	heap_sort(array, len(array))
	
	
	
	
	
if __name__ == '__main__':
	main()
