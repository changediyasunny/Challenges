"""

Reverse Shuffle Merge


1) Used an array freq[26] to store frequency of each character (a to z) in the original string S


2) Characters of A will be known using this frequency array, since, each character will appear in A exactly 1/2 times of the frequency array (or S). This is because S was formed using A twice, once in form of shuffle(A) and again as reverse(A)


3) Now, size of A (n/2) and characters already known, try building A (getting order of characters) using the original string S


4) To do that, understand the following : Since reverse(A) is a subsequence of S, hence, A must be subsequence of reverse(S). Thus, to find A, either reverse the array S and move normally, or traverse S in reverse direction (right to left)


5) I selected traversing S in reverse direction from right to left, in order to gradually build A, character by character. For each position in S, a choice is to be made, wether or not to select the character for A (this is where frequency array will help !)


6) To fulfill the condition of lexicographically smallest A, always try to select lexicographically smallest character. This can be done be leaving larger characters and selecting the smallest one seen till then, untill its critical to select larger character


7) In order to decide upon the criticality of selection, just understand that you can't leave out a character 'i' if freq[i] in A is same as the count of 'i' left to be seen in string S. You might need some array to keep track of this. To give an example : if 'x' appears 6 times in S, then A would have exactly 3'x'. Now while traversing S if you leave 'x' 3 times and select some smaller character instead (to form lexicographically smaller A), you cannot leave it 4th time, because there are only 3 'x' left to be seen in S and you need all of them.

Once, you get all the characters required for A, print it as answer !

"""

def small_lexi(s):
    letters = list(set(list(s)))
    letters.sort()
    reverse_s = s[::-1]
    counter = {i:(s.count(i))/2 for i in letters}
    A = ''
    for j in xrange(len(s)):
        if reverse_s[j:].count(reverse_s[j]) == counter[reverse_s[j]]:
            counter[reverse_s[j]] -= 1
            A += reverse_s[j]
        elif reverse_s[j] == letters[0]:
            if counter[letters[0]] > 0:
                counter[letters[0]] -= 1
                A += letters[0]
            else:
                letters.pop(0)
        else:
            continue
    return A

def main():
	s = "eggegg"
	print small_lexi(s)
	
if __name__ == '__main__':
    main()
