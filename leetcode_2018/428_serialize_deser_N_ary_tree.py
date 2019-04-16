"""
428. Serialize and Deserialize N-ary Tree

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be
stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later
in the same or another computer environment.

Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree in which each node has
no more than N children. There is no restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that an N-ary tree can be serialized to a string and this string can be deserialized to the original tree structure.

"""

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        # [1 [ 3 [ 5 6 ] 2 4 ]
        result = []
        def helper(node):
            result.append(str(node.val))
            if node.children:
                result.append("[")
                for kid in node.children:
                    helper(kid)
                result.append("]")    # end of root children
        helper(root)
        print(" ".join(result))
        return " ".join(result)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if not data:
            return
        def helper(node, i):
            while i < len(self.new_data):
                tmp = self.new_data[i]
                if tmp.isdigit():
                    # node is here
                    curr=Node(int(tmp),[])
                    node.children.append(curr)
                    i+=1
                elif tmp == "[":
                    i = helper(curr,i+1)
                elif tmp == "]":
                    return i + 1

        self.new_data = data.split()
        root=Node(int(self.new_data[0]),[])
        helper(root, 2)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
