/*

Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

Input: [2, 3, -4, -5, -3]
Output: 120


*/

public class Solution {
    public int maxProduct(int[] nums) {
        
        if(nums.length == 0) return 0;
        if(nums.length == 1) return nums[0];
        
        int pre_max = nums[0], pre_min = nums[0], result = nums[0];
        for(int i=1; i<nums.length; i++){
            int temp = pre_max;
            System.out.println("Number is:"+ " "+ nums[i]);
            pre_max = Math.max( Math.max(pre_max*nums[i], pre_min*nums[i]), nums[i] );
            System.out.println("maximum is:"+ " "+ pre_max);
            pre_min = Math.min( Math.min(temp*nums[i], pre_min*nums[i]), nums[i] );
            System.out.println("minimum is:"+ " "+ pre_min);
            if(pre_max > result){
                result = pre_max;
                System.out.println("result is:"+ " "+ result);
            }
        }
        return result;
    }
}