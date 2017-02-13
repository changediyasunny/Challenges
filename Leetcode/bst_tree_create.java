/*

BINARY SEARCH TREE Creation...
*/

package binary_search;

import java.util.LinkedList;
import java.util.List;
import java.util.Stack;

public class Graph {
	
	
	class TreeNode{
		
		int key;
		TreeNode left, right;
		
		public TreeNode(int val){
			key = val;
			left = right = null;
		}
	}	// class TreeNode ends here...
	TreeNode root;
	Graph(){
		root = null;
	}
	
	public TreeNode insert(TreeNode root, int temp)
	{
		if(root == null){
			root = new TreeNode(temp);
			return root;
		}
		if(temp <= root.key){
			root.left = insert(root.left, temp);
		}
		else{
			root.right = insert(root.right, temp);
		}
		return root;
	}
	
	// In-Order traversal
	public List<Integer> inorder_print(TreeNode root){
			
		List<Integer> result = new LinkedList<Integer>();
		if(root == null) return result;
			
		// create stack for node tracking
		Stack<TreeNode> stack = new Stack<TreeNode>();
		TreeNode curr = root;
			
		while(!stack.isEmpty() || curr != null){
				
			while(curr != null){
				// traverse left as far as you can & push to stack
				stack.push(curr);
				curr = curr.left;
			}
			// pop it now...
			curr = stack.pop();
			result.add(curr.key);	// add to list
			curr = curr.right;	// go to right
		}
		return result;
	} 	// in-order complete
		
		
	public static void main(String[] args){
		
		Graph tree = new Graph();
		TreeNode g = null; 
		g = tree.insert(g, 50);
		g = tree.insert(g, 20);
		g = tree.insert(g, 100);
		g = tree.insert(g, 10);
		g = tree.insert(g, 40);
		g = tree.insert(g, 80);
		g = tree.insert(g, 110);
		g = tree.insert(g, 5);
		g = tree.insert(g, 30);
		g = tree.insert(g, 60);
		g = tree.insert(g, 70);
		g = tree.insert(g, 90);
		
		
		//BinarySearchTree tree = new BinarySearchTree();
		System.out.println("Inorder traversal of the given tree");
		System.out.println(tree.inorder_print(g));
		
	}	// Main() finished
}
