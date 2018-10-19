"""

10. Regular Expression match

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Note:

    s could be empty and contains only lowercase letters a-z.
    p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".

Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false

"""
import sys, pprint
pp = pprint.PrettyPrinter(indent=4)


def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    # adding 1 because index is starting from 1
    # pattern on X-Axis & text on Y-Axis
    T = [[False] * (len(p)+1) for _ in range(len(s)+1)]
    T[0][0] = True
    pp.pprint(T)
    # dealing with pattern like a*, a*b*
    # check how negative indexing in array in python works
    for i in range(1, len(T[0])):
        if p[i-1] == '*':
            T[0][i] = T[0][i-2]
    
    # go through columns: text len
    for i in range(1, len(T)):
        # go thorough rows: pattern len
        for j in range(1, len(T[0])):
            if (p[j-1] == '.' or p[j-1] == s[i-1]):
                T[i][j] = T[i-1][j-1]    # char match, go diagonal
            elif (p[j-1] == '*'):
                T[i][j] = T[i][j-2]    # 0 or more occurance of *
                if(p[j-2] == '.' or p[j-2] == s[i-1]):
                    T[i][j] = T[i][j] or T[i-1][j]
            else:
                T[i][j] = False
    return T[len(s)][len(p)]

pp.pprint(isMatch(s='a', p='*'))






