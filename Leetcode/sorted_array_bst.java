/*
    Given an array where elements are sorted in ascending order, 
    convert it to a height balanced BST.

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

         TreeNode helper(int[] num, int low, int high) {
            if (low > high) { // Done
                  return null;
            }
            int mid = low + (high-low) / 2;
            TreeNode node = new TreeNode(num[mid]);
            node.left = helper(num, low, mid - 1);
            node.right = helper(num, mid + 1, high);
            return node;
        }
    
    public TreeNode sortedArrayToBST(int[] nums) {
        if (nums.length == 0)
        {
            return null;
        }
        TreeNode head = helper(nums, 0, nums.length - 1);
        return head;
    }
}

