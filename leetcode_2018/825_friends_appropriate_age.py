"""
825. Friends Of Appropriate Ages

Some people will make friend requests. The list of their ages is given and ages[i]
is the age of the ith person. Person A will NOT friend request person B (B != A) if
any of the following conditions are true:

age[B] <= 0.5 * age[A] + 7
age[B] > age[A]
age[B] > 100 && age[A] < 100
Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.  Also, people will
not friend request themselves. How many total friend requests are made?


Example 1:
Input: [16,16]
Output: 2
Explanation: 2 people friend request each other.

Example 2:
Input: [16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 16, 18 -> 17.

Example 3:
Input: [20,30,100,110,120]
Output:
Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.

"""
class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        maps = collections.Counter(ages)
        result = 0
        for age1 in maps:
            for age2 in maps:
                if age2 > age1:
                    continue
                if age2 <= 0.5*age1 + 7:
                    continue
                if age2 > 100 and age1 < 100:
                    continue
                result += maps[age1] * maps[age2]
                if age1 == age2:
                    result -= maps[age2]
        return result


class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        maps = collections.Counter(ages)
        result = 0
        for age1 in maps:
            for age2 in maps:
                if age2 > age1:
                    continue
                if age2 <= 0.5*age1 + 7:
                    continue
                if age2 > 100 and age1 < 100:
                    continue
                result += maps[age1] * (maps[age2] - (age1 == age2))
        return result
