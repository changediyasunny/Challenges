/*
find how many chars to be deleted to make 2 strings anagram of each other

*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>


int main()
{
	int i=0, count=0;
	char str1[10000], str2[10000];
	int temp1[26]={0};
	int temp2[26]={0};
	
	scanf("%s", str1);
	scanf("%s", str2);
	
	while(i < strlen(str1))
	{
		temp1[ str1[i] - 'a']++;
		i++;
	}
	i=0;
	while(i < strlen(str2))
	{
		temp2[ str2[i] - 'a']++;
		i++;
	}
	i=0;
	while(i < 26)
	{
		count = count + abs(temp1[i]-temp2[i]);
		i++;
	}	
	printf("%d", count);		
}
