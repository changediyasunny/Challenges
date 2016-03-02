


#    list1 = {1, 5, 9, 10, 15, 20};
#    list2 = {2, 3, 8, 13};



def msort(list1, list2):

	for j  in range(len(list2)-1, -1, -1):
		
		last = list1[ len(list1)-1]
		for i in range(len(list1)-1, -1, -1):
			
			if list1[i] > list2[j]:
				try:
					list1[i+1] = list1[i]
				except IndexError:
					list1.append(list1[i])
			#else:
			#	list1[i+1] = list2[j]
			#	list2[j] = last
		
		if i != len(list1)-1:
			list1[i+1] = list2[j]
			list2[j] = last
	
	print(list1)
	print(list2)


def main():
	msort([1, 5, 9, 10, 15, 20], [2,3,8,13])
	
if __name__ == '__main__':
    main()
