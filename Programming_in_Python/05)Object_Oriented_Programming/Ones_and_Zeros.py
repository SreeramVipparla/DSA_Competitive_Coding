"""
QUESTION-
You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.

 

Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.
 

Constraints:

1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] consists only of digits '0' and '1'.
1 <= m, n <= 100
"""
"""
ANSWER-
"""
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counter = Counter([(s.count('0'), s.count('1')) for s in strs])
        d = defaultdict(lambda: -1)
        
        def dfs(m, n, count):
            if d[(m, n)] >= count: return d[(m, n)]
            max_count = count
            d[(m, n)] = count
            
            for k, v in counter.items():
                if v <= 0: continue
                zeros, ones = k[0], k[1]
                if zeros <= m and ones <= n:
                    counter[k] -= 1
                    max_count = max(max_count, dfs(m - zeros, n - ones, count + 1))
                    counter[k] += 1
            return max_count
        
        result = dfs(m, n, 0)
        return result
"""
SOURCE-LEETCODE
"""