"""
124. Binary Tree Maximum Path Sum

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node
to any node in the tree along the parent-child connections. The path must contain at least
one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6 [2, 3, 1]

Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42 [15, 20, 7]


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Recursive
def maxPathSum(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    self.result_val = -99999999
    def helper(node):
        if not node:
            return 0
        left = helper(node.left)
        # print("left = %s | node = %s | " %(left, node.val))
        right = helper(node.right)
        # print("right = %s | node = %s | " %(right, node.val))
        self.result_val = max(self.result_val, left + node.val + right)
        # print("returning something: %s" %(max(node.val + max(left, right), 0)))
        # print("=============================")
        return max(node.val + max(left, right), 0)
    # print("Start.....")
    helper(root)
    return self.result_val

# Iterative stack + postorder
def maxPathSum(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return

    def helper(node):
        stack = [node]
        result = []
        while stack:
            curr = stack.pop()
            result.append(curr)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return result
    # postorder traversal using two stacks
    result = helper(root)
    final = -999999
    hashmap = {None: 0}
    for node in result[::-1]:
        left = max(hashmap.get(node.left), 0)
        right = max(hashmap.get(node.right), 0)
        hashmap[node] = max(left, right) + node.val
        final = max(left+right+node.val, final)
    return final

root = TreeNode(10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.right = TreeNode(7)
root.right.left = TreeNode(15)
obj = Solution()
print(obj.maxPathSum(root))
