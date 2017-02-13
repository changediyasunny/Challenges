/*
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.


For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]



*/

public class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        
        List<List<Integer>> final_list = new ArrayList<List<Integer>>();
        Arrays.sort(nums);
        
        for(int i=0; i<nums.length - 2; i++){
            
            // for unique elements
            if(i > 0 && nums[i] == nums[i-1]){
                continue;
            }
            
            //
            int j = i +1;
            int k = nums.length - 1;
            int target = 0 - nums[i];
            while(j < k){
                if(nums[i] + nums[j] + nums[k] == 0){
                    // final result found
                    final_list.add(Arrays.asList(nums[i], nums[j], nums[k]));
                    // skip duplicates
                    j++;
                    k--;
                    while(j < k && nums[j] == nums[j-1]){
                        j++;
                    }
                    while(j < k && nums[k] == nums[k+1]){
                        k--;
                    }
                }else if(nums[i] + nums[j] + nums[k] < 0){
                    j++;
                }
                else{
                    k--;
                }
                
            }
        }
        // end
        return final_list;
    }
}