#include<stdio.h>
#include<stdio.h>
#include<string.h>


int partition(int arr[], int low, int high, int pivot)
{
        int j, i = low;

        int temp1, temp2;
        
        for (j = low; j < high; j++)
        {
            if (arr[j] < pivot)
            {
                temp1 = arr[i];
                arr[i] = arr[j];
                arr[j] = temp1;
                i++;
            } 
            else if(arr[j] == pivot)
            {
                temp1 = arr[j];
                arr[j] = arr[high];
                arr[high] = temp1;
                j--;
            }
        }
        temp2 = arr[i];
        arr[i] = arr[high];
        arr[high] = temp2;
 
        // Return the partition index of an array based on the pivot 
        // element of other array.
        return i;
}

void matchPairs(int nuts[], int bolts[], int low, int high)
{
        if (low < high)
        {
            // Choose last intacter of bolts array for nuts partition.
            int pivot = partition(nuts, low, high, bolts[high]);
 
            // Now using the partition of nuts choose that for bolts
            // partition.
            partition(bolts, low, high, nuts[pivot]);
 
            // Recur for [low...pivot-1] & [pivot+1...high] for nuts and
            // bolts array.
            matchPairs(nuts, bolts, low, pivot-1);
            matchPairs(nuts, bolts, pivot+1, high);
        }
        
}


int main()
{
        // Nuts and bolts are represented as array of intacters
        int nuts[] = {2,3,1,4,5,6};
        int bolts[] = {5,6,3,1,2,4};
 
        matchPairs(nuts, bolts, 0, 5);
		
		int i;
        for(i=0; i<6; i++)
        {
        	printf("%d", nuts[i]);
        
        }
        printf("\n");
        for(i=0; i<6; i++)
        {
        	printf("%d", bolts[i]);
        
        }
		
		return 0;
}


