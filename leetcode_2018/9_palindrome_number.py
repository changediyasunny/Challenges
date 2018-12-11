"""
9. Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when it
reads the same backward as forward.

Example 1:

Input: 121
Output: true

Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
Therefore it is not a palindrome.

Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

"""
# Reverse only half of numbers
# when x < rev, it means we have traversed half of numbers
# x == rev//10: because middel number doesn;t matter in palindrome
# Eg: 12321 and rev == 123 so we remove 3.
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev = 0
        if x < 0 or (x != 0 and x%10==0 ):
            return False
        while x > rev:
            rev = rev * 10 + x%10
            x = x // 10
        return ((x == rev) or (x == rev//10))
