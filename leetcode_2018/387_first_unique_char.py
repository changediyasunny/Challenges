"""

387. First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's index.
If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

RUnning TIme: O(n) + time to traverse data dict

"""


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        data = {}
        for i, char in enumerate(s):
            try:
                tmp = data[char]
                data[char] = -1
            except:
                data[char] = i
        try:
            return min( i for i in data.values() if i >=0)
        except:
            return -1
