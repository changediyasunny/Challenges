"""

139. Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be
segmented into a space-separated sequence of one or more dictionary words.

Note:

    The same word in the dictionary may be reused multiple times in the segmentation.
    You may assume the dictionary does not contain duplicate words.

Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

both solutions:
Time complexity : O(n^2). Two loops are their to fill dp array.
Space complexity : O(n). Length of p array is n+1.
"""

### Using BFS
def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    visited = set()
    queue_list = [0]
    while(queue_list):
        start = queue_list.pop()
        if start not in visited:
            for i in range(start+1, len(s)+1):
                if s[start:i] in wordDict:
                    queue_list.append(i)
                    if i == len(s):
                        return True
            visited.add(start)
    return False


### Using DP
def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    wordDict = ['leet', 'code']
    dp = [False for i in range(len(s)+1)] # dp[i] means wordBreak(s[:i],wordDict)
    dp[0] = True
    for i in range(1, len(s)+1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break
    return dp[-1]
