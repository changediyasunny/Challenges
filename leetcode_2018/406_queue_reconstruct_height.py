"""
406. Queue Reconstruction by Height

Suppose you have a random list of people standing in a queue. Each person is described by a
pair of integers (h, k), where h is the height of the person and k is the number of people
in front of this person who have a height greater than or equal to h. Write an algorithm to
reconstruct the queue.
Note:
The number of people is less than 1,100.

Example
Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

Pick out tallest group of people and sort them in a subarray (S). Since there's no other
groups of people taller than them, therefore each guy's index will be just as same as his k value.
For 2nd tallest group (and the rest), insert each one of them into (S) by k value. So on and so forth.

E.g.
input: [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
subarray after step 1: [[7,0], [7,1]]
subarray after step 2: [[7,0], [6,1], [7,1]]
"""
import pprint
pp = pprint.PrettyPrinter(indent=4)

### Solution: 1
def reconstructQueue(people):
    if not people:
        return []
    peopledct, height, res = {}, [], []
    for ind, p in enumerate(people):
        h, k = p[0], p[1]
        if p[0] in peopledct:
            peopledct[h] += (k, ind),
        else:
            peopledct[h] = [(k, ind)]
            height.append(h)
    height.sort()
    # sort from the tallest group
    for h in height[::-1]:
        for k, ind in sorted(peopledct[h]):
            res.insert(k, people[ind])
    return res

### Solution: 2
def reconstructQueue2(people):

    people = sorted(people, key=lambda x: x[1])
    people = sorted(people, key=lambda x: -x[0])
    res = []
    for p in people:
        res.insert(p[1], p)
    return res

people = [[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]

pp.pprint(people)
print("=======================")
print(reconstructQueue2(people))
