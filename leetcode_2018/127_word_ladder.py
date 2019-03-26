"""
127. Word Ladder

Given two words (beginWord and endWord), and a dictionary's word list,
find the length of shortest transformation sequence from beginWord to endWord,
such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a
transformed word.

Note:

Return 0 if there is no such transformation sequence. All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5
Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.


Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0
Explanation: The endWord "cog" is not in wordList, therefore
no possible transformation.

The time complexity would be O(NL), where N is the number of words and L is
the length of each word

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

# Queue: BFS
def ladderLength(beginWord, endWord, wordList):
    def bfs_words(begin, end, dict_words):
        queue = [(begin, 1)]
        visited = set()
        while queue:
            word, steps = queue.pop(0)
            for i in range(len(word)):
                s = word[:i] + "_" + word[i+1:]
                neigh_words = dict_words.get(s, [])
                for neigh in neigh_words:
                    if neigh == endWord:
                        return steps + 1
                    if neigh not in visited:
                        visited.add(word)
                        queue.append((neigh, steps + 1))
                dict_words[s] = []
        return 0
    d = construct_dict(wordList)
    return bfs_words(beginWord, endWord, d)


# Stack DFS
def word_ladder(beginword, endword, word_list):
    def dfs(begin, end, hashmap):
        visited = set()
        stack = [(begin, 1)]
        while stack:
            word, steps = stack.pop()
            for i in range(len(word)):
                s = word[:i] + '_' + word[i+1:]
                kids = hashmap.get(s, [])
                for kid in kids:
                    if kid == end:
                        return steps + 1
                    if kid not in visited:
                        stack.append((kid, steps+1))
                hashmap[s] = []
        return 0

    hashmap = construct_dict(word_list)
    return dfs(beginword, endword, hashmap)

# using label strategy
def ladder_label(beginWord, endWord, wordList):

    d = construct_dict(wordList)
    thisLevel = [beginWord]
    count = 1
    visited = set()
    while thisLevel:
        nextLevel = []
        count += 1
        for word in thisLevel:
            for i in range(len(word)):
                label = word[:i] + '_' + word[i+1:]
                if label in visited:
                    continue
                else:
                    visited.add(label)
                    nextLevel.extend(d.get(label, []))
        if endWord in nextLevel:
            print(visited)
            return count
        thisLevel = nextLevel
    return 0

beginWord = 'hit'
endWord = 'cog'
wordList = ["hot","dot","dog","lot","log","cog"]
print(ladderLength(beginWord, endWord, wordList))
print(word_ladder(beginWord, endWord, wordList))
