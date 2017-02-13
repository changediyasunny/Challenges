/*
Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],


#TODO: try to do using Queue...

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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> output = new ArrayList<List<Integer>>();
    if (root == null) return output;
    Stack<TreeNode> cur_layer = new Stack<TreeNode>(); cur_layer.push(root);
    Stack<TreeNode> next_layer = new Stack<TreeNode>();
    List<Integer> layer_output = new ArrayList<Integer>();
    int d = 0; // 0: left to right; 1: right to left.
    
    while (!cur_layer.isEmpty()){
    	TreeNode node = cur_layer.pop();
    	layer_output.add(node.val);
    	if(d==0){
    		if (node.left != null) next_layer.push(node.left);
    		if (node.right != null) next_layer.push(node.right);
    	}else{
    		if (node.right != null) next_layer.push(node.right);
    		if (node.left != null) next_layer.push(node.left);
    	}
    	
    	if (cur_layer.isEmpty()){
    		output.add(layer_output);
    		layer_output = new ArrayList<Integer>();
    		cur_layer = next_layer;
    		next_layer = new Stack<TreeNode>();;
    		d ^= 1;
    	}
    }
    return output;
    }
}