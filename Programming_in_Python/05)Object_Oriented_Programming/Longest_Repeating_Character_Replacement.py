"""
QUESTION-
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""
"""
ANSWER-
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
        
        best = 0
        
        for c in chars:
            best =  max(best, self.solve_char(s, k, c))
            
        return best
    
    def solve_char(self, s, k, c):
        n = len(s)
        lo = 0
        hi = 0
        best = 0
        
        while hi < n:
            if k: 
                if s[hi] != c:
                    k = k - 1
                hi = hi + 1
            else:  
                if s[hi] == c:
                    hi = hi + 1
                else:
                    if lo == hi:
                        lo = lo + 1
                        hi = hi + 1
                    else:
                        if s[lo] != c:
                            k = k + 1
                        lo = lo + 1
            best = max(best, hi - lo)
            
        return best
"""
SOURCE-LEETCODE
"""