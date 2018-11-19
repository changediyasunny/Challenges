"""
99. Recover Binary Search Tree
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def recoverTree(root):
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """
    current = root
    first = second = temp = None
    while current:
        if current.left is None:
            # left is null and print node & go right
            if temp and temp.val > current.val:
                second = current
                if first is None:
                    first = temp
            temp = current
            current = current.right
        else:
            # find pre-decessor
            pred = current.left
            while (pred.right and pred.right != current):
                pred = pred.right

            if pred.right is None:
                # if right link is NULL, then go left after link created to root
                pred.right = current
                current = current.left
            else:
                # link already created. go to root node after VISIT(node)
                if temp and temp.val > current.val:
                    second = current
                    if first is None:
                        first = temp
                temp = current
                pred.right = None
                current = current.right     # this takes back to root again
    if first and second:
        k = first.val
        first.val = second.val
        second.val = k



### Morris Tree Traversal
def morris_tree(root):
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """
    current = root
    while current:
        if current.left is None:
            # left is null and print node & go right
            # VISIT()
            current = current.right
        else:
            # find pre-decessor
            pred = current.left
            while (pred.right and pred.right != current):
                pred = pred.right

            if pred.right is None:
                # if right link is NULL, then go left after link created to root
                pred.right = current
                current = current.left
            else:
                # link already created. go to root node after VISIT(node)
                pred.right = None
                # VISIT()
                current = current.right     # this takes back to root again
    return root
