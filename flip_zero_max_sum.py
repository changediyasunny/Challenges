

"""
Sliding window Problem...




"""

def flip(list1, n):

	wL =0
	wR = 0
	Lindex = 0
	window = 0
	
	zero_cnt = 0
	
	while wR < len(list1):
	
		# Widen window if zero-count is < given flips...
		if zero_cnt <= n:
			if list1[wR] == 0:
				zero_cnt = zero_cnt + 1
			
			wR = wR + 1
		
		# zero-cnt is more...
		if zero_cnt > n:
			
			if list1[wL] == 0:
				zero_cnt = zero_cnt - 1
			
			wL = wL + 1
		
		# Keep track of maximum window found yet...
		# ALways max is preserved under (wR - wL) condition...		
		if (wR-wL) > window:
			window = wR - wL
			Lindex = wL
	
	#......................
	for i in range(window):
		if list1[Lindex+i] == 0:
			print(Lindex+i)
			
			
def main():

	list1 = [1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1]
	n = 1
	
	flip(list1, n)

if __name__ == '__main__':
	main()
