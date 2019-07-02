"""
267. Palindrome Permutation II

Given a string s, return all the palindromic permutations (without duplicates) of it.
Return an empty list if no palindromic permutation could be form.

Example 1:
Input: "aabb"
Output: ["abba", "baab"]

Example 2:
Input: "abc"
Output: []

Time complexity: O(((n+1)/2)!),
space complexity: O(n).


"""
class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def helper(strs):
            res =[""]
            for char in strs:
                temp = []
                for r in res:
                    for i in range(len(r)+1):
                        temp.append(r[:i]+char+r[i:])
                        if i < len(r) and char == r[i]:
                            # remove duplicate
                            break
                res = temp
            return res

        data = collections.Counter(s)
        # find if string is atleast pallindrome
        odd = [k for k, v in data.items() if v%2]
        if len(odd) > 1:
            return []
        odd = '' if odd == [] else odd[0]
        # get half of string
        strs = ''.join(k * (v//2) for k, v in data.items())
        # find pallindromes
        print(strs)
        result = helper(strs)
        #print(result)
        for i in range(len(result)):
            result[i] = result[i] + odd + result[i][::-1]
        return result
