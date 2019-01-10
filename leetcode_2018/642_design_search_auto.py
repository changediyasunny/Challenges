"""
642. Design Search Autocomplete System

Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#'). For each character they type except '#', you need to return the top 3 historical hot sentences that have prefix the same as the part of sentence already typed. Here are the specific rules:

The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same degree of hot, you need to use ASCII-code order (smaller one appears first).
If less than 3 hot sentences exist, then just return as many as you can. When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.
Your job is to implement the following functions:

The constructor function:

AutocompleteSystem(String[] sentences, int[] times):
This is the constructor. The input is historical data. Sentences is a string array consists of previously typed sentences. Times is the corresponding times a sentence has been typed. Your system should record these historical data.

Now, the user wants to input a new sentence. The following function will provide the next character the user types:
List<String> input(char c): The input c is the next character typed by the user. The character will only be lower-case letters ('a' to 'z'), blank space (' ') or a special character ('#'). Also, the previously typed sentence should be recorded in your system. The output will be the top 3 historical hot sentences that have prefix the same as the part of sentence already typed.


Example:
Operation: AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
The system have already tracked down the following sentences and their corresponding times:
"i love you" : 5 times
"island" : 3 times
"ironman" : 2 times
"i love leetcode" : 2 times
Now, the user begins another search:

Operation: input('i')
Output: ["i love you", "island","i love leetcode"]
Explanation:
There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.

Operation: input(' ')
Output: ["i love you","i love leetcode"]
Explanation:
There are only two sentences that have prefix "i ".

Operation: input('a')
Output: []
Explanation:
There are no sentences that have prefix "i a".

Operation: input('#')
Output: []
Explanation:
The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.

Note:
The input sentence will always start with a letter and end with '#', and only one blank space will exist between two words. The number of complete sentences that to be searched won't exceed 100. The length of each sentence including those in the historical data won't exceed 100.
Please use double-quote instead of single-quote when you write test cases even for a character input.
Please remember to RESET your class variables declared in class AutocompleteSystem, as static/class variables are persisted across multiple test cases. Please see here for more details.



Input:
["AutocompleteSystem","input","input","input","input"]
[[["i love you","island","iroman","i love leetcode"],[5,3,2,2]],["i"],[" "],["a"],["#"]]

Output:
[null,["i love you","island","i love leetcode"],["i love you","i love leetcode"],[],[]]

AutocompleteSystem() takes O(k*L) time. We need to iterate over L sentences each of average length k,
to create the trie for the given set of sentences.

input() takes O(p+q+mlog(m)) time. Here, p refers to the length of the sentence formed till now, cur_sens and
q refers to the number of nodes in the trie considering the sentence formed till now as the root node. Again, we need to sort the list of length m indicating the options available for the hot sentences, which takes O(mlog(m)) time.

"""


import sys, os

class TrieNode():
    def __init__(self):
        self.child = {}
        self.data = None
        self.isEnd = False
        self.rank = 0

class AutocompleteSystem:

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.keyword = ""
        self.root = TrieNode()
        for sent, rank in zip(sentences, times):
            self.insert(sent, rank)

    def insert(self, sent, rank):
        current = self.root
        for s in sent:
            if s not in current.child:
                current.child[s] = TrieNode()
            current = current.child[s]
        current.data = sent
        # because to get ranking in descending order, with +, sorting will be in asc.
        # trick to fool
        # also to deal with duplicate sentences ['aaa', 'aaa'] & [2, 3]
        current.rank -= rank

    def dfs(self, node):
        ret = []
        if node:
            if node.data:
                ret.append([node.rank, node.data])
            for t in node.child:
                ret.extend(self.dfs(node.child[t]))
        return ret

    def getTopSent(self, strs):
        current = self.root
        for char in strs:
            if char not in current.child:
                return []
            current = current.child[char]
        result = self.dfs(current)
        return result

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        result = []
        if c == '#':
            # end of sentence
            self.insert(self.keyword, 1)
            self.keyword = ""
        else:
            # actual input char
            self.keyword += c
            result = self.getTopSent(self.keyword)
        print(result)
        return [k[1] for k in sorted(result)[:3]]

# Your AutocompleteSystem object will be instantiated and called as such:

sentences = ["i love you","island","iroman","i love leetcode"]
times = [5,3,2,2]
obj = AutocompleteSystem(sentences, times)
print(obj.input('i'))
print("==================")
print(obj.input(' '))
print("==================")
print(obj.input('a'))
print("==================")
print(obj.input('#'))
