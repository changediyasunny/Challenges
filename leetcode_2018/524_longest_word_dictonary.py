"""
524. Longest Word in Dictionary through Deleting

Given a string and a string dictionary, find the longest string in the dictionary
that can be formed by deleting some characters of the given string. If there are more
than one possible results, return the longest word with the smallest lexicographical order.
If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output:
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output:
"a"

"""
def findLongestWord(s, d):
    """
    :type s: str
    :type d: List[str]
    :rtype: str
    """
    best_match = ''
    for strs in d:
        # using this construct since 'ab' < 'ba' so if lengths are equal,
        # we need comparison between strs itself.
        # using -ve length because best-string starts with '' and strs < best
        # at the beginning
        if (-len(strs), strs) < (-len(best_match), best_match):
            itrr = iter(s)
            if all(c in itrr for c in strs):
                best_match = strs
    return best_match


# Using Sorting
def findLongestWord(S, D):
    D.sort(key = lambda x: (-len(x), x))
    for word in D:
        i = 0
        for c in S:
            if i < len(word) and word[i] == c:
                i += 1
        if i == len(word):
            return word
    return ""


# Using heap sort
def findLongestWord(s, d):
    heap = [(-len(word), word) for word in d]
    heapq.heapify(heap)
    while heap:
        word = heapq.heappop(heap)[1]
        itrr = iter(s)
        if all(c in itrr for c in word):
            return word
    return ''
