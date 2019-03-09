"""
222. Count Complete Tree Nodes

Given a complete binary tree, count the number of nodes.
Input:
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6

Explanation:
The height of a tree can be found by just going left. Let a single node tree have height 0.
Find the height h of the whole tree.
If the whole tree is empty, i.e., has height = -1, there are 0 nodes.
Otherwise check whether the height of the right subtree is just one less than that of the whole tree,
meaning left and right subtree have the same height.

If yes, then the last node on the last tree row is in the right subtree and the left subtree is a full tree of height h-1. So we take the 2^h-1 nodes of the left subtree plus the 1 root node plus recursively the number of nodes in the right subtree.

If no, then the last node on the last tree row is in the left subtree and the right subtree is a full tree of height h-2. So we take the 2^(h-1)-1 nodes of the right subtree plus the 1 root node plus recursively the number of nodes in the left subtree. Since I halve the tree in every recursive step,
I have O(log(n)) steps. Finding a height costs O(log(n)).

So overall O(log(n)^2).
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def height(node):
            if node is None:
                return -1
            return 1 + height(node.left)

        count = 0
        lh = height(root)
        while root:
            if height(root.right) == lh-1:
                count += 1<<lh
                root = root.right
            else:
                count += 1<< lh-1
                root = root.left
            lh = lh -1
        return count
