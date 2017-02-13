/*
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

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
    public boolean isValidBST(TreeNode root) {
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode curr = root;
        TreeNode pre = null;
        
        while(!stack.isEmpty() || curr != null ){
            
            if(curr != null){
                // go left till end
                stack.push(curr);
                curr = curr.left;
            }
            else{
                
                // pop form stack
                TreeNode k = stack.pop();
                if(pre != null && k.val <= pre.val){
                    // very wise condition
                    return false;
                }
                pre = k;
                curr = k.right;
            }
        }
        return true;
    }
}