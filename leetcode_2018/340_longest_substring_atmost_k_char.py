"""
340. Longest Substring with At Most K Distinct Characters

Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.

Running time: O(N)
Space: O(k) We use orderedDict() which has all operations at O(1) time

# using hash cause (K+1) of space so running timebecomes O(Nk)
"""
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s or not k:
            return 0
        n = len(s)
        hashmap = collections.OrderedDict()
        left = 0
        right = 0
        maxlen = 1
        while right < n:
            ch = s[right]

            # check hashmap for char
            if ch in hashmap:
                # needed because ordered dict has left element
                # eg. abacccc  # left-a needs to be removed
                del hashmap[ch]
            hashmap[ch] = right

            # check length
            if len(hashmap) == k+1:
                # pop only left from dict
                _, del_idx = hashmap.popitem(last = False)
                left = del_idx + 1

            right += 1
            maxlen = max(maxlen, right-left)
        return maxlen
