/*
	Binary Tree Iterative Inorder Traversal...

*/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new LinkedList<Integer>();
	    if (root == null) return res;
	    Stack<TreeNode> stack = new Stack<TreeNode>();
	    TreeNode cur = root;
	    while (cur != null || !stack.isEmpty()) { 
		    while (cur != null) {// Travel to each node's left child, till reach the left leaf
			    stack.push(cur);
			    cur = cur.left;				
		    }		 
		    //System.out.println("1st cur= " + cur.val);
		    cur = stack.pop(); // Backtracking to higher level node A
		    //System.out.println("Popped cur= " + cur.val);
		    res.add(cur.val);  // Add the node to the result list
		    cur = cur.right;   // Switch to A'right branch
		    //System.out.println("After Right cur= " + cur.val);
	    }
	return res;
    }
}