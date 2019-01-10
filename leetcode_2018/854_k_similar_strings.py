"""
854. K-Similar Strings

Strings A and B are K-similar (for some non-negative integer K) if we can swap the
positions of two letters in A exactly K times so that the resulting string equals B.
Given two anagrams A and B, return the smallest K for which A and B are K-similar.

Example 1:
Input: A = "ab", B = "ba"
Output: 1

Example 2:
Input: A = "abc", B = "bca"
Output: 2

Example 3:
Input: A = "abac", B = "baca"
Output: 2

Example 4:
Input: A = "aabc", B = "abca"
Output: 2

###
Problem-2:
Given two string s and t and a positive integer K, determine whether we can swap
any two characters in string s at most K times so that s is equal to t.

Example 1

s = "converse"
t = "conserve"
K = 1
>> return true.
because we can swap v and s in string s and we swap only once
which is not greater than K times.

Example 2

s = "aabbccdd"
t = "ddbbccaa"
K = 3

>> return true.
because string s can be converted to string t in two swaps which is not
greater than K. But in example 2, if string s and string t are still the same but K
becomes 1, then we should return false.

The length of string s and t are guaranteed to be the same.

time: 2^(N + W) where W is length of alphabet
space: O(N * t) where N is length of string and t is time complexity given above
"""
def kSimilarity(strs1, strs2, k):
    def neighbors(strs):
        for i, c in enumerate(strs):
            if c != strs2[i]:
                break
        data = []
        temp_strs = list(strs)
        for j in range(i+1, len(strs)):
            if strs[j] == strs2[i]:
                temp_strs[i], temp_strs[j] = temp_strs[j], temp_strs[i]
                data.append("".join(temp_strs))
                temp_strs[j], temp_strs[i] = temp_strs[i], temp_strs[j]
        return data

    queue = deque([strs1])
    seen = {strs1: 0}
    while queue:
        strs = queue.popleft()
        if strs == strs2:
            if seen[strs] > k:
                return False
            return True

        for tmp_strs in neighbors(strs):
            print(tmp_strs)
            if tmp_strs not in seen:
                seen[tmp_strs] = seen[strs] + 1
                queue.append(tmp_strs)
