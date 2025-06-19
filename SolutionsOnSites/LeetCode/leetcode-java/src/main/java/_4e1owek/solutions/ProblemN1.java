package _4e1owek.solutions;

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target){
        Map<Integer, Integer> n = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            int c = target - nums[i];
            if (n.containsKey(c)){
                return new int[]{n.get(c), i};
            }
            else {
                n.put(nums[i], i);
            }
        }
        return null;
    }
}
