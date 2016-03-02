/*

Given a pattern containing only I’s and D’s. I for increasing and D for decreasing. Devise an algorithm to print the minimum number following that pattern. Digits from 1-9 and digits can’t repeat.

Examples:

   Input: D        Output: 21
   Input: I        Output: 12
   Input: DD       Output: 321
   Input: II       Output: 123
   Input: DIDI     Output: 21435
   Input: IIDDD    Output: 126543
   Input: DDIDDIID Output: 321654798 



*/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>


void PrintMinNumberForPattern(char arr[10])
{
    // Initialize current_max (to make sure that
    // we don't use repeated character
    int i, j, curr_max = 0;
    int last_entry = 0;
 
 	int size = strlen(arr);
 	
    // Iterate over input array
    for (i=0; i<size; i++)
    {
        // Initialize 'noOfNextD' to get count of
        // next D's available
        int noOfNextD = 0;
 
        switch(arr[i])
        {
        case 'I':
            // If letter is 'I'
 
            // Calculate number of next consecutive D's
            // available
            j = i+1;
            while (arr[j] == 'D' && j < size)
            {
                noOfNextD++;
                j++;
            }
               
            if (i==0)
            {
                curr_max = noOfNextD + 2;
 
                // If 'I' is first letter, print incremented
                // sequence from 1
                printf("%d", ++last_entry);
                printf("%d", curr_max);
 
                // Set max digit reached
                last_entry = curr_max;
            }
            else
            {
                // If not first letter
 
                // Get next digit to print
                curr_max = curr_max + noOfNextD + 1;
 
                // Print digit for I
                last_entry = curr_max;
                printf("%d", last_entry);
            }
 			int k;
            // For all next consecutive 'D' print 
            // decremented sequence
            for (k=0; k<noOfNextD; k++)
            {
                printf("%d", --last_entry);
                i++;
            }
            break;
 
        // If letter is 'D'
        case 'D':
            if (i == 0)
            {
                // If 'D' is first letter in sequence
                // Find number of Next D's available
                j = i+1;
                while (arr[j] == 'D' && j < size)
                {
                    noOfNextD++;
                    j++;
                }
 
                // Calculate first digit to print based on 
                // number of consecutive D's
                curr_max = noOfNextD + 2;
 
                // Print twice for the first time
                printf("%d %d", curr_max, curr_max-1);
 
                // Store last entry
                last_entry = curr_max - 1;
            }
            else
            {
                // If current 'D' is not first letter
 
                // Decrement last_entry
                printf("%d",last_entry - 1);
                last_entry--;
            }
            break;
        }
    }
    printf("\n");
}
 
// Driver program to test above
int main()
{
    PrintMinNumberForPattern("IIII");
    return 0;
}
