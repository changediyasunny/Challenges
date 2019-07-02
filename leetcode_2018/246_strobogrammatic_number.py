"""
246. Strobogrammatic Number

A strobogrammatic number is a number that looks the same when rotated 180 degrees
(looked at upside down). Write a function to determine if a number is strobogrammatic.
The number is represented as a string.

Example 1:
Input:  "69"
Output: true

Example 2:
Input:  "88"
Output: true

Example 3:
Input:  "962"
Output: false

"""

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        data = {'0':'0', '1':'1', '8':'8', '6':'9', '9':'6'}
        i = 0
        j = len(num)-1
        while i <= j:
            if num[i] not in data or data[num[i]] != num[j]:
                return False
            i += 1
            j -= 1
        return True
