"""
161. One Edit Distance

Given two strings s and t, determine if they are both one edit distance apart.

Note:

There are 3 possiblities to satisify one edit distance apart:

Insert a character into s to get t
Delete a character from s to get t
Replace a character of s to get t
Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "cab", t = "ad"
Output: false
Explanation: We cannot get t from s by only one step.

Running time: O(n)

"""

class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ns = len(s)
        nt = len(t)

        if ns > nt:
            return self.isOneEditDistance(t, s)

        if nt - ns > 1:
            return False

        for i in range(ns):
            if s[i] != t[i]:
                # if strings are equal, comapre exact slice
                if ns == nt:
                    return s[i+1:] == t[i+1:]
                else:
                    # strings not equal but T is larger,
                    # compare (i+1)th slice
                    return s[i:] == t[i+1:]
        # if strings are equal and there's no difference.
        # then strings are one edit distance only if
        # T has one more character.
        return ns + 1 == nt
