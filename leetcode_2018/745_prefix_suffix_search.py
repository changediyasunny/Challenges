"""
745. Prefix and Suffix Search

Given many words, words[i] has weight i.

Design a class WordFilter that supports one function, WordFilter.f(String prefix, String suffix). It will
return the word with given prefix and suffix with maximum weight. If no word exists, return -1.

Examples:
Input:
WordFilter(["apple"])
WordFilter.f("a", "e") // returns 0
WordFilter.f("b", "") // returns -1

Note:
words has length in range [1, 15000].
For each test case, up to words.length queries WordFilter.f may be made.
words[i] has length in range [1, 10].
prefix, suffix have lengths in range [0, 10].
words[i] and prefix, suffix queries consist of lowercase letters only.

Time Complexity: O(NK^2 + QK) where N is the number of words, K is the maximum length of a word,
and Q is the number of queries.
Space Complexity: O(NK^2) the size of the trie. 
"""
# trie data structure
class WordFilter:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        from collections import defaultdict
        self.prefix_tr = defaultdict(set)
        self.suffix_tr = defaultdict(set)
        self.weights = {}

        for weight, word in enumerate(words):
            pref = ''
            suff = ''
            for ch in [''] + list(word):
                pref += ch
                self.prefix_tr[pref].add(word)
            for ch in [''] + list(word[::-1]):
                suff += ch
                self.suffix_tr[suff[::-1]].add(word)
            self.weights[word] = weight
        ###

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        weight = -1
        for w in self.prefix_tr[prefix] & self.suffix_tr[suffix]:
            if self.weights[w] > weight:
                weight = self.weights[w]
        return weight

# Hash of prefix & suffix words delimited by #
class WordFilter:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.combs = {}
        for weight, word in enumerate(words):
            pref = ''
            for p in [''] + list(word):
                pref += p
                suff = ''
                for s in [''] + list(word[::-1]):
                    suff += s
                    self.combs[pref+'#'+suff[::-1]] = weight
        ###

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        return self.combs.get(prefix+'#'+suffix, -1)
