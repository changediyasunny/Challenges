import sys


class TreeNode(object):

	def __init__(self, item):
		self.key = item
		self.left = None
		self.right = None


def insert(node, item):
	
	if node == None:
		return TreeNode(item)

	if item <= node.key:
		# left part
		node.left = insert(node.left, item)
	else:
		# right part
		node.right = insert(node.right, item)
	return node

def inorder_print(root):

	final_list = []
	# python lists can be used as stack: append & pop
	if root == None:
		return root
	stack_list = []
	curr = root
	while( len(stack_list) !=0 or curr != None):

		while(curr != None):
			stack_list.append(curr)
			curr = curr.left

		curr = stack_list.pop()
		final_list.append(curr.key)
		curr = curr.right
	return final_list




def main():
	root = TreeNode(50)
	root = insert(root, 20)
	root = insert(root, 100)
	root = insert(root, 10)
	root = insert(root, 40)
	root = insert(root, 80)
	root = insert(root, 110)
	root = insert(root, 5)
	root = insert(root, 30)
	root = insert(root, 60)
	root = insert(root, 70)
	root = insert(root, 90)
	# print(root.key)

	result = inorder_print(root)
	print(result)





if __name__ == '__main__':
	main()