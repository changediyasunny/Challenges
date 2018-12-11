"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        max_idx = min([len(s) for s in strs])
        for i in range(max_idx, 0, -1):
            for temp in strs[1:]:
                print(temp)
                if temp[:i] != strs[0][:i]:
                    break
            else:
                # only executed if above for loop completes without breaking.
                return strs[0][:i]
        return ''
