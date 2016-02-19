/*

to count the number of unordered anagrams...

*/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>


int check_anagram(char a[], char b[])
{
   int first[26] = {0}, second[26] = {0}, c = 0;

   while (a[c] != '\0') {
      first[a[c]-'a']++;
      c++;
   }
   c = 0;
   while (b[c] != '\0') {
      second[b[c]-'a']++;
      c++;
   }

   for (c = 0; c < 26; c++) {
      if (first[c] != second[c])
         return 0;
   }

   return 1;
}

int main() 
{
    int t, i, j;
    scanf("%d", &t);
    while (t--)
    {
        char s[100];
        char sub1[100] = {0};
        char sub2[100] = {0};
        scanf("%s", s);

        int len, count = 0;
        for (len = 1; len < strlen(s); len++)
        {
            memset(sub1, 0, len);
            for (i = 0; i < strlen(s) - len; i++) 
            {
                strncpy(sub1, &s[i], len);
                memset(sub2, 0, len);
                for (j = i + 1; j < strlen(s) - len + 1; j++) 
                {
                    strncpy(sub2, &s[j], len);
                    if (check_anagram(sub1, sub2) == 1) 
                    {
                        count++;
                    }  
                }
            }     
        }
        printf("%d\n", count);
	}

return 0;
}
