"""
765. Couples Holding Hands

N couples sit in 2N seats arranged in a row and want to hold hands. We want to
know the minimum number of swaps so that every couple is sitting side by side.
A swap consists of choosing any two people, then they stand up and switch seats.

The people and seats are represented by an integer from 0 to 2N-1, the couples
are numbered in order, the first couple being (0, 1), the second couple being (2, 3),
and so on with the last couple being (2N-2, 2N-1).

The couples' initial seating is given by row[i] being the value of the person who is
initially sitting in the i-th seat.

Example 1:

Input: row = [0, 2, 1, 3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.
Example 2:

Input: row = [3, 2, 0, 1]
Output: 0
Explanation: All couples are already seated side by side.

Running Time: O(N^2)

If a person is number x, their partner is x ^ 1, where ^ is the bitwise XOR operator.
For each first person x = row[i] on a couch who is unpartnered, let's find their partner at row[j] and have them swap seats with row[i+1]
"""
# XOR of a number with 1 gives next number
class Solution(object):
    def minSwapsCouples(self, row):
        ans = 0
        for i in range(0, len(row), 2):
            x = row[i]
            if row[i+1] == x^1:
                continue
            ans += 1
            for j in range(i+1, len(row)):
                if row[j] == x^1:
                    row[i+1], row[j] = row[j], row[i+1]
                    break
        return ans


"""
#TODO: Couples represented with similar integer value (2,2)

N different couple goes to a cinema with 2N different seats. They take their place randomly.
You could make swap operation. Write a code for given input what is the minimum number of
swap operations for sitting all couples with their partners? Additionally, be sure that no
one swaps more than 2 times.

"""

# example array: [2,1,2,3,1,3]
# array will sorted to: [2,2,1,1,3,3]
# with n_swaps = 2
def couple_pairing(array):
    if array == None or (len(array) % 2) != 0:
        return 0
    # hash: previous found element, value: desired index for partner
    hash_table = dict()
    n_swaps = 0
    for index, element in enumerate(array):
        # if element in hash, then swap with the index value in hash
        if element in hash_table:
            desired_index = hash_table[element]
            value_at_desired_index = array[desired_index]
            # avoid an extra swap for itself, for example if array was [1,1]
            if value_at_desired_index != element:
                array[index], array[desired_index] = array[desired_index], array[index]
                n_swaps += 1
                hash_table[value_at_desired_index] = get_desired_index(index)
        else:
            hash_table[element] = get_desired_index(index)
        print(hash_table)
        print(array)
        print(">>>>>")
    return n_swaps

def get_desired_index(curr_index):
    if (curr_index % 2) == 0:
        return curr_index + 1
    return curr_index - 1
