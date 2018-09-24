"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 


Example 2:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

import sys

def lengthOfLongestSubstring(strs):
    """ """
    
    if len(strs) == 0:
        return 0

    hashmap = {}
    maxlen = 0
    start = 0

    for i, c in enumerate(strs):
        if c in hashmap and hashmap[c] >= start:
            # if char found

            # repeated cahr found, update max length
            maxlen = max(maxlen, i-start)

            # set start index of new subsequence to previous index
            # of repeated letter + 1
            start = hashmap[c] + 1
        hashmap[c] = i
    return max(maxlen, len(strs) - start)


# sliding window solution
def length_longest_substring(strs):
    """ """
    if len(strs) == 0:
        return 0

    visited = {}
    maxlen = 0
    start = 0
    for end, c in enumerate(strs):
        if c in visited:
            start = max(start, visited[c] + 1)
        visited[c] = end
        maxlen = max(maxlen, end - start + 1)
    return maxlen

print(lengthOfLongestSubstring('ABDEFGABEF'))

