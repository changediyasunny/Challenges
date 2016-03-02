#include<stdio.h>
#include<stdlib.h>
#include<string.h>

char *repeat(char *temp) 
{
	int i;
	char counter[26];
	char *str = (char *)malloc(sizeof(char) );
	
	for(i=0; i<strlen(temp); i++)
	{
		
		if(counter[temp[i]] == 1) 
		{
			*str = temp[i];
			return str;
		}
		else
		{
			counter[temp[i]] = 1;
		}
	}
	return NULL;
}

int main() 
{
	char *str = repeat("sunny");
	    
    printf("\n %s", str);
    printf("\n");
    return 0;
}


