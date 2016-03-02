
"""

Length of the longest valid substring

Given a string consisting of opening and closing parenthesis, find length of the longest valid parenthesis substring.

Examples:

Input : ((()
Output : 2
Explanation : ()

"""


def valid_bracket(string):
	
	stack = []
	
	stack.append(-1)
	result = 0
	
	for i in range(len(string)):
		
		if string[i] == '(':
			stack.append(i)
		else:
			
			stack.pop()
			
			if len(stack) != 0:
				result = max(result , i - stack[ len(stack) - 1 ])
			else:
				stack.append(i)

	return result

def main():
	
	print(valid_bracket('((()()'))


if __name__ == '__main__':
	main()
