"""
QUESTION-
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

 

Example 1:

Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
 

Constraints:

1 <= expression.length <= 20
expression consists of digits and the operator '+', '-', and '*'.
All the integer values in the input expression are in the range [0, 99].
"""
"""
ANSWER-
"""
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        nums = '0123456789'
        
        def op(a, b, c):
            if c == '+':
                return a + b
            elif c == '-':
                return a - b
            else:
                return a * b
        
        @lru_cache(None)
        def func(l, r):
            if l == r:
                return [expression[l]]
            elif l > r:
                return []
            
            this = []
            went = 0
            for i in range(l, r + 1):
                if expression[i] not in nums:
                    went = 1
                    left = func(l, i - 1)
                    right = func(i + 1, r)
                    for leftvals in left:
                        for rightvals in right:
                            temp = op(int(leftvals), int(rightvals), expression[i])
                            #print(temp)
                            this.append(temp)
            
            if went:
                return this
            else:
                return [expression[l: r + 1]]
        
        arr = func(0, len(expression) - 1)
        #print(arr)
        return arr
"""
SOURCE-LEETCODE
"""