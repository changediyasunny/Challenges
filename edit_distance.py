

def editDistDP(str1, str2, m, n):
	
	# Create a table to store results of subproblems
	dp = [[0 for x in range(n+1)] for x in range(m+1)]
 
	# Fill d[][] in bottom up manner
	for i in range(m+1):

		for j in range(n+1):
			
			# If first string is empty, only option is to
		  	# isnert all characters of second string
		  	""" This makes, 1st Row as: [0,1,2,3,4,5,6,7,8] """
			if i == 0:
				dp[i][j] = j
  			
  			
			# If second string is empty, only option is to
			# remove all characters of second string
			
			elif j == 0:
				dp[i][j] = i
				  
			# If last characters are same, ignore last char
			# and recur for remaining string
  			
			elif str1[i-1] == str2[j-1]:
				dp[i][j] = dp[i-1][j-1]
				
			# If last character are different, consider all
			# possibilities and find minimum
   
			else:
				dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
				  
	return dp[m][n]
	
	"""
		Time Complexity: O(m * n), Where m & n are lengths of both strings.
		Auxillary Space: O(m * n)
	
	"""
	
def main():

	str1 = "sunday"
	str2 = "saturday"
	print(editDistDP(str1, str2, len(str1), len(str2) ) )

if __name__ == '__main__':
	main()
