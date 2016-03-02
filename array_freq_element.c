/*
	
Count frequencies of all elements in array in O(1) extra space and O(n) time

Given an unsorted array of     """ n integers which can contain integers from 1 to n""".

Some elements can be repeated multiple times and some other elements can be absent from the array. Count frequency of all
elements that are present and print the missing elements.

Examples:

Input: arr[] = {2, 3, 3, 2, 5}
Output: Below are frequencies of all elements
        1 -> 0
        2 -> 2
        3 -> 2
        4 -> 0
        5 -> 1

Input: arr[] = {4, 4, 4, 4}
Output: Below are frequencies of all elements
        1 -> 0
        2 -> 0
        3 -> 0
        4 -> 4

*/



#include<stdio.h>
#include<string.h>
#include<stdlib.h> 

/*
	METHOD 1

*/

// Function to find counts of all elements present in
// arr[0..n-1]. The array elements must be range from
// 1 to n
void findCounts(int *arr, int n)
{
    // Traverse all array elements
    int i = 0;
    while (i<n)
    {
        // If this element is already processed,
        // then nothing to do
        if (arr[i] <= 0)
        {
            i++;
            continue;
        }
 
        // Find index corresponding to this element
        // For example, index for 5 is 4
        int elementIndex = arr[i]-1;
 
        // If the elementIndex has an element that is not
        // processed yet, then first store that element
        // to arr[i] so that we don't loose anything.
        if (arr[elementIndex] > 0)
        {
            arr[i] = arr[elementIndex];
 
            // After storing arr[elementIndex], change it
            // to store initial count of 'arr[i]'
            arr[elementIndex] = -1;
        }
        else
        {
            // If this is NOT first occurrence of arr[i],
            // then increment its count.
            arr[elementIndex]--;
 
            // And initialize arr[i] as 0 means the element
            // 'i+1' is not seen so far
            arr[i] = 0;
            i++;
        }
    }
 
    printf("\nBelow are counts of all elements\n");
    for (int i=0; i<n; i++)
        printf("%d -> %d\n", i+1, abs(arr[i]));
}


/*

	METHOD 2

*/


// Function to find counts of all elements present in
// arr[0..n-1]. The array elements must be range from
// 1 to n
void printfrequency(int arr[],int n)
{
	int i, j;
    // Subtract 1 from every element so that the elements
    // become in range from 0 to n-1
    for (j =0; j<n; j++)
        arr[j] = arr[j]-1;
 
    // Use every element arr[i] as index and add 'n' to
    // element present at arr[i]%n to keep track of count of
    // occurrences of arr[i]
    for (i=0; i<n; i++)
        arr[arr[i]%n] = arr[arr[i]%n] + n;
 
    // To print counts, simply print the number of times n
    // was added at index corresponding to every element
    for (i =0; i<n; i++)
        printf("\n %d->%d", i + 1, arr[i]/n);
}
 
// Driver program to test above function
int main()
{
    int arr[] = {2, 3, 3, 2, 8};
    int n = sizeof(arr)/sizeof(arr[0]);
    
    printfrequency(arr,n);
    return 0;
}
