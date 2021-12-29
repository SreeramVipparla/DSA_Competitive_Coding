"""
QUESTION-
In the "100 game" two players take turns adding, to a running total, any integer from 1 to 10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers from 1 to 15 without replacement until they reach a total >= 100.

Given two integers maxChoosableInteger and desiredTotal, return true if the first player to move can force a win, otherwise, return false. Assume both players play optimally.

 

Example 1:

Input: maxChoosableInteger = 10, desiredTotal = 11
Output: false
Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.
Example 2:

Input: maxChoosableInteger = 10, desiredTotal = 0
Output: true
Example 3:

Input: maxChoosableInteger = 10, desiredTotal = 1
Output: true
 

Constraints:

1 <= maxChoosableInteger <= 20
0 <= desiredTotal <= 300
"""
"""
ANSWER-
"""
class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if desiredTotal == 0:
            return True
        self.max = maxChoosableInteger
        self.d = {}
        
        if desiredTotal > maxChoosableInteger * (maxChoosableInteger+1) // 2:
            return False
        
        return self.recursion(2**maxChoosableInteger-1, desiredTotal)
        
    
    def recursion(self, mask, total): 
        
        if mask >= 2**(total-1):
            return True
        if mask in self.d:
            return self.d[mask]
        
        for i in range(self.max):
            if mask & (1<<i): 
                newmask = mask & ~(1<<i) 
                if self.recursion(newmask, total-i-1) == False:
                    self.d[mask] = True
                    return True
        self.d[mask] = False
        return False
"""
SOURCE-LEETCODE
"""