"""

44. Wildcard Matching

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

Note:

    s could be empty and contains only lowercase letters a-z.
    p could be empty and contains only lowercase letters a-z, and characters like ? or *.

Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

Example 5:

Input:
s = "acdcb"
p = "a*c?b"
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
    # reduce pattern for multiple *
    # a***b***c --> a*b*c
    flag = True
    temp_pat = ''
    for i in range(len(p)):
        if p[i] == '*':
            if flag:
                temp_pat += p[i]
                flag = False
        else:
            temp_pat += p[i]
            flag = True
    
    if not temp_pat:
        temp_pat = p
    # DP Table
    # string on X-axis & pattern on Y-axis
    T = [ [False] * (len(temp_pat)+1) for _ in range(len(s)+1) ]
    
    # init empty strings & * pattern
    T[0][0] = True
    if(temp_pat and temp_pat[0] == '*'):
        T[0][1] = True

    for i in range(1, len(T)):    # string
        for j in range(1, len(T[0])):    #pattern
            if (temp_pat[j-1] == '?' or temp_pat[j-1] == s[i-1]):
                T[i][j] = T[i-1][j-1]
            elif (temp_pat[j-1] == '*'):
                T[i][j] = T[i-1][j] or T[i][j-1]
    return T[len(s)][len(temp_pat)]

print(isMatch(s='aab', p='c*a*b'))




