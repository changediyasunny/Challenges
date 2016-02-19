/*

Explanation:
=======================
A O(n) time and O(1) extra space solution:
The idea is similar to method 2 of this post. Let the two odd occurring numbers be x and y. We use bitwise XOR to get x and y. The first step is to do XOR of all elements present in array. XOR of all elements gives us XOR of x and y because of the following properties of XOR operation.
1) XOR of any number n with itself gives us 0, i.e., n ^ n = 0
2) XOR of any number n with 0 gives us n, i.e., n ^ 0 = n
3) XOR is cumulative and associative.

So we have XOR of x and y after the first step. Let the value of XOR be xor2. Every set bit in xor2 
indicates that the corresponding bits in x and y have values different from each other. For example,
if x = 6 (0110) and y is 15 (1111), then xor2 will be (1001), the two set bits in xor2 indicate that 
the corresponding bits in x and y are different. In the second step, we pick a set bit of xor2 and 
divide array elements in two groups. Both x and y will go to different groups. In the following code,
the rightmost set bit of xor2 is picked as it is easy to get rightmost set bit of a number. If we do XOR 
of all those elements of array which have the corresponding bit set (or 1), then we get the first odd number. 
And if we do XOR of all those elements which have the corresponding bit 0, then we get the other odd occurring number. 
This step works because of the same properties of XOR. All the occurrences of a number will go in same set. 
XOR of all occurrences of a number which occur even number number of times will result in 0 in its set. And the xor
of a set will be one of the odd occurring elements.

METHOD 2:
=================
Subtraction of 1 from a number toggles all the bits (from right to left) till the rightmost set bit(including
the righmost set bit). So if we subtract a number by 1 and do bitwise & with itself (n & (n-1)), we unset the 
righmost set bit. If we do n & (n-1) in a loop and count the no of times loop executes we get the set bit count.
Beauty of the this solution is number of times it loops is equal to the number of set bits in a given integer.

countSetBits(a): 
   1  Initialize count: = 0
   2  If integer n is not zero
      (a) Do bitwise & with (n-1) and assign the value back to n
          n: = n&(n-1)
      (b) Increment count by 1
      (c) go to step 2
   3  Else return count
 


Count number of bits to be flipped to convert A to B

Question: You are given two numbers A and B. Write a program to count number of bits needed to be flipped to convert A to B.

Solution:

  1. Calculate XOR of A and B.      
        a_xor_b = A ^ B
  2. Count the set bits in the above calculated XOR result.
        countSetBits(a_xor_b)


*/

// Program to find the two odd occurring elements
#include<stdio.h>
 
/* Prints two numbers that occur odd number of times. The
   function assumes that the array size is at least 2 and
   there are exactly two numbers occurring odd number of times. */
void printTwoOdd(int arr[], int size)
{
  int xor2 = arr[0]; /* Will hold XOR of two odd occurring elements */
  int set_bit_no;  /* Will have only single set bit of xor2 */
  int i;
  int n = size - 2;
  int x = 0, y = 0;
 
  /* Get the xor of all elements in arr[]. The xor will basically
     be xor of two odd occurring elements */
  for(i = 1; i < size; i++)
    xor2 = xor2 ^ arr[i];
 
  /* Get one set bit in the xor2. We get rightmost set bit
     in the following line as it is easy to get */
  set_bit_no = xor2 & ~(xor2-1);
 
  /* Now divide elements in two sets: 
    1) The elements having the corresponding bit as 1. 
    2) The elements having the corresponding bit as 0.  */
  for(i = 0; i < size; i++)
  {
     /* XOR of first set is finally going to hold one odd 
       occurring number x */
    if(arr[i] & set_bit_no)
      x = x ^ arr[i];
 
     /* XOR of second set is finally going to hold the other 
       odd occurring number y */
    else
      y = y ^ arr[i]; 
  }
 
  printf("\n The two ODD elements are %d & %d ", x, y);
}
 
/* Driver program to test above function */
int main()
{
  int arr[] = {4, 2, 4, 5, 2, 3, 3, 1};
  int arr_size = sizeof(arr)/sizeof(arr[0]);
  printTwoOdd(arr, arr_size);
  getchar();
  return 0;
}
