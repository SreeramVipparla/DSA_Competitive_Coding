"""
QUESTION-

Given a set of n items numbered from 1 up to n, each with a weight wi and a value vi, along with a maximum weight capacity W, maximize the sum of the values of the items in the knapsack so that the sum of the weights is less than or equal to the knapsack's capacity.
"""
"""
ANSWER-
"""
class Solution:
  def integerBreak(self, n: int) -> int:
    if n == 0:
        return 0
    dp = [0]*(n+1)
    dp[0] = 1
    mx = float('-inf')
    for i in range(1, n): 
        for j in range(i, n+1):
            dp[j] = max(dp[j], i*dp[j-i])
    
    return max(dp)
"""
SOURCE-TALENTSPRINT
"""