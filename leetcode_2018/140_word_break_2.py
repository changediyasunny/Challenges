"""

140. Word Break II

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

    The same word in the dictionary may be reused multiple times in the segmentation.
    You may assume the dictionary does not contain duplicate words.

Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]

Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]


"""

def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: List[str]
    """
    # Throws memory error
    # input: 
    #       s = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    #       wordDict: {'a', 'aaa', 'aaaaa', ....}
    
    result_table = [[""]]
    dp = [False] * (len(s)+1)
    dp[0] = result_table[0]
    
    for i in range(1, len(s)+1):
        temp_list = []
        for j in range(i):
            if len(dp[j]) and s[j:i] in wordDict:
                for sol in dp[j]:
                    temp_list.append(sol + ("" if sol == "" else " " )+ s[j:i])
        dp[i] = temp_list
    return dp[len(s)]

def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: List[str]
    """
    result_table = [[""]]
    n = len(s)
    # Check if there is at least one possible sentence
    dp_temp = [0]*(n+1);
    dp_temp[0] = True;
    for i in range(1, n+1): 
        for j in range(i): 
            if dp_temp[j] and s[j:i] in wordDict: 
                dp_temp[i] = True
                break
    
    # We are done if there isn't a valid sentence at all
    if not dp_temp[n]: return []
    
    # Fill dp with its solutions
    for i in range(1, n+1):
        liste = []
        for j in range(i):
            if result_table[j] and s[j:i] in wordDict :
                for sol in result_table[j]: 
                    liste.append(sol + ("" if sol == "" else " " )+ s[j:i])
                
        result_table.append(liste)
    return result_table[n]