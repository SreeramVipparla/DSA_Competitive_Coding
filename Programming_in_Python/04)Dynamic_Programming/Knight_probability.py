"""
QUESTION-

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""
"""
ANSWER-
"""
from functools import lru_cache

class Solution:

    def knightProbability(self, N, K, r, c):
        
        def is_within_board(square):
            (i, j) = square
            return 0 <= i < N and 0 <= j < N
        
        def get_successors(square):
           
            (i, j) = square
            return (
                (i + si*di, j + sj*dj)
                for (di, dj) in [(1, 2), (2, 1)]
                for si in (-1, 1)
                for sj in (-1, 1)
            )
        
        def get_canonical(square):
         
            (i, j) = square

            i = min(i, N-1-i)

            j = min(j, N-1-j)

            return (max(i, j), min(i, j))
        
        @lru_cache(None)
        def get_probability(square, k):
            if not is_within_board(square):
                return 0
            elif k == 0:
                return 1
            else:
                probabilities = [
                    get_probability(get_canonical(successor), k-1)
                    for successor in get_successors(square)
                ]
                return sum(probabilities) / len(probabilities)
        
        return get_probability((r, c), K)
"""
SOURCE-LEETCODE
"""