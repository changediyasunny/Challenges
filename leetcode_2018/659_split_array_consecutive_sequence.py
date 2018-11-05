"""
659. Split Array into Consecutive Subsequences

You are given an integer array sorted in ascending order (may contain duplicates), you need to split 
them into several subsequences, where each subsequences consist of at least 3 consecutive integers. 
Return whether you can make such a split.

Example 1:

Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5

Example 2:

Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5

Example 3:

Input: [1,2,3,4,4,5]
Output: False

Backtracking:
Time Complexity: O(N), where N is the length of nums. We iterate over the array.
Space Complexity: O(N), the size of count and tails.

"""

def isPossible(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    count = collections.Counter(nums)
    tails = collections.Counter()
    
    for n in nums:
        if count[n] == 0:
            continue
        elif tails[n] > 0:
            tails[n] -= 1
            tails[n+1] += 1
        elif count[n+1] > 0 and count[n+2] > 0:
            count[n+1] -= 1
            count[n+2] -= 1
            tails[n+3] += 1
        else:
            return False
        count[n] -= 1
    return True