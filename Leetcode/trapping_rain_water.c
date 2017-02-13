#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int trap_rain_water(int* height, int n) 
{
    int level = 0, water = 0;
    while (n--) {
        int lower = *height < height[n] ? *height++ : height[n];
        if (lower > level)
        {
        	level = lower;	
        } 
        water += level - lower;
    }
    return water;
}



int main()
{	
	int height[] = {0,1,0,2,1,0,1,3,2,1,2,1};
	int n;
	n = sizeof(height) / sizeof(height[0]);
	printf("\n size of array is : %d", n);
	int water_amount;
	water_amount = trap_rain_water(height, n);
	printf("\n water amount received: %d", water_amount);

	printf("\n");
	return 0;
}