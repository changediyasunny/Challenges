
/*

finding whether anagram of a string can be a pallindrome...

Logic: there should be only/ atmost 1 letter with odd count present...

*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    char *a;
    static int arr[26];
    int i=0,count=0;
    a=(char *)calloc(1,10001*100);
    scanf("%s",a);
    while(a[i])
    {
        arr[a[i]-'a']=(arr[a[i]-'a']+1)%2;
        i++;
    }
    i=0;
    while(i<26)
    {
        if(arr[i]==1)
             count++;
        
        i++;
    }
    if(count >1)
    {
        printf("NO");
    }
    else
    {
        printf("YES");
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}

