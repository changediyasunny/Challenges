"""
106. Construct Binary Tree from Inorder and Postorder Traversal

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7


The core idea is: Starting from the last element of the postorder and inorder array,
we put elements from postorder array to a stack and each one is the right child of the
last one until an element in postorder array is equal to the element on the inorder array.
Then, we pop as many as elements we can from the stack and decrease the mark in inorder array
until the peek() element is not equal to the mark value or the stack is empty. Then, the new
element that we are gonna scan from postorder array is the left child of the last element we have
popped out from the stack.

(a) Inorder (Left, Root, Right)
(b) Preorder (Root, Left, Right)
(c) Postorder (Left, Right, Root)
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None
    print("inorder=%s" %inorder)
    print("postorder=%s" %postorder)
    rootval = postorder.pop()
    print("rootval=%s" %rootval)
    index_ = inorder.index(rootval)
    print("index_=%s" %index_)
    print("=============================")
    root = TreeNode(rootval)
    root.left = buildTree(inorder[:index_], postorder[:index_])
    root.right = buildTree(inorder[index_+1:], postorder[index_:])
    return root


def buildTree_stack(inorder, postorder):
    """ iterative solution """
    if not inorder or not postorder:
            return None
    stack = []
    prev = None
    root = TreeNode(postorder.pop())
    stack.append(root)
    while postorder:
        while(stack and stack[-1].val == inorder[-1]):
            prev = stack.pop()
            tmp = inorder.pop()
        curr = TreeNode(postorder.pop())
        if prev is not None:
            prev.left = curr
        elif stack:
            stack[-1].right = curr
        stack.append(curr)
        prev = None
    return root

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

# root = buildTree(inorder=inorder, postorder=postorder)
root = buildTree_stack(inorder=inorder, postorder=postorder)
print(root.val)
print(root.left.val)
print(root.right.val)
