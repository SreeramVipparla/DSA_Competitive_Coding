"""
QUESTION-

Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

 

Example 1:

Input: n = 13
Output: 6
Example 2:

Input: n = 0
Output: 0
 

Constraints:

0 <= n <= 109
Accepted
59,430

"""
"""
ANSWER-
"""
class Solution:
  def countDigitOne(self, n):
    if n <= 0:
        return 0
    if 1 <= n <= 9:
        return 1

    head, level = n, 1
    while head > 9:
        level *= 10
        head //= 10
    if head == 1:
        return  self.countDigitOne(level-1) + self.countDigitOne(n-level) + n-level +1
    return (head) * self.countDigitOne(level-1) + self.countDigitOne(n-head*level) + level
"""
SOURCE-LEETCODE
"""