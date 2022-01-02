"""
QUESTION-
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

 

Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
Example 2:

Input: n = 2
Output: [1,2]
 

Constraints:

1 <= n <= 5 * 104
"""
"""
ANSWER-
"""
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        lexOrder = [1]*n
        for i in range(n-1):

            if  lexOrder[i]*10<=n:
                lexOrder[i+1] = lexOrder[i]*10

            elif lexOrder[i]==n:
                lexOrder[i+1] = lexOrder[i]//10+1

                while lexOrder[i+1]%10==0:
                    lexOrder[i+1] //= 10
            else:
                lexOrder[i+1] = lexOrder[i]+1

                while not lexOrder[i+1]%10:
                    lexOrder[i+1] //= 10
        return lexOrder
"""
SOURCE-LEETCODE
"""