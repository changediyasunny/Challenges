#include<stdio.h>
#include<stdlib.h>
#include<string.h>


int main()
{
	char *temp, str[500];
	int app[100]={0};
	int count = 0, i=0;
	char c;
	
	scanf("%[^\n]s",str);
	
	temp = str;
	
	
	while(str[i] != '\0')
	{
		if(str[i] >= 'a' && str[i] <='z')
		{
			c = (str[i] - 32);
		}
		else if(str[i] >= 'A' && str[i] <='Z')
			c = str[i];
        else
        {
        	i++;
            continue;
		}
		
		if(c >= 'A' && c <= 'Z')
		{
			if(app[c - 'A'] == 0)
			{
				count++;
				app[c - 'A']=1;
			}
		}
		i++;
	}
	if(count == 26)
		printf("pangram");
	else
		printf("not pangram");

}
