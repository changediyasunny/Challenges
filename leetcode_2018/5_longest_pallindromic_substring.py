"""
5. Given a string s, find the longest palindromic substring in s. You may assume
that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"

"""

import pprint
pp = pprint.PrettyPrinter(indent=4)

""" Expand around center:
In fact, we could solve it in O(n^2) time using only constant space.
We observe that a palindrome mirrors around its center. Therefore, a palindrome
can be expanded from its center, and there are only 2n-1 such centers.
You might be asking why there are 2n-1 but not n centers? The reason is the center of
a palindrome can be in between two letters. Such palindromes have even number of
letters (such as "abba") and its center are between the two 'b's.

time complexity: O(n^2)
space complexity: O(1)
"""
def longest_pallindrome_substring(strs):
    """ """
    start = 0
    end = 0
    for i in range(len(strs)):
        len1 = expand_center(strs, i, i)     # char of length 1
        len2 = expand_center(strs, i, i+1)   # char of length 2
        lenn = max(len1, len2)
        if lenn > (end-start):
            start = i - (lenn-1)/2
            end = i + lenn/2
        #print("i = %s    | start = %s    | end = %s" %(i, start, end))
    return strs[start:end+1]

def expand_center(strs, L, R):
    """ this expands around center """
    while (L >=0 and R < len(strs) and strs[L] == strs[R]):
        L = L - 1
        R = R + 1
    return R-L-1

print("expand around center:")
print(longest_pallindrome_substring('pqabbars'))



""" Dynamic Programming:

"""
def long_pall_substring(strs):
    """ """
    if not s:
        return ""

    N = len(s)
    dp = [[False for i in range(N)] for _ in range(N)]
    maxlen = 1
    # for lenght of 1
    for i in range(N):
        dp[i][i] = True

    start = 0
    for i in range(N-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            start = i
            maxlen = 2

    # of all lengths
    for k in range(3, N+1):
        for i in range(N-k+1):
            j = i + k -1
            if dp[i+1][j-1] and s[i] == s[j]:
                dp[i][j] = True
                if k > maxlen:
                    start = i
                    maxlen = k
    return s[start:start+maxlen]

print("Dynamic Programming:")
print(long_pall_substring('pqabbars'))
