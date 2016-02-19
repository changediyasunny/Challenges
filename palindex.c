/*
You are given a string of lower case letters. Your task is to figure out the index of the character 
on whose removal it will make the string a palindrome. There will always be a valid solution.
In case the string is already a palindrome, then -1 is also a valid answer along with possible indices.

*/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main()
{

int t;
scanf("%d", &t);
while (t--) {
    char s[100005];
    scanf("%s", s);
    int l = 0;
    int r = strlen(s) - 1;

    while (l < r) {
        if (s[l] == s[r]) {
            l++;
            r--;
        }
        else {
            break;
        }
    }

    if (l >= r) {
        printf("-1\n");
        continue;
    }

    int saveLeft = l;
    int saveRight = r;

    l++;
    int leftFault = 1;
    while (l < r) {
        if (s[l] == s[r]) {
            l++;
            r--;
        }
        else {
            leftFault = 0;
            break;
        }
    }

    printf("%d\n", leftFault ? saveLeft : saveRight);

	}
	return 0;
}
