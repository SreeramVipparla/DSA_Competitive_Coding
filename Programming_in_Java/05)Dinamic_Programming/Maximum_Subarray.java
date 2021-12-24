

/**
QUESTION
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
/**
 * ANSWER
 */
import java.io.*;

public class Maximum_Subarray {
  
  public int maxSubArray(int[] nums) {
    int omax=nums[0];  // omax: overall maximum
    int cmax=nums[0]; //  cmax: current maximum
    
    for(int i=1;i<nums.length;i++){
        cmax=Math.max(nums[i],nums[i] + cmax);
        
        omax=Math.max(cmax,omax);
    }
    return omax;
}
}

 /**
 * SOURCE-LEETCODE
 */