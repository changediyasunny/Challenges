// C++ program to find minimum number of
// operations required to transform one string to other
#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int minOps(char A[], char B[])
{
    int m = strlen(A), n = strlen(B);
 	int i, j;
     // This parts checks whether conversion is
     // possible or not
    if (n != m)
       return -1;
       
    int count[256];
    
    memset(count, 0, sizeof(count));
    
    for (i=0; i<n; i++)   // count characters in A
       count[ tolower(B[i]) ]++;
    for (i=0; i<n; i++)   // subtract count for
       count[ tolower(A[i]) ]--;         // every character in B
    for (i=0; i<26; i++)   // Check if all counts become 0
      if (count[i])
         return -1;
 
    // This part calculates the number of operations required
    int res = 0;
    for (i=n-1, j=n-1; i>=0; )
    {
        // If there is a mismatch, then keep incrementing
        // result 'res' until B[j] is not found in A[0..i]
        while (i>=0 && A[i] != B[j])
        {
            i--;
            res++;
        }
 
        // If A[i] and B[j] match
        if (i >= 0)
        {
            i--;
            j--;
        }
    }
    return res;
}
 
// Driver program
int main()
{
    char A[10] = "EPAGFD";
    char B[10] = "PEFGAD";
    printf("Minimum number of operations required is %d", minOps(A, B) );
    return 0;
}
