"""
676. Implement Magic Dictionary

Implement a magic directory with buildDict, and search methods.

For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.

For the method search, you'll be given a word, and judge whether if you modify exactly one character 
into another character in this word, the modified word is in the dictionary you just built.

Example 1:
Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False


Time Complexity: O(S) to build and O(NK) to search, where N is the number of words in our magic dictionary, 
S is the total number of letters in it, and K is the length of the search word.

Space Complexity: O(S), the space used by buckets.

"""
class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data_dict = collections.defaultdict(list)

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            self.data_dict[len(word)].append(word)
        
    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        count = 0
        for words in self.data_dict[len(word)]:
            count = 0
            for a, b in zip(word, words):
                if a != b:
                    count += 1
                    if count > 1:
                        break
            if count == 1:
                return True
        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)