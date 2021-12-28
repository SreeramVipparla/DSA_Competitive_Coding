"""
QUESTION-
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""
"""
ANSWER-
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        rows, cols = m, n
        
        path_dp = [ [ 1 for j in range(cols)] for i in range(rows) ]
        
        
        # Dynamic Programming relation:
        
        # Base case:
        # DP(0, j) = 1 , only reachable from one step left
        # DP(i, 0) = 1 , only reachable from one step up
        
        # General case:
        # DP(i,j) = number of path reach to (i, j)
        #         = number of path reach to one step left + number of path reach to one step up
        #         = number of path reach to (i, j-1) + number of path to (i-1, j)
        #         = DP(i, j-1) + DP(i-1, j)
        
        
        
        for i in range(1, rows):
            for j in range(1, cols):
                
                path_dp[i][j] = path_dp[i][j-1] + path_dp[i-1][j]
        
        
        # Destination coordination = (rows-1, cols-1)
        return path_dp[rows-1][cols-1]
"""
SOURCE-LEETCODE
"""