"""
QUESTION-
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

 

Example 1:

Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
Example 2:

Input: nums = [1,5]
Output: 10
 

Constraints:

n == nums.length
1 <= n <= 500
0 <= nums[i] <= 100"""
"""
ANSWER-
"""
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        size = len(nums)        
        
        t = [[-1 for p in range(0,size+1)]
            for q in range(0,size+1)]
        
        return self.solve(nums,1,size-1,t)
        
    def solve(self,arr,i,j,t):
        if i >= j:
            return 0
        
        if t[i][j] > 0:
            return t[i][j]
        
        ans = float('-inf')
        
        for k in range(i,j):
            if t[i][k] != -1:
                left = t[i][k]
            else:
                left = self.solve(arr,i,k,t)
                t[i][k] = left
                
            if t[k+1][j] != -1:
                right = t[k+1][j]
            else:
                right = self.solve(arr,k+1,j,t)
                t[k+1][j] = right
                
            temp = left + right + (arr[i-1]*arr[k]*arr[j])
            
            ans = max(ans,temp)
            
        t[i][j] = ans
        return t[i][j]

"""
SOURCE-LEETCODE
"""