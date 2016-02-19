#include <stdio.h>
#include <string.h>
#include<stdlib.h>

#define true 1
 
// A utility function to print a substring str[low..high]
void printSubStr( char* str, int low, int high )
{
	int i;
	
    for( i = low; i <= high; ++i )
        printf("%c", str[i]);
}
 
// This function prints the longest palindrome substring
// of str[].
// It also returns the length of the longest palindrome
int longestPalSubstr( char *str )
{
    int n = strlen( str ); // get length of input string
 	int i, k;
 	
    // table[i][j] will be false if substring str[i..j]
    // is not palindrome.
    // Else table[i][j] will be true
    int table[n][n];
    memset(table, 0, sizeof(table));
 
    // All substrings of length 1 are palindromes
    int maxLength = 1;
    for (i = 0; i < n; ++i)
        table[i][i] = true;
 
    // check for sub-string of length 2.
    int start = 0;
    for (i = 0; i < n-1; ++i)
    {
        if (str[i] == str[i+1])
        {
            table[i][i+1] = true;
            start = i;
            maxLength = 2;
        }
    }
 
    // Check for lengths greater than 2. k is length
    // of substring
    for (k = 3; k <= n; ++k)
    {
        // Fix the starting index
        for (i = 0; i < n-k+1 ; ++i)
        {
            // Get the ending index of substring from
            // starting index i and length k
            int j = i + k - 1;
 
            // checking for sub-string from ith index to
            // jth index iff str[i+1] to str[j-1] is a
            // palindrome
            if (table[i+1][j-1] && str[i] == str[j])
            {
                table[i][j] = true;
 
                if (k > maxLength)
                {
                    start = i;
                    maxLength = k;
                }
            }
        }
    }
 
    printf("Longest palindrome substring is: ");
    printSubStr( str, start, start + maxLength - 1 );
 
    return maxLength; // return length of LPS
}

int main()
{
    char str[] = "fabcba";
    printf("\nLength is: %d\n", longestPalSubstr( str ) );
    return 0;
}





