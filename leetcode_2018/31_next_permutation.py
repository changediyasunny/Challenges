"""
31. Next Permutation:

Implement next permutation, which rearranges numbers into the lexicographically next greater
permutation of numbers. If such arrangement is not possible, it must rearrange it as the lowest
possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory. Here are some examples.
Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 = 1,3,2
3,2,1 = 1,2,3
1,1,5 = 1,5,1

Time complexity : O(n). In worst case, only two scans of the whole array are needed.
Space complexity : O(1). No extra space is used. In place replacements are done.

Solution: ( to find next larger permutation)
1. Find 1st decreasing element from right side of the list. A[i]
2. Find element just larger than A[i] which is A[i- 1] such that A[i] <= a[i-1]
3. Swap both elements and since all elements after A[i] are in decreasing order,
4. Find next largest element than A[i] which is A[j]. A[i] <= A[j]
5. Reverse numbers from A[i+1]

"""

def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    # swap numbers in-place
    def swap(nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
    # reverse array to find smallest range
    def reverse(nums, start):
        i, j = start, len(nums)-1
        while(i < j):
            swap(nums, i, j)
            i +=1
            j -= 1
    # actual logic
    i = len(nums) - 2
    while(i >=0 and nums[i] >= nums[i+1]):
        i = i -1
    if i >= 0:
        j = len(nums) - 1
        while(j >=0 and nums[j] <= nums[i]):
            j = j -1
        swap(nums, i, j)
    reverse(nums, i+1)
    return nums

print(nextPermutation([1,5,8,4,7,6,5,3,1]))
