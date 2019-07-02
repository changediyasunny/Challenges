"""
68. Text Justification

Given an array of words and a width maxWidth, format the text such that each line has
exactly maxWidth characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as
you can in each line. Pad extra spaces ' ' when necessary so that each line has
exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number
of spaces on a line do not divide evenly between words, the empty slots on the left
will be assigned more spaces than the slots on the right.

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified because it contains only one word.

Running time: O(N)
"""

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        char_count = 0
        word_count = 0
        space = 1
        line = []
        result = []

        for word in words:
            total_length = len(word) + space + char_count
            if total_length > maxWidth:
                space_left = maxWidth - char_count
                # words go beyond screen
                if word_count == 1:
                    # single word
                    string = line[0] + " "*(maxWidth - len(line[0]))
                else:
                    q, r = divmod(space_left, word_count-1)
                    front = (" "*(q+2)).join(line[:r+1])
                    end = (" "*(q+1)).join(line[r+1:])
                    string = front + " "*(q+1) + end
                if string:
                    result.append(string)
                line = [word]
                word_count = 1
                char_count = len(word)

            else:
                # chars still fits into line
                char_count += len(word)
                # space between two chars
                if line: char_count += 1
                line.append(word)
                word_count += 1
        if line:
            line = ' '.join(line)
            line += ' '*(maxWidth - len(line))
            result.append(line)
        return result

# Using tricky add space operations
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    # this is tricky to add spaces based off 0 & 1
                    # "or 1 " is taken for len(cur) == 1
                    cur[i%(len(cur)-1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]
