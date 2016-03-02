"""
Nuts & Bolts Problem (Lock & Key problem)

Given a set of n nuts of different sizes and n bolts of different sizes. There is a one-one mapping 
between nuts and bolts. Match nuts and bolts efficiently.
Constraint: Comparison of a nut to another nut or a bolt to another bolt is not allowed. It means nut 
can only be compared with bolt and bolt can only be compared with nut to see which one is bigger/smaller.

Other way of asking this problem is, given a box with locks and keys where one lock can be opened by one 
key in the box. We need to match the pair.
"""

#	Constraint: Comparison of a nut to another nut or a bolt to another bolt is not allowed. It means nut can only 
#	be compared with bolt and #bolt can only be compared with nut to see which one is bigger/smaller.
#	Other way of asking this problem is, given a box with locks and keys where one lock can be opened by one key
#	in the box. We need to match the pair.


def partition(array, left, right, pivot):

	i = left
	j = 0
	
	while j < (right+1):
		
		if array[j] < pivot:
			temp1 = array[i]
			array[i] = array[j]
			array[j] = temp1
			i = i + 1
		elif array[j] == pivot:
			temp1 = array[j]
			array[j] = array[right]
			array[right] = temp1
			j = j - 1
			
		j += 1
		
	temp2 = array[i]
	array[i] = array[right]
	array[right] = temp2
	
	return i


def nuts_bolts(nuts, bolts, low, high):

	if low < high:
	
		nuts_index = partition(nuts, low, high, bolts[high])
		
		bolt_index= partition(bolts, low, high, nuts[nuts_index])
		
		
		nuts_bolts(nuts, bolts, low, nuts_index - 1)
		nuts_bolts(nuts, bolts, nuts_index+1, high)


def main():

	nuts = [2,3,1,5,4]
	bolts = [1,4,5,3,2]
	
	nuts_bolts(nuts, bolts, 0, len(bolts)-1)
	print(nuts)
	print(bolts)
	
if __name__ == '__main__':
	main()
