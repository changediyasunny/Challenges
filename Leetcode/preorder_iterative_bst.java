/*
    Given a binary tree, return the preorder traversal of its nodes' values.
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
    public List<Integer> preorderTraversal(TreeNode root) {
     
     List<Integer> result = new ArrayList<Integer>();
     Stack<TreeNode> stack = new Stack<TreeNode>();
     
     if(root == null) return result;
     TreeNode curr = root;
     while(!stack.isEmpty() || curr != null){
         if(curr != null){
             
             stack.push(curr);
             result.add(curr.val);
             curr = curr.left;
             
         }
         else{
             
             TreeNode k = stack.pop();
             if(k.right != null){
                 curr = k.right;
             }else{
                 
                 curr = null;
             }
         }
     }
     return result;
    }
}


/*

Solution Using Stack & storing only Right subtree...
==========================================================


public List<Integer> preorderTraversal(TreeNode node) {
    List<Integer> list = new LinkedList<Integer>();
    Stack<TreeNode> rights = new Stack<TreeNode>();
    while(node != null) {
        list.add(node.val);
        if (node.right != null) {
            rights.push(node.right);
        }
        node = node.left;
        if (node == null && !rights.isEmpty()) {
            node = rights.pop();
        }
    }
    return list;
}


*/