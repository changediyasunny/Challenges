#include<stdio.h>

#include<string.h>

#define R 3

#define C 3

char *my_strcat(char *str1, char *str2) 
{

	*str1++ = ' ' ;

	while (*str2 != '\0') 
	{

		*str1++ = *str2++;

	}
}

void printRecur(char *arr[R][C], char *output, int lenght, int r_count, int c_count) 
{

	char temp[40];

	int i;

	if (r_count == R) 
	{

		output[lenght] = '\0';

		printf("%s\n", output);

	}

	else 
	{

		for (i = 0; i < C; i++) 
		{

			if (arr[r_count][i] != NULL) 
			{

				my_strcat(&output[lenght], arr[r_count][i]);

				printRecur(arr, output, lenght+1+strlen(arr[r_count][i]), r_count+1, i);

			}

		}

	}

}

void print(char *arr[R][C]) 
{

	char output[40];

	int lenght = 0, r_count = 0, c_count = 0;

	printRecur(arr, output, lenght, r_count, c_count);

}

int main()
{
	int i, j;

	char *arr[3][3] = {{"you", "we"},{"have", "are"},{"sleep", "eat", "drink"}};

	print(arr);

	return 0;
}
