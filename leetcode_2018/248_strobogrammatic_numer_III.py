"""
248. Strobogrammatic Number III

A strobogrammatic number is a number that looks the same when rotated 180 degrees
(looked at upside down). Write a function to count the total strobogrammatic numbers
that exist in the range of low <= num <= high.

Example:
Input: low = "50", high = "100"
Output: 3
Explanation: 69, 88, and 96 are three strobogrammatic numbers.


"""

class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        stack = ["", "0", "1", "8"]
        low = int(low)
        maxlen = len(high)
        high = int(high)
        cnt = 0

        while stack:
            # pop(0) in this case leads to TLE.
            # stack grows exponentially because we append invalids
            # and remove required
            char = stack.pop()
            if char and char[0] != "0" and low <= int(char) <= high:
                cnt += 1
            if len(char) <= maxlen-2:
                for a, b in '00 11 69 88 96'.split():
                    stack.append(a+char+b)
        return cnt if low != 0 else cnt + 1

### Using method to find such number of length
class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        temp_list = []
        for i in range(1, len(high)+1):
            # 50 & 100
            # this will go from length of 1, 2, 3
            temp_list += self.number_of_length(i)

        cnt = 0
        for n in set(temp_list):
            if int(n) >= int(low) and int(n) <= int(high):
                cnt += 1
        return cnt

    def number_of_length(self, n):
        nums = n % 2 * list('018') or ['']
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
