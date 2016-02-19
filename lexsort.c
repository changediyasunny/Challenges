/*

Following are the steps to print the permutations lexicographic-ally

1. Sort the given string in non-decreasing order and print it. The first permutation is always the string sorted in non-decreasing order.

2. Start generating next higher permutation. Do it until next higher permutation is not possible. If we reach a permutation where all characters are sorted in non-increasing order, then that permutation is the last permutation.

Steps to generate the next higher permutation:
1. Take the previously printed permutation and find the rightmost character in it, which is smaller than its next character. Let us call this character as ‘first character’.

2. Now find the ceiling of the ‘first character’. Ceiling is the smallest character on right of ‘first character’, which is greater than ‘first character’. Let us call the ceil character as ‘second character’.

3. Swap the two characters found in above 2 steps.

4. Sort the substring (in non-decreasing order) after the original index of ‘first character’.

Let us consider the string “ABCDEF”. Let previously printed permutation be “DCFEBA”. The next permutation in sorted order should be “DEABCF”. Let us understand above steps to find next permutation. The ‘first character’ will be ‘C’. The ‘second character’ will be ‘E’. After swapping these two, we get “DEFCBA”. The final step is to sort the substring after the character original index of ‘first character’. Finally, we get “DEABCF”.


*/


#include<stdio.h>
#include<string.h>
#include<stdlib.h>



void mergesort(char arr[], int low, int mid, int right)
{
    int i, j, k;
    int n1 = mid - low + 1;
    int n2 =  right - mid;
 
    char L[n1], R[n2];
 
    for (i = 0; i < n1; i++)
        L[i] = arr[low + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[mid + 1+ j];
 
    i = 0;
    j = 0;
    k = low;
    while (i < n1 && j < n2)
    {
        if (L[i] <= R[j])
        {
            arr[k] = L[i];
            i++;
        }
        else
        {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
 
    while (i < n1)
    {
        arr[k] = L[i];
        i++;
        k++;
    }
 
    while (j < n2)
    {
        arr[k] = R[j];
        j++;
        k++;
    }
}


void partition(char arr[], int l, int r)
{
   if (l < r)
   {
      int m = l+(r-l)/2; //Same as (l+r)/2 but avoids overflow for large l & h
      
      partition(arr, l, m);
      partition(arr, m+1, r);
      
      mergesort(arr, l, m, r);
      
   }
}
 

void lexsort(char str[])
{
	int len = strlen(str);
	
	partition(str, 0, len-1);
	
	printf("\n Sorted string is=%s\n", str);	

}

int findceil(char str[], char frstchr, int lo, int h)
{
	int ceilind = lo;
	int i;
	
	for(i=lo+1; i<=h; i++)
	{
		if (str[i] > frstchr && str[i] < str[ceilind])
            ceilind = i;
	}
	
	return ceilind;

}

void swap(char *a, char *b)
{
	char t = *a;
	*a = *b;
	*b = t;
}

void reverse(char str[], int l, int h)
{
   while (l < h)
   {
       swap(&str[l], &str[h]);
       l++;
       h--;
   }
}
void sortpermute(char str[])
{
	int size = strlen(str);
	int i, j, k;
	
	lexsort(str);
	
	int finished = 0;
	
	while(!finished)
	{
		printf("\n Permutations: %s \n", str);
		
		//step1: find rightmost char less than <  next cahracter...
		for(i= (size-2); i>=0; i--)
		{
			if(str[i] < str[i+1])
			{
				char firstchar = str[i];
				break;
			}
		}//found 1st character at ith location of str[i];
		
		if(i == -1)
		{
			finished = 1;
		}
		else
		{
			int ceiling;
			
			ceiling = findceil(str, str[i], i + 1, size - 1);
			
			char secondchar = str[ceiling]; //found 2nd cahracter... index of 1st char...
			
			//Swap the two positions....
			swap(&str[i], &str[ceiling]);
			
			//Now reverse the subarray after firstchar, to get permutation...
			
			reverse(str, i+1, size-1);			
		}		
	}			
}

int main()
{
	
	char str[]="eggegg";
	
	sortpermute(str);
	printf("\n");
	return 0;
	
}

