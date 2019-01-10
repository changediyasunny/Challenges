"""
421. Maximum XOR of Two Numbers in an Array

Given a non-empty array of numbers, a0, a1, a2, … , an-1
Find the maximum result of ai xor aj , where 0 ≤ i, j < n. Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.

Time: O(n)

"""
import os, sys

class TrieNode():
    def __init__(self):
        self.one = None
        self.zero = None

def insert(root, nums):
    for num in nums:
        print("===num====> %s" %num)
        node = root
        for j in range(31, -1, -1):
            bit_val = num & 1 << j
            if bit_val:
                print("====j => %s" %j)
                if not node.one:
                    node.one = TrieNode()
                node = node.one
            else:
                if not node.zero:
                    node.zero = TrieNode()
                node = node.zero

def findMaximumXOR(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    root = TrieNode()
    insert(root, nums)
    print("traverse tree to find XOR.")
    max_xor = 0
    for num in nums:
        print("=====>num = %s" %num)
        node = root
        curr_xor = 0
        for j in range(31, -1, -1):
            bit_val = num & 1 << j
            if node.one and not bit_val:
                # strive for 1 & 0 combination
                node = node.one
                curr_xor += 1 << j
            elif node.zero and bit_val:
                 # strive for 0 & 1 combination
                node = node.zero
                curr_xor += 1 << j
            else:
                node = node.one or node.zero
            # print("===========curr_xor ===> %s" %curr_xor)
        max_xor = max(curr_xor, max_xor)
    return max_xor


nums = [3,10,5,25,2,8]
findMaximumXOR(nums)
