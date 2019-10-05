"""
792. Number of Matching Subsequences

Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

Example :
Input:
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".

"""

class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        data_dict = collections.defaultdict(list)
        for word in words:
            data_dict[word[0]].append(word)

        count = 0
        for char in S:
            expected_words = data_dict[char]
            data_dict[char] = []
            for wd in expected_words:
                if len(wd) == 1:
                    count += 1
                else:
                    data_dict[wd[1]].append(wd[1:])
        return count
