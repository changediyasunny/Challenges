#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>


/*  ARRAY SUM==========================
int main()
{
    int n; 
    scanf("%d",&n);
    
    int arr[n], arr_i, total = 0;
    
    
    for(arr_i = 0; arr_i < n; arr_i++)
    {
       scanf("%d",&arr[arr_i]);
       total = total + arr[arr_i];
    }
    
    printf("\n Totla=%d", total);
    
    return 0;
}
================================================= */

/* TIme format....
*/
int main()
{
    char *time = (char *)malloc(1024 * sizeof(char));
    scanf("%s",time);
	
	int hour, minut, sec;
	char *token, zone[3]={0}, tmp[5]={0}, temp[10];
	char time1[20], amtime[20]={0};
	
	strcpy(amtime, time);
	
	token = strtok(time,":");
	hour = atoi(token);
	
	token = strtok(NULL,":");	
	minut = atoi(token);
	
	token = strtok(NULL,"M");
	
	//bzero(temp,10);
	strcpy(temp, token);
	strcat(temp, "\0");
	
	//bzero(tmp,5);
	//bzero(zone,3);
	
	int i=0;
	while(temp[i] != '\0')
	{
		if(temp[i] >= 48 && temp[i] <= 57 )
		{
			strncat(tmp,&temp[i],1);
		}
		else
		{
			strncat(zone,&temp[i],1);
		}
		i++;
	}	
	
	sec = atoi(tmp);
	
	char tmp1[5], tmp2[5];
	
	if(strcmp(zone, "P") == 0 || strcmp(zone, "p") == 0)
	{
		if(hour <= 12 )
		{
			
			//bzero(time1,20);
			
			hour = hour + 12;
			sprintf(time1,"%d", hour);
			
			strcat(time1,":0");
		}
		
		sprintf(tmp1,"%d", minut);
		
		sprintf(tmp2, "%d", sec);
			
		strcat(time1,tmp1);
		strcat(time1,":");
		strcat(time1,tmp2);		
	}
	else if(strcmp(zone, "A") == 0)
	{
		
		//token = strtok(amtime, "A");
		
		if(hour == 12 )
		{
			
			//bzero(time1,20);
			
			strcat(time1, "00:");

			sprintf(tmp1,"%d", minut);
			
			sprintf(tmp2, "%d", sec);
			
			strcat(time1,tmp1);
			strcat(time1,":");
			strcat(time1,tmp2);
									
		}		
		
	}
		
	printf("%s", time1);
	
    return 0;
}

