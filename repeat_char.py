
from collections import defaultdict

def repeat_char(string):

	my_dict = defaultdict(lambda:0)
	
	counter = 0
	
	for i in string:
		
		if my_dict[i] == 1:
			
			return i
		else:
			my_dict[i] += 1

def main():
	print(repeat_char('geeksforgeeks'))
	
if __name__ == '__main__':
	main()
