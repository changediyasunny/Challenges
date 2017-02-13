/*
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Remember:  1 <= nums[i] <= N   ( N=size of array)
=============
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

*/


public class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        
        List<Integer> result = new ArrayList<Integer>();
        //if(nums.length == 0) return nums;
        
        for(int i=0; i<nums.length; i++){
            
            int k = Math.abs(nums[i]);
            
            if(nums[k-1] < 0){
                result.add(Math.abs(k));
            }else{
                nums[k-1] *= -1;
            }
        }
        return result;
    }
}