


/**
 * QUESTION

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
*/


 /**
 * ANSWER
 */
import java.io.*;
import java.util.*;
public class House_Robber {

  public int rob(int[] nums) {

    //if nums is null or length 0, return 0
    if(nums==null || nums.length==0)
        return 0;
        
    //if only 1 element is present,return it as the answer
    if(nums.length==1)
        return nums[0];
        
    //array to store the maxProfit attained
    int[] maxProfit=new int[nums.length];
    
    //assign fisrt value
    maxProfit[0]=nums[0];
    
    //second value is higher of first and second
    maxProfit[1]=Math.max(nums[0],nums[1]);
    
    //do dynamic programming for subsequent values
    for(int i=2;i<nums.length;i++)
    {
        maxProfit[i]=Math.max(maxProfit[i-2]+nums[i],maxProfit[i-1]);
    }
    
    //return the last value as answer
    return maxProfit[nums.length-1];
}

}
 /**
 * SOURCE-LEETCODE
 */