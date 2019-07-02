"""
247. Strobogrammatic Number II

A strobogrammatic number is a number that looks the same when rotated 180 degrees
(looked at upside down).
Find all strobogrammatic numbers that are of length = n.

Example:

Input:  n = 2
Output: ["11","69","88","96"]


"""

class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # if n is odd then we need nums to be [0,1,8]
        # it adds to the middle part of large number
        # [6, 9] can not be in the middel as they are opposite
        # they only work sideways
        nums = n%2 * list('018') or ['']
        result = []
        while n > 1:
            n = n - 2
            temp_list = '00 11 69 88 96'.split()[n<2:]
            for a, b in temp_list:
                for nb in nums:
                    result.append(a+nb+b)
            nums = result
            result = []
        return nums
