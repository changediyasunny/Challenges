"""
126. Word Ladder II

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]


Input:
"a"
"c"
["a","b","c"]
Output:
[["a","c"],["a","b","c"]]
Expected:
[["a","c"]]

"""


def construct_dict(word_list):
    d = {}
    for word in word_list:
        for i in range(len(word)):
            s = word[:i] + "_" + word[i+1:]
            try:
                d[s].append(word)
            except:
                d[s] = [word]
    return d

def findLadders(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: List[List[str]]
    """
    def bfs_words(begin, end, dict_words):
        queue= [(begin, 1, [begin])]
        order = {}
        result = []
        while queue:
            word, level, steps = queue.pop(0)
            if word == end:
                if not result:
                    result.append(steps)
                elif result and len(steps) <= len(result[0]):
                    result.append(steps)
            if word in order and level > order[word]:
                continue
            order[word] = level
            for i in range(len(word)):
                s = word[:i] + "_" + word[i+1:]
                neigh_words = dict_words.get(s, [])
                for neigh in neigh_words:
                    if neigh not in order:
                        queue.append((neigh, level+1, steps + [neigh]))
        return result

    d = construct_dict(wordList)
    return bfs_words(beginWord, endWord, d)

beginWord = 'hit'
endWord = 'cog'
wordList = ["hot","dot","dog","lot","log","cog"]
print(findLadders(beginWord, endWord, wordList))
