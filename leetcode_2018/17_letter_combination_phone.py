"""
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations
that the number could represent. A mapping of digit to letters (just like on the telephone buttons)
is given below. Note that 1 does not map to any letters.

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Time and space: 3^N * 4^M
"""

class Solution:
    def __init__(self):
        self.d = {
            '0': '',
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        combinations = list()

        def helper(strs, path):
            print(strs, path)
            if not strs:
                combinations.append(path)
                return
            first, rest = strs[0], strs[1:]
            letters = self.d[first]
            for letter in letters:
                helper(rest, path+letter)

        helper(digits, "")
        return [] if digits == "" else combinations

obj = Solution()
print(obj.letterCombinations("23"))
