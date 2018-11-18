"""
106. Construct Binary Tree from Inorder and Postorder Traversal

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
        newNode = TreeNode(postorder.pop())
        if prev is not None:
            prev.left = newNode
        elif stack:
            currTop = stack[-1]
            currTop.right = newNode
        stack.append(newNode)
        prev = None
    return root

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

# root = buildTree(inorder=inorder, postorder=postorder)
root = buildTree_stack(inorder=inorder, postorder=postorder)
print(root.val)
print(root.left.val)
print(root.right.val)
