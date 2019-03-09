"""
418. Sentence Screen Fitting
Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.

Input:
rows = 2, cols = 8, sentence = ["hello", "world"]
Output:
1

Explanation:
hello---
world---

The character '-' signifies an empty space on the screen.

Example 2:
Input:
rows = 3, cols = 6, sentence = ["a", "bcd", "e"]
Output:
2

Explanation:
a-bcd-
e-a---
bcd-e-
The character '-' signifies an empty space on the screen.

Example 3:
Input:
rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]
Output:
1

Explanation:
I-had
apple
pie-I
had--

The character '-' signifies an empty space on the screen.

"""

class Solution:
    def wordsTyping(self, sentence, rows, cols):
        s = ' '.join(sentence) + ' '
        start = 0
        for i in range(rows):
            start += cols
            print(s[start % len(s)])
            if s[start % len(s)] == ' ':
                start += 1
            else:
                while start > 0 and s[ (start - 1) % len(s) ] != ' ':
                    start -= 1
        return start// len(s)
