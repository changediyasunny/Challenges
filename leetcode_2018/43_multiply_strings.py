"""
43. Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"


Start from right to left, perform multiplication on every pair of digits, and add them together. Let's draw the process!
From the following draft, we can immediately conclude:

num1[i] * num2[j] >> will be placed at indices [i + j, i + j + 1]

"""



class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = [0] * (len(num1) + len(num2))
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                # print(i, j)
                result[i+j+1] += int(num1[i]) * int(num2[j])
                result[i+j] += result[i+j+1] // 10
                result[i+j+1] = result[i+j+1] % 10
        k = 0
        while k < len(result) and result[k] == 0:
            k += 1

        res = ''.join(str(elem) for elem in result[k:])
        return res if res else '0'
