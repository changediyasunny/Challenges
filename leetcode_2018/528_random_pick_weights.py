"""
528. Random Pick with Weight

Given an array w of positive integers, where w[i] describes the weight of index i,
write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input:
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
Example 2:

Input:
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor
has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list,
even if there aren't any.

Explanation:
say we have the numbers 1, 5, 2 easiest solution is to construct the following array
arr[] = {0,1,1,1,1,1,2,2}
then generate a random number between 0 and 7 and return the arr[rnd]. This is solution
is not really good though due to the space requirements it has (imagine a number beeing 2billion).

The solution here is similar but instead we construct the following array (accumulated sum)
{1, 6, 8} generate a number between 1-8 and say all numbers generated up to 1 is index 0.
all numbers generated greater than 1 and up to 6 are index 1 and all numbers greater than 6 and
up to 8 are index 2. After we generate a random number to find which index to return we use binary search.

"""

class Solution:

    def __init__(self, w):
        """
        :type w: List[int]
        """
        for i in range(1, len(w)):
            w[i] = w[i-1] + w[i]
        self.weights = w
        self.tot = self.weights[-1]

    def pickIndex(self):
        """
        :rtype: int
        """
        def bsearch(num):
            lo = 0
            hi = len(self.weights) - 1
            while lo < hi:
                mid = lo + (hi-lo)//2
                if self.weights[mid] == num:
                    return mid
                elif self.weights[mid] < num:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        num = random.randint(1, self.tot)
        return bsearch(num)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
