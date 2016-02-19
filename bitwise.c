#include<stdio.h>


int main()
{
    unsigned char a = 4, b = 9; // 
    
    
    //	a = 4(00000100), 
    //	b = 9(00001001)
    // left Shift: multiplication, Right Shift: division, 
    
    
    printf("a = %d, b = %d\n", a, b);
    printf("a&b = %d\n", a&b); // The result is 00000001
    printf("a|b = %d\n", a|b);  // The result is 00001101
    printf("a^b = %d\n", a^b); // The result is 00001100
    printf("~a = %d\n", a = ~a);   // The result is 11111010
    printf("b<<1 = %d\n", b<<1);  // The result is 000100100 
    printf("b>>1 = %d\n", b>>1);  // The result is 00000100 
    return 0;
}


/*
 getMissingNo takes array and size of array as arguments
METHOD 1:
1. Get the sum of numbers 
       total = n*(n+1)/2
2  Subtract all the numbers from sum and
   you will get the missing number.

METHOD 2(Use XOR):

  1) XOR all the array elements, let the result of XOR be X1.
  2) XOR all numbers from 1 to n, let XOR be X2.
  3) XOR of X1 and X2 gives the missing number.


#include<stdio.h>
 

int getMissingNo(int a[], int n)
{
    int i;
    int x1 = a[0]; /* For xor of all the elemets in arary 
    int x2 = 1; /* For xor of all the elemets from 1 to n+1 
     
    for (i = 1; i< n; i++)
        x1 = x1^a[i];
            
    for ( i = 2; i <= n+1; i++)
        x2 = x2^i;         
    
    return (x1^x2);
}
 
/*program to test above function 
int main()
{
    int a[] = {1, 2, 4, 5, 6};
    int miss = getMissingNo(a, 5);
    printf("%d", miss);
    getchar();
}


*/

/*
GCD(a,b) of two numbers....

int gcd(int a, int b)
{
    // Base cases
    if (b == 0 || a == b) return a;
    if (a == 0) return b;
 
    // If both a and b are even, divide both a
    // and b by 2.  And multiply the result with 2
    if ( (a & 1) == 0 && (b & 1) == 0 )
       return gcd(a>>1, b>>1) << 1;
 
    // If a is even and b is odd, divide a bb 2
    if ( (a & 1) == 0 && (b & 1) != 0 )
       return gcd(a>>1, b);
 
    // If a is odd and b is even, divide b bb 2
    if ( (a & 1) != 0 && (b & 1) == 0 )
       return gcd(a, b>>1);
 
    // If both are odd, then apply normal subtraction 
    // algorithm.  Note that odd-odd case always 
    // converts odd-even case after one recursion
    return (a > b)? gcd(a-b, b): gcd(a, b-a);
}

*/

/*
int findOdd(int arr[], int n) {
   int res = 0, i;
   for (i = 0; i < n; i++)
   {
     res ^= arr[i];
     printf("\n %d", res);
   }
   return res;
}
 
int main(void) {
   int arr[] = {12, 12, 14, 90, 14, 14, 14};
   int n = sizeof(arr)/sizeof(arr[0]);
   printf ("The odd occurring element is %d \n", findOdd(arr, n));
   return 0;
}*/



/*

ROTATE CIRCULAR BITS ............


#include<stdio.h>
#define INT_BITS 32
 
int leftRotate(int n, unsigned int d)
{
   /* In n<<d, last d bits are 0. To put first 3 bits of n at 
     last, do bitwise or of n<<d with n >>(INT_BITS - d) 
   return (n << d)|(n >> (INT_BITS - d));
}
 
int rightRotate(int n, unsigned int d)
{
   /* In n>>d, first d bits are 0. To put last 3 bits of at 
     first, do bitwise or of n>>d with n <<(INT_BITS - d) 
   return (n >> d)|(n << (INT_BITS - d));
}
 
int main()
{
  int n = 16;
  int d = 2;
  printf("Left Rotation of %d by %d is ", n, d);
  printf("%d", leftRotate(n, d));
  printf("\nRight Rotation of %d by %d is ", n, d);
  printf("%d", rightRotate(n, d));
  getchar();
} 
*/
