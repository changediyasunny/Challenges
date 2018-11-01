"""
297. Serialize and Deserialize Binary Tree

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, 
or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization 
algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"


Time complexity : in both serialization and deserialization functions, we visit each node exactly once, thus the time complexity is O(N), 
where NN is the number of nodes, i.e. the size of tree.

Space complexity : in both serialization and deserialization functions, we keep the entire tree, 
either at the beginning or at the end, therefore, the space complexity is O(N).

DFS & BFS approach

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def __init__(self):
        self.data = []

    def serializeHelper(self, root):
        if root is None:
            self.data.append(None)
        else:
            self.data.append(root.val)
            self.serialize(root.left)
            self.serialize(root.right)

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.serializeHelper(root)
        return self.data
    
    def deserializeHelper(self):
        if len(self.data):
            if self.data[0] is None:
                self.data = self.data[1:]
                return None
            root = TreeNode(self.data[0])
            self.data = self.data[1:]
            root.left = self.deserializeHelper()
            root.right = self.deserializeHelper()
            return root
        else:
            return None

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not len(data):
            return []
        self.data = data
        return self.deserializeHelper()



class Codec:
    
    def __init__(self):
        self.data = []

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def r_helper(root):
            if root is None:
                self.data.append(None)
            else:
                self.data.append(root.val)
                r_helper(root.left)
                r_helper(root.right)
            return self.data
        return r_helper(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not len(data):
            return []
        
        def d_helper():
            if len(self.data):
                if self.data[0] is None:
                    self.data = self.data[1:]
                    return None
                root = TreeNode(self.data[0])
                self.data = self.data[1:]
                root.left = d_helper()
                root.right = d_helper()
                return root
            else:
                return None

        self.data = data
        return d_helper()