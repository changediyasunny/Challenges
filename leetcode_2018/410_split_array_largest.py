"""
410. Split Array Largest Sum

Given an array which consists of non-negative integers and an integer m, you can split
the array into m non-empty continuous subarrays. Write an algorithm to minimize the
largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:
1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)

Examples:
Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.

"""
# Binary search on array of ranges
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def is_valid(nums, m, mid):
            curr_sum = 0
            cuts = 1
            for n in nums:
                curr_sum += n
                if curr_sum > mid:
                    cuts += 1
                    curr_sum = n
                    #print(">> {} | cuts= {}".format(curr_sum, cuts))
                    if cuts > m:
                        return False
            return True

        low = max(nums)
        high = sum(nums)
        while low <= high:
            mid = (low + high)//2
            #print(low, mid, high)
            # can you make at-most m sub-arrays with maximum sum atmost mid
            if is_valid(nums, m, mid):
                high = mid
            else:
                low = mid + 1
        return low

# Dynamic Programming + Memoization

class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """

        def helper(i, nums, cache, m):
            if i == len(nums):
                return 0
            elif m == 1:
                return sum(nums[i:])
            else:
                if cache[i][m]:
                    return cache[i][m]
                cache[i][m] = float('inf')
                for j in range(1, len(nums)+1):
                    left = sum(nums[i: i+j])
                    right = helper(i+j, nums, cache, m-1)
                    cache[i][m] = min(cache[i][m], max(left, right))
                    if left > right: break
                return cache[i][m]

        cache = [[0]*(m+1) for _ in range(len(nums)+1)]
        temp = helper(0, nums, cache, m)
        print(cache)
        return temp
